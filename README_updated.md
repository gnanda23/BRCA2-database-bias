# BRCA2 Database Bias Project
A multi-phase pipeline to analyze BRCA2 population allele frequency bias, perform ACMG BA1/BS1 reclassification, and generate publication-ready outputs.

## Overview
This repository contains a full, reproducible pipeline for analyzing South Asian underrepresentation in BRCA2 variant databases, performing ACMG frequency-based reclassification, and generating figures and tables for manuscripts, posters, and Regeneron/ISEF submissions.

## Project Structure
BRCA2-database-bias/
├── data/
│   ├── raw/
│   ├── intermediate/
│   └── processed/
├── results/
│   ├── tables/
│   └── figures/
├── notebooks/
│   ├── BRCA2_Colab_Phase1_DataPrep.ipynb
│   ├── BRCA2_Colab_Phase2_SAAnalysis.ipynb
│   ├── BRCA2_Colab_Phase3_ACMG.ipynb
│   ├── BRCA2_Colab_Phase4_BiasValidation.ipynb
│   ├── BRCA2_Colab_Phase5_PublicationFigures.ipynb
│   └── BRCA2_Colab_00_RunAll.ipynb
└── README.md

## Pipeline Summary
### Phase 1 — Data Download & Merge
Downloads ClinVar + gnomAD, merges into master dataset.

### Phase 2 — South Asian Population Analysis
Examines SAS allele frequencies and descriptive patterns.

### Phase 3 — ACMG BA1/BS1 Reclassification
Applies ACMG frequency rules and outputs reclassification tables + Figure 2.

### Phase 4 — Bias Validation
Validates SAS underrepresentation, ClinVar review bias, SAS/EUR skew.

### Phase 5 — Publication Figures & Tables
Generates publication-ready figures and manuscript tables.

### Run-All Notebook
BRCA2_Colab_00_RunAll.ipynb executes all phases in sequence.

## Reproducibility
All notebooks are Google Colab–ready, Drive-mounted, modular, and plug-and-play for competitions and manuscripts.

## Citation
If using this code in research, please cite this repository.
