"""NBA teams (30 franchises, Eastern + Western Conference)."""

NBA_TEAMS = [
    # Eastern Conference - Atlantic
    ("Boston Celtics",        "Boston Celtics",        "Eastern"),
    ("Brooklyn Nets",         "Brooklyn Nets",         "Eastern"),
    ("New York Knicks",       "New York Knicks",       "Eastern"),
    ("Philadelphia 76ers",    "Philadelphia 76ers",    "Eastern"),
    ("Toronto Raptors",       "Toronto Raptors",       "Eastern"),
    # Eastern Conference - Central
    ("Chicago Bulls",         "Chicago Bulls",         "Eastern"),
    ("Cleveland Cavaliers",   "Cleveland Cavaliers",   "Eastern"),
    ("Detroit Pistons",       "Detroit Pistons",       "Eastern"),
    ("Indiana Pacers",        "Indiana Pacers",        "Eastern"),
    ("Milwaukee Bucks",       "Milwaukee Bucks",       "Eastern"),
    # Eastern Conference - Southeast
    ("Atlanta Hawks",         "Atlanta Hawks",         "Eastern"),
    ("Charlotte Hornets",     "Charlotte Hornets",     "Eastern"),
    ("Miami Heat",            "Miami Heat",            "Eastern"),
    ("Orlando Magic",         "Orlando Magic",         "Eastern"),
    ("Washington Wizards",    "Washington Wizards",    "Eastern"),
    # Western Conference - Northwest
    ("Denver Nuggets",        "Denver Nuggets",        "Western"),
    ("Minnesota Timberwolves", "Minnesota Timberwolves", "Western"),
    ("Oklahoma City Thunder", "Oklahoma City Thunder", "Western"),
    ("Portland Trail Blazers", "Portland Trail Blazers", "Western"),
    ("Utah Jazz",             "Utah Jazz",             "Western"),
    # Western Conference - Pacific
    ("Golden State Warriors", "Golden State Warriors", "Western"),
    ("LA Clippers",           "Los Angeles Clippers",  "Western"),
    ("Los Angeles Lakers",    "Los Angeles Lakers",    "Western"),
    ("Phoenix Suns",          "Phoenix Suns",          "Western"),
    ("Sacramento Kings",      "Sacramento Kings",      "Western"),
    # Western Conference - Southwest
    ("Dallas Mavericks",      "Dallas Mavericks",      "Western"),
    ("Houston Rockets",       "Houston Rockets",       "Western"),
    ("Memphis Grizzlies",     "Memphis Grizzlies",     "Western"),
    ("New Orleans Pelicans",  "New Orleans Pelicans",  "Western"),
    ("San Antonio Spurs",     "San Antonio Spurs",     "Western"),
]

ALL = [t[0] for t in NBA_TEAMS]
WIKIPEDIA = {t[0]: t[1] for t in NBA_TEAMS}
CONFERENCES = {t[0]: t[2] for t in NBA_TEAMS}


def _slug(name):
    return name.lower().replace(" ", "_")


LOGOS = {name: f"/static/logos/{_slug(name)}.png" for name, *_ in NBA_TEAMS}
