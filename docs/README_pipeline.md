
# BRCA2 South-Asian Database Bias — Reproducible Pipeline

Quickstart:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt
cp .env.example .env
python scripts/download_clinvar.py
python scripts/query_gnomad_graphql.py
python scripts/prepare_brca2_variants.py
python scripts/apply_acmg_frequency_rules.py
python scripts/train_model.py
python scripts/evaluate_model.py
streamlit run app/streamlit_app.py
```
