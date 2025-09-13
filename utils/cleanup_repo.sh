#!/usr/bin/env bash
set -euo pipefail

echo "🧹 Cleaning-up repository before pushing to GitHub..."

# 1. Remove Jupyter checkpoints, cache dirs, compiled Python, venvs, Git ignore files, and macOS metadata
echo " - Removing temp, cache, venvs, and gitignore files..."
find . -name ".ipynb_checkpoints" -type d -exec rm -rf {} +
find . -name ".DS_Store" -type f -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name ".pytest_cache" -type d -exec rm -rf {} +
find . -name "*.pyc" -type f -delete
find . -name "*.pyo" -type f -delete
find . -type d \( -name "venv" -o -name ".venv" -o -name "env" -o -name ".env" \) -exec rm -rf {} +
find . -maxdepth 1 -type f \( -name ".gitignore" -o -name ".gitattributes" -o -name ".gitmodules" \) -delete
rm -f .coverage coverage.xml

# 2. Fix notebook schema, clear outputs and execution counts
echo " - Normalizing notebooks..."
find . -name "*.ipynb" -print0 | while IFS= read -r -d '' nb; do
  tmpfile=$(mktemp)
  trap 'rm -f "$tmpfile"' EXIT

  # Normalize schema: ensure outputs: [] and clean execution_count
  jq '(.cells[]? | select(.cell_type=="code") | .outputs) //= []
      | (.cells[]? | select(.cell_type=="code") | .execution_count) |= (if . == " " then null else . end)' \
      "$nb" > "$tmpfile"

  mv "$tmpfile" "$nb"

  # Clear outputs and execution counts (official tool)
  jupyter nbconvert --to notebook \
    --ClearOutputPreprocessor.enabled=True \
    --inplace "$nb" >/dev/null 2>&1 || true
done

# 3. Stage deletions in Git
echo " - Staging deletions in Git..."
git add -u

echo "✅ Repo cleaned, notebooks normalized, and deletions staged for commit!"

