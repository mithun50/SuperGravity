---
name: playwright
description: Browser automation and E2E testing
priority: medium
---

# Playwright MCP

> **Framework Note**: Enables browser automation for testing and verification.

## Purpose
Automate browser interactions for E2E testing and visual verification.

## When Used
- E2E test generation
- Visual verification
- Form testing
- User flow automation

## Configuration
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-playwright"]
    }
  }
}
```

## Tools

### browser_navigate
Navigate to URL.
```
Input: { "url": "http://localhost:3000" }
```

### browser_click
Click element.
```
Input: { "selector": "[data-testid='submit']" }
```

### browser_fill
Fill input field.
```
Input: {
  "selector": "#email",
  "value": "test@example.com"
}
```

### browser_screenshot
Capture screenshot.
```
Input: { "fullPage": true }
```

## E2E Test Generation

```typescript
test('user can login', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', 'user@test.com');
  await page.fill('#password', 'password');
  await page.click('[data-testid="login-btn"]');
  await expect(page.locator('.dashboard')).toBeVisible();
});
```

## Integration with Commands
- `/sg:test --type e2e` - E2E generation
- `/sg:implement` - Visual verification
- @tester agent - Test automation

## Best Practices
- Use data-testid for selectors
- Wait for elements properly
- Capture screenshots on failure
- Test critical user paths
