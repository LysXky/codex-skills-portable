# Install on Linux and VSCodium

## Complete collection

```bash
git clone https://github.com/LysXky/codex-skills-portable.git
cd codex-skills-portable
chmod +x scripts/*.sh
./scripts/install.sh
```

The default destination is `~/.codex/skills`. Override it with:

```bash
CODEX_HOME=/custom/codex/home ./scripts/install.sh
```

Restart Codex or the VSCodium extension host after installation.

## PDF conversion dependency

Debian/Ubuntu:

```bash
sudo apt-get install python3 python3-venv
./scripts/setup-pdf-to-markdown.sh
```

Fedora:

```bash
sudo dnf install python3
./scripts/setup-pdf-to-markdown.sh
```

Arch:

```bash
sudo pacman -S python
./scripts/setup-pdf-to-markdown.sh
```

## Selective installation

```bash
mkdir -p ~/.codex/skills
cp -R skills/tdd-workflow ~/.codex/skills/
cp -R skills/pdf-to-markdown ~/.codex/skills/
```

## Updating

```bash
git pull
./scripts/install.sh
```

The installer replaces matching skill directories but does not delete unrelated local skills.
