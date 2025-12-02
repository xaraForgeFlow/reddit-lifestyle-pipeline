"""
config/subreddits.py

Subreddit lists for coarse filtering and labeling.
"""

# ----------------------------------------------
# SUBREDDIT WHITELIST (Highly relevant)
# ----------------------------------------------

WHITELIST_SUBREDDITS = {
    # Sleep
    "insomnia",
    "sleep",
    "sleepapnea",

    # Diet & weight loss
    "loseit",
    "nutrition",
    "intermittentfasting",
    "keto",
    "xxketo",

    # Stress & mental health
    "anxiety",
    "socialanxiety",
    "depression",
    "offmychest",

    # Exercise
    "fitness",
    "running",
    "bodyweightfitness",

    # Addiction
    "stopdrinking",
    "stopgaming",
    "leaves",
    "addiction",

    # Cognition / neuro
    "adhd",
    "adhdwomen",
    "migraine",

    # Social
    "lonely",
    "relationship_advice",

    # Nature / purpose
    "hiking",
    "camping",
}

# ----------------------------------------------
# SUBREDDIT GRAYLIST (Mixed content)
# ----------------------------------------------

GRAYLIST_SUBREDDITS = {
    "askreddit",
    "askwomen",
    "askmen",
    "casualconversation",
    "amitheasshole",
    "confession",
    "trueoffmychest",
}

# ----------------------------------------------
# SUBREDDIT BLACKLIST (Irrelevant content)
# ----------------------------------------------

BLACKLIST_SUBREDDITS = {
    "gaming",
    "leagueoflegends",
    "dota2",
    "anime",
    "memes",
    "politics",
    "worldnews",
    "news",
}
