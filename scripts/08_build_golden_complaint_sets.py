import pandas as pd
import re

# -----------------------------
# CONFIG
# -----------------------------
INPUT_PATH = "data/manual_labeling_top_nli.csv"
OUTPUT_PATH = "data/expert_labeling_top_200.csv"

MIN_WORDS = 30
MAX_WORDS = 400
TOP_K = 200


# -----------------------------
# TEXT SIGNALS
# -----------------------------
QUESTION_PATTERNS = [
    "anyone else",
    "does anyone",
    "is it normal",
    "should i",
    "what should i do",
    "how do i",
    "how can i",
    "why do i",
    "?"
]

COMPLAINT_PATTERNS = [
    "i feel",
    "i have been",
    "i'm struggling",
    "i am struggling",
    "i can't",
    "i cannot",
    "it's hard",
    "it is hard",
    "i don't know",
    "i dont know",
    "i'm worried",
    "i am worried",
    "this is affecting",
    "makes me feel",
    "problem",
    "issue"
]

FIRST_PERSON_PATTERNS = [
    " i ",
    " i'm ",
    " i’m ",
    " my ",
    " me "
]

BAD_PATTERNS = [
    "here's how",
    "this worked for me",
    "tips for",
    "guide to",
    "you should",
    "everyone should",
    "psa",
    "success story"
]


# -----------------------------
# HELPERS
# -----------------------------
def count_matches(text, patterns):
    text = text.lower()
    return sum(p in text for p in patterns)

def contains_any(text, patterns):
    text = text.lower()
    return any(p in text for p in patterns)

def summarize(text, max_sentences=2):
    """
    Very short gist-style summary.
    Max 2 sentences, removes very short fragments.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s.strip() for s in sentences if len(s.split()) >= 6]
    return " ".join(sentences[:max_sentences])


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(INPUT_PATH)

df = df.dropna(subset=["text", "pillar", "nli_score"])
df["text"] = df["text"].astype(str)

# -----------------------------
# DEDUPLICATION (IMPORTANT)
# -----------------------------
df["text_norm"] = (
    df["text"]
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

df = df.drop_duplicates(subset="text_norm")

# -----------------------------
# LENGTH FILTER
# -----------------------------
df["word_len"] = df["text"].str.split().str.len()
df = df[
    (df["word_len"] >= MIN_WORDS) &
    (df["word_len"] <= MAX_WORDS)
]

# -----------------------------
# SIGNAL SCORING
# -----------------------------
df["question_score"] = df["text"].apply(
    lambda t: count_matches(t, QUESTION_PATTERNS)
)

df["complaint_score"] = df["text"].apply(
    lambda t: count_matches(t, COMPLAINT_PATTERNS)
)

df["first_person"] = df["text"].apply(
    lambda t: contains_any(t, FIRST_PERSON_PATTERNS)
)

# keep posts that have *some* first-person framing
df = df[df["first_person"]]

# remove PSA / guide-style content
df = df[
    ~df["text"].apply(lambda t: contains_any(t, BAD_PATTERNS))
]

# require explicit struggle signal
df = df[df["complaint_score"] >= 2]

# -----------------------------
# FINAL GOLD SCORE
# -----------------------------
df["gold_score"] = (
    2.0 * df["nli_score"] +
    1.5 * df["complaint_score"] +
    1.0 * df["question_score"] -
    0.002 * df["word_len"]
)

df = df.sort_values("gold_score", ascending=False)

# -----------------------------
# SELECT TOP 200
# -----------------------------
df_top = df.head(TOP_K).copy()

# -----------------------------
# ADD SHORT SUMMARIES (EXPERT-FRIENDLY)
# -----------------------------
df_top["summary"] = df_top["text"].apply(summarize)

# -----------------------------
# FINAL COLUMN ORDER
# -----------------------------
final_columns = [
    "pillar",
    "nli_score",
    "gold_score",
    "complaint_score",
    "question_score",
    "word_len",
    "summary",
    "text"
]

df_top = df_top[final_columns]

# -----------------------------
# SAVE
# -----------------------------
df_top.to_csv(OUTPUT_PATH, index=False)

print(f"✅ Saved {len(df_top)} expert-ready posts to:")
print(f"   {OUTPUT_PATH}")
