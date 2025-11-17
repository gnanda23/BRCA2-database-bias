import pandas as pd

IN_PATH = "/content/drive/MyDrive/BRCA2-database-bias/data/raw/variant_summary.txt.gz"
OUT_PATH = "/content/drive/MyDrive/BRCA2-database-bias/data/raw/clinvar_brca2.tsv.gz"

print("[ClinVar Filter] Loading only required columns...")

usecols = [
    "GeneSymbol","Chromosome","Start","Stop",
    "ReferenceAllele","AlternateAllele",
    "ClinicalSignificance","ReviewStatus",
    "LastEvaluated","VariationID"
]

df = pd.read_csv(IN_PATH, sep="\t", low_memory=False, usecols=usecols)

print("[ClinVar Filter] Filtering to BRCA2...")
df = df[df["GeneSymbol"].astype(str).str.upper() == "BRCA2"].copy()

# BRCA2 HGVS fields do not exist in this file → create placeholders
df["HGVS_coding"] = None
df["HGVS_protein"] = None
df["DateLastUpdated"] = df["LastEvaluated"]

print("[ClinVar Filter] Saving BRCA2-only file...")
df.to_csv(OUT_PATH, sep="\t", index=False, compression="gzip")

print("[ClinVar Filter] Done. Rows:", len(df))
