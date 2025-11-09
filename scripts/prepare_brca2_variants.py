
#!/usr/bin/env python
import os, math
import pandas as pd

RAW = "data/raw"
PROC = "data/processed"
os.makedirs(PROC, exist_ok=True)

clinvar_path = os.path.join(RAW, "clinvar_brca2.tsv.gz")
gnomad_path = os.path.join(PROC, "gnomad_brca2_af.csv")
out_path = os.path.join(PROC, "brca2_merged.csv")

def build_variant_key(df):
    return (
        df["Chromosome"].astype(str).str.replace("chr","",regex=False) + "-" +
        df["Start"].astype(str) + "-" +
        df["ReferenceAllele"].astype(str) + "-" +
        df["AlternateAllele"].astype(str)
    )

def main():
    print("[Merge] Loading ClinVar and gnomAD...")
    cv = pd.read_csv(clinvar_path, sep="\t", low_memory=False)
    cv["variant_key"] = build_variant_key(cv)

    gd = pd.read_csv(gnomad_path)
    gd["variant_key"] = gd["chrom"].astype(str) + "-" + gd["pos"].astype(str) + "-" + gd["ref"].astype(str) + "-" + gd["alt"].astype(str)

    merged = cv.merge(gd, on="variant_key", how="left", suffixes=("_clinvar","_gnomad"))

    merged["sas_eur_ratio"] = (merged["sas_af"].fillna(0) + 1e-12) / (merged["eur_af"].fillna(0) + 1e-12)
    merged["log10_sas_af"] = (merged["sas_af"].fillna(1e-12)).apply(lambda x: math.log10(x))
    merged["log10_eur_af"] = (merged["eur_af"].fillna(1e-12)).apply(lambda x: math.log10(x))
    merged["is_vus"] = merged["ClinicalSignificance"].astype(str).str.contains("Uncertain", case=False, na=False)

    keep = [
        "variant_key","GeneSymbol","ClinicalSignificance","ReviewStatus","Chromosome","Start","Stop",
        "ReferenceAllele","AlternateAllele","HGVS_coding","HGVS_protein","DateLastUpdated",
        "variant_id","pos","ref","alt","consequence",
        "sas_af","eur_af","afr_af","eas_af","amr_af","sas_eur_ratio","log10_sas_af","log10_eur_af","is_vus"
    ]
    for c in keep:
        if c not in merged.columns:
            merged[c] = None

    merged[keep].to_csv(out_path, index=False)
    print(f"[Merge] Wrote: {out_path}  (n={len(merged):,})")

if __name__ == "__main__":
    main()
