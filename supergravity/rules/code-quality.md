# Code Quality Rules

> Standards for maintainable, readable code.

## Functions
- Single responsibility
- Descriptive names (verb + noun)
- Max 20-30 lines preferred
- Limited parameters (max 3-4)

## Naming
```typescript
// Functions: verb + noun
function getUserById(id: string) { }
function calculateTotalPrice(items: Item[]) { }

// Variables: descriptive
const activeUsers = users.filter(u => u.isActive);
const currentTimestamp = Date.now();

// Constants: SCREAMING_SNAKE_CASE
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = '/api/v1';

// Booleans: is/has/should prefix
const isLoading = true;
const hasPermission = checkPermission(user);
```

## Error Handling
```typescript
// Always handle errors
try {
  const result = await riskyOperation();
  return result;
} catch (error) {
  logger.error('Operation failed', { error, context });
  throw new CustomError('Operation failed', { cause: error });
}

// Never swallow errors
// BAD: catch (e) { }
```

## Comments
- Explain "why", not "what"
- Keep comments updated
- Use JSDoc/docstrings for public APIs
- Remove commented-out code

## Complexity
- Avoid deep nesting (max 3 levels)
- Early returns over else chains
- Extract complex conditions to variables

```typescript
// Bad
if (user && user.profile && user.profile.settings && user.profile.settings.notifications) {
  // ...
}

// Good
const hasNotificationsEnabled = user?.profile?.settings?.notifications;
if (hasNotificationsEnabled) {
  // ...
}
```

## Testing
- Write tests for new code
- Test edge cases
- Keep tests focused
- Use descriptive test names
