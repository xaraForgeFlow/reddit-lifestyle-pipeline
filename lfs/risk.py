from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE BIOMARKER RISK LFs
# =========================================================

def lf_risk_blood_pressure(post):
    t = _text(post)
    if "blood pressure" in t:
        return Pillar.RISK
    return ABSTAIN


def lf_risk_hypertension(post):
    t = _text(post)
    if "hypertension" in t or "high blood pressure" in t:
        return Pillar.RISK
    return ABSTAIN


def lf_risk_blood_sugar(post):
    t = _text(post)
    if "blood sugar" in t:
        return Pillar.RISK
    return ABSTAIN


def lf_risk_glucose(post):
    if "glucose" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_cholesterol(post):
    if "cholesterol" in _text(post):
        return Pillar.RISK
    return ABSTAIN


# =========================================================
# 2. LIPIDS / CARDIOMETABOLIC MARKERS
# =========================================================

def lf_risk_triglycerides(post):
    if "triglycerides" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_ldl_hdl(post):
    t = _text(post)
    if "ldl" in t or "hdl" in t:
        return Pillar.RISK
    return ABSTAIN


def lf_risk_apob(post):
    if "apob" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_lipoprotein_a(post):
    t = _text(post)
    if "lipoprotein(a)" in t or "lp(a)" in t:
        return Pillar.RISK
    return ABSTAIN


# =========================================================
# 3. GLYCEMIC CONTROL / METABOLIC RISK
# =========================================================

def lf_risk_diabetes(post):
    if "diabetes" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_prediabetes(post):
    if "prediabetes" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_insulin_resistance(post):
    if "insulin resistance" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_a1c(post):
    t = _text(post)
    if "a1c" in t or "hba1c" in t:
        return Pillar.RISK
    return ABSTAIN


# =========================================================
# 4. BODY COMPOSITION / METABOLIC CONTEXT
# =========================================================

def lf_risk_bmi(post):
    if "bmi" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_obesity(post):
    t = _text(post)
    if "obese" in t or "obesity" in t:
        return Pillar.RISK
    return ABSTAIN


def lf_risk_metabolic_syndrome(post):
    if "metabolic syndrome" in _text(post):
        return Pillar.RISK
    return ABSTAIN


# =========================================================
# 5. CARDIOVASCULAR DISEASE CONTEXT
# =========================================================

def lf_risk_heart_disease(post):
    if "heart disease" in _text(post):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_cardiovascular(post):
    t = _text(post)
    if "cardiovascular risk" in t or "cv risk" in t:
        return Pillar.RISK
    return ABSTAIN


def lf_risk_atherosclerosis(post):
    if "atherosclerosis" in _text(post):
        return Pillar.RISK
    return ABSTAIN


# =========================================================
# 6. CLINICAL / LAB CONTEXT LFs
# =========================================================

def lf_risk_lab_results(post):
    t = _text(post)
    patterns = [
        "lab results came back",
        "blood test results",
        "labs show",
    ]
    if any(p in t for p in patterns):
        return Pillar.RISK
    return ABSTAIN


def lf_risk_doctor_warning(post):
    t = _text(post)
    patterns = [
        "doctor warned me",
        "doctor said i need to lower",
        "doctor told me my levels are high",
    ]
    if any(p in t for p in patterns):
        return Pillar.RISK
    return ABSTAIN


# =========================================================
# 7. SUBREDDIT CONTEXT LFs
# =========================================================

def lf_risk_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "diabetes",
        "prediabetes",
        "cholesterol",
        "hypertension",
        "cardiology",
        "metabolicsyndrome",
    }:
        return Pillar.RISK
    return ABSTAIN


# =========================================================
# 8. EXCLUSION / SAFETY LFs
# =========================================================

def lf_risk_family_history_exclusion(post):
    t = _text(post)
    if "family history" in t and "my levels" not in t:
        return ABSTAIN
    return ABSTAIN


def lf_risk_hypothetical_exclusion(post):
    t = _text(post)
    if "what if i get diabetes" in t:
        return ABSTAIN
    return ABSTAIN
