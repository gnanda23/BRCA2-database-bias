import os
import time
import requests
import pandas as pd

# ================================================================
# BRCA2 South-Asian Database Bias Project
# Script: query_gnomad_graphql.py
# Purpose: Query BRCA2 variant allele frequencies by population
# Output: data/processed/gnomad_brca2_af.csv
# Project folder: /My Drive/BRCA2-database-bias/
# ================================================================

API = "https://gnomad.broadinstitute.org/api"
CHR = "13"
GENE_START = 32315086
GENE_END = 32400268
WINDOW = 5000

QUERY = '''
query Region($chrom: String!, $start: Int!, $stop: Int!) {
  region(chrom: $chrom, start: $start, stop: $stop, reference_genome: GRCh38) {
    variants(dataset: gnomad_r4) {
      variant_id
      pos
      ref
      alt
      consequence
      exome { populations { id ac an } }
      genome { populations { id ac an } }
    }
  }
}
'''

def graphql(query, variables):
    """Send a GraphQL query to the gnomAD API and return the JSON response."""
    response = requests.post(API, json={"query": query, "variables": variables}, timeout=60)
    response.raise_for_status()
    return response.json()

rows = []
s = GENE_START
while s <= GENE_END:
    e = min(s + WINDOW - 1, GENE_END)
    data = graphql(QUERY, {"chrom": CHR, "start": s, "stop": e})
    region = data.get("data", {}).get("region")
    if region:
        for v in region.get("variants", []):
            pops = {}
            for layer in ("exome", "genome"):
                layer_data = v.get(layer) or {}
                for p in (layer_data.get("populations") or []):
                    ac, an = p.get("ac") or 0, p.get("an") or 0
                    af = (ac / an) if an else 0.0
                    pid = p.get("id")
                    pops[pid] = max(pops.get(pid, 0), af)
            rows.append({
                "variant_id": v["variant_id"],
                "chrom": CHR,
                "pos": v["pos"],
                "ref": v["ref"],
                "alt": v["alt"],
                "consequence": v.get("consequence"),
                "sas_af": pops.get("sas", 0.0),
                "eur_af": pops.get("nfe", 0.0) or pops.get("eur", 0.0),
                "afr_af": pops.get("afr", 0.0),
                "eas_af": pops.get("eas", 0.0),
                "amr_af": pops.get("amr", 0.0)
            })
    s = e + 1
    time.sleep(0.25)

# Ensure output directory exists
os.makedirs("data/processed", exist_ok=True)

# Save the resulting CSV
out_csv = "data/processed/gnomad_brca2_af.csv"
pd.DataFrame(rows).drop_duplicates("variant_id").to_csv(out_csv, index=False)

print("✅ Saved:", out_csv)
print(f"Total variants retrieved: {len(rows)}")
