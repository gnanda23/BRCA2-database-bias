"""
query_gnomad_graphql_updated.py
--------------------------------
Fetches BRCA2 variant allele frequency data from the gnomAD GraphQL API (v4)
and saves it to data/processed/gnomad_brca2_af.csv
"""

import requests
import pandas as pd
import os

# === gnomAD GraphQL endpoint ===
GNOMAD_GRAPHQL_URL = "https://gnomad.broadinstitute.org/api"

# === Updated GraphQL query (v4 schema) ===
query = """
query BRCA2Variants {
  gene(gene_symbol: "BRCA2") {
    variants {
      variant_id
      chrom
      pos
      ref
      alt
      allele_freq
      populations {
        id
        allele_freq
      }
    }
  }
}
"""

def fetch_gnomad_variants():
    print("🔗 Connecting to gnomAD GraphQL API (v4)...")
    response = requests.post(GNOMAD_GRAPHQL_URL, json={"query": query})
    if response.status_code != 200:
        raise Exception(f"❌ GraphQL query failed: {response.status_code} - {response.text}")

    data = response.json()
    variants = data.get("data", {}).get("gene", {}).get("variants", [])
    if not variants:
        raise Exception("❌ No variants returned from gnomAD API.")

    df = pd.json_normalize(variants)
    print(f"✅ Retrieved {len(df):,} BRCA2 variants from gnomAD.")

    # Extract population-level frequencies
    pop_cols = ["populations." + str(i) + ".id" for i in range(10)]
    pop_freq_cols = ["populations." + str(i) + ".allele_freq" for i in range(10)]
    pop_cols_present = [c for c in df.columns if c.startswith("populations.")]

    # Flatten population data dynamically
    pop_data = []
    for _, row in df.iterrows():
        if isinstance(row.get("populations"), list):
            pop_entry = {p["id"]: p["allele_freq"] for p in row["populations"] if p.get("id")}
        else:
            pop_entry = {}
        pop_data.append(pop_entry)
    pop_df = pd.DataFrame(pop_data).add_prefix("AF_")

    # Merge back to main DataFrame
    df = pd.concat([df.drop(columns=["populations"], errors="ignore"), pop_df], axis=1)

    # Save clean columns
    cols = ["chrom", "pos", "ref", "alt", "allele_freq"] + [c for c in df.columns if c.startswith("AF_")]
    df = df[cols]

    # Convert numeric
    for c in df.columns:
        if c != "chrom" and not c.startswith("AF_"):
            df[c] = pd.to_numeric(df[c], errors="coerce")

    return df

def main():
    base_dir = "/content/drive/MyDrive/BRCA2-database-bias"
    output_path = os.path.join(base_dir, "data/processed/gnomad_brca2_af.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = fetch_gnomad_variants()
    df.to_csv(output_path, index=False)
    print(f"💾 Saved to: {output_path}")

    print("\\n=== Summary ===")
    print(df.describe(include='all'))
    print("\\nSample rows:")
    print(df.head())

if __name__ == "__main__":
    main()