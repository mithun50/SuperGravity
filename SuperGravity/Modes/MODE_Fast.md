---
name: fast
description: Quick execution with minimal ceremony
activation: Simple fixes, quick changes, time-sensitive work
---

# Fast Mode

> **Context Framework Note**: Optimizes for speed with minimal overhead.

## When to Use
- Simple bug fixes
- Quick changes
- Typo corrections
- Small additions
- Time-sensitive work

## Behavioral Changes

### Direct Execution
- Skip lengthy planning
- Execute immediately
- Minimal artifacts
- Quick iterations

### Reduced Ceremony
- No implementation plans for small changes
- Skip optional validations
- Minimal documentation
- Focused output

### Still Safe
- Core safety checks remain
- Security validations active
- Type checking enabled
- Tests still run

## What's Different

| Normal | Fast Mode |
|--------|-----------|
| Full plan | Quick assessment |
| Detailed artifacts | Minimal artifacts |
| Multiple checkpoints | Single checkpoint |
| Verbose output | Concise output |

## What Stays Same
- Security checks
- Error handling
- Type safety
- Code quality

## Examples

### Quick Fix
```
/sg:mode fast
/sg:implement fix typo in header
```

### Small Addition
```
/sg:implement add loading state --fast
```

## Activation
```
/sg:mode fast
```
Or use `--fast` flag:
```
/sg:implement feature --fast
```

## Deactivation
- `/sg:mode planning` for thorough mode
- After completing quick task
- When scope grows
