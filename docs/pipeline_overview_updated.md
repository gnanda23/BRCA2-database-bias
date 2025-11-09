# Pipeline Overview — BRCA2-database-bias

1️⃣ **download_clinvar.py** → Download ClinVar variant_summary.txt.gz into `/data/raw/`
2️⃣ **query_gnomad_graphql.py** → Query BRCA2 frequencies via gnomAD GraphQL API  
  ➡ Output: `/data/processed/gnomad_brca2_af.csv`
3️⃣ **prepare_brca2_variants.py** → Merge ClinVar + gnomAD  
  ➡ Output: `/data/processed/brca2_merged.csv`
4️⃣ **apply_acmg_frequency_rules.py** → Flag BA1/BS1 frequency-based reclassification  
  ➡ Output: `/results/tables/table1_acmg_reclassifications.csv`
5️⃣ **train_model.py** → Train XGBoost classifier  
  ➡ Output: `/models/brca2_xgb.joblib`
6️⃣ **evaluate_model.py** → Evaluate and visualize model performance  
  ➡ Output: `/results/figures/figure3_pr_curve.png`
7️⃣ **app/streamlit_app.py** → Launch the web app  
  ➡ Run from `/My Drive/BRCA2-database-bias/`
