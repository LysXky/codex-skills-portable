---
estado: publicado
github: https://github.com/LysXky/codex-skills-portable
skills: 1091
tags:
  - codex
  - github
  - linux
  - vscodium
---

# Codex Skills Portable

Repositorio público para transportar las skills locales de Codex a Linux y VSCodium.

- GitHub: [LysXky/codex-skills-portable](https://github.com/LysXky/codex-skills-portable)
- Skills exportadas: **1.091**
- Instaladores: Linux y Windows
- Catálogo: `docs/CATALOG.md`
- Manifiesto: `manifest.json`
- Proyecto manual PDF → Markdown: `projects/pdf-to-markdown`

## Instalación rápida en Linux

```bash
git clone https://github.com/LysXky/codex-skills-portable.git
cd codex-skills-portable
chmod +x scripts/*.sh
./scripts/install.sh
./scripts/setup-pdf-to-markdown.sh
```

Reiniciar Codex o VSCodium después de instalar.

## Consideraciones

- Los runtimes y cachés locales no se versionan.
- La dependencia de MarkItDown se reconstruye en Linux mediante un entorno virtual.
- La colección contiene licencias mixtas y conserva atribución.
- Los ejemplos con apariencia de credencial fueron redactados en la copia pública.
- Las skills ofensivas requieren autorización explícita y revisión de scripts antes de ejecutarlos.
