# Reddit Lifestyle Behavior Pipeline

This project builds a large-scale NLP pipeline to extract **lifestyle-related complaints and questions** from Reddit posts
(diet, sleep, stress, activity, social connection, substance use, cognition, etc.).

It uses:

- **Coarse filtering** (keywords + subreddits) to reduce millions of posts
- **Weak supervision** (labeling functions / LFs) to assign noisy labels
- **Zero-shot NLI** (later) to capture subtle, semantic lifestyle content
- **Representative sampling** to evaluate and refine the pipeline
- A **label model** (e.g. Snorkel) to turn weak labels into probabilities

## Project structure

```text
reddit-lifestyle-pipeline/
├── data/           # raw, interim, and processed data (not tracked by git)
├── config/         # configuration files (pillars, keywords, subreddits)
├── lfs/            # labeling functions (weak supervision rules)
├── nli/            # zero-shot NLI wrapper + hypotheses (later)
├── sampling/       # representative sampling utilities (later)
├── scripts/        # pipeline scripts (01_coarse_filter, 02_run_lfs, etc.)
├── README.md       # this file
└── requirements.txt
