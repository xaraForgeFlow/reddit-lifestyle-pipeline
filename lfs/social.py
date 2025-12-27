from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE SOCIAL CONNECTION / ISOLATION SIGNALS
# =========================================================

def lf_social_lonely(post):
    if "lonely" in _text(post):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_loneliness(post):
    if "loneliness" in _text(post):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_isolation(post):
    t = _text(post)
    if "isolated" in t or "isolation" in t or "social isolation" in t:
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_disconnected(post):
    t = _text(post)
    if "feel disconnected" in t or "disconnected from others" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 2. SOCIAL SUPPORT / BELONGING
# =========================================================

def lf_social_social_support(post):
    if "social support" in _text(post):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_support_system(post):
    t = _text(post)
    patterns = [
        "support system",
        "people who support me",
        "emotional support",
    ]
    if any(p in t for p in patterns):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_belonging(post):
    t = _text(post)
    if "sense of belonging" in t or "feel like i belong" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 3. LACK OF SOCIAL CONNECTION / COMPLAINTS
# =========================================================

def lf_social_no_friends(post):
    t = _text(post)
    patterns = [
        "no friends",
        "don't have friends",
        "have no friends",
        "no close friends",
    ]
    if any(p in t for p in patterns):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_no_one_to_talk_to(post):
    t = _text(post)
    if "no one to talk to" in t or "nobody to talk to" in t:
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_feel_unwanted(post):
    t = _text(post)
    if "feel unwanted" in t or "feel invisible" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 4. SOCIAL ANXIETY / AVOIDANCE
# =========================================================

def lf_social_social_anxiety(post):
    if "social anxiety" in _text(post):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_awkwardness(post):
    t = _text(post)
    if "socially awkward" in t or "awkward socially" in t:
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_avoid_people(post):
    t = _text(post)
    patterns = [
        "avoid people",
        "hate being around people",
        "don't like being around people",
        "avoid social situations",
    ]
    if any(p in t for p in patterns):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_fear_of_rejection(post):
    t = _text(post)
    if "fear of rejection" in t or "afraid of rejection" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 5. SOCIAL WITHDRAWAL / DISENGAGEMENT
# =========================================================

def lf_social_withdrawal(post):
    t = _text(post)
    patterns = [
        "social withdrawal",
        "withdrawing from people",
        "stopped talking to people",
    ]
    if any(p in t for p in patterns):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_staying_home(post):
    t = _text(post)
    if "stay home all the time" in t or "never go out" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 6. RELATIONSHIPS / INTERPERSONAL CONTEXT
# =========================================================

def lf_social_relationship(post):
    if "relationship" in _text(post):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_breakup(post):
    t = _text(post)
    if "breakup" in t or "broke up" in t or "divorce" in t:
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_conflict(post):
    t = _text(post)
    if "relationship conflict" in t or "constant arguing" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 7. ATTACHMENT / TRUST / CONNECTION
# =========================================================

def lf_social_attachment_issues(post):
    t = _text(post)
    if "attachment issues" in t or "fear of attachment" in t:
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_trust_issues(post):
    t = _text(post)
    if "trust issues" in t or "can't trust people" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 8. SOCIAL ENGAGEMENT / PARTICIPATION (POSITIVE!)
# =========================================================

def lf_social_social_engagement(post):
    t = _text(post)
    patterns = [
        "social engagement",
        "social life",
        "spend time with friends",
    ]
    if any(p in t for p in patterns):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_community(post):
    t = _text(post)
    if "community" in t or "community support" in t:
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_volunteering(post):
    if "volunteer" in _text(post) or "volunteering" in _text(post):
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 9. RECOVERY / IMPROVING CONNECTION (IMPORTANT)
# =========================================================

def lf_social_reconnecting(post):
    t = _text(post)
    patterns = [
        "reconnecting with people",
        "making new friends",
        "working on my social life",
    ]
    if any(p in t for p in patterns):
        return Pillar.SOCIAL
    return ABSTAIN


def lf_social_feel_connected(post):
    t = _text(post)
    if "feel connected" in t or "closer to people" in t:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 10. SUBREDDIT CONTEXT
# =========================================================

def lf_social_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "lonely",
        "socialanxiety",
        "relationships",
        "relationship_advice",
        "dating_advice",
        "friendship",
        "needafriend",
    }:
        return Pillar.SOCIAL
    return ABSTAIN


# =========================================================
# 11. EXCLUSION / SAFETY LFs
# =========================================================

def lf_social_metaphor_exclusion(post):
    t = _text(post)
    if "that song made me feel lonely" in t or "lonely road" in t:
        return ABSTAIN
    return ABSTAIN


def lf_social_positive_solitude(post):
    t = _text(post)
    if "enjoy being alone" in t or "like solitude" in t:
        return ABSTAIN
    return ABSTAIN
