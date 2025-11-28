from enum import IntEnum

# Special value for "no label"
ABSTAIN = -1


class Pillar(IntEnum):
    DIET = 0
    ACTIVITY = 1
    SOCIAL = 2
    SLEEP = 3
    STRESS = 4
    SUBSTANCE = 5
    NATURE = 6
    PURPOSE = 7
    COGNITION = 8
    RISK = 9          # blood pressure, sugar, etc.
    NOT_LIFESTYLE = 10   # explicit "this is not lifestyle"
