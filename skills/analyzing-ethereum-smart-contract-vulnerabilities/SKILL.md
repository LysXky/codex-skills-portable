---
name: "analyzing-ethereum-smart-contract-vulnerabilities"
description: "Perform static and symbolic analysis of Solidity smart contracts using"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Analyzing Ethereum Smart Contract Vulnerabilities

## Overview

Smart contract vulnerabilities have led to billions of dollars in losses across DeFi protocols. Unlike traditional software, deployed smart contracts are immutable and handle real financial assets, making pre-deployment security analysis critical. Slither performs fast static analysis using an intermediate representation to detect over 90 vulnerability patterns in seconds, while Mythril uses symbolic execution and SMT solving to discover complex execution path vulnerabilities like reentrancy and integer overflows. This skill covers running both tools against Solidity contracts, interpreting results, triaging findings by severity, and generating audit reports.


## When to Use

- When investigating security incidents that require analyzing ethereum smart contract vulnerabilities
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Python 3.10+ with pip
- Slither (pip install slither-analyzer) and solc compiler
- Mythril (pip install mythril) with solc-select for compiler version management
- Solidity source code or compiled contract bytecode
- Foundry or Hardhat development framework (optional, for project-level analysis)

## Steps

### Step 1: Run Slither Static Analysis

Execute Slither against the contract codebase to identify vulnerability patterns, optimization opportunities, and code quality issues using its 90+ built-in detectors.

### Step 2: Run Mythril Symbolic Execution

Run Mythril deep analysis to explore execution paths and discover reentrancy, unchecked external calls, and arithmetic vulnerabilities that require path-sensitive analysis.

### Step 3: Triage and Correlate Findings

Combine results from both tools, deduplicate findings, assess severity based on exploitability and financial impact, and filter false positives.

### Step 4: Generate Audit Report

Produce a structured audit report with vulnerability descriptions, affected code locations, exploit scenarios, and remediation recommendations.

## Expected Output

JSON report listing vulnerabilities with SWC (Smart Contract Weakness Classification) identifiers, severity ratings, affected functions, and suggested fixes.
