from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE LIFE PURPOSE / MEANING LFs
# =========================================================

def lf_purpose_life_purpose(post):
    t = _text(post)
    if "life purpose" in t or "purpose in life" in t:
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_life_meaning(post):
    t = _text(post)
    if "life meaning" in t or "meaning of life" in t:
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_no_purpose(post):
    t = _text(post)
    if "no purpose" in t or "without purpose" in t:
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_lack_of_meaning(post):
    t = _text(post)
    if "lack of meaning" in t or "life feels meaningless" in t:
        return Pillar.PURPOSE
    return ABSTAIN


# =========================================================
# 2. EXISTENTIAL DISTRESS / NIHILISM
# =========================================================

def lf_purpose_existential_crisis(post):
    if "existential crisis" in _text(post):
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_nothing_matters(post):
    t = _text(post)
    patterns = [
        "nothing matters",
        "nothing feels meaningful",
        "everything feels pointless",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_why_am_i_here(post):
    t = _text(post)
    if "why am i here" in t or "what's the point of life" in t:
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_lost_direction(post):
    t = _text(post)
    patterns = [
        "lost in life",
        "feel lost",
        "directionless",
        "no direction in life",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


# =========================================================
# 3. ANHEDONIA / EMOTIONAL FLATNESS
# =========================================================

def lf_purpose_anhedonia(post):
    if "anhedonia" in _text(post):
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_no_motivation(post):
    t = _text(post)
    patterns = [
        "no motivation",
        "lost motivation",
        "no drive",
        "zero motivation",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_emptiness(post):
    t = _text(post)
    if "feel empty" in t or "emptiness" in t:
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_disinterest(post):
    t = _text(post)
    patterns = [
        "don't care about anything",
        "nothing excites me",
        "nothing brings joy",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


# =========================================================
# 4. IDENTITY / VALUES / FUTURE ORIENTATION
# =========================================================

def lf_purpose_identity_crisis(post):
    if "identity crisis" in _text(post):
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_no_goals(post):
    t = _text(post)
    if "no goals" in t or "lost my goals" in t:
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_future_void(post):
    t = _text(post)
    patterns = [
        "no future",
        "future feels pointless",
        "can't imagine a future",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_values_conflict(post):
    t = _text(post)
    patterns = [
        "don't know what i want in life",
        "questioning my values",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


# =========================================================
# 5. POSITIVE PURPOSE SEEKING (IMPORTANT!)
# =========================================================

def lf_purpose_searching_for_meaning(post):
    t = _text(post)
    patterns = [
        "searching for meaning",
        "trying to find my purpose",
        "looking for direction in life",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


def lf_purpose_self_reflection(post):
    t = _text(post)
    patterns = [
        "reflecting on my life",
        "re-evaluating my life",
    ]
    if any(p in t for p in patterns):
        return Pillar.PURPOSE
    return ABSTAIN


# =========================================================
# 6. SUBREDDIT CONTEXT LFs
# =========================================================

def lf_purpose_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "existentialism",
        "findapath",
        "decidingtobebetter",
        "selfimprovement",
        "meaningoflife",
        "lifeadvice",
    }:
        return Pillar.PURPOSE
    return ABSTAIN


# =========================================================
# 7. EXCLUSION / SAFETY LFs
# =========================================================

def lf_purpose_philosophical_discussion_exclusion(post):
    t = _text(post)
    if "philosophy class" in t or "philosophy essay" in t:
        return ABSTAIN
    return ABSTAIN


def lf_purpose_quotes_exclusion(post):
    t = _text(post)
    if "quote" in t and "meaning of life" in t:
        return ABSTAIN
    return ABSTAIN


def lf_purpose_positive_resolution_exclusion(post):
    t = _text(post)
    if "found my purpose" in t or "life finally has meaning" in t:
        return ABSTAIN
    return ABSTAIN
