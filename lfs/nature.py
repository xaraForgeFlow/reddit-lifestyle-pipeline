from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE NATURE / ENVIRONMENT LFs
# =========================================================

def lf_nature_general(post):
    if "nature" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_outdoors(post):
    t = _text(post)
    if "outdoors" in t or "outdoor" in t:
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_green_space(post):
    t = _text(post)
    if "green space" in t or "green spaces" in t or "park nearby" in t:
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_blue_space(post):
    t = _text(post)
    if "blue space" in t or "blue spaces" in t:
        return Pillar.NATURE
    return ABSTAIN


# =========================================================
# 2. GREEN ENVIRONMENTS (LAND-BASED)
# =========================================================

def lf_nature_forest(post):
    if "forest" in _text(post) or "woods" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_park(post):
    t = _text(post)
    if "park" in t or "parks" in t:
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_garden(post):
    t = _text(post)
    if "garden" in t or "gardening" in t:
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_mountains(post):
    if "mountain" in _text(post) or "mountains" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


# =========================================================
# 3. BLUE ENVIRONMENTS (WATER-BASED)
# =========================================================

def lf_nature_ocean_sea(post):
    t = _text(post)
    if "ocean" in t or "sea" in t:
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_beach(post):
    if "beach" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_lake_river(post):
    t = _text(post)
    if "lake" in t or "river" in t:
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_waterfall(post):
    if "waterfall" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


# =========================================================
# 4. NATURE-BASED ACTIVITIES / ADVENTURE
# =========================================================

def lf_nature_hiking(post):
    if "hiking" in _text(post) or "hike" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_camping(post):
    if "camping" in _text(post) or "camp site" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_trail(post):
    if "trail" in _text(post) or "nature trail" in _text(post):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_adventure(post):
    t = _text(post)
    if "adventure" in t or "exploring nature" in t:
        return Pillar.NATURE
    return ABSTAIN


# =========================================================
# 5. URBAN ESCAPE / EXPOSURE TO NATURE
# =========================================================

def lf_nature_escape_city(post):
    t = _text(post)
    patterns = [
        "escape the city",
        "get out of the city",
        "need more nature",
        "away from the city",
    ]
    if any(p in t for p in patterns):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_access(post):
    t = _text(post)
    patterns = [
        "access to nature",
        "lack of green space",
        "no parks nearby",
    ]
    if any(p in t for p in patterns):
        return Pillar.NATURE
    return ABSTAIN


# =========================================================
# 6. RESTORATIVE / WELLBEING CONTEXT
# =========================================================

def lf_nature_relaxation(post):
    t = _text(post)
    patterns = [
        "relaxing in nature",
        "nature calms me",
        "being outside helps",
        "fresh air helps",
    ]
    if any(p in t for p in patterns):
        return Pillar.NATURE
    return ABSTAIN


def lf_nature_mental_health(post):
    t = _text(post)
    patterns = [
        "nature helps my mental health",
        "outdoors helps my anxiety",
        "nature reduces my stress",
    ]
    if any(p in t for p in patterns):
        return Pillar.NATURE
    return ABSTAIN


# =========================================================
# 7. SUBREDDIT CONTEXT LFs
# =========================================================

def lf_nature_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "hiking",
        "camping",
        "outdoors",
        "nature",
        "earthporn",
        "getoutside",
        "nationalparks",
    }:
        return Pillar.NATURE
    return ABSTAIN


# =========================================================
# 8. EXCLUSION / SAFETY LFs
# =========================================================

def lf_nature_metaphor_exclusion(post):
    t = _text(post)
    if "human nature" in t or "by nature i am" in t:
        return ABSTAIN
    return ABSTAIN


def lf_nature_documentary_exclusion(post):
    t = _text(post)
    if "nature documentary" in t or "wildlife documentary" in t:
        return ABSTAIN
    return ABSTAIN


def lf_nature_game_exclusion(post):
    t = _text(post)
    if "game called nature" in t:
        return ABSTAIN
    return ABSTAIN
