#!/usr/bin/env bash
set -euo pipefail

CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
SKILL_DIR="$CODEX_HOME/skills/pdf-to-markdown"
PYTHON_BIN="${PYTHON_BIN:-python3}"
RUNTIME="$SKILL_DIR/.runtime"

test -f "$SKILL_DIR/requirements.txt" || {
  echo "pdf-to-markdown is not installed at $SKILL_DIR" >&2
  exit 1
}

"$PYTHON_BIN" -m venv "$RUNTIME"
"$RUNTIME/bin/python" -m pip install --upgrade pip
"$RUNTIME/bin/python" -m pip install -r "$SKILL_DIR/requirements.txt"
"$RUNTIME/bin/python" -m pip check
"$RUNTIME/bin/python" -m markitdown --version

echo "PDF conversion runtime installed at: $RUNTIME"
