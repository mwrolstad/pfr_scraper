from lxml import html

import argparse
import json
import logging
import numpy as np
import os
import random
import re
import requests
import pandas as pd
import urllib.request


def derive_player_name(play_description: str) -> str:
    return " ".join(play_description.split(" ")[0:2])


def derive_play_category(play_description: str) -> str:
    if "pass" in play_description:
        return "pass"
    if "left tackle" in play_description:
        return "run"
    if "right tackle" in play_description:
        return "run"
    if "left end" in play_description:
        return "run"
    if "right end" in play_description:
        return "run"
    if "kicks off" in play_description:
        return "kick off"
    if "field goal" in play_description:
        return "field goal"
    if "punts" in play_description:
        return "punt"


def derive_field_side(location: str, yard_line: bool = True) -> str:
    if type(location) != str:
        return 50 if yard_line else "MID"
    else:
        if yard_line:
            return int(location.split(" ")[1])
        else:
            return location.split(" ")[0]


def derive_yards(
    field_side: str, 
    yard_line: int,
    next_field_side: str, 
    next_yard_line: int,
) -> str:
    if next_yard_line is None:
        return None
    elif field_side == next_field_side:
        return yard_line - next_yard_line
    else:
        return 100 - yard_line - next_yard_line


def convert_date_to_number(dt, override_year=None):
    try:
        yr = re.search("(20|19)[0-9]{2}", dt, re.IGNORECASE)
        yr = str(dt.datetime.today().year) if yr is None else yr.group(0)

        mt = re.search(
            "(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)",
            dt,
            re.IGNORECASE,
        ).group(0)
        mt = month_string_to_number(mt)

        if override_year is not None:
            yr = str(override_year - 1 if int(mt.replace("0", "")) < 8 else override_year)

        dy = re.search("[0-9]{1,2}", dt, re.IGNORECASE).group(0).zfill(2)

        return f"{yr}{mt}{dy}"

    except:
        return ""


def month_string_to_number(string):
    m = {
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12",
    }

    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError("Not a month")


