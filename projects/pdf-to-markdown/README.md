# PDF to Markdown for Codex

Portable manual installation of the `$pdf-to-markdown` skill. It converts local PDFs into plain Markdown with [Microsoft MarkItDown](https://github.com/microsoft/markitdown), without an LLM or external document service.

## Linux / VSCodium

Prerequisites:

- Python 3.10 or newer
- `python3-venv`
- Codex configured to discover `$CODEX_HOME/skills` or `~/.codex/skills`

Install:

```bash
git clone https://github.com/LysXky/codex-skills-portable.git
cd codex-skills-portable
chmod +x projects/pdf-to-markdown/install.sh
./projects/pdf-to-markdown/install.sh
```

Restart Codex or VSCodium. Then request:

```text
Use $pdf-to-markdown to convert /home/user/Documents/example.pdf
```

## Manual installation

```bash
mkdir -p ~/.codex/skills
cp -R skills/pdf-to-markdown ~/.codex/skills/
python3 -m venv ~/.codex/skills/pdf-to-markdown/.runtime
~/.codex/skills/pdf-to-markdown/.runtime/bin/python -m pip install \
  -r ~/.codex/skills/pdf-to-markdown/requirements.txt
```

## Direct CLI usage

```bash
~/.codex/skills/pdf-to-markdown/.runtime/bin/python \
  ~/.codex/skills/pdf-to-markdown/scripts/convert_pdf.py \
  /absolute/path/document.pdf
```

Options:

```text
--output PATH
--output-dir DIR
--overwrite
--timeout SECONDS
--max-mib MIB
```

## Design

- Validates `.pdf`, file size and `%PDF-` signature.
- Calls MarkItDown without a shell.
- Performs deterministic text normalization.
- Avoids overwrite unless requested.
- Detects near-empty output from scanned PDFs.
- Uses zero LLM tokens during conversion.

## Repository layout

```text
pdf-to-markdown/
├── install.sh
├── install.ps1
├── requirements.txt
├── skill/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── requirements.txt
│   └── scripts/convert_pdf.py
├── src/convert_pdf.py
└── tests/test_convert_pdf.py
```

Run the deterministic tests:

```bash
python3 -m unittest discover -s tests -v
```

## Limitation

This workflow extracts textual Markdown. It does not preserve exact page layout, images, complex tables, formulas or reliable reading order in every multi-column PDF. Scanned documents require a separate OCR workflow.
