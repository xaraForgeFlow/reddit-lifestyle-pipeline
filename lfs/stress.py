from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE STRESS / ANXIETY SIGNALS
# =========================================================

def lf_stress_stress(post):
    if "stress" in _text(post):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_anxiety(post):
    if "anxiety" in _text(post) or "anxious" in _text(post):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_panic(post):
    t = _text(post)
    if "panic attack" in t or "panic attacks" in t or "panicking" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_burnout(post):
    t = _text(post)
    if "burnout" in t or "burned out" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_overwhelmed(post):
    if "overwhelmed" in _text(post):
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 2. WORRY / RUMINATION / ANTICIPATORY STRESS
# =========================================================

def lf_stress_constant_worry(post):
    t = _text(post)
    patterns = [
        "constant worry",
        "always worrying",
        "can't stop worrying",
        "worried all the time",
    ]
    if any(p in t for p in patterns):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_racing_thoughts(post):
    t = _text(post)
    if "racing thoughts" in t or "mind won't stop" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_catastrophizing(post):
    t = _text(post)
    if "worst case scenario" in t or "expect the worst" in t:
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 3. EMOTIONAL / AFFECTIVE STATES
# =========================================================

def lf_stress_emotional_exhaustion(post):
    t = _text(post)
    patterns = [
        "emotionally exhausted",
        "mentally exhausted",
        "emotionally drained",
    ]
    if any(p in t for p in patterns):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_sadness(post):
    t = _text(post)
    if "sad all the time" in t or "deep sadness" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_hopelessness(post):
    t = _text(post)
    if "hopeless" in t or "feel hopeless" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_anger(post):
    t = _text(post)
    if "angry all the time" in t or "rage" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_grief(post):
    t = _text(post)
    if "grief" in t or "mourning" in t or "lost someone" in t:
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 4. PHYSIOLOGICAL / SOMATIC STRESS RESPONSES
# =========================================================

def lf_stress_physical_symptoms(post):
    t = _text(post)
    patterns = [
        "stress headaches",
        "stress nausea",
        "stress chest pain",
        "stress stomach",
    ]
    if any(p in t for p in patterns):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_heart_racing(post):
    t = _text(post)
    if "heart racing" in t or "heart pounding" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_shortness_of_breath(post):
    t = _text(post)
    if "shortness of breath" in t or "can't breathe when anxious" in t:
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 5. FUNCTIONAL IMPAIRMENT / COPING FAILURE
# =========================================================

def lf_stress_cant_cope(post):
    t = _text(post)
    patterns = [
        "can't cope",
        "unable to cope",
        "can't handle it anymore",
    ]
    if any(p in t for p in patterns):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_breakdown(post):
    t = _text(post)
    if "mental breakdown" in t or "breaking down" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_crying(post):
    t = _text(post)
    if "crying all the time" in t or "burst into tears" in t:
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 6. SITUATIONAL / LIFE-STRESS CONTEXTS
# =========================================================

def lf_stress_work_related(post):
    t = _text(post)
    patterns = [
        "work stress",
        "job stress",
        "burned out at work",
        "toxic workplace",
    ]
    if any(p in t for p in patterns):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_school_related(post):
    t = _text(post)
    patterns = [
        "school stress",
        "college stress",
        "exam stress",
    ]
    if any(p in t for p in patterns):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_financial(post):
    t = _text(post)
    if "financial stress" in t or "money stress" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_relationship(post):
    t = _text(post)
    if "relationship stress" in t or "relationship anxiety" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_health_related(post):
    t = _text(post)
    if "health anxiety" in t or "worried about my health" in t:
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 7. RESILIENCE / WELLBEING / POSITIVE ADAPTATION (IMPORTANT)
# =========================================================

def lf_stress_resilience(post):
    t = _text(post)
    if "resilience" in t or "resilient" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_coping(post):
    t = _text(post)
    if "coping better" in t or "learning to cope" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_well_being(post):
    t = _text(post)
    if "well being" in t or "wellbeing" in t:
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_positive_emotion(post):
    t = _text(post)
    patterns = [
        "feeling calm",
        "at peace",
        "emotionally stable",
    ]
    if any(p in t for p in patterns):
        return Pillar.STRESS
    return ABSTAIN


def lf_stress_positivity(post):
    t = _text(post)
    if "positivity" in t or "positive mindset" in t:
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 8. SUBREDDIT CONTEXT
# =========================================================

def lf_stress_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "anxiety",
        "stress",
        "offmychest",
        "trueoffmychest",
        "burnout",
        "mentalhealth",
        "depression",
    }:
        return Pillar.STRESS
    return ABSTAIN


# =========================================================
# 9. EXCLUSION / SAFETY LFs
# =========================================================

def lf_stress_joking_exclusion(post):
    t = _text(post)
    if "stressed lol" in t or "jk" in t:
        return ABSTAIN
    return ABSTAIN


def lf_stress_positive_stress_exclusion(post):
    t = _text(post)
    if "good stress" in t or "eustress" in t:
        return ABSTAIN
    return ABSTAIN


def lf_stress_quote_exclusion(post):
    t = _text(post)
    if "quote" in t and "stress" in t:
        return ABSTAIN
    return ABSTAIN
