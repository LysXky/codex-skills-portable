---
name: "performing-threat-emulation-with-atomic-red-team"
description: "Executes Atomic Red Team tests for MITRE ATT&CK technique validation using the atomic-operator Python framework. Loads test definitions from YAML atomics, runs attack simulations, and validates detection coverage. Use when testing SIEM detection rules, validating EDR coverage, or conducting purple team exercises."
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Performing Threat Emulation with Atomic Red Team


## When to Use

- When conducting security assessments that involve performing threat emulation with atomic red team
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Familiarity with threat intelligence concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

Use atomic-operator to execute Atomic Red Team tests and validate detection coverage
against MITRE ATT&CK techniques.

```python
from atomic_operator import AtomicOperator

operator = AtomicOperator()
# Run a specific technique test
operator.run(
    technique="T1059.001",  # PowerShell execution
    atomics_path="./atomic-red-team/atomics",
)
```

Key workflow:
1. Clone the atomic-red-team repository for test definitions
2. Select ATT&CK techniques matching your detection rules
3. Execute atomic tests using atomic-operator
4. Check SIEM/EDR for corresponding alerts
5. Document detection gaps and update rules

## Examples

```python
# Parse atomic test YAML definitions
import yaml
with open("atomics/T1059.001/T1059.001.yaml") as f:
    tests = yaml.safe_load(f)
for test in tests.get("atomic_tests", []):
    print(f"Test: {test['name']}")
    print(f"  Platforms: {test.get('supported_platforms', [])}")
```
