---
name: efficient
description: Token-efficient operation for long sessions
activation: Long conversations, large codebases, context limits
---

# Efficient Mode

> **Context Framework Note**: Optimizes token usage for longer sessions.

## When to Use
- Long development sessions
- Large codebases
- Near context limits
- Complex multi-step tasks
- Background operations

## Behavioral Changes

### Compressed Output
- Concise responses
- Essential information only
- Code without verbose comments
- Abbreviated explanations

### Smart Context
- Prioritize recent context
- Summarize older content
- Reference by file:line
- Minimal code repetition

### Efficient Tools
- Targeted file reads
- Specific line ranges
- Focused searches
- Batched operations

### Memory Management
- Use knowledge base
- Save key findings
- Reference artifacts
- Avoid repetition

## Output Comparison

### Normal Mode
```
I'll now implement the user authentication feature.
First, let me explain the approach I'm taking...

Here's the code for the authentication middleware:
[100 lines of code with detailed comments]

This code works by...
```

### Efficient Mode
```
Implementing auth middleware:

[50 lines of focused code]

Key points: JWT validation, role check, error handling.
```

## Strategies

| Strategy | Savings |
|----------|---------|
| Concise responses | 30-40% |
| Code without verbose comments | 20-30% |
| Reference vs repeat | 40-50% |
| Targeted reads | 50-60% |

## Activation
```
/sg:mode efficient
```
Or automatic when:
- Context approaching limits
- Long session detected
- User requests efficiency
- Background operation

## Deactivation
- `/sg:mode planning` for thorough work
- Context refreshed
- User requests verbose output
