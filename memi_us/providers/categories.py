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
from memi_us.categories.nfl import (
    ALL as NFL_LIST,
    WIKIPEDIA as NFL_WIKI,
    CONFERENCES as NFL_CONF,
)
from memi_us.categories.monuments import (
    ALL as MONUMENT_LIST,
    WIKIPEDIA as MONUMENT_WIKI,
    LOCATIONS as MONUMENT_LOCATIONS,
)
from memi_us.categories.people import ALL as PEOPLE_LIST
from memi_us.categories.landscapes import (
    ALL as LANDSCAPE_LIST,
    WIKIPEDIA as LANDSCAPE_WIKI,
    LOCATIONS as LANDSCAPE_LOCATIONS,
)
from memi_us.categories.animals import (
    ALL as ANIMAL_LIST,
    WIKIPEDIA as ANIMAL_WIKI,
    SCIENTIFIC_NAMES as ANIMAL_SCIENTIFIC,
)
from memi_us.categories.plants import (
    ALL as PLANT_LIST,
    WIKIPEDIA as PLANT_WIKI,
    SCIENTIFIC_NAMES as PLANT_SCIENTIFIC,
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


_NFL_CONF_FILTER = {
    "afc": [name for name, c in NFL_CONF.items() if c == "AFC"],
    "nfc": [name for name, c in NFL_CONF.items() if c == "NFC"],
}


class NFLTeamsProvider(CategoryProvider):
    key = "sports:nfl teams"
    items = NFL_LIST
    override_name = True
    filters = {"conference": _NFL_CONF_FILTER}

    def get_image(self, item):
        return images.get_wikipedia_image(NFL_WIKI.get(item, item))

    def get_tag(self, item):
        return f"{NFL_CONF.get(item, '')} Conference"


class MonumentsProvider(CategoryProvider):
    key = "culture:monuments"
    items = MONUMENT_LIST
    override_name = True

    def get_image(self, item):
        return images.get_wikipedia_image(MONUMENT_WIKI.get(item, item))

    def get_tag(self, item):
        return MONUMENT_LOCATIONS.get(item)


class PeopleProvider(CategoryProvider):
    key = "culture:people"
    items = PEOPLE_LIST

    def get_tag(self, item):
        desc = images.get_wikipedia_description(item)
        if desc:
            desc = desc.replace("(born ", "(").replace("(", "").replace(")", "")
            return desc
        return None


class LandscapesProvider(CategoryProvider):
    key = "nature:landscapes"
    items = LANDSCAPE_LIST
    override_name = True

    def get_image(self, item):
        return images.get_wikipedia_image(LANDSCAPE_WIKI.get(item, item))

    def get_tag(self, item):
        return LANDSCAPE_LOCATIONS.get(item)


class AnimalsProvider(CategoryProvider):
    key = "nature:animals"
    items = ANIMAL_LIST
    override_name = True

    def get_image(self, item):
        return images.get_wikipedia_image(ANIMAL_WIKI.get(item, item))

    def get_tag(self, item):
        sci = ANIMAL_SCIENTIFIC.get(item, "")
        if sci and sci.lower() != item.lower():
            return sci
        return None


class PlantsProvider(CategoryProvider):
    key = "nature:plants"
    items = PLANT_LIST
    override_name = True

    def get_image(self, item):
        return images.get_wikipedia_image(PLANT_WIKI.get(item, item))

    def get_tag(self, item):
        sci = PLANT_SCIENTIFIC.get(item, "")
        if sci and sci.lower() != item.lower():
            return sci
        return None


register(StateFlagsProvider())
register(StateCapitalsProvider())
register(StateShapesProvider())
register(NBATeamsProvider())
register(NFLTeamsProvider())
register(MonumentsProvider())
register(PeopleProvider())
register(LandscapesProvider())
register(AnimalsProvider())
register(PlantsProvider())
