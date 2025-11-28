from config.pillars import ABSTAIN, Pillar


def _text(post):
    return post.get("text", "").lower()


def lf_sleep_insomnia(post):
    """Fire when the word 'insomnia' appears."""
    text = _text(post)
    if "insomnia" in text:
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_schedule(post):
    """Fire on typical 'sleep schedule' complaints."""
    text = _text(post)
    patterns = [
        "sleep schedule",
        "my sleep is messed up",
        "my sleep is ruined",
        "barely sleep",
        "only sleep",
    ]
    if any(p in text for p in patterns):
        return Pillar.SLEEP
    return ABSTAIN


def lf_sleep_subreddit(post):
    """If subreddit clearly about sleep, mark as sleep."""
    sub = post.get("subreddit", "").lower()
    if sub in {"insomnia", "sleep", "sleepapnea"}:
        return Pillar.SLEEP
    return ABSTAIN
