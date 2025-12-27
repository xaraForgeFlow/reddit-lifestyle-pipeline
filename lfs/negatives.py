from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


def _sub(post):
    return post.get("subreddit", "").lower()


# =========================================================
# 1. ENTERTAINMENT / MEDIA / FANDOM SUBREDDITS
# =========================================================

def lf_negative_gaming_subreddits(post):
    if _sub(post) in {
        "gaming",
        "leagueoflegends",
        "dota2",
        "valorant",
        "csgo",
        "wow",
        "minecraft",
        "fortnite",
        "pcgaming",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_movies_tv_subreddits(post):
    if _sub(post) in {
        "movies",
        "television",
        "netflix",
        "anime",
        "televisionsuggestions",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_music_subreddits(post):
    if _sub(post) in {
        "music",
        "listentothis",
        "hiphopheads",
        "popheads",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_books_comics(post):
    if _sub(post) in {
        "books",
        "comics",
        "manga",
        "lightnovels",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 2. MEMES / JOKES / SHITPOSTING (REDDIT-NATIVE NOISE)
# =========================================================

def lf_negative_meme_subreddits(post):
    if _sub(post) in {
        "memes",
        "dankmemes",
        "shitposting",
        "me_irl",
        "2meirl4meirl",
        "okbuddyretard",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_joking_language(post):
    t = _text(post)
    if any(x in t for x in {"lol", "lmao", "haha", "rofl", "xd"}):
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_low_effort(post):
    t = _text(post)
    if len(t.split()) < 5:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 3. POLITICS / NEWS / IDEOLOGY
# =========================================================

def lf_negative_politics_subreddits(post):
    if _sub(post) in {
        "politics",
        "worldnews",
        "news",
        "conservative",
        "liberal",
        "politicaldiscussion",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_political_language(post):
    t = _text(post)
    if any(x in t for x in {
        "election",
        "government",
        "politician",
        "policy",
        "lawmakers",
        "president",
    }):
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 4. TECH / CAREER / NON-LIFESTYLE PRACTICALS
# =========================================================

def lf_negative_programming(post):
    if _sub(post) in {
        "programming",
        "learnprogramming",
        "datascience",
        "machinelearning",
        "coding",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_finance(post):
    if _sub(post) in {
        "personalfinance",
        "investing",
        "stocks",
        "wallstreetbets",
        "cryptocurrency",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_career_only(post):
    t = _text(post)
    if "resume" in t or "job interview" in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 5. ABSTRACT / GENERALIZED / NON-PERSONAL SPEECH
# =========================================================

def lf_negative_general_advice(post):
    t = _text(post)
    if t.startswith("people should") or t.startswith("everyone needs to"):
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_third_person_only(post):
    t = _text(post)
    if "my friend" in t and "i feel" not in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_impersonal_language(post):
    t = _text(post)
    if "one must" in t or "society today" in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 6. METAPHOR / NON-LITERAL USE OF HEALTH TERMS
# =========================================================

def lf_negative_metaphorical_addiction(post):
    t = _text(post)
    if "addicted to this show" in t or "addicted to gaming" in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_metaphorical_sleep(post):
    t = _text(post)
    if "this lecture put me to sleep" in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_metaphorical_exhaustion(post):
    t = _text(post)
    if "this homework is exhausting" in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 7. PHILOSOPHY / THEORY (NON-EXPERIENTIAL)
# =========================================================

def lf_negative_philosophy_subreddits(post):
    if _sub(post) in {
        "philosophy",
        "askphilosophy",
        "debatephilosophy",
    }:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_theoretical_discussion(post):
    t = _text(post)
    if "the concept of" in t and "i feel" not in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 8. PROMOTIONAL / BOT / SPAM CONTENT
# =========================================================

def lf_negative_advertising(post):
    t = _text(post)
    if any(x in t for x in {
        "buy now",
        "use my code",
        "subscribe to my channel",
        "affiliate link",
    }):
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_link_only(post):
    t = _text(post).strip()
    if t.startswith("http") or t.startswith("www"):
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


def lf_negative_bot_signals(post):
    t = _text(post)
    if "i am a bot" in t or "this action was performed automatically" in t:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN


# =========================================================
# 9. IMAGE / MEDIA ONLY POSTS (PUSHSHIFT COMMON)
# =========================================================

def lf_negative_image_only(post):
    t = _text(post)
    if t in {"", "[removed]", "[deleted]"}:
        return Pillar.NOT_LIFESTYLE
    return ABSTAIN
