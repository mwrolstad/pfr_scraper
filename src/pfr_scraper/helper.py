import re
import datetime as dt


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
