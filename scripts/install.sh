#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$REPO_ROOT/skills"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
DEST="$CODEX_HOME/skills"

mkdir -p "$DEST"

if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude '.runtime/' --exclude '__pycache__/' "$SOURCE/" "$DEST/"
else
  cp -R "$SOURCE/." "$DEST/"
  find "$DEST" -type d -name __pycache__ -prune -exec rm -rf {} +
  find "$DEST" -type d -name .runtime -prune -exec rm -rf {} +
fi

echo "Installed skills into: $DEST"
echo "Run scripts/setup-pdf-to-markdown.sh to enable local PDF conversion."
echo "Restart Codex or VSCodium after installation."
