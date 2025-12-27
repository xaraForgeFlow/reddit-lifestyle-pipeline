from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE DIET / NUTRITION LFs
# =========================================================

def lf_diet_diet(post):
    if "diet" in _text(post):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_nutrition(post):
    if "nutrition" in _text(post) or "nutritional" in _text(post):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_food(post):
    if "food" in _text(post) or "eating" in _text(post):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_meals(post):
    t = _text(post)
    if "meal" in t or "meals" in t:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 2. CALORIE / INTAKE / TRACKING LFs
# =========================================================

def lf_diet_calories(post):
    t = _text(post)
    if "calorie" in t or "calories" in t:
        return Pillar.DIET
    return ABSTAIN


def lf_diet_calorie_tracking(post):
    t = _text(post)
    patterns = [
        "counting calories",
        "track calories",
        "calorie deficit",
        "calorie surplus",
    ]
    if any(p in t for p in patterns):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_macros(post):
    t = _text(post)
    if "macros" in t or "macronutrients" in t:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 3. WEIGHT / BODY COMPOSITION
# =========================================================

def lf_diet_weight_management(post):
    t = _text(post)
    patterns = [
        "weight loss",
        "lose weight",
        "weight gain",
        "manage my weight",
    ]
    if any(p in t for p in patterns):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_body_composition(post):
    if "body composition" in _text(post):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_bmi(post):
    if "bmi" in _text(post):
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 4. EATING BEHAVIOR / HABITS
# =========================================================

def lf_diet_eating_habits(post):
    t = _text(post)
    patterns = [
        "eating habits",
        "eating pattern",
        "how i eat",
    ]
    if any(p in t for p in patterns):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_overeating(post):
    t = _text(post)
    if "overeating" in t or "binge eating" in t:
        return Pillar.DIET
    return ABSTAIN


def lf_diet_undereating(post):
    t = _text(post)
    if "not eating enough" in t or "undereating" in t:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 5. EATING DISORDERS / DISORDERED EATING
# =========================================================

def lf_diet_eating_disorder(post):
    t = _text(post)
    if "eating disorder" in t:
        return Pillar.DIET
    return ABSTAIN


def lf_diet_anorexia(post):
    if "anorexia" in _text(post):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_bulimia(post):
    if "bulimia" in _text(post):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_bed(post):
    t = _text(post)
    if "binge eating disorder" in t:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 6. SUPPLEMENTS / NUTRIENTS
# =========================================================

def lf_diet_supplements(post):
    t = _text(post)
    if "supplement" in t or "supplements" in t:
        return Pillar.DIET
    return ABSTAIN


def lf_diet_vitamins(post):
    t = _text(post)
    if "vitamin" in t or "vitamins" in t:
        return Pillar.DIET
    return ABSTAIN


def lf_diet_protein(post):
    if "protein intake" in _text(post) or "protein" in _text(post):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_minerals(post):
    t = _text(post)
    if "iron deficiency" in t or "magnesium" in t or "zinc" in t:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 7. DIETARY PATTERNS / APPROACHES
# =========================================================

def lf_diet_restrictive_diet(post):
    t = _text(post)
    patterns = [
        "restrictive diet",
        "cutting out food",
        "food restriction",
    ]
    if any(p in t for p in patterns):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_plant_based(post):
    t = _text(post)
    if "plant based" in t or "vegetarian" in t or "vegan" in t:
        return Pillar.DIET
    return ABSTAIN


def lf_diet_keto_lowcarb(post):
    t = _text(post)
    if "keto" in t or "low carb" in t:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 8. HEALTH / LIFESTYLE CONTEXT (FOOD-SPECIFIC)
# =========================================================

def lf_diet_health_habits(post):
    t = _text(post)
    patterns = [
        "healthy eating",
        "eat healthier",
        "improve my diet",
    ]
    if any(p in t for p in patterns):
        return Pillar.DIET
    return ABSTAIN


def lf_diet_lifestyle_food(post):
    t = _text(post)
    if "lifestyle change" in t and "diet" in t:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 9. SUBREDDIT CONTEXT LFs
# =========================================================

def lf_diet_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "nutrition",
        "diet",
        "loseit",
        "weightloss",
        "eatingdisorders",
        "supplements",
        "caloriecounting",
    }:
        return Pillar.DIET
    return ABSTAIN


# =========================================================
# 10. EXCLUSION / SAFETY LFs
# =========================================================

def lf_diet_nonfood_diet_exclusion(post):
    t = _text(post)
    if "media diet" in t or "news diet" in t:
        return ABSTAIN
    return ABSTAIN


def lf_diet_metaphor_exclusion(post):
    t = _text(post)
    if "diet of lies" in t:
        return ABSTAIN
    return ABSTAIN
