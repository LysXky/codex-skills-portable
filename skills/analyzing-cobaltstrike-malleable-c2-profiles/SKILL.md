---
name: "analyzing-cobaltstrike-malleable-c2-profiles"
description: "Parse and analyze Cobalt Strike Malleable C2 profiles using dissect.cobaltstrike"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Analyzing CobaltStrike Malleable C2 Profiles

## Overview

Cobalt Strike Malleable C2 profiles are domain-specific language scripts that customize how Beacon communicates with the team server, defining HTTP request/response transformations, sleep intervals, jitter values, user agents, URI paths, and process injection behavior. Threat actors use malleable profiles to disguise C2 traffic as legitimate services (Amazon, Google, Slack). Analyzing these profiles reveals network indicators for detection: URI patterns, HTTP headers, POST/GET transforms, DNS settings, and process injection techniques. The `dissect.cobaltstrike` library can parse both profile files and extract configurations from beacon payloads, while `pyMalleableC2` provides AST-based parsing using Lark grammar for programmatic profile manipulation and validation.


## When to Use

- When investigating security incidents that require analyzing cobaltstrike malleable c2 profiles
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Python 3.9+ with `dissect.cobaltstrike` and/or `pyMalleableC2`
- Sample Malleable C2 profiles (available from public repositories)
- Understanding of HTTP protocol and Cobalt Strike beacon communication model
- Network monitoring tools (Suricata/Snort) for signature deployment
- PCAP analysis tools for traffic validation

## Steps

1. Install libraries: `pip install dissect.cobaltstrike` or `pip install pyMalleableC2`
2. Parse profile with `C2Profile.from_path("profile.profile")`
3. Extract HTTP GET/POST block configurations (URIs, headers, parameters)
4. Identify user agent strings and spoof targets
5. Extract sleep time, jitter percentage, and DNS beacon settings
6. Analyze process injection settings (spawn-to, allocation technique)
7. Generate Suricata/Snort signatures from extracted network indicators
8. Compare profile against known threat actor profile collections
9. Extract staging URIs and payload delivery mechanisms
10. Produce detection report with IOCs and recommended network signatures

## Expected Output

A JSON report containing extracted C2 URIs, HTTP headers, user agents, sleep/jitter settings, process injection config, spawned process paths, DNS settings, and generated Suricata-compatible detection rules.
