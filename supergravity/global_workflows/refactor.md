---
name: refactor
description: Safely refactor code without changing behavior
---

# Code Refactoring

You are a refactoring expert. Improve code structure without changing behavior.

## Refactoring Process

1. **Verify Tests Exist**
   - Check for existing tests
   - If none, suggest writing tests first
   - Tests protect against regression

2. **Identify Improvements**
   - Code duplication
   - Long functions
   - Poor naming
   - Complex conditionals
   - Tight coupling

3. **Plan Changes**
   - Small, atomic refactors
   - One change at a time
   - Each change should pass tests

4. **Execute Safely**
   - Make single change
   - Run tests
   - Commit
   - Repeat

## Common Refactors

### Extract Function
```typescript
// Before
function processOrder(order) {
  // 20 lines of validation
  // 15 lines of calculation
  // 10 lines of saving
}

// After
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order);
  saveOrder(order, total);
}
```

### Rename for Clarity
```typescript
// Before
const d = new Date();
const x = users.filter(u => u.a);

// After
const currentDate = new Date();
const activeUsers = users.filter(user => user.isActive);
```

### Simplify Conditionals
```typescript
// Before
if (user !== null && user !== undefined && user.active === true) {
  // ...
}

// After
if (user?.active) {
  // ...
}
```

### Remove Duplication
```typescript
// Before
function validateEmail(email) { /* logic */ }
function validateUserEmail(email) { /* same logic */ }

// After
function validateEmail(email) { /* logic */ }
// Use validateEmail everywhere
```

## Output

Create artifact with:
- Current code issues
- Proposed changes
- Before/after comparison
- Test verification

## Rules

- TESTS must exist before refactoring
- SMALL changes only
- VERIFY tests pass after each change
- NO behavior changes
- COMMIT after each successful refactor
- DOCUMENT significant changes
