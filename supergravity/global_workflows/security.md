---
description: Perform security audit and vulnerability scanning on the codebase
---

1. Ask the user which files or directories to audit (or audit entire project).

2. Scan for Broken Access Control (OWASP A01):
   - Check for missing authorization checks
   - Look for IDOR vulnerabilities
   - Identify path traversal risks

3. Scan for Cryptographic Failures (OWASP A02):
   - Check for weak hashing (MD5, SHA1 for passwords)
   - Search for hardcoded secrets and API keys
   - Verify encryption is used for sensitive data

4. Scan for Injection vulnerabilities (OWASP A03):
   - SQL injection (string concatenation in queries)
   - NoSQL injection
   - Command injection
   - XSS (innerHTML, dangerouslySetInnerHTML)

5. Check for Security Misconfiguration (OWASP A05):
   - Debug mode enabled in production
   - Default credentials
   - Missing security headers
   - Unnecessary features enabled

6. Check for Authentication Failures (OWASP A07):
   - Weak password policies
   - Missing rate limiting
   - Insecure session management

7. Create a security audit report with findings categorized by severity:
   - CRITICAL: Immediate exploitation risk
   - HIGH: Significant security impact
   - MEDIUM: Potential security issue
   - LOW: Best practice violation

8. For each finding, provide:
   - File location and line number
   - OWASP category
   - Risk description
   - Vulnerable code snippet
   - Remediation code

9. Summarize total findings by severity level.

## Rules
- Check ALL OWASP Top 10 categories
- Provide SPECIFIC file locations
- Include WORKING remediation code
- NEVER provide exploitation techniques
