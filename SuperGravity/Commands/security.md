---
name: security
description: Security audit and vulnerability scanning
category: quality
agents: [security]
---

# /sg:security - Security Audit

> **Context Framework Note**: Performs security analysis and vulnerability detection.

## Triggers
- `/sg:security [--flags]`
- Security review requests
- Vulnerability scanning needs

## Syntax
```
/sg:security [path] [options]

Options:
  --thorough      Deep scan (slower)
  --fast          Quick scan
  --severity critical|high|medium
  --json          JSON output
  --artifact      Create report artifact
```

## Behavioral Flow

1. **Scan** - Check for OWASP Top 10
2. **Identify** - Find secrets, vulnerabilities
3. **Categorize** - Rate by severity
4. **Report** - Generate findings
5. **Remediate** - Provide fix examples

## OWASP Coverage

| ID | Category | Checks |
|----|----------|--------|
| A01 | Access Control | Auth, IDOR, path traversal |
| A02 | Crypto Failures | Weak hash, hardcoded keys |
| A03 | Injection | SQL, NoSQL, command, XSS |
| A05 | Misconfig | CORS, headers, debug mode |
| A07 | Auth Failures | Session, JWT, rate limits |

## Report Format

```
# Security Audit Report

## Summary
- CRITICAL: 2
- HIGH: 5
- MEDIUM: 8

## Findings

### [CRITICAL] SQL Injection
**File:** src/api/users.js:42
**Risk:** Data theft, auth bypass
**Code:**
  db.query(`SELECT * FROM users WHERE id = '${id}'`)
**Fix:**
  db.query('SELECT * FROM users WHERE id = ?', [id])
```

## Examples

### Full Audit
```
/sg:security --thorough --artifact
```

### Quick Check
```
/sg:security src/ --fast --severity critical
```

### CI Integration
```
/sg:security --json > security-report.json
```

## Outputs
- Security report
- Severity-rated findings
- Remediation examples
- Artifact (if requested)

## Boundaries
**Will:** Find real vulnerabilities, provide fixes
**Won't:** Provide exploitation techniques
