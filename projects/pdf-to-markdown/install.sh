#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
DEST="$CODEX_HOME/skills/pdf-to-markdown"

mkdir -p "$CODEX_HOME/skills"
rm -rf "$DEST"
cp -R "$PROJECT_ROOT/skill" "$DEST"

python3 -m venv "$DEST/.runtime"
"$DEST/.runtime/bin/python" -m pip install --upgrade pip
"$DEST/.runtime/bin/python" -m pip install -r "$DEST/requirements.txt"
"$DEST/.runtime/bin/python" -m pip check

echo "Installed pdf-to-markdown at: $DEST"
