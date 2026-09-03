#!/bin/zsh

# Paths
SOURCE_DIR="$HOME/gtm-revops-toolkit"
TARGET_DIR="$HOME/maya-htt-gtm-toolkit"

echo "🔄 Starting GTM Toolkit Sync..."

# Ensure target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "❌ Target directory $TARGET_DIR does not exist."
    exit 1
fi

cd "$TARGET_DIR" || exit

# Pull latest remote changes first
echo "📥 Fetching latest remote changes..."
git pull origin main --rebase

# Sync modular assets from gtm-revops-toolkit
if [ -d "$SOURCE_DIR" ]; then
    echo "📦 Copying modules from gtm-revops-toolkit..."
    
    # Core logic & scripts
    rsync -av --ignore-existing "$SOURCE_DIR/core/" ./src/core/ 2>/dev/null || true
    rsync -av --ignore-existing "$SOURCE_DIR/scripts/" ./src/scripts/ 2>/dev/null || true
    rsync -av --ignore-existing "$SOURCE_DIR/config/" ./config/ 2>/dev/null || true
    rsync -av --ignore-existing "$SOURCE_DIR/Signals/" ./src/enrichment/signals/ 2>/dev/null || true
    rsync -av --ignore-existing "$SOURCE_DIR/Templates/" ./templates/ 2>/dev/null || true
    
    echo "✅ Modules synced successfully."
else
    echo "⚠️ Source directory $SOURCE_DIR not found. Skipping file copy."
fi

# Git Commit and Push Sequence
echo "🚀 Staging and committing changes..."
git add .

if git diff-index --quiet HEAD --; then
    echo "✨ No new changes to commit."
else
    git commit -m "sync: update modular engines and configs from primary RevOps toolkit"
    echo "📤 Pushing to GitHub..."
    git push origin main
    echo "🎉 Sync & Push Complete!"
fi
