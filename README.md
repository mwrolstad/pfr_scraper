# sports_line_scraper

An easy tool to scrape the game data from pro-football-reference.com

* Simply provide two variables to get the entire weeks worth of game data that week
  * `year`
  * `week`

### Use as a command line:

```cmd
python3 src/pfr_scraper/__init__.py --year 2022 --week 20
```

### Import and use as a package:

```python
from src.pfr_scraper import GameScraper
import json
game_scraper = GameScraper()
stats = game_scraper(nfl_year=2022, nfl_week=20)
print(json.dumps(stats[0], indent=2))
{
  "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
  "away_team": "Jacksonville Jaguars",
  "home_team": "Kansas City Chiefs",
  "away_abrv": "JAX",
  "home_abrv": "KC",
  "game_date": "20230121",
  "player_stats": [
    {
      "player": "Trevor Lawrence",
      "team_abrv": "JAX",
      "passing_cmp": "24",
      "passing_att": "39",
      "passing_yds": "217",
      "passing_tD": "1",
      "passing_int": "1",
      "passing_sk": "2",
      "passing_sk_yds": "12",
      "passing_lng": "37",
      "passing_rate": "74.4",
      "pushing_att": "3",
      "rushing_yds": "26",
      "rushing_td": "0",
      "rushing_lng": "12",
      "receiving_tgt": "0",
      "receiving_rec": "0",
      "receiving_yds": "0",
      "receiving_td": "0",
      "receiving_lng": "0",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Travis Etienne",
      "team_abrv": "JAX",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "10",
      "rushing_yds": "62",
      "rushing_td": "1",
      "rushing_lng": "19",
      "receiving_tgt": "3",
      "receiving_rec": "3",
      "receiving_yds": "18",
      "receiving_td": "0",
      "receiving_lng": "9",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Jamycal Hasty",
      "team_abrv": "JAX",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "4",
      "rushing_yds": "36",
      "rushing_td": "0",
      "rushing_lng": "23",
      "receiving_tgt": "2",
      "receiving_rec": "1",
      "receiving_yds": "7",
      "receiving_td": "0",
      "receiving_lng": "7",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Christian Kirk",
      "team_abrv": "JAX",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "1",
      "rushing_yds": "18",
      "rushing_td": "0",
      "rushing_lng": "18",
      "receiving_tgt": "14",
      "receiving_rec": "7",
      "receiving_yds": "52",
      "receiving_td": "1",
      "receiving_lng": "15",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Jamal Agnew",
      "team_abrv": "JAX",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "1",
      "rushing_yds": "2",
      "rushing_td": "0",
      "rushing_lng": "2",
      "receiving_tgt": "3",
      "receiving_rec": "2",
      "receiving_yds": "5",
      "receiving_td": "0",
      "receiving_lng": "3",
      "fumbles_fmb": "1",
      "fumbles_fl": "1",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Zay Jones",
      "team_abrv": "JAX",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "7",
      "receiving_rec": "5",
      "receiving_yds": "83",
      "receiving_td": "0",
      "receiving_lng": "37",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Evan Engram",
      "team_abrv": "JAX",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "6",
      "receiving_rec": "5",
      "receiving_yds": "31",
      "receiving_td": "0",
      "receiving_lng": "16",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Marvin Jones",
      "team_abrv": "JAX",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "3",
      "receiving_rec": "1",
      "receiving_yds": "21",
      "receiving_td": "0",
      "receiving_lng": "21",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Patrick Mahomes",
      "team_abrv": "KC",
      "passing_cmp": "22",
      "passing_att": "30",
      "passing_yds": "195",
      "passing_tD": "2",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "27",
      "passing_rate": "112.5",
      "pushing_att": "3",
      "rushing_yds": "8",
      "rushing_td": "0",
      "rushing_lng": "5",
      "receiving_tgt": "0",
      "receiving_rec": "0",
      "receiving_yds": "0",
      "receiving_td": "0",
      "receiving_lng": "0",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Chad Henne",
      "team_abrv": "KC",
      "passing_cmp": "5",
      "passing_att": "7",
      "passing_yds": "23",
      "passing_tD": "1",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "8",
      "passing_rate": "114.9",
      "pushing_att": "1",
      "rushing_yds": "-1",
      "rushing_td": "0",
      "rushing_lng": "-1",
      "receiving_tgt": "0",
      "receiving_rec": "0",
      "receiving_yds": "0",
      "receiving_td": "0",
      "receiving_lng": "0",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Isiah Pacheco",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "12",
      "rushing_yds": "95",
      "rushing_td": "0",
      "rushing_lng": "39",
      "receiving_tgt": "1",
      "receiving_rec": "1",
      "receiving_yds": "6",
      "receiving_td": "0",
      "receiving_lng": "6",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Jerick McKinnon",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "11",
      "rushing_yds": "25",
      "rushing_td": "0",
      "rushing_lng": "7",
      "receiving_tgt": "0",
      "receiving_rec": "0",
      "receiving_yds": "0",
      "receiving_td": "0",
      "receiving_lng": "0",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Kadarius Toney",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "1",
      "rushing_yds": "14",
      "rushing_td": "0",
      "rushing_lng": "14",
      "receiving_tgt": "7",
      "receiving_rec": "5",
      "receiving_yds": "36",
      "receiving_td": "0",
      "receiving_lng": "9",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Skyy Moore",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "1",
      "rushing_yds": "3",
      "rushing_td": "0",
      "rushing_lng": "3",
      "receiving_tgt": "1",
      "receiving_rec": "1",
      "receiving_yds": "0",
      "receiving_td": "0",
      "receiving_lng": "0",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Travis Kelce",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "17",
      "receiving_rec": "14",
      "receiving_yds": "98",
      "receiving_td": "2",
      "receiving_lng": "15",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "JuJu Smith-Schuster",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "2",
      "receiving_rec": "2",
      "receiving_yds": "29",
      "receiving_td": "0",
      "receiving_lng": "16",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Noah Gray",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "1",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "2",
      "receiving_rec": "1",
      "receiving_yds": "27",
      "receiving_td": "0",
      "receiving_lng": "27",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Justin Watson",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "1",
      "receiving_rec": "1",
      "receiving_yds": "12",
      "receiving_td": "0",
      "receiving_lng": "12",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Marquez Valdes-Scantling",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "2",
      "receiving_rec": "1",
      "receiving_yds": "6",
      "receiving_td": "1",
      "receiving_lng": "6",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    },
    {
      "player": "Blake Bell",
      "team_abrv": "KC",
      "passing_cmp": "0",
      "passing_att": "0",
      "passing_yds": "0",
      "passing_tD": "0",
      "passing_int": "0",
      "passing_sk": "0",
      "passing_sk_yds": "0",
      "passing_lng": "0",
      "passing_rate": 0,
      "pushing_att": "0",
      "rushing_yds": "0",
      "rushing_td": "0",
      "rushing_lng": "0",
      "receiving_tgt": "2",
      "receiving_rec": "1",
      "receiving_yds": "4",
      "receiving_td": "0",
      "receiving_lng": "4",
      "fumbles_fmb": "0",
      "fumbles_fl": "0",
      "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
      "game_date": "20230121"
    }
  ],
  "offensive_drives": [
    [
      {
        "#": 1,
        "quarter": 1,
        "time": "15:00",
        "los": 75,
        "plays": 3,
        "length": "1:04",
        "net_yds": 6,
        "result": "Punt",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 2,
        "quarter": 1,
        "time": "7:56",
        "los": 61,
        "plays": 5,
        "length": "2:52",
        "net_yds": 39,
        "result": "Touchdown",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 3,
        "quarter": 2,
        "time": "14:09",
        "los": 75,
        "plays": 7,
        "length": "4:10",
        "net_yds": 36,
        "result": "Punt",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 4,
        "quarter": 2,
        "time": "3:54",
        "los": 75,
        "plays": 11,
        "length": "3:27",
        "net_yds": 52,
        "result": "Field Goal",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 5,
        "quarter": 3,
        "time": "12:02",
        "los": 85,
        "plays": 7,
        "length": "3:36",
        "net_yds": 25,
        "result": "Punt",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 6,
        "quarter": 3,
        "time": "6:08",
        "los": 89,
        "plays": 6,
        "length": "3:43",
        "net_yds": 11,
        "result": "Punt",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 7,
        "quarter": 3,
        "time": "0:08",
        "los": 75,
        "plays": 7,
        "length": "3:19",
        "net_yds": 75,
        "result": "Touchdown",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 8,
        "quarter": 4,
        "time": "7:08",
        "los": 55,
        "plays": 8,
        "length": "1:39",
        "net_yds": 49,
        "result": "Fumble",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 9,
        "quarter": 4,
        "time": "4:18",
        "los": 54,
        "plays": 2,
        "length": "0:30",
        "net_yds": 4,
        "result": "Interception",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 10,
        "quarter": 4,
        "time": "1:04",
        "los": 67,
        "plays": 6,
        "length": "0:39",
        "net_yds": 37,
        "result": "Field Goal",
        "team_abrv": "JAX",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      }
    ],
    [
      {
        "#": 1,
        "quarter": 1,
        "time": "13:56",
        "los": 83,
        "plays": 12,
        "length": "6:00",
        "net_yds": 83,
        "result": "Touchdown",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 2,
        "quarter": 1,
        "time": "5:04",
        "los": 75,
        "plays": 11,
        "length": "5:55",
        "net_yds": 43,
        "result": "Field Goal",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 3,
        "quarter": 2,
        "time": "9:59",
        "los": 98,
        "plays": 12,
        "length": "6:05",
        "net_yds": 98,
        "result": "Touchdown",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 4,
        "quarter": 2,
        "time": "0:27",
        "los": 75,
        "plays": 1,
        "length": "0:27",
        "net_yds": -1,
        "result": "End of Half",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 5,
        "quarter": 3,
        "time": "15:00",
        "los": 75,
        "plays": 6,
        "length": "2:58",
        "net_yds": 13,
        "result": "Punt",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 6,
        "quarter": 3,
        "time": "8:26",
        "los": 80,
        "plays": 3,
        "length": "2:18",
        "net_yds": 9,
        "result": "Punt",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 7,
        "quarter": 3,
        "time": "2:25",
        "los": 61,
        "plays": 5,
        "length": "2:17",
        "net_yds": 29,
        "result": "Field Goal",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 8,
        "quarter": 4,
        "time": "11:49",
        "los": 75,
        "plays": 10,
        "length": "4:41",
        "net_yds": 75,
        "result": "Touchdown",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 9,
        "quarter": 4,
        "time": "5:29",
        "los": 97,
        "plays": 3,
        "length": "1:11",
        "net_yds": 9,
        "result": "Punt",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 10,
        "quarter": 4,
        "time": "3:48",
        "los": 84,
        "plays": 5,
        "length": "2:44",
        "net_yds": 20,
        "result": "Punt",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      },
      {
        "#": 11,
        "quarter": 4,
        "time": "0:25",
        "los": 54,
        "plays": 1,
        "length": "0:25",
        "net_yds": -1,
        "result": "End of Game",
        "team_abrv": "KC",
        "game_url": "https://www.pro-football-reference.com/boxscores/202301210kan.htm",
        "game_date": "20230121"
      }
    ]
  ],
  "box_score": [
    {
      "team_abrv": "JAX",
      "team_name": "Jacksonville Jaguars",
      "first_downs": "20",
      "net_yards": "205",
      "total_yards": "349",
      "turnovers": "2",
      "fourth_down": "0-0",
      "time_pos": "24:59",
      "drives": "10",
      "rush_attempts": "19",
      "rush_yards": "144",
      "rush_tds": "1",
      "pass_comp": "24",
      "pass_att": "39",
      "pass_yards": "217",
      "pass_tds": "1",
      "pass_ints": "1",
      "sacks": "2",
      "sack_yards": "12",
      "fumbles_total": "1",
      "fumbles_lost": "1",
      "penalty_count": "5",
      "penalty_yards": "40",
      "third_down_conv": "7",
      "third_down_att": "13"
    },
    {
      "team_abrv": "KC",
      "team_name": "Kansas City Chiefs",
      "first_downs": "23",
      "net_yards": "218",
      "total_yards": "362",
      "turnovers": "0",
      "fourth_down": "0-0",
      "time_pos": "35:01",
      "drives": "9",
      "rush_attempts": "30",
      "rush_yards": "144",
      "rush_tds": "0",
      "pass_comp": "27",
      "pass_att": "37",
      "pass_yards": "218",
      "pass_tds": "3",
      "pass_ints": "0",
      "sacks": "0",
      "sack_yards": "0",
      "fumbles_total": "0",
      "fumbles_lost": "0",
      "penalty_count": "3",
      "penalty_yards": "30",
      "third_down_conv": "6",
      "third_down_att": "12"
    }
  ]
}
```
