---
description: Perform code review with security, quality, and performance checks
---

1. Ask the user which files or changes to review.

2. Read the code to be reviewed thoroughly.

3. Check for security issues:
   - No hardcoded secrets
   - Input validation present
   - No SQL/command injection
   - Proper authentication checks
   - Secure error handling (no information leaks)

4. Check code quality:
   - Clear, descriptive naming
   - Functions are focused (single responsibility)
   - No excessive complexity
   - Proper error handling
   - No code duplication

5. Check performance:
   - No N+1 queries
   - Appropriate caching
   - No memory leaks
   - Efficient algorithms

6. Check for test coverage:
   - Tests for new code
   - Edge cases covered
   - Tests are meaningful

7. For each issue found, categorize as:
   - 🚨 Blocking (Must Fix) - Security issues, bugs
   - 💡 Suggestion (Should Consider) - Improvements
   - ❓ Question (Need Clarification) - Unclear intent
   - ✨ Praise (Good Pattern) - Highlight good code

8. Create review summary with:
   - Count of blocking issues
   - Count of suggestions
   - Count of questions
   - Highlighted good patterns

9. Provide verdict:
   - Approved
   - Approved with suggestions
   - Changes requested

10. For each blocking issue, provide specific fix with code.

## Rules
- Be CONSTRUCTIVE not critical
- Explain the WHY behind suggestions
- PRAISE good patterns
- Focus on SIGNIFICANT issues
- Provide ACTIONABLE feedback
