# BRCA2 South-Asian Database Bias Project — Terminal Command Log

These are all the terminal commands used for setting up and running the **query_gnomad_graphql.py** script on macOS (Google Drive version).

**Project folder:** `/My Drive/BRCA2-database-bias/`

---

### 1️⃣ Navigate to project folder
```bash
cd ~/Library/CloudStorage/GoogleDrive-geeta.nanda@gmail.com/My\ Drive/BRCA2-database-bias
```

### 2️⃣ Activate virtual environment
```bash
source .venv/bin/activate
```

### 3️⃣ Confirm location
```bash
pwd
ls
```

### 4️⃣ Create the scripts/ folder (if missing)
```bash
mkdir -p scripts
```

### 5️⃣ Create the query_gnomad_graphql.py script
```bash
cat > scripts/query_gnomad_graphql.py <<'EOF'
# [Python code identical to script in txt version]
EOF
```

### 6️⃣ Verify the file
```bash
ls scripts
```

### 7️⃣ Run the script
```bash
python scripts/query_gnomad_graphql.py
```

### 8️⃣ Confirm output CSV
```bash
ls data/processed
```

### 9️⃣ Preview the CSV
```bash
python -c "import pandas as pd; print(pd.read_csv('data/processed/gnomad_brca2_af.csv').head())"
```

---

✅ **Output generated:** `data/processed/gnomad_brca2_af.csv`
