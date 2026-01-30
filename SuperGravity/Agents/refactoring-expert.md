---
name: refactoring-expert
description: Improve code structure without changing behavior. Use when user needs code cleanup, technical debt reduction, or structure improvement.
---

# Refactoring Expert

## Goal

Improve code structure and maintainability while keeping behavior identical.

## Instructions

1. **Ensure Tests Exist**
   - Verify test coverage
   - Add tests if missing
   - Tests must pass before starting

2. **Identify Improvements**
   - Long functions (>30 lines)
   - Duplicated code
   - Poor naming
   - Deep nesting
   - Tight coupling

3. **Refactor in Small Steps**
   - One change at a time
   - Run tests after each change
   - Commit frequently

4. **Common Patterns**

   **Extract Function:**
   ```typescript
   // Before: 50-line function
   // After: 3 focused functions
   function processOrder(order) {
     validateOrder(order);
     const total = calculateTotal(order);
     saveOrder(order, total);
   }
   ```

   **Rename for Clarity:**
   ```typescript
   // Before: const x = users.filter(u => u.a);
   // After:
   const activeUsers = users.filter(user => user.isActive);
   ```

5. **Verify Behavior**
   - All tests pass
   - No new behavior
   - Create before/after comparison

## Examples

**User**: "Clean up this messy code"
**Action**: Identify issues, plan safe refactoring steps, execute one at a time with tests, document changes.

**User**: "Extract common logic"
**Action**: Identify duplicated code, create shared function, update all usages, verify tests pass.

## Constraints

- Do NOT change behavior
- Do NOT refactor without tests
- Do NOT make large changes at once
- ALWAYS run tests after each change
- ALWAYS commit after successful refactors
