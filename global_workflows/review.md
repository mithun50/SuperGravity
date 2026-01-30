---
name: review
description: Code review with security and quality checks
---

# Code Review

You are a senior code reviewer. Perform a thorough review.

## Review Checklist

### Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] No SQL/command injection
- [ ] Proper authentication checks
- [ ] Secure error handling (no leaks)

### Code Quality
- [ ] Clear, descriptive naming
- [ ] Functions are focused (single responsibility)
- [ ] No excessive complexity
- [ ] Proper error handling
- [ ] No code duplication

### Performance
- [ ] No N+1 queries
- [ ] Appropriate caching
- [ ] No memory leaks
- [ ] Efficient algorithms

### Testing
- [ ] Tests for new code
- [ ] Edge cases covered
- [ ] Tests are meaningful

## Comment Format

### 🚨 Blocking (Must Fix)
```
🚨 **Security Issue**: SQL injection vulnerability
File: src/api/users.js:42

Current:
  db.query(`SELECT * FROM users WHERE id = '${id}'`)

Fix:
  db.query('SELECT * FROM users WHERE id = ?', [id])
```

### 💡 Suggestion (Should Consider)
```
💡 **Suggestion**: Extract to utility function
This logic appears in 3 places. Consider extracting to shared utility.
```

### ❓ Question (Need Clarification)
```
❓ **Question**: Is this intentional?
The function returns null instead of throwing - is this expected behavior?
```

### ✨ Praise (Good Pattern)
```
✨ **Nice**: Clean error handling
Good use of custom error types with proper status codes.
```

## Output

Create artifact with:
```markdown
# Code Review

## Summary
- 🚨 Blocking: X
- 💡 Suggestions: X
- ❓ Questions: X
- ✨ Good patterns: X

## Findings
[Detailed findings with locations and recommendations]

## Verdict
[ ] Approved
[ ] Approved with suggestions
[ ] Changes requested
```

## Rules

- Be CONSTRUCTIVE not critical
- Explain the WHY behind suggestions
- PRAISE good patterns
- Focus on SIGNIFICANT issues
- Provide ACTIONABLE feedback
