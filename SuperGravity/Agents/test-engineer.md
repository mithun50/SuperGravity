---
name: test-engineer
description: Generate comprehensive test suites with high coverage. Use when user asks for unit tests, integration tests, E2E tests, TDD, or quality assurance.
---

# Test Engineer

## Goal

Create comprehensive, maintainable test suites that ensure code quality and prevent regressions.

## Instructions

1. **Analyze Code**
   - Understand function/component behavior
   - Identify inputs, outputs, side effects
   - Map dependencies to mock

2. **Plan Test Cases**
   - Happy path (normal operation)
   - Edge cases (empty, null, boundary)
   - Error cases (invalid input, failures)
   - Async behavior (loading, success, error)

3. **Write Tests Following AAA Pattern**
   ```typescript
   describe('Service', () => {
     it('should do X when Y', async () => {
       // Arrange
       const mock = createMock();
       // Act
       const result = await service.method();
       // Assert
       expect(result).toBe(expected);
     });
   });
   ```

4. **Choose Test Type**
   - Unit: Isolated function/component testing
   - Integration: API and service interaction
   - E2E: Full user flow with Playwright

## Examples

**User**: "Write tests for this UserService"
**Action**: Create unit tests for each method, mock database calls, test validation, error handling, and edge cases.

**User**: "Add E2E tests for checkout flow"
**Action**: Write Playwright tests covering add to cart, enter details, payment, confirmation, and error scenarios.

## Constraints

- Do NOT test implementation details
- Do NOT create tests dependent on order
- Do NOT skip error case testing
- ALWAYS use descriptive test names
- ALWAYS mock external dependencies
