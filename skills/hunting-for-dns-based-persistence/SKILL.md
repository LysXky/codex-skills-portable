---
name: "hunting-for-dns-based-persistence"
description: "Hunt for DNS-based persistence mechanisms including DNS hijacking, dangling"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Hunting for DNS-based Persistence

## Overview

Attackers establish DNS-based persistence by hijacking DNS records, creating unauthorized subdomains, abusing wildcard DNS entries, or modifying NS delegations to redirect traffic through attacker-controlled infrastructure. These techniques survive credential rotations, endpoint reimaging, and traditional remediation because DNS changes persist independently of compromised hosts. Detection requires passive DNS historical analysis, zone file auditing, and monitoring for unauthorized record modifications. This skill covers hunting methodologies using SecurityTrails passive DNS API, DNS audit logs from Route53/Azure DNS/Cloudflare, and zone transfer analysis.


## When to Use

- When investigating security incidents that require hunting for dns based persistence
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- SecurityTrails API key (free tier provides 50 queries/month)
- Access to DNS provider audit logs (Route53, Azure DNS, Cloudflare, or on-premises DNS)
- Python 3.9+ with requests library
- DNS zone file access or AXFR capability for internal zones
- Historical DNS baseline for comparison

## Steps

### Step 1: Baseline DNS Records

Export current DNS zone records and establish baseline for all authorized A, AAAA, CNAME, MX, NS, and TXT records.

### Step 2: Query Passive DNS History

Use SecurityTrails API to retrieve historical DNS records and identify unauthorized changes, new subdomains, and CNAME records pointing to decommissioned services (dangling CNAMEs).

### Step 3: Detect Anomalies

Compare current records against baseline to identify unauthorized modifications, wildcard records that resolve all subdomains, NS delegation changes, and MX record hijacking.

### Step 4: Investigate Findings

Correlate DNS anomalies with threat intelligence feeds, check resolution targets against known malicious infrastructure, and validate record ownership.

## Expected Output

JSON report listing DNS anomalies with record type, historical changes, risk severity, and remediation recommendations for each finding.
