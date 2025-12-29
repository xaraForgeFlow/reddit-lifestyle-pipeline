"""
lf_allowlist.py
----------------

Temporary allowlist for labeling functions (LFs) with
meaningful coverage on the pilot dataset.

Purpose:
- Prune dead or near-dead LFs
- Reduce noise before aggregation
- Make LF behavior interpretable

IMPORTANT:
This file is NOT permanent.
LFs can be added back once improved or expanded.
"""

# =========================================================
# Allowlist of LF names
# =========================================================

LF_ALLOWLIST = {

    # =========================
    # ACTIVITY
    # =========================
    "lf_activity_running",
    "lf_activity_gym",
    "lf_activity_workout",
    "lf_activity_walking",
    "lf_activity_exercise",
    "lf_activity_fitness",
    "lf_activity_movement",
    "lf_activity_subreddit",

    # =========================
    # DIET
    # =========================
    "lf_diet_food",
    "lf_diet_diet",
    "lf_diet_calories",
    "lf_diet_meals",
    "lf_diet_bmi",
    "lf_diet_weight_management",
    "lf_diet_subreddit",

    # =========================
    # SLEEP
    # =========================
    "lf_sleep_sleep",
    "lf_sleep_insomnia",
    "lf_sleep_nightmares",
    "lf_sleep_naps",

    # =========================
    # STRESS
    # =========================
    "lf_stress_anger",
    "lf_stress_anxiety",
    "lf_stress_stress",
    "lf_stress_panic",
    "lf_stress_overwhelmed",
    "lf_stress_hopelessness",
    "lf_stress_subreddit",

    # =========================
    # SOCIAL
    # =========================
    "lf_social_relationship",
    "lf_social_breakup",
    "lf_social_lonely",
    "lf_social_isolation",
    "lf_social_community",
    "lf_social_subreddit",

    # =========================
    # SUBSTANCE
    # =========================
    "lf_substance_alcohol",
    "lf_substance_smoking",
    "lf_substance_cannabis",
    "lf_substance_caffeine",
    "lf_substance_prescription_stimulants",
    "lf_substance_illicit_stimulants",
    "lf_substance_withdrawal",
    "lf_substance_relapse",

    # =========================
    # NEGATIVE / EXCLUSION
    # =========================
    "lf_negative_political_language",
    "lf_negative_third_person_only",
}
