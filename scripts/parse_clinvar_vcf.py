import pysam
import pandas as pd

vcf_path = "/content/drive/MyDrive/BRCA2-database-bias/data/raw/clinvar_brca2.vcf.gz"
records = []

vcf = pysam.VariantFile(vcf_path)

for rec in vcf.fetch():
    # Skip rows with missing REF or ALT
    if rec.ref is None:
        continue
    if rec.alts is None:
        continue

    csig = rec.info.get("CLNSIG")
    review = rec.info.get("CLNREVSTAT")

    for alt in rec.alts:
        if alt in [None, ".", ""]:
            continue

        records.append({
            "Chromosome": rec.chrom.replace("chr",""),
            "Start": rec.pos,
            "ReferenceAllele": rec.ref,
            "AlternateAllele": alt,
            "ClinicalSignificance": str(csig),
            "ReviewStatus": str(review)
        })

df = pd.DataFrame(records)
df.to_csv("/content/drive/MyDrive/BRCA2-database-bias/data/raw/clinvar_brca2_parsed.csv", index=False)

print("Parsed:", len(df), "valid variants.")
