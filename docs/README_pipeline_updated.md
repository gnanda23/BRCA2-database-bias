# BRCA2 South-Asian Database Bias — Reproducible Pipeline

Quickstart (Mac or Colab):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt

# Navigate to your Google Drive project folder
cd ~/Library/CloudStorage/GoogleDrive-geeta.nanda@gmail.com/My\ Drive/BRCA2-database-bias

# Run data integration pipeline
python scripts/query_gnomad_graphql.py
python scripts/prepare_brca2_variants.py
python scripts/apply_acmg_frequency_rules.py
python scripts/train_model.py
python scripts/evaluate_model.py

# Launch the Streamlit app
streamlit run app/streamlit_app.py
```

All data and results are saved in:
`/My Drive/BRCA2-database-bias/data/processed/` and `/My Drive/BRCA2-database-bias/results/`.
