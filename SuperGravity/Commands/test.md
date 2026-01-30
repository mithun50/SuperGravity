---
name: test
description: Generate and run test suites
category: quality
mcp-servers: [playwright]
agents: [tester]
---

# /sg:test - Test Generation

> **Context Framework Note**: Creates comprehensive test suites.

## Triggers
- `/sg:test [target] [--flags]`
- Test creation requests
- Coverage improvement needs

## Syntax
```
/sg:test [target] [options]

Targets:
  [file]        Test specific file
  [function]    Test specific function
  [component]   Test component
  all           Test everything

Options:
  --type unit|integration|e2e
  --coverage    Generate coverage report
  --watch       Watch mode
  --update      Update snapshots
```

## Behavioral Flow

1. **Analyze** - Understand code to test
2. **Plan** - Determine test strategy
3. **Generate** - Create test cases
4. **Verify** - Run tests
5. **Report** - Coverage if requested

## Test Types

### Unit Tests
```typescript
describe('calculateTotal', () => {
  it('should sum items correctly', () => {
    const items = [{ price: 10 }, { price: 20 }];
    expect(calculateTotal(items)).toBe(30);
  });

  it('should return 0 for empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });
});
```

### Integration Tests
```typescript
describe('POST /api/orders', () => {
  it('should create order', async () => {
    const res = await request(app)
      .post('/api/orders')
      .send({ items: [{ id: 1, qty: 2 }] })
      .expect(201);

    expect(res.body.total).toBeDefined();
  });
});
```

### E2E Tests (Playwright)
```typescript
test('checkout flow', async ({ page }) => {
  await page.goto('/products');
  await page.click('[data-testid="add-to-cart"]');
  await page.click('[data-testid="checkout"]');
  await expect(page.locator('.success')).toBeVisible();
});
```

## Examples

### Generate Unit Tests
```
/sg:test src/services/UserService.ts --type unit
```

### Generate E2E Tests
```
/sg:test checkout-flow --type e2e
```

### Run with Coverage
```
/sg:test all --coverage
```

## Outputs
- Test files
- Coverage report (if --coverage)
- Test utilities if needed

## Boundaries
**Will:** Generate meaningful, maintainable tests
**Won't:** Write tests just for coverage numbers
