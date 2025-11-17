#!/bin/bash
# ------------------------------------------------------------------
# BRCA2-database-bias Sync Script
# Copies updated files FROM Google Drive TO local GitHub repo
# Then commits and pushes them automatically.
# ------------------------------------------------------------------

# Paths
DRIVE="/Users/geetmacbookpro/My Drive/BRCA2-database-bias"
REPO="/Users/geetmacbookpro/Documents/GitHub/BRCA2-database-bias"

echo "--------------------------------------------------------------"
echo "   SYNCING BRCA2 DATABASE BIAS PROJECT"
echo "--------------------------------------------------------------"
echo ""
echo "Copying updated notebooks from Drive → GitHub repo..."

# Copy notebooks
rsync -av --delete \
    "$DRIVE/notebooks/" \
    "$REPO/notebooks/"

echo ""
echo "Copying results tables (optional)..."

# Copy tables
rsync -av \
    "$DRIVE/results/tables/" \
    "$REPO/results/tables/"

echo ""
echo "Copying results figures (optional)..."

# Copy figures
rsync -av \
    "$DRIVE/results/figures/" \
    "$REPO/results/figures/"

echo ""
echo "Copying updated README if present..."

# Copy README
if [ -f "$DRIVE/README.md" ]; then
    cp "$DRIVE/README.md" "$REPO/README.md"
fi

echo ""
echo "Staging changes in Git..."

cd "$REPO"

git add -A

# Create timestamp for commit
timestamp=$(date +"%Y-%m-%d %H:%M:%S")
msg="Auto-sync from Google Drive on $timestamp"

echo "Committing with message:"
echo "   $msg"
git commit -m "$msg"

echo ""
echo "Pushing to GitHub (SSH)..."

git push origin main

echo ""
echo "--------------------------------------------------------------"
echo "   SYNC COMPLETE ✔"
echo "   GitHub is now up to date."
echo "--------------------------------------------------------------"
