---
name: "analyzing-persistence-mechanisms-in-linux"
description: "Detect and analyze Linux persistence mechanisms including crontab entries,"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Analyzing Persistence Mechanisms in Linux

## Overview

Adversaries establish persistence on Linux systems through crontab jobs, systemd service/timer units, LD_PRELOAD library injection, shell profile modifications (.bashrc, .profile), SSH authorized_keys backdoors, and init script manipulation. This skill scans for all known persistence vectors, checks file timestamps and integrity, and correlates findings with auditd logs to build a timeline of persistence installation.


## When to Use

- When investigating security incidents that require analyzing persistence mechanisms in linux
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Root or sudo access on target Linux system (or forensic image)
- auditd configured with file watch rules on persistence paths
- Python 3.8+ with standard library (os, subprocess, json)
- Optional: OSSEC/Wazuh agent for file integrity monitoring alerts

## Steps

1. **Scan Crontab Entries** — Enumerate all user crontabs, /etc/cron.d/, /etc/cron.daily/, and anacron jobs for suspicious commands
2. **Audit Systemd Units** — Check /etc/systemd/system/ and ~/.config/systemd/user/ for non-package-managed service and timer units
3. **Detect LD_PRELOAD Hijacking** — Check /etc/ld.so.preload and LD_PRELOAD environment variable for injected shared libraries
4. **Inspect Shell Profiles** — Scan .bashrc, .bash_profile, .profile, /etc/profile.d/ for injected commands or reverse shells
5. **Check SSH Authorized Keys** — Audit all authorized_keys files for unauthorized public keys with command restrictions
6. **Correlate Auditd Logs** — Search auditd logs for file modification events on persistence paths to build an installation timeline
7. **Generate Persistence Report** — Produce a risk-scored report of all discovered persistence mechanisms

## Expected Output

- JSON report of all persistence mechanisms found with risk scores
- Timeline of persistence installation from auditd correlation
- MITRE ATT&CK technique mapping (T1053, T1543, T1574, T1546)
- Remediation commands for each detected persistence mechanism
