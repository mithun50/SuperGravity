---
name: review
description: Code review with best practice checks
category: quality
agents: [reviewer, security]
---

# /sg:review - Code Review

> **Context Framework Note**: Performs comprehensive code review.

## Triggers
- `/sg:review [path] [--flags]`
- Code review requests
- PR review needs

## Syntax
```
/sg:review [path] [options]

Paths:
  [file]       Review specific file
  [dir]        Review directory
  --staged     Review staged changes
  --pr [num]   Review pull request

Options:
  --thorough   Deep review
  --security   Focus on security
  --artifact   Create review artifact
```

## Behavioral Flow

1. **Scan** - Read code changes
2. **Analyze** - Check patterns and issues
3. **Security** - Check for vulnerabilities
4. **Comment** - Generate feedback
5. **Summarize** - Overall assessment

## Review Categories

### 🚨 Blocking
Must fix before merge:
- Security vulnerabilities
- Critical bugs
- Missing error handling

### 💡 Suggestions
Should consider:
- Better patterns
- Performance improvements
- Readability

### ❓ Questions
Need clarification:
- Unclear intent
- Missing context
- Design decisions

### ✨ Praise
Good patterns:
- Clean code
- Good tests
- Smart solutions

## Example Review

```markdown
## Code Review: src/api/users.js

### Summary
- 🚨 1 blocking issue
- 💡 3 suggestions
- ✨ 2 good patterns

### 🚨 Blocking: SQL Injection (Line 42)
User input directly in query.
**Fix:** Use parameterized query

### 💡 Suggestion: Extract validation (Line 15-30)
Consider extracting to `validateUser()` function.

### ✨ Nice: Error handling (Line 55)
Clean try-catch with proper logging!
```

## Examples

### Review File
```
/sg:review src/services/UserService.ts
```

### Review PR
```
/sg:review --pr 123 --thorough
```

### Security Focus
```
/sg:review src/ --security
```

## Outputs
- Review comments
- Severity ratings
- Fix suggestions
- Review artifact

## Boundaries
**Will:** Provide constructive, actionable feedback
**Won't:** Nitpick style, block without reason
