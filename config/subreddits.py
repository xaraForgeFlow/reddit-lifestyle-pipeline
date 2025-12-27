"""
config/subreddits.py

High-recall subreddit filtering for lifestyle detection.
"""

# =========================================================
# 1. ALWAYS INCLUDE (personal, health, support-heavy)
# =========================================================

SEED_WHITELIST = {
    # Emotional disclosure / advice
    "offmychest", "trueoffmychest", "confession",
    "advice", "needadvice", "relationship_advice",
    "twoXchromosomes", "twoxchromosomes",
    "self", "assistance",

    # Mental health
    "mentalhealth", "anxiety", "depression", "ptsd",
    "bipolar", "bipolarreddit", "ocd",
    "suicidewatch", "selfharm",

    # Sleep
    "insomnia", "sleep", "sleepapnea",

    # Diet & fitness
    "fitness", "xxfitness", "loseit", "running",
    "gym", "exercise", "bodyweightfitness",
    "nutrition", "diet", "healthyfood", "supplements",

    # Substance use
    "stopsmoking", "stopdrinking", "alcoholism",
    "leaves", "addiction",

    # Medical / neuro
    "medical", "askdocs", "medicine",
    "neurology", "braininjury", "stroke",
    "chronicpain", "disability",

    # Nature
    "hiking", "camping", "backpacking", "outdoors",

    # Social
    "lonely", "relationships",
}

# =========================================================
# 2. GRAYLIST (keep only if text matches keywords)
# =========================================================

GRAYLIST_SUBREDDITS = {
    "askreddit", "askwomen", "askmen",
    "casualconversation",
    "amitheasshole",
    "rant", "vent",
    "health", "mental",
}

# =========================================================
# 3. ALWAYS EXCLUDE (high-noise domains)
# =========================================================

BLACKLIST_SUBREDDITS = {
    # Gaming
    "gaming", "leagueoflegends", "dota2", "csgo",
    "minecraft", "overwatch", "valorant",

    # Memes / jokes
    "memes", "dankmemes", "shitposting",
    "me_irl", "circlejerk", "funny",

    # Politics / news
    "politics", "worldnews", "news",
    "liberal", "conservative",

    # Finance / crypto
    "bitcoin", "crypto", "stocks",
    "wallstreetbets", "investing",

    # Porn / NSFW
    "nsfw", "porn", "gonewild",

    # Tech
    "programming", "learnpython",
    "linux", "pcmasterrace",

    # Media fandoms
    "anime", "manga", "kpop",
    "movies", "television", "music",
}
