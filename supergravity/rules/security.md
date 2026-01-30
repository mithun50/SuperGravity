# Security Rules

> Security guidelines for all code operations.

## Input Validation
- Validate all user inputs
- Sanitize data before use
- Use allowlists over denylists
- Check types and bounds

## Authentication
- Use secure session management
- Implement proper password hashing (bcrypt)
- Add rate limiting to auth endpoints
- Use HTTPS only

## Data Protection
- Encrypt sensitive data at rest
- Use TLS for data in transit
- Never log sensitive information
- Implement proper access controls

## Secrets Management
- Use environment variables
- Never commit secrets to git
- Rotate credentials regularly
- Use secret managers in production

## SQL/Injection Prevention
```
# Bad
query = f"SELECT * FROM users WHERE id = '{user_id}'"

# Good
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, [user_id])
```

## XSS Prevention
```
# Bad
element.innerHTML = userInput

# Good
element.textContent = userInput
# Or sanitize with DOMPurify
```

## OWASP Top 10 Awareness
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Data Integrity Failures
9. Logging Failures
10. SSRF
