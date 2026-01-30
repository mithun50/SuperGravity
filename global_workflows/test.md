---
description: Generate comprehensive test suites for code coverage
---

1. Ask the user which files or functions to generate tests for.

2. Read the target code to understand its functionality.

3. Identify the appropriate testing framework (Jest, Vitest, Pytest, etc.).

4. Generate unit tests for each function:
   - Happy path (normal operation)
   - Edge cases (empty, null, boundary values)
   - Error cases (invalid input, failures)

5. For React components, generate:
   - Render tests
   - User interaction tests
   - State change tests
   - Loading and error state tests

6. For API endpoints, generate integration tests:
   - Valid request tests
   - Invalid input tests (400 responses)
   - Authentication tests (401/403)
   - Not found tests (404)

7. For critical user flows, suggest E2E tests with Playwright:
   - Complete user journey tests
   - Form submission tests
   - Navigation tests

8. Create test files with:
   - Descriptive test names
   - Proper setup/teardown
   - Mocked external dependencies
   - AAA pattern (Arrange, Act, Assert)

// turbo
9. Run `npm test` or `pytest` to verify tests pass.

10. Report test coverage and suggest additional test cases if needed.

## Test Patterns

```typescript
describe('functionName', () => {
  it('should do X when given Y', () => {
    // Arrange
    const input = ...;
    // Act
    const result = functionName(input);
    // Assert
    expect(result).toBe(expected);
  });
});
```

## Rules
- Test BEHAVIOR not implementation
- ONE assertion per concept
- DESCRIPTIVE test names
- INDEPENDENT tests (no test order dependencies)
- MOCK external dependencies