def scrape_games(year: int, week: int, proxies=None):
    game_ls = []
    proxy = None

    URL_TEMPLATE = "https://www.pro-football-reference.com/years/{0}/week_{1}.htm"
    NFL_ABRV = json.load(open(os.path.join(os.path.dirname(__file__), "nfl_abbreviations.json")))

    url = URL_TEMPLATE.format(year, week)
    print("||====== Calling the URL: {url} =======||".format(url=url))

    if proxies:
        proxy = random.choice(proxies)

    response = requests.get(url, proxies=proxy)

    tree = html.fromstring(response.content)
    games_count = len(tree.xpath('//*[@class="right gamelink"]'))

    print("||")
    print(
        "||====== We found {games_count} game(s) for {yr}, week {wk}".format(games_count=games_count, yr=year, wk=week)
    )
    for g in range(1, games_count + 1):
        
        try:
            game_dict = {}

            away_team_link = tree.xpath(f'//*[@id="content"]/div[4]/div[{g}]/table[1]/tbody/tr[2]/td[1]/a')
            home_team_link = tree.xpath(f'//*[@id="content"]/div[4]/div[{g}]/table[1]/tbody/tr[3]/td[1]/a')
            game_url_ls = tree.xpath(f'//*[@id="content"]/div[4]/div[{g}]/table[1]/tbody/tr[2]/td[3]/a')

            if len(away_team_link) > 0 and len(home_team_link) > 0 and len(game_url_ls) > 0:
                game_dict["game_url"] = f"https://www.pro-football-reference.com{game_url_ls[0].attrib['href']}"

                print("||")
                print("||====== game link:", game_dict["game_url"])

                game_dict["away_team"] = away_team_link[0].text
                game_dict["home_team"] = home_team_link[0].text

                print("||")
                print("||====== away team...", game_dict["away_team"])
                print("||")
                print("||====== home team...", game_dict["home_team"])
                print("||")

                game_dict["away_abrv"] = NFL_ABRV[game_dict["away_team"]]
                game_dict["home_abrv"] = NFL_ABRV[game_dict["home_team"]]

                teams = [game_dict["away_team"], game_dict["home_team"]]
                abrvs = [game_dict["away_abrv"], game_dict["home_abrv"]]

                if proxies:
                    proxy_support = urllib.request.ProxyHandler(proxies=random.choice(proxies))
                    opener = urllib.request.build_opener(proxy_support)
                    urllib.request.install_opener(opener)

                print("||====== Grabbing the game data now...")
                print("||")

                req = urllib.request.Request(game_dict["game_url"])
                game_response = urllib.request.urlopen(req).read()
                game_tree = html.fromstring(game_response)

                game_date = game_tree.xpath('//*[@id="content"]/div[2]/div[3]/div[1]')

                print("||====== Got the game data, continuing...")
                print("||")

                if len(game_date) > 0:
                    game_dict["game_date"] = convert_date_to_number(game_date[0].text)
                    stats_table = re.search(
                        '(<table class="add_controls stats_table" id="team_stats")(.+?)(<\/table>)',
                        game_response.decode("latin-1"),
                        re.DOTALL | re.MULTILINE,
                    )

                    print("||====== Got the stats table, continuing...")
                    print("||")

                    if stats_table:
                        player_stats_dfs = pd.read_html(game_dict["game_url"])

                        if len(player_stats_dfs) == 3:
                            player_stats_df = player_stats_dfs[2]
                            player_stats_columns = [
                                "player",
                                "team_abrv",
                                "passing_cmp",
                                "passing_att",
                                "passing_yds",
                                "passing_tD",
                                "passing_int",
                                "passing_sk",
                                "passing_sk_yds",
                                "passing_lng",
                                "passing_rate",
                                "rushing_att",
                                "rushing_yds",
                                "rushing_td",
                                "rushing_lng",
                                "receiving_tgt",
                                "receiving_rec",
                                "receiving_yds",
                                "receiving_td",
                                "receiving_lng",
                                "fumbles_fmb",
                                "fumbles_fl",
                            ]
                            player_stats_df.columns = player_stats_columns
                            player_stats_df = player_stats_df[
                                (player_stats_df["player"] != "Player") & (player_stats_df["player"].notnull())
                            ]
                            player_stats_df = player_stats_df.assign(
                                team_abrv=player_stats_df["team_abrv"].apply(lambda x: NFL_ABRV[x])
                            )
                            player_stats_df = player_stats_df.assign(game_url=game_dict["game_url"])
                            player_stats_df = player_stats_df.assign(game_date=game_dict["game_date"])
                            player_stats_df = player_stats_df.fillna(0)
                            # add the list of dictionaries to the overall list
                            game_dict["player_stats"] = player_stats_df.to_dict(orient="records")

                        logging.info("About to grab the stats table")
                        stats_dfs = pd.read_html(f"<html>{stats_table[0]}</html>")
                        stats_df = stats_dfs[0]

                        team_ls = []
                        drive_ls = []

                        for i in range(1, 3):
                            stat_dict = {}
                            stat_dict["team_abrv"] = abrvs[i - 1]
                            stat_dict["team_name"] = teams[i - 1]
                            stat_dict["first_downs"] = stats_df.iloc[0][i] if stats_df.iloc[0][i] else None
                            rush_stats = stats_df.iloc[1][i] if stats_df.iloc[1][i] else None
                            pass_stats = stats_df.iloc[2][i] if stats_df.iloc[2][i] else None
                            sack_stats = stats_df.iloc[3][i] if stats_df.iloc[3][i] else None
                            stat_dict["net_yards"] = stats_df.iloc[4][i] if stats_df.iloc[4][i] else None
                            stat_dict["total_yards"] = stats_df.iloc[5][i] if stats_df.iloc[5][i] else None
                            fumbles = stats_df.iloc[6][i] if stats_df.iloc[6][i] else None
                            stat_dict["turnovers"] = stats_df.iloc[7][i] if stats_df.iloc[7][i] else None
                            penalty_stats = stats_df.iloc[8][i] if stats_df.iloc[8][i] else None
                            third_down = stats_df.iloc[9][i] if stats_df.iloc[9][i] else None
                            stat_dict["fourth_down"] = stats_df.iloc[10][i] if stats_df.iloc[10][i] else None
                            stat_dict["time_pos"] = stats_df.iloc[11][i] if stats_df.iloc[11][i] else None

                            drive_team = "vis_drives" if i == 1 else "home_drives"

                            home_drive_table = re.search(
                                f'(<table class="sortable stats_table" id="{drive_team}")(.*)(<\/table>)',
                                game_response.decode("latin-1"),
                                re.DOTALL | re.MULTILINE,
                            )
                            drives = None

                            # drive information
                            if home_drive_table:
                                drive_columns = [
                                    "#",
                                    "quarter",
                                    "time",
                                    "los",
                                    "plays",
                                    "length",
                                    "net_yds",
                                    "result",
                                    "team_abrv",
                                    "game_url",
                                    "game_date",
                                ]

                                logging.info("About to grab the drive table")
                                drive_dfs = pd.read_html(f"<html>{home_drive_table[0]}</html>")
                                drive_df = drive_dfs[0]
                                drives = len(drive_df)
                                drive_text = str(drive_df["Result"])

                                if "End of Game" in drive_text:
                                    drives = drives - 1
                                if "End of Half" in drive_text:
                                    drives = drives - 1
                                if "0 0" in drive_text:
                                    drives = drives - 1

                                stat_dict["drives"] = str(drives)

                                home_abrv_check = url.split(".htm")[0][-3:]

                                for index, row in drive_df.iterrows():
                                    start_line = (
                                        int(row["LOS"].split(" ")[1])
                                        if type(row["LOS"]) is str and row["LOS"] != "50"
                                        else 50
                                    )

                                    if start_line != 50 and home_abrv_check not in row["LOS"].lower():
                                        start_line = 100 - start_line
                                    drive_df.at[index, "LOS"] = start_line

                                    drive_df["team_abrv"] = stat_dict["team_abrv"]
                                    drive_df["game_url"] = game_dict["game_url"]
                                    drive_df["game_date"] = game_dict["game_date"]

                                drive_df.columns = drive_columns
                                drive_ls = drive_ls + drive_df.to_dict(orient="records")

                            stat_dict["game_url"] = game_dict["game_url"]
                            stat_dict["game_date"] = game_dict["game_date"]
                            stat_dict["rush_attempts"] = rush_stats.split("-")[0] if rush_stats is not np.nan else None
                            stat_dict["rush_yards"] = rush_stats.split("-")[1] if rush_stats is not np.nan else None
                            stat_dict["rush_tds"] = rush_stats.split("-")[2] if rush_stats is not np.nan else None

                            stat_dict["pass_comp"] = pass_stats.split("-")[0] if pass_stats is not np.nan else None
                            stat_dict["pass_att"] = pass_stats.split("-")[1] if pass_stats is not np.nan else None
                            stat_dict["pass_yards"] = pass_stats.split("-")[2] if pass_stats is not np.nan else None
                            stat_dict["pass_tds"] = pass_stats.split("-")[3] if pass_stats is not np.nan else None
                            stat_dict["pass_ints"] = pass_stats.split("-")[4] if pass_stats is not np.nan else None

                            stat_dict["sacks"] = sack_stats.split("-")[0] if fumbles is not np.nan else None
                            stat_dict["sack_yards"] = sack_stats.split("-")[1] if fumbles is not np.nan else None

                            stat_dict["fumbles_total"] = fumbles.split("-")[0] if fumbles is not np.nan else None
                            stat_dict["fumbles_lost"] = fumbles.split("-")[1] if fumbles is not np.nan else None

                            stat_dict["penalty_count"] = (
                                penalty_stats.split("-")[0] if penalty_stats is not np.nan else None
                            )
                            stat_dict["penalty_yards"] = (
                                penalty_stats.split("-")[1] if penalty_stats is not np.nan else None
                            )

                            stat_dict["third_down_conv"] = third_down.split("-")[0] if third_down is not np.nan else None
                            stat_dict["third_down_att"] = third_down.split("-")[1] if third_down is not np.nan else None
                            team_ls.append(stat_dict)
                        
                        pattern = re.compile(r'(?:<div class="table_container" id="div_pbp">)([\S\s]*)(?:</div>)')
                        matches = pattern.findall(game_response.decode("latin-1"))
                        plays_ls = []

                        # play by play data
                        if len(matches) > 0:
                            play_by_play_df = pd.read_html(matches[0].replace("\n", "").strip())[0]

                            play_df = play_by_play_df[play_by_play_df.Quarter.notna()]
                            play_df = play_df[
                                (play_df.Quarter.str.endswith("Quarter") == False) &
                                (play_df.Quarter.str.endswith("Regulation") == False)
                            ]
                            play_df.columns = [
                                'quarter', 
                                'time', 
                                'down', 
                                'to_go', 
                                'location', 
                                'away', 
                                'home', 
                                'play_description',
                                'epb', 
                                'epa',
                            ]

                            play_df["game_url"] = game_dict["game_url"]
                            play_df["game_date"] = game_dict["game_date"]
                            play_df["home_abrv"] = NFL_ABRV[game_dict["home_team"]]
                            play_df["away_abrv"] = NFL_ABRV[game_dict["away_team"]]
                            play_df["player_name"] = play_df["play_description"].apply(lambda x: derive_player_name(x))
                            play_df["play_category"] = play_df["play_description"].apply(lambda x: derive_play_category(x))
                            play_df["field_side"] = play_df["location"].apply(lambda x: derive_field_side(x, False))
                            play_df["yard_line"] = play_df["location"].apply(lambda x: derive_field_side(x, True))
                            play_df["next_yard_line"] = play_df["yard_line"].shift(-1)
                            play_df["next_field_side"] = play_df["field_side"].shift(-1)
                            play_df["yards"] = play_df.apply(lambda x: derive_yards(
                                field_side=x["field_side"],
                                yard_line=x["yard_line"],
                                next_field_side=x["next_field_side"],
                                next_yard_line=x["next_yard_line"],
                            ), axis=1)

                            plays_ls = plays_ls + play_df.to_dict(orient="records")

                        game_dict["offensive_drives"] = drive_ls
                        game_dict["box_score"] = team_ls
                        game_dict["play_by_play"] = plays_ls
                        game_ls.append(game_dict)
                
        except Exception as e:
            print(f"Ran into an error:\n{e}")

    return game_ls


class GameScraper:
    def scrape_week(self, year, week, proxies=None):
        try:
            return scrape_games(year=year, week=week, proxies=proxies)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return


def main(year: int, week: int):
    g = GameScraper()
    stats = g.scrape_week(year=year, week=week)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Crawl the pro-football-reference game result pages for a year NFL year and week provided."
    )
    parser.add_argument(
        "--year",
        required=False,
        help="The NFL season year...",
    )
    parser.add_argument(
        "--week",
        required=False,
        help="The week number to crawl...",
    )
    args = parser.parse_args()
    main(args.year, args.week)
