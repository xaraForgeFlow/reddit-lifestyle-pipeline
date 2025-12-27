from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE SLEEP / REST SIGNALS
# =========================================================

def lf_sleep_sleep(post):
    if "sleep" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_insomnia(post):
    if "insomnia" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_sleep_disorder(post):
    if "sleep disorder" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 2. INSOMNIA SUBTYPES / NIGHTTIME COMPLAINTS
# =========================================================

def lf_sleep_cant_fall_asleep(post):
    t = _text(post)
    patterns = [
        "can't fall asleep",
        "cannot fall asleep",
        "cant fall asleep",
        "takes hours to fall asleep",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_cant_stay_asleep(post):
    t = _text(post)
    patterns = [
        "can't stay asleep",
        "wake up every hour",
        "keep waking up",
        "frequent awakenings",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_early_waking(post):
    t = _text(post)
    patterns = [
        "wake up too early",
        "early morning awakening",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_barely_sleep(post):
    t = _text(post)
    patterns = [
        "barely sleep",
        "hardly sleep",
        "sleep very little",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 3. SLEEP TIMING / CIRCADIAN RHYTHM
# =========================================================

def lf_sleep_circadian(post):
    if "circadian" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_irregular_schedule(post):
    t = _text(post)
    patterns = [
        "irregular sleep",
        "messed up sleep schedule",
        "sleep schedule is off",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_delayed_sleep(post):
    t = _text(post)
    if "delayed sleep phase" in t or "can't sleep until morning" in t:
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 4. DAYTIME CONSEQUENCES / FATIGUE
# =========================================================

def lf_sleep_daytime_fatigue(post):
    t = _text(post)
    patterns = [
        "daytime fatigue",
        "always tired",
        "exhausted during the day",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_excessive_sleepiness(post):
    if "excessive sleepiness" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_unrefreshing_sleep(post):
    t = _text(post)
    patterns = [
        "unrefreshing sleep",
        "wake up tired",
        "sleep but still tired",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_naps(post):
    t = _text(post)
    if "napping" in t or "nap during the day" in t or "constant naps" in t:
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 5. SLEEP DISORDERS / PARASOMNIAS
# =========================================================

def lf_sleep_sleep_apnea(post):
    if "sleep apnea" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_snoring(post):
    if "snoring" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_restless_legs(post):
    if "restless legs" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_nightmares(post):
    if "nightmares" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_sleep_paralysis(post):
    if "sleep paralysis" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_narcolepsy(post):
    if "narcolepsy" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 6. SLEEP HYGIENE / BEHAVIORAL CONTEXT
# =========================================================

def lf_sleep_sleep_hygiene(post):
    if "sleep hygiene" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_screen_time(post):
    t = _text(post)
    if "screen before bed" in t or "phone before sleep" in t:
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_caffeine(post):
    t = _text(post)
    if "caffeine" in t and "sleep" in t:
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 7. MEDICATION / SLEEP AID CONTEXT
# =========================================================

def lf_sleep_sleeping_pills(post):
    t = _text(post)
    if "sleeping pills" in t or "sleep medication" in t:
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_melatonin(post):
    if "melatonin" in _text(post):
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 8. POSITIVE SLEEP / RECOVERY (IMPORTANT)
# =========================================================

def lf_sleep_restful_sleep(post):
    t = _text(post)
    patterns = [
        "restful sleep",
        "deep sleep",
        "finally slept well",
    ]
    if any(p in t for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_improving_sleep(post):
    t = _text(post)
    if "improving my sleep" in t or "sleep is getting better" in t:
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 9. SUBREDDIT CONTEXT
# =========================================================

def lf_sleep_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "sleep",
        "insomnia",
        "sleepapnea",
        "narcolepsy",
        "bedbros",
    }:
        return Pillar.SLEEP
    return ABSTAIN


# =========================================================
# 10. EXCLUSION / SAFETY LFs
# =========================================================

def lf_sleep_metaphor_exclusion(post):
    t = _text(post)
    if "put me to sleep" in t and "movie" in t:
        return ABSTAIN
    return ABSTAIN


def lf_sleep_positive_sleep_exclusion(post):
    t = _text(post)
    if "best sleep ever" in t and "vacation" in t:
        return ABSTAIN
    return ABSTAIN
