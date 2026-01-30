---
name: context7
description: Up-to-date framework documentation
priority: high
---

# Context7 MCP

> **Framework Note**: Provides live documentation for frameworks and libraries.

## Purpose
Fetch current, accurate documentation for any framework or library during development.

## When Used
- Framework-specific implementation
- API lookups
- Best practice verification
- Pattern reference

## Configuration
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp"]
    }
  }
}
```

## Tools

### resolve-library-id
Find Context7-compatible library ID.
```
Input: { "libraryName": "react" }
Output: { "id": "/facebook/react" }
```

### get-library-docs
Fetch documentation for topic.
```
Input: {
  "context7CompatibleLibraryID": "/facebook/react",
  "topic": "hooks"
}
Output: Documentation content
```

## Supported Libraries
- React, Next.js, Vue, Svelte
- Express, FastAPI, Django
- Prisma, Drizzle, SQLAlchemy
- Tailwind, Bootstrap
- TypeScript, Python
- And many more...

## Integration with Commands
- `/sg:implement` - Framework patterns
- `/sg:scaffold` - Project templates
- `/sg:document` - API references

## Best Practices
- Always resolve library ID first
- Use specific topics for focused results
- Cache frequently used docs
- Combine with Sequential for analysis
