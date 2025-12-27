from config.pillars import Pillar, ABSTAIN


def _text(post):
    return post.get("text", "").lower()


# =========================================================
# 1. CORE COGNITION / BRAIN FUNCTION LFs
# =========================================================

def lf_cognition_cognition(post):
    t = _text(post)
    if "cognition" in t or "cognitive function" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_brain_health(post):
    if "brain health" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_neuro(post):
    t = _text(post)
    if "neurological" in t or "neuropsych" in t:
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 2. MEMORY / ATTENTION LFs
# =========================================================

def lf_cognition_memory(post):
    if "memory" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_memory_loss(post):
    t = _text(post)
    if "memory loss" in t or "losing my memory" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_attention(post):
    if "attention" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_cant_focus(post):
    t = _text(post)
    patterns = [
        "can't focus",
        "cannot focus",
        "no focus",
        "unable to concentrate",
        "trouble concentrating",
    ]
    if any(p in t for p in patterns):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_forgetful(post):
    t = _text(post)
    if "forgetful" in t or "forget things" in t:
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 3. COGNITIVE SYMPTOMS / PERCEPTION
# =========================================================

def lf_cognition_brain_fog(post):
    if "brain fog" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_confusion(post):
    t = _text(post)
    if "confused" in t or "confusion" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_slow_thinking(post):
    t = _text(post)
    patterns = [
        "slow thinking",
        "mentally slow",
        "thinking feels slow",
    ]
    if any(p in t for p in patterns):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_perception(post):
    t = _text(post)
    if "perception" in t or "things feel unreal" in t:
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 4. NEUROLOGICAL / NEUROPSYCHIATRIC SYMPTOMS
# =========================================================

def lf_cognition_hallucinations(post):
    t = _text(post)
    if "hallucination" in t or "hallucinating" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_delusions(post):
    t = _text(post)
    if "delusion" in t or "delusional" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_consciousness(post):
    if "loss of consciousness" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 5. NEURODEGENERATIVE / MEDICAL CONDITIONS
# =========================================================

def lf_cognition_dementia(post):
    if "dementia" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_neurodegeneration(post):
    if "neurodegeneration" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 6. SOMATIC NEURO SIGNS (IMPORTANT FOR MEDICAL DOMAIN)
# =========================================================

def lf_cognition_headache(post):
    if "headache" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_dizziness(post):
    t = _text(post)
    if "dizzy" in t or "dizziness" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_speech(post):
    t = _text(post)
    if "speech problems" in t or "slurred speech" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_vision(post):
    t = _text(post)
    if "vision problems" in t or "blurry vision" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_dysphagia(post):
    if "dysphagia" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 7. DIAGNOSIS / CONDITION CONTEXT
# =========================================================

def lf_cognition_adhd(post):
    if "adhd" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_ocd(post):
    t = _text(post)
    if "obsessive compulsive disorder" in t or "ocd" in t:
        return Pillar.COGNITION
    return ABSTAIN


def lf_cognition_bipolar(post):
    if "bipolar" in _text(post):
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 8. SUBREDDIT CONTEXT LFs
# =========================================================

def lf_cognition_subreddit(post):
    sub = post.get("subreddit", "").lower()
    if sub in {
        "adhd",
        "adhdwomen",
        "dementia",
        "brainfog",
        "neurology",
        "neuro",
    }:
        return Pillar.COGNITION
    return ABSTAIN


# =========================================================
# 9. EXCLUSION / SAFETY LFs
# =========================================================

def lf_cognition_metaphor_exclusion(post):
    t = _text(post)
    if "mind blown" in t:
        return ABSTAIN
    return ABSTAIN


def lf_cognition_temporary_confusion_exclusion(post):
    t = _text(post)
    if "confused by the rules of the game" in t:
        return ABSTAIN
    return ABSTAIN
