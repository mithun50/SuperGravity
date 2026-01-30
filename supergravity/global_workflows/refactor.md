---
description: Safely refactor code to improve structure without changing behavior
---

1. Ask the user which code to refactor and what improvements they want.

2. Read the target code thoroughly to understand current implementation.

3. Check if tests exist for the code to be refactored.

4. If no tests exist, suggest writing tests first to protect against regression.

// turbo
5. Run `npm test` or `pytest` to verify current tests pass.

6. Identify improvement opportunities:
   - Code duplication
   - Long functions (>30 lines)
   - Poor naming
   - Complex conditionals
   - Tight coupling
   - Deep nesting

7. Plan changes as small, atomic refactors (one change at a time).

8. Execute first refactor:
   - Extract function, rename, simplify, or remove duplication

// turbo
9. Run `npm test` or `pytest` to verify tests still pass.

10. If tests pass, continue with next refactor. Repeat steps 8-9.

11. Create before/after comparison showing improvements.

12. Suggest any new tests needed for refactored code.

## Common Refactors

### Extract Function
Break large functions into smaller, focused ones.

### Rename for Clarity
Replace abbreviated or unclear names with descriptive ones.

### Simplify Conditionals
Use optional chaining, early returns, and guard clauses.

### Remove Duplication
Extract shared logic into reusable functions.

## Rules
- TESTS must exist before refactoring
- SMALL changes only
- VERIFY tests pass after each change
- NO behavior changes
- COMMIT after each successful refactor
