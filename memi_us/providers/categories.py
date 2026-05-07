"""US category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_us.categories.states import (
    ALL as STATE_LIST,
    ABBREVIATIONS as STATE_ABBREVS,
    CAPITALS as STATE_CAPITALS,
    REGIONS as STATE_REGIONS,
)
from memi_us.categories.nba import (
    ALL as NBA_LIST,
    WIKIPEDIA as NBA_WIKI,
    CONFERENCES as NBA_CONF,
    LOGOS as NBA_LOGOS,
)


def _state_map(state):
    """Locator map for a US state from Wikimedia Commons."""
    abbr = STATE_ABBREVS.get(state)
    if not abbr:
        return None
    return images.get_commons_file_image(f"Map of USA {abbr}.svg")


class StateFlagsProvider(CategoryProvider):
    key = "geography:states:flags"
    items = STATE_LIST
    filters = {"region": STATE_REGIONS}

    def get_image(self, item):
        clean_name = item.split("(")[0].strip()
        result = images.get_wikipedia_image("Flag of " + clean_name)
        if result and result.get("image"):
            result["name"] = clean_name
            return result
        return None


class StateCapitalsProvider(CategoryProvider):
    key = "geography:states:capitals"
    items = STATE_LIST
    filters = {"region": STATE_REGIONS}

    def get_image(self, item):
        result = _state_map(item)
        if result:
            clean_name = item.split("(")[0].strip()
            capital = STATE_CAPITALS.get(item, "Unknown")
            result["clue"] = clean_name
            result["name"] = capital
            return result
        return None

    def get_clue(self, item):
        return item.split("(")[0].strip()


class StateShapesProvider(CategoryProvider):
    key = "geography:states:shapes"
    items = STATE_LIST
    filters = {"region": STATE_REGIONS}

    def get_image(self, item):
        result = _state_map(item)
        if result:
            result["name"] = item.split("(")[0].strip()
            return result
        return None


_NBA_CONF_FILTER = {
    "eastern": [name for name, c in NBA_CONF.items() if c == "Eastern"],
    "western": [name for name, c in NBA_CONF.items() if c == "Western"],
}


class NBATeamsProvider(CategoryProvider):
    key = "sports:nba teams"
    items = NBA_LIST
    light_bg = True
    override_name = True
    filters = {"conference": _NBA_CONF_FILTER}

    def get_image(self, item):
        logo = NBA_LOGOS.get(item)
        if logo:
            return {"name": item, "image": logo}
        return images.get_wikipedia_image(NBA_WIKI.get(item, item))

    def get_tag(self, item):
        return f"{NBA_CONF.get(item, '')} Conference"


register(StateFlagsProvider())
register(StateCapitalsProvider())
register(StateShapesProvider())
register(NBATeamsProvider())
