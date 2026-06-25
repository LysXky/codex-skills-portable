---
name: "implementing-syslog-centralization-with-rsyslog"
description: "Configure rsyslog for centralized log collection with TLS encryption,"
---

## Codex adaptation and authorization boundary

Adapted from mukul975/Anthropic-Cybersecurity-Skills for Codex.

- Use this skill only for defensive work, education, controlled labs, CTFs, or systems covered by explicit authorization.
- Establish the target scope and authorization before taking intrusive, exploitative, credential-access, persistence, or destructive actions.
- Treat bundled scripts as untrusted utilities: inspect their source, dependencies, inputs, and side effects before execution.
- Prefer analysis, detection, validation, and safe simulation when live execution is not explicitly required.
- Translate Claude-specific tool names into available Codex tools. Translate Bash examples to PowerShell on Windows when appropriate.
- Verify current tool syntax and vendor documentation before relying on commands that may have changed.

# Implementing Syslog Centralization with Rsyslog


## When to Use

- When deploying or configuring implementing syslog centralization with rsyslog capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Familiarity with security operations concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

1. Install dependencies: `pip install jinja2 paramiko`
2. Generate TLS certificates for rsyslog server and clients using OpenSSL.
3. Run the agent to generate rsyslog server and client configurations:
   - Server: TLS listener on port 6514, per-host directory output, JSON-format templates
   - Client: TLS forwarding with disk-assisted queues for reliability
4. Deploy configurations to servers via SSH (paramiko).
5. Validate TLS connectivity and log delivery.

```bash
python scripts/agent.py --server-ip 10.0.0.1 --clients 10.0.0.10,10.0.0.11 --ca-cert ca.pem --output syslog_report.json
```

## Examples

### Server Configuration (TLS)
```
module(load="imtcp" StreamDriver.Name="gtls" StreamDriver.Mode="1"
       StreamDriver.Authmode="x509/name")
input(type="imtcp" port="6514")
template(name="PerHostLog" type="string" string="/var/log/remote/%HOSTNAME%/%PROGRAMNAME%.log")
*.* ?PerHostLog
```

### Client Configuration (Reliable Forwarding)
```
action(type="omfwd" target="10.0.0.1" port="6514" protocol="tcp"
       StreamDriver="gtls" StreamDriverMode="1"
       StreamDriverAuthMode="x509/name"
       queue.type="LinkedList" queue.filename="fwdRule1"
       queue.maxdiskspace="1g" queue.saveonshutdown="on"
       action.resumeRetryCount="-1")
```
