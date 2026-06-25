#!/usr/bin/env python3
"""Convert one local PDF to normalized Markdown through Microsoft MarkItDown."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Local PDF path")
    destination = parser.add_mutually_exclusive_group()
    destination.add_argument("--output", type=Path, help="Exact output .md path")
    destination.add_argument("--output-dir", type=Path, help="Directory for the generated .md")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--max-mib", type=int, default=100)
    return parser.parse_args()


def validate_input(path: Path, max_mib: int) -> Path:
    path = path.expanduser().resolve()
    if not path.is_file():
        raise ValueError(f"PDF not found or not a regular file: {path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError("Input must use the .pdf extension")
    if path.stat().st_size == 0:
        raise ValueError("Input PDF is empty")
    if path.stat().st_size > max_mib * 1024 * 1024:
        raise ValueError(f"Input exceeds the {max_mib} MiB limit")
    with path.open("rb") as stream:
        if stream.read(5) != b"%PDF-":
            raise ValueError("Input does not have a valid PDF signature")
    return path


def available_output(path: Path, overwrite: bool) -> Path:
    path = path.expanduser().resolve()
    if path.suffix.lower() != ".md":
        path = path.with_suffix(".md")
    path.parent.mkdir(parents=True, exist_ok=True)
    if overwrite or not path.exists():
        return path
    candidate = path.with_name(f"{path.stem}-converted{path.suffix}")
    index = 2
    while candidate.exists():
        candidate = path.with_name(f"{path.stem}-{index}{path.suffix}")
        index += 1
    return candidate


def normalize_markdown(text: str) -> str:
    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n" if text.strip() else ""


def convert(pdf: Path, output: Path, timeout: int) -> tuple[int, bool]:
    with tempfile.TemporaryDirectory(prefix="pdf-to-md-") as temp_dir:
        raw_output = Path(temp_dir) / "output.md"
        command = [
            sys.executable,
            "-m",
            "markitdown",
            str(pdf),
            "-o",
            str(raw_output),
        ]
        environment = os.environ.copy()
        environment["PYTHONUTF8"] = "1"
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                env=environment,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(f"Conversion exceeded {timeout} seconds") from exc
        if result.returncode != 0:
            detail = (result.stderr or result.stdout or "Unknown MarkItDown error").strip()
            raise RuntimeError(f"MarkItDown failed: {detail[:2000]}")
        if not raw_output.exists():
            raise RuntimeError("MarkItDown completed without creating an output file")
        normalized = normalize_markdown(raw_output.read_text(encoding="utf-8", errors="replace"))
        output.write_text(normalized, encoding="utf-8", newline="\n")
        visible = len(re.sub(r"[\s#>*_`\-]", "", normalized))
        return len(normalized), visible < 20


def main() -> int:
    options = parse_args()
    try:
        pdf = validate_input(options.input, options.max_mib)
        requested = options.output or (
            options.output_dir.expanduser().resolve() / f"{pdf.stem}.md"
            if options.output_dir
            else pdf.with_suffix(".md")
        )
        output = available_output(requested, options.overwrite)
        character_count, likely_scanned = convert(pdf, output, options.timeout)
        print(f"OUTPUT={output}")
        print(f"CHARACTERS={character_count}")
        print(f"LIKELY_SCANNED={'true' if likely_scanned else 'false'}")
        return 0
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"ERROR={exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
