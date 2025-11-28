# Reddit Lifestyle Behavior Pipeline

This project implements a large-scale weak supervision + NLI-based NLP pipeline
to extract lifestyle-related complaints/questions from Reddit posts (2009–2023).

## Features
- Coarse filtering (keywords, subreddits)
- Weak supervision labeling functions (Snorkel-style)
- Zero-shot NLI labeling functions (HuggingFace)
- Representative sampling strategy for evaluation
- Label model to compute pillar probabilities
- Multi-pillar lifestyle labeling
- Condition-specific filtering (e.g., diabetes, ADHD, anxiety)
- Highly modular architecture for research

## Project Structure
reddit-lifestyle-pipeline/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── lf_outputs/
│   ├── label_model/
│   └── eval/
├── config/
│   ├── pillars.py
│   ├── subreddits.py
│   └── keywords.py
├── lfs/
│   ├── __init__.py
│   ├── complaint.py
│   ├── sleep.py
│   ├── diet.py
│   ├── stress.py
│   ├── activity.py
│   ├── cognition.py
│   ├── substance.py
│   ├── nature_purpose.py
│   └── negatives.py
├── nli/
│   ├── hypotheses.py
│   └── nli_model.py
├── sampling/
│   ├── stratified.py
│   ├── uncertainty.py
│   ├── clusters.py
│   └── hard_negatives.py
├── scripts/
│   ├── 01_coarse_filter.py
│   ├── 02_run_lfs.py
│   ├── 03_run_nli_lfs.py
│   ├── 04_fit_label_model.py
│   ├── 05_sampling_and_eval.py
│   ├── 06_rerun_with_refined_lfs.py
│   └── 07_condition_filtering.py
├── README.md
└── .gitignore

