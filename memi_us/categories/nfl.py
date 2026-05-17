"""NFL teams (32 franchises, AFC + NFC)."""

NFL_TEAMS = [
    # AFC East
    ("Buffalo Bills",         "Buffalo Bills",         "AFC"),
    ("Miami Dolphins",        "Miami Dolphins",        "AFC"),
    ("New England Patriots",  "New England Patriots",  "AFC"),
    ("New York Jets",         "New York Jets",         "AFC"),
    # AFC North
    ("Baltimore Ravens",      "Baltimore Ravens",      "AFC"),
    ("Cincinnati Bengals",    "Cincinnati Bengals",    "AFC"),
    ("Cleveland Browns",      "Cleveland Browns",      "AFC"),
    ("Pittsburgh Steelers",   "Pittsburgh Steelers",   "AFC"),
    # AFC South
    ("Houston Texans",        "Houston Texans",        "AFC"),
    ("Indianapolis Colts",    "Indianapolis Colts",    "AFC"),
    ("Jacksonville Jaguars",  "Jacksonville Jaguars",  "AFC"),
    ("Tennessee Titans",      "Tennessee Titans",      "AFC"),
    # AFC West
    ("Denver Broncos",        "Denver Broncos",        "AFC"),
    ("Kansas City Chiefs",    "Kansas City Chiefs",    "AFC"),
    ("Las Vegas Raiders",     "Las Vegas Raiders",     "AFC"),
    ("Los Angeles Chargers",  "Los Angeles Chargers",  "AFC"),
    # NFC East
    ("Dallas Cowboys",        "Dallas Cowboys",        "NFC"),
    ("New York Giants",       "New York Giants",       "NFC"),
    ("Philadelphia Eagles",   "Philadelphia Eagles",   "NFC"),
    ("Washington Commanders", "Washington Commanders", "NFC"),
    # NFC North
    ("Chicago Bears",         "Chicago Bears",         "NFC"),
    ("Detroit Lions",         "Detroit Lions",         "NFC"),
    ("Green Bay Packers",     "Green Bay Packers",     "NFC"),
    ("Minnesota Vikings",     "Minnesota Vikings",     "NFC"),
    # NFC South
    ("Atlanta Falcons",       "Atlanta Falcons",       "NFC"),
    ("Carolina Panthers",     "Carolina Panthers",     "NFC"),
    ("New Orleans Saints",    "New Orleans Saints",    "NFC"),
    ("Tampa Bay Buccaneers",  "Tampa Bay Buccaneers",  "NFC"),
    # NFC West
    ("Arizona Cardinals",     "Arizona Cardinals",     "NFC"),
    ("Los Angeles Rams",      "Los Angeles Rams",      "NFC"),
    ("San Francisco 49ers",   "San Francisco 49ers",   "NFC"),
    ("Seattle Seahawks",      "Seattle Seahawks",      "NFC"),
]

ALL = [t[0] for t in NFL_TEAMS]
WIKIPEDIA = {t[0]: t[1] for t in NFL_TEAMS}
CONFERENCES = {t[0]: t[2] for t in NFL_TEAMS}
