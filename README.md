# Codex Skills Portable

Portable collection of **1,110 Codex skills** prepared for Windows, Linux and VSCodium.

## What is included

- Engineering, testing, architecture, research and content skills from ECC.
- 817 cybersecurity skills adapted for explicit invocation and authorized use.
- A legal cybersecurity training-lab finder with 111 cataloged resources.
- Graph-based codebase exploration with `graphify`.
- UI and design workflow skills including `ui-ux-pro-max`, `ui-styling`, and `banner-design`.
- Superpowers development-process skills for brainstorming, planning, TDD, debugging, review, and branch completion.
- `$pdf-to-markdown`, a local zero-token PDF-to-Markdown converter based on Microsoft MarkItDown.
- Linux and Windows installers.
- A generated catalog and machine-readable manifest.

See [the complete catalog](docs/CATALOG.md).

## Linux / VSCodium quick start

```bash
git clone https://github.com/LysXky/codex-skills-portable.git
cd codex-skills-portable
chmod +x scripts/*.sh
./scripts/install.sh
```

Enable PDF conversion:

```bash
./scripts/setup-pdf-to-markdown.sh
```

Restart Codex or VSCodium after installation.

## Windows quick start

```powershell
git clone https://github.com/LysXky/codex-skills-portable.git
cd codex-skills-portable
.\scripts\install.ps1
.\scripts\setup-pdf-to-markdown.ps1
```

## Selective installation

Copy only the skill directories you need into `$CODEX_HOME/skills` or `~/.codex/skills`.

```bash
cp -R skills/tdd-workflow ~/.codex/skills/
cp -R skills/pdf-to-markdown ~/.codex/skills/
```

## PDF-to-Markdown project

See [projects/pdf-to-markdown](projects/pdf-to-markdown/README.md) for manual setup and direct CLI usage. Conversion is local and consumes no LLM tokens.

## Security

- Cybersecurity skills are knowledge and workflow packages, not authorization to test third-party systems.
- Use offensive material only in environments you own or are explicitly authorized to assess.
- Inspect bundled scripts before execution.
- Runtimes, caches, credentials and local configuration are intentionally excluded.

## Licenses

This is a mixed-license aggregation. Read [docs/LICENSING.md](docs/LICENSING.md) and retain the per-skill license files.
