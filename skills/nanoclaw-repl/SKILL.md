---
name: "nanoclaw-repl"
description: "Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p."
metadata:
  origin: ECC
---

## Codex compatibility

This skill was imported from ECC for Codex.

- Interpret generic references to Claude Code as the equivalent Codex workflow.
- Treat slash commands as named workflows unless the current Codex surface exposes them.
- Replace hook-only enforcement with explicit checks during the task.
- Verify that any referenced MCP server, CLI, API key, or external service is available before relying on it.
- On Windows, translate Bash-only examples to PowerShell or use an available compatible shell.

# NanoClaw REPL

Use this skill when running or extending `scripts/claw.js`.

## Capabilities

- persistent markdown-backed sessions
- model switching with `/model`
- dynamic skill loading with `/load`
- session branching with `/branch`
- cross-session search with `/search`
- history compaction with `/compact`
- export to md/json/txt with `/export`
- session metrics with `/metrics`

## Operating Guidance

1. Keep sessions task-focused.
2. Branch before high-risk changes.
3. Compact after major milestones.
4. Export before sharing or archival.

## Extension Rules

- keep zero external runtime dependencies
- preserve markdown-as-database compatibility
- keep command handlers deterministic and local
