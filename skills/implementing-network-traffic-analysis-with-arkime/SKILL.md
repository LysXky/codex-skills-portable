---
name: "implementing-network-traffic-analysis-with-arkime"
description: "Deploy and query Arkime (formerly Moloch) for full packet capture network"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Implementing Network Traffic Analysis with Arkime


## When to Use

- When deploying or configuring implementing network traffic analysis with arkime capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Familiarity with network security concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

1. Install dependencies: `pip install requests`
2. Configure Arkime viewer URL and credentials.
3. Run the agent to query Arkime sessions and analyze traffic:
   - Search sessions by IP, port, protocol, or expression
   - Download PCAP data for forensic analysis
   - Detect C2 beaconing via connection interval analysis
   - Identify DNS tunneling through query length statistics
   - Flag connections to known-bad TLS certificate issuers

```bash
python scripts/agent.py --arkime-url https://arkime.local:8005 --user admin --password secret --output arkime_report.json
```

## Examples

### Beaconing Detection
```
Source: 10.1.2.50 -> 185.220.101.34:443
Sessions: 288 over 24 hours
Avg interval: 300s, Jitter: 4.2%
Verdict: HIGH confidence C2 beaconing (jitter < 5%)
```
