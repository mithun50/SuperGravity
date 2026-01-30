---
description: Debug issues systematically with root cause analysis
---

1. Ask the user to describe the problem:
   - What is the expected behavior?
   - What is the actual behavior?
   - When did it start happening?
   - Can it be reproduced consistently?

2. Gather information:
   - Error messages and stack traces
   - Relevant log output
   - Recent code changes
   - Environment details (OS, Node version, etc.)

3. Read the relevant code files where the error occurs.

4. Form hypothesis based on symptoms:
   - List possible causes in order of likelihood
   - Identify what could trigger this behavior

5. Add strategic logging to verify hypothesis:
   - Log variable values at key points
   - Log function entry/exit
   - Log API request/response

6. Test the hypothesis:
   - Reproduce the issue with logging
   - Check specific code paths
   - Verify assumptions about data

7. Identify the root cause based on evidence.

8. Implement the fix for the root cause.

9. Write a test that would have caught this bug.

// turbo
10. Run `npm test` or `pytest` to verify fix works and no regressions.

11. Verify fix in the actual environment where bug occurred.

12. Check for similar issues in related code.

13. Document the bug and fix for future reference.

## Common Debug Patterns

### Undefined/Null Errors
Check the object chain with optional chaining.

### Async/Promise Issues
Verify await keywords and catch blocks.

### API Errors
Log full request/response including status and headers.

### Database Issues
Check query results and verify data exists.

## Rules
- REPRODUCE before fixing
- UNDERSTAND before changing
- ONE fix at a time
- ADD TEST for the bug
- VERIFY fix doesn't break other things
