# 🧬 BRCA2 Database Bias Project

### Overview
This project investigates **data bias in BRCA2 variant databases**, with a focus on underrepresented populations (e.g., South Asian genetic data).  
It is part of a broader research effort to improve **genomic diversity, variant interpretation accuracy,** and **fairness in precision medicine datasets.**

---

## 📂 Project Structure
```
BRCA2-database-bias/
│
├── data/
│   ├── raw/               # Original datasets (ClinVar, COSMIC, etc.)
│   └── processed/         # Cleaned, standardized data
│
├── results/
│   ├── figures/           # Visualizations, charts, and plots
│   └── tables/            # Processed outputs and summary tables
│
├── models/                # Machine learning models
├── scripts/               # Helper scripts
├── app/                   # Streamlit web app (Phase 4)
├── docs/                  # Documentation and notes
├── notebooks/             # Jupyter/Colab notebooks
│
├── .venv/                 # Virtual environment (auto-created)
├── setup_env.sh           # One-time environment setup
├── activate_env.sh        # Daily environment activation
├── reset_env.sh           # Full rebuild of environment
└── README.md              # Project documentation
```

---

## ⚙️ Environment Setup

### 🧩 Option 1: First-Time Setup
Run this command in Terminal (Mac):
```bash
./setup_env.sh
```
This will:
- Create the `.venv` virtual environment  
- Install all core dependencies  
- Confirm installation success

---

### 🚀 Option 2: Daily Activation
To start working in your project environment:
```bash
./activate_env.sh
```
You’ll see your terminal change to:
```
(.venv) geetmacbookpro@Geetas-MBP ...
```

---

### 🧹 Option 3: Environment Rebuild (if needed)
If dependencies break or you need a clean environment:
```bash
./reset_env.sh
```
This deletes `.venv` and reinstalls everything cleanly.

---

## 🧠 Project Phases

| Phase | Description | Status |
|:------|:-------------|:--------|
| 🟩 0 | Environment setup and configuration | ✅ Complete |
| 🟨 1 | Data sourcing (ClinVar, gnomAD, COSMIC, etc.) | ⏳ In progress |
| 🟨 2 | Data cleaning + population annotation | ⏳ Planned |
| 🟧 3 | Feature extraction + machine learning sandbox | 🔜 Upcoming |
| 🟦 4 | Streamlit app dashboard | 🔜 Upcoming |
| 🟪 5 | Final reporting and visualization | 🔜 Upcoming |

---

## 🧰 Requirements
- **Python ≥ 3.10**
- macOS / Google Colab / Linux environment
- (Optional) Google Drive sync for persistence

---

## 🤝 How to Contribute
1. Clone this repository or download from Google Drive  
2. Run `./setup_env.sh` to configure your environment  
3. Work within notebooks or scripts under version control  
4. Commit new code and push updates to your GitHub fork  

**Naming Convention:**  
Branch names should use this format — `phaseX-description` (e.g., `phase2-cleaning`).

---

## 🧭 Future Enhancements
- Streamlit dashboard (`launch_app.sh`) for interactive exploration  
- Integration with population-specific BRCA2 datasets  
- Automated summary tables (results/tables/)  
- Bias visualization dashboard

---

## 📬 Contact
**Project Lead:** Geeta Nanda  
**Purpose:** Educational / Research – BRCA2 Variant Database Bias  
**Keywords:** BRCA2, South Asian Genomics, Database Fairness, Machine Learning

---

> 💡 *Tip:* When you reach **Phase 4**, I’ll remind you to generate your one-click Streamlit launcher (`launch_app.sh`).  
> 🧠 Stay organized: always activate your environment before running notebooks or scripts.
