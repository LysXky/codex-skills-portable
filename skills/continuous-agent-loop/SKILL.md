---
name: "continuous-agent-loop"
description: "Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls."
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

# Continuous Agent Loop

This is the v1.8+ canonical loop skill name. It supersedes `autonomous-loops` while keeping compatibility for one release.

## Loop Selection Flow

```text
Start
  |
  +-- Need strict CI/PR control? -- yes --> continuous-pr
  |
  +-- Need RFC decomposition? -- yes --> rfc-dag
  |
  +-- Need exploratory parallel generation? -- yes --> infinite
  |
  +-- default --> sequential
```

## Combined Pattern

Recommended production stack:
1. RFC decomposition (`ralphinho-rfc-pipeline`)
2. quality gates (`plankton-code-quality` + `/quality-gate`)
3. eval loop (`eval-harness`)
4. session persistence (`nanoclaw-repl`)

## Failure Modes

- loop churn without measurable progress
- repeated retries with same root cause
- merge queue stalls
- cost drift from unbounded escalation

## Recovery

- freeze loop
- run `/harness-audit`
- reduce scope to failing unit
- replay with explicit acceptance criteria
