---
name: debug
description: Debug issues systematically
---

# Debugging

You are debugging an issue. Follow a systematic approach.

## Debug Process

1. **Understand the Problem**
   - What is the expected behavior?
   - What is the actual behavior?
   - When did it start happening?
   - Can it be reproduced?

2. **Gather Information**
   - Error messages and stack traces
   - Relevant logs
   - Recent changes
   - Environment details

3. **Form Hypothesis**
   - Based on symptoms, what could cause this?
   - List possible causes in order of likelihood

4. **Test Hypothesis**
   - Add logging/debugging
   - Check specific code paths
   - Verify assumptions

5. **Fix and Verify**
   - Implement fix
   - Write test to prevent regression
   - Verify fix works
   - Check for side effects

## Common Debug Patterns

### Undefined/Null Errors
```typescript
// Check the chain
console.log('user:', user);
console.log('user.profile:', user?.profile);
console.log('user.profile.name:', user?.profile?.name);

// Fix with optional chaining
const name = user?.profile?.name ?? 'Unknown';
```

### Async/Promise Issues
```typescript
// Check if awaiting properly
async function getData() {
  const result = await fetchData(); // Missing await?
  console.log('result:', result);
  return result;
}

// Check for unhandled rejections
try {
  await riskyOperation();
} catch (error) {
  console.error('Failed:', error);
}
```

### API Errors
```typescript
// Log full request/response
const response = await fetch(url, options);
console.log('Status:', response.status);
console.log('Headers:', Object.fromEntries(response.headers));
const data = await response.json();
console.log('Body:', data);
```

### Database Issues
```sql
-- Check query results
SELECT * FROM users WHERE id = '...' LIMIT 1;

-- Check for missing data
SELECT COUNT(*) FROM related_table WHERE user_id = '...';

-- Check indexes
EXPLAIN ANALYZE SELECT ...;
```

## Output

Create artifact with:
- Problem description
- Root cause analysis
- Fix implementation
- Prevention (test to add)

## Rules

- REPRODUCE before fixing
- UNDERSTAND before changing
- ONE fix at a time
- ADD TEST for the bug
- VERIFY fix doesn't break other things
