---
name: secure
description: Maximum safety checks and human oversight
activation: Sensitive code, production changes, security-critical work
---

# Secure Mode

> **Context Framework Note**: Maximizes safety for sensitive operations.

## When to Use
- Production deployments
- Security-sensitive code
- Financial/payment systems
- User data handling
- Infrastructure changes
- Credential management

## Behavioral Changes

### Approval Required
- All terminal commands reviewed
- File changes confirmed
- Deployments verified
- Database operations approved

### Extra Validation
- Additional security scans
- Input validation checks
- Dependency audits
- Configuration reviews

### Explicit Confirmations
- No auto-execution
- Step-by-step approval
- Rollback points created
- Backup before changes

### Comprehensive Logging
- All actions logged
- Artifacts for everything
- Audit trail maintained
- Change history tracked

## Safety Checks

| Category | Checks |
|----------|--------|
| Secrets | No hardcoded credentials |
| Injection | Input validation |
| Auth | Access control review |
| Data | Encryption verified |
| Deps | Vulnerability scan |

## Example Flow

```
User: Deploy to production

Agent: [Secure Mode Active]

I'll deploy to production. This requires several checks:

1. ✅ Tests passing
2. ✅ Security scan clean
3. ✅ Build successful
4. ⏳ Awaiting your approval

Deployment plan:
- Target: production
- Changes: 12 files
- Migrations: 1

Type 'approve' to proceed or 'abort' to cancel.
```

## Activation
```
/sg:mode secure
```
Or automatic when:
- "production" detected
- "security" context
- Sensitive file patterns
- `--safe` flag used

## Deactivation
- Explicit `/sg:mode planning` or `/sg:mode fast`
- Never auto-deactivates for safety
