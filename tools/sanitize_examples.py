#!/usr/bin/env python3
"""Redact credential-shaped examples from the portable export."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS = [
    (
        re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"),
        "EXAMPLE_GITHUB_TOKEN_REDACTED",
    ),
    (
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "EXAMPLE_AWS_ACCESS_KEY_REDACTED",
    ),
    (
        re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "EXAMPLE_OPENAI_KEY_REDACTED",
    ),
    (
        re.compile(
            r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----.*?"
            r"-----END (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
            re.DOTALL,
        ),
        "EXAMPLE_PRIVATE_KEY_REDACTED",
    ),
    (
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
        "EXAMPLE_PRIVATE_KEY_HEADER_REDACTED",
    ),
    (
        re.compile(r"-----END (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
        "EXAMPLE_PRIVATE_KEY_FOOTER_REDACTED",
    ),
]

BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".exe", ".dll",
    ".so", ".onnx", ".ico", ".woff", ".woff2", ".ttf",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    changed = 0
    replacements = 0

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() in BINARY_SUFFIXES:
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        updated = original
        for pattern, replacement in PATTERNS:
            updated, count = pattern.subn(replacement, updated)
            replacements += count
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1

    print(f"Sanitized {replacements} credential-shaped examples across {changed} files.")


if __name__ == "__main__":
    main()
