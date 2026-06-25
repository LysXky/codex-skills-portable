---
name: "implementing-zero-trust-with-beyondcorp"
description: "Deploy Google BeyondCorp Enterprise zero trust access controls using"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Implementing Zero Trust with BeyondCorp

## Overview

Google BeyondCorp Enterprise implements the zero trust security model by eliminating the concept of a trusted network perimeter. Instead of relying on VPNs and network location, BeyondCorp authenticates and authorizes every request based on user identity, device posture, and contextual attributes. Identity-Aware Proxy (IAP) serves as the enforcement point, intercepting all requests to protected resources and evaluating them against Access Context Manager policies. This skill covers configuring IAP for web applications, defining access levels based on device trust and network attributes, and auditing access policies for compliance.


## When to Use

- When deploying or configuring implementing zero trust with beyondcorp capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Google Cloud project with BeyondCorp Enterprise license
- IAP API enabled (iap.googleapis.com)
- Access Context Manager API enabled (accesscontextmanager.googleapis.com)
- GCP resources to protect (Compute Engine, App Engine, or GKE services)
- Endpoint Verification deployed on managed devices
- Python 3.9+ with google-cloud-iap library

## Steps

### Step 1: Enable IAP on Target Resources
Configure Identity-Aware Proxy on Compute Engine, App Engine, or HTTPS load balancer backends.

### Step 2: Define Access Levels
Create Access Context Manager access levels based on IP ranges, device attributes (OS version, encryption, screen lock), and geographic location.

### Step 3: Bind Access Policies
Apply access levels as IAP conditions to enforce context-aware access decisions on protected resources.

### Step 4: Audit and Monitor
Query IAP audit logs, verify policy enforcement, and identify gaps in zero trust coverage.

## Expected Output

JSON report containing IAP-protected resources, access level definitions, policy binding audit results, and zero trust coverage metrics.
