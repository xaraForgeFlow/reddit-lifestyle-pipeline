"""
config/keywords.py

Keyword definitions used across the pipeline.

Roles:
1. COARSE_LIFESTYLE_KEYWORDS  -> high-recall filtering
2. COARSE_EXCLUSION_KEYWORDS  -> hard removal
3. PILLAR_KEYWORDS            -> LF / analysis support
"""

# =========================================================
# 1. COARSE FILTER — HIGH RECALL (MOST IMPORTANT)
# =========================================================
# Goal: KEEP anything that *might* be lifestyle-related

COARSE_LIFESTYLE_KEYWORDS = {
    # -------- Experiential / complaint language --------
    "i feel", "i am", "i'm", "ive been", "i have been",
    "struggling", "struggle with",
    "dealing with", "suffering from",
    "hard for me", "hard to",
    "cant", "can't", "cannot",
    "worried", "frustrated", "overwhelmed",
    "tired of", "fed up with",

    # -------- Sleep --------
    "sleep", "insomnia", "sleep apnea", "sleep paralysis",
    "tired", "fatigue",

    # -------- Diet / nutrition --------
    "diet", "nutrition", "calorie", "calories",
    "food", "eating", "binge", "overeating",
    "weight loss", "weight gain",

    # -------- Stress / mental health --------
    "stress", "anxiety", "panic", "burnout",
    "depressed", "sad", "hopeless",

    # -------- Physical activity --------
    "exercise", "gym", "running", "walking",
    "steps", "workout", "physical activity",

    # -------- Social --------
    "lonely", "loneliness", "isolation",
    "friends", "no friends", "social support",

    # -------- Substance use --------
    "smoking", "smoke", "vaping",
    "alcohol", "drinking", "addiction", "craving",

    # -------- Cognition --------
    "memory", "focus", "brain fog",
    "attention", "forgetting", "confused",

    # -------- Nature / purpose --------
    "hiking", "nature", "outdoors",
    "purpose", "meaning", "empty",
}


# =========================================================
# 2. COARSE FILTER — HARD EXCLUSIONS
# =========================================================
# Goal: REMOVE obvious junk even if keywords appear

COARSE_EXCLUSION_KEYWORDS = {
    # Memes / jokes
    "meme", "shitpost", "circlejerk",
    "lmao", "lol", "haha",

    # Gaming
    "league of legends", "dota", "csgo",
    "fortnite", "minecraft",

    # Media fandom
    "anime", "manga", "waifu", "kpop",

    # Politics
    "politics", "election", "trump", "biden",

    # Finance / crypto
    "bitcoin", "crypto", "stock", "trading",

    # Porn / NSFW
    "nsfw", "porn", "onlyfans",

    # Tech
    "programming", "coding", "linux", "windows",
}


# =========================================================
# 3. PILLAR-SPECIFIC KEYWORDS (FOR LFs / ANALYSIS)
# =========================================================
# Goal: semantic specificity, NOT coarse filtering

PILLAR_KEYWORDS = {
    "sleep": [
        "insomnia", "sleep", "sleep schedule",
        "tired all the time", "barely sleep",
        "can't fall asleep", "wake up every hour",
        "sleep hygiene", "sleep apnea", "nightmares"
    ],

    "diet": [
        "calories", "calorie deficit", "calorie surplus",
        "binge eating", "overeating", "diet plan",
        "meal prep", "junk food",
        "weight gain", "weight loss", "fasting"
    ],

    "stress": [
        "stress", "anxiety", "panic attack",
        "overwhelmed", "burnout",
        "mentally exhausted", "emotionally drained",
        "can't cope", "hopeless"
    ],

    "activity": [
        "exercise", "working out", "gym",
        "running", "walking", "steps",
        "endurance", "strength training"
    ],

    "social": [
        "lonely", "loneliness", "isolation",
        "no friends", "social anxiety",
        "awkward", "no one to talk to",
        "social support"
    ],

    "substance": [
        "vape", "vaping", "smoking",
        "cigarettes", "weed", "cannabis",
        "alcohol", "drinking problem",
        "addiction", "craving", "relapse"
    ],

    "cognition": [
        "brain fog", "memory loss", "forgetful",
        "can't concentrate", "no focus",
        "adhd", "confused", "dizzy",
        "delusion", "hallucination"
    ],

    "nature_purpose": [
        "hiking", "forest", "park",
        "nature", "beach",
        "meaning", "life purpose",
        "anhedonia"
    ],

    "risk": [
        "blood sugar", "glucose",
        "blood pressure", "cholesterol",
        "hypertension", "diabetes"
    ],
}
