---
estado: publicado
github: https://github.com/LysXky/codex-skills-portable
skills: 1111
tags:
  - codex
  - github
  - linux
  - vscodium
---

# Codex Skills Portable

Repositorio público para transportar las skills locales de Codex a Linux y VSCodium.

- GitHub: [LysXky/codex-skills-portable](https://github.com/LysXky/codex-skills-portable)
- Skills exportadas: **1.111**
- Instaladores: Linux y Windows
- Catálogo: `docs/CATALOG.md`
- Manifiesto: `manifest.json`
- Proyecto manual PDF → Markdown: `projects/pdf-to-markdown`
- Nuevas fuentes agregadas: `graphify`, `ui-ux-pro-max-skill`, `superpowers`, `ian-xiaohei-illustrations`

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
- El exportador del repo maneja mejor directorios de solo lectura en Windows para regenerar `skills/` sin fallar.
