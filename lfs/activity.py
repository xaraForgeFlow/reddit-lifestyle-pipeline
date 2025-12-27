from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE ACTIVITY / MOVEMENT LFs
# =========================================================

def lf_activity_physical_activity(post):
    t = _text(post)
    if "physical activity" in t or "active lifestyle" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_movement(post):
    t = _text(post)
    if "movement" in t or "daily activity" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_exercise(post):
    if "exercise" in _text(post):
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_workout(post):
    if "workout" in _text(post):
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_fitness(post):
    if "fitness" in _text(post):
        return Pillar.ACTIVITY
    return ABSTAIN


# =========================================================
# 2. ACTIVITY TYPE / MODALITY LFs
# =========================================================

def lf_activity_running(post):
    t = _text(post)
    if "running" in t or "go for a run" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_walking(post):
    t = _text(post)
    if "walking" in t or "daily steps" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_gym(post):
    if "gym" in _text(post):
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_strength(post):
    t = _text(post)
    patterns = [
        "strength training",
        "lifting weights",
        "weight training",
        "resistance training",
    ]
    if any(p in t for p in patterns):
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_endurance(post):
    t = _text(post)
    if "endurance" in t or "stamina" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_cardio(post):
    t = _text(post)
    if "cardio" in t or "aerobic" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


# =========================================================
# 3. FUNCTIONAL LIMITATION / COMPLAINT LFs
# =========================================================

def lf_activity_low_energy(post):
    t = _text(post)
    patterns = [
        "too tired to exercise",
        "no energy to work out",
        "physically exhausted",
        "can't be active",
    ]
    if any(p in t for p in patterns):
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_sedentary(post):
    t = _text(post)
    patterns = [
        "sedentary lifestyle",
        "sit all day",
        "barely move",
        "inactive lifestyle",
    ]
    if any(p in t for p in patterns):
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_weakness(post):
    t = _text(post)
    if "muscle weakness" in t or "physically weak" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_balance_falls(post):
    t = _text(post)
    patterns = [
        "balance issues",
        "imbalance",
        "frequent falls",
        "afraid of falling",
    ]
    if any(p in t for p in patterns):
        return Pillar.ACTIVITY
    return ABSTAIN


# =========================================================
# 4. MOTOR FUNCTION / REHABILITATION LFs
# =========================================================

def lf_activity_rehabilitation(post):
    t = _text(post)
    if "rehabilitation" in t or "physical therapy" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_motor_skills(post):
    t = _text(post)
    if "fine motor" in t or "gross motor" in t or "motor skills" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


def lf_activity_coordination(post):
    t = _text(post)
    if "coordination" in t or "clumsy" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


# =========================================================
# 5. BODY / PHYSICAL CAPACITY CONTEXT
# =========================================================

def lf_activity_bmi_weight_context(post):
    t = _text(post)
    if "bmi" in t:
        return Pillar.ACTIVITY
    return ABSTAIN


# =========================================================
# 6. SUBREDDIT CONTEXT LFs
# =========================================================

def lf_activity_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "fitness",
        "running",
        "bodyweightfitness",
        "physicaltherapy",
        "rehab",
        "exercise",
    }:
        return Pillar.ACTIVITY
    return ABSTAIN


# =========================================================
# 7. EXCLUSION / SAFETY LFs
# =========================================================

def lf_activity_nonphysical_training(post):
    t = _text(post)
    if "mental training" in t or "cognitive training" in t:
        return ABSTAIN
    return ABSTAIN


def lf_activity_metaphor_exclusion(post):
    t = _text(post)
    if "that game was a workout" in t:
        return ABSTAIN
    return ABSTAIN
