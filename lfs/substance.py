from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE SUBSTANCE KEYWORD LFs
# =========================================================

def lf_substance_smoking(post):
    t = _text(post)
    if "smoking" in t or "smoke cigarettes" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_tobacco(post):
    t = _text(post)
    if "tobacco" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_vaping(post):
    t = _text(post)
    if "vape" in t or "vaping" in t or "e-cig" in t or "ecig" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_alcohol(post):
    t = _text(post)
    if "alcohol" in t or "drinking" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_drug_use_general(post):
    t = _text(post)
    patterns = [
        "drug use",
        "using drugs",
        "substance use",
        "getting high",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


# =========================================================
# 2. NICOTINE PRODUCTS / SLANG
# =========================================================

def lf_substance_nicotine(post):
    if "nicotine" in _text(post):
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_cigarettes_slang(post):
    t = _text(post)
    patterns = [
        "cigarette",
        "cigarettes",
        "cigs",
        "smokes",
        "pack a day",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_snus_pouches(post):
    t = _text(post)
    patterns = [
        "snus",
        "nicotine pouch",
        "zyn",
        "dip",
        "chewing tobacco",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


# =========================================================
# 3. ALCOHOL SPECIFICS / SLANG / PATTERNS
# =========================================================

def lf_substance_alcohol_terms(post):
    t = _text(post)
    patterns = [
        "beer",
        "wine",
        "vodka",
        "whiskey",
        "tequila",
        "liquor",
        "booze",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_binge_drinking(post):
    t = _text(post)
    patterns = [
        "binge drinking",
        "blackout drunk",
        "blacked out",
        "drink until i pass out",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_hangover(post):
    t = _text(post)
    if "hangover" in t or "hungover" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


# =========================================================
# 4. CANNABIS / THC
# =========================================================

def lf_substance_cannabis(post):
    t = _text(post)
    patterns = [
        "weed",
        "cannabis",
        "marijuana",
        "thc",
        "edibles",
        "dab",
        "dabs",
        "cart",
        "carts",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


# =========================================================
# 5. OPIOIDS / PAINKILLERS
# =========================================================

def lf_substance_opioids(post):
    t = _text(post)
    patterns = [
        "opioid",
        "opioids",
        "painkillers",
        "oxy",
        "oxycodone",
        "hydrocodone",
        "fentanyl",
        "heroin",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


# =========================================================
# 6. STIMULANTS
# =========================================================

def lf_substance_stimulants(post):
    t = _text(post)
    patterns = [
        "stimulant",
        "stimulants",
        "amphetamine",
        "adderall",
        "ritalin",
        "vyvanse",
        "cocaine",
        "meth",
        "methamphetamine",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


# =========================================================
# 7. OTHER COMMON SUBSTANCES
# =========================================================

def lf_substance_benzos(post):
    t = _text(post)
    patterns = [
        "benzo",
        "benzodiazepine",
        "xanax",
        "klonopin",
        "valium",
        "ativan",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_mdma_psychedelics(post):
    t = _text(post)
    patterns = [
        "mdma",
        "ecstasy",
        "lsd",
        "acid",
        "shrooms",
        "mushrooms",
        "psychedelic",
        "ketamine",
    ]
    if any(p in t for p in patterns):
        return Pillar.SUBSTANCE
    return ABSTAIN


# =========================================================
# 8. ADDICTION / DEPENDENCE / WITHDRAWAL / CRAVINGS
# =========================================================

def lf_substance_addiction(post):
    t = _text(post)
    if "addiction" in t or "addicted" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_dependence(post):
    t = _text(post)
    if "dependence" in t or "dependent on" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_cravings(post):
    t = _text(post)
    if "craving" in t or "cravings" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_withdrawal(post):
    t = _text(post)
    if "withdrawal" in t or "withdrawing" in t:
        return Pillar.SUBSTANCE
    return ABSTAIN


def lf_substance_relapse(post
