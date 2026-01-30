---
name: sequential
description: Complex multi-step reasoning and analysis
priority: high
---

# Sequential Thinking MCP

> **Framework Note**: Enables structured, step-by-step problem solving.

## Purpose
Break down complex problems into manageable steps with revision capability.

## When Used
- Complex architecture decisions
- Multi-step implementations
- Problem analysis
- Planning with unknowns

## Configuration
```json
{
  "mcpServers": {
    "sequential": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-sequential-thinking"]
    }
  }
}
```

## Tools

### sequentialthinking
Step-by-step reasoning with branches.
```
Input: {
  "thought": "First, analyze the current auth system...",
  "thoughtNumber": 1,
  "totalThoughts": 5,
  "nextThoughtNeeded": true
}
```

## Features
- **Branching**: Explore alternative approaches
- **Revision**: Go back and revise earlier thinking
- **Flexibility**: Adjust total thoughts as needed
- **Verification**: Validate conclusions

## Use Cases

### Architecture Planning
1. Analyze requirements
2. Identify constraints
3. Propose options
4. Evaluate trade-offs
5. Recommend approach

### Debugging
1. Understand the error
2. Trace the cause
3. Identify root cause
4. Propose fix
5. Verify solution

## Integration with Commands
- `/sg:implement` - Complex features
- `/sg:debug` - Root cause analysis
- Planning mode - Architecture decisions

## Best Practices
- Start with clear problem statement
- Allow for revision and backtracking
- Document key decision points
- Verify conclusions before acting
