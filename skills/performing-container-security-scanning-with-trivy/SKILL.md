---
name: "performing-container-security-scanning-with-trivy"
description: "Scan container images, filesystems, and Kubernetes manifests for vulnerabilities,"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Performing Container Security Scanning with Trivy

## Overview

Trivy is an open-source security scanner by Aqua Security that detects vulnerabilities in OS packages and language-specific dependencies, infrastructure-as-code misconfigurations, exposed secrets, and software license issues across container images, filesystems, Git repositories, and Kubernetes clusters. Trivy generates Software Bill of Materials (SBOM) in CycloneDX and SPDX formats for supply chain transparency. This skill covers comprehensive container image scanning, CI/CD pipeline integration, Kubernetes operator deployment, and scan result triage for security operations.


## When to Use

- When conducting security assessments that involve performing container security scanning with trivy
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Trivy v0.50+ installed (binary, Docker, or Homebrew)
- Docker daemon access for local image scanning
- Container registry credentials for remote image scanning
- CI/CD platform (GitHub Actions, GitLab CI, Jenkins) for pipeline integration
- Kubernetes cluster for Trivy Operator deployment (optional)

## Steps

### Step 1: Scan Container Images

Run vulnerability and secret scanning against container images from local builds or remote registries. Configure severity thresholds and ignore unfixed vulnerabilities.

### Step 2: Generate SBOM

Produce CycloneDX or SPDX SBOM documents from scanned images for supply chain compliance and vulnerability tracking across the software lifecycle.

### Step 3: Scan IaC and Kubernetes Manifests

Detect misconfigurations in Dockerfiles, Kubernetes YAML, Terraform, and Helm charts using built-in policy checks aligned with CIS benchmarks.

### Step 4: Integrate into CI/CD

Add Trivy scanning as a pipeline gate that blocks builds with critical/high vulnerabilities, generates SARIF reports for GitHub Advanced Security, and produces JUnit XML for test dashboards.

## Expected Output

JSON/table report listing CVEs with severity, CVSS scores, fixed versions, affected packages, misconfiguration findings, and exposed secrets with file locations.
