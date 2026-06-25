---
name: "detecting-aws-cloudtrail-anomalies"
description: "Detect unusual API call patterns in AWS CloudTrail logs using boto3,"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Detecting AWS CloudTrail Anomalies

## Overview

AWS CloudTrail records API calls across AWS services. This skill covers querying CloudTrail events with boto3's `lookup_events` API, building statistical baselines of normal API activity, detecting anomalies such as unusual event sources, geographic anomalies, high-frequency API calls, and first-time API usage patterns that indicate compromised credentials or insider threats.


## When to Use

- When investigating security incidents that require detecting aws cloudtrail anomalies
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Python 3.9+ with `boto3` library
- AWS credentials with CloudTrail read permissions (cloudtrail:LookupEvents)
- Understanding of AWS IAM and common API patterns
- CloudTrail enabled in target AWS account (management events at minimum)

## Steps

### Step 1: Query CloudTrail Events
Use boto3 CloudTrail client's lookup_events to retrieve recent API activity with pagination.

### Step 2: Build Activity Baseline
Aggregate events by user, source IP, event source, and event name to establish normal behavior patterns.

### Step 3: Detect Anomalies
Flag unusual patterns: new event sources per user, first-time API calls, geographic IP changes, high error rates, and sensitive API usage (IAM, KMS, S3 policy changes).

### Step 4: Generate Detection Report
Produce a JSON report with anomaly scores, top suspicious users, and recommended investigation actions.

## Expected Output

JSON report with event statistics, baseline deviations, anomalous users/IPs, sensitive API calls, and error rate analysis.
