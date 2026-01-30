---
name: magic
description: UI component generation from 21st.dev
priority: high
---

# Magic MCP (21st.dev)

> **Framework Note**: Generates production-ready UI components.

## Purpose
Create beautiful, accessible UI components with modern design patterns.

## When Used
- UI component creation
- Design system implementation
- Component inspiration
- Rapid prototyping

## Configuration
```json
{
  "mcpServers": {
    "magic": {
      "command": "npx",
      "args": ["-y", "@21st/magic-mcp"]
    }
  }
}
```

## Tools

### 21st_magic_component_builder
Generate component from description.
```
Input: {
  "message": "Create a pricing card",
  "searchQuery": "pricing card",
  "absolutePathToCurrentFile": "/src/components/",
  "absolutePathToProjectDirectory": "/project"
}
```

### 21st_magic_component_inspiration
Find component examples.
```
Input: {
  "message": "Show me dashboard layouts",
  "searchQuery": "dashboard"
}
```

### 21st_magic_component_refiner
Improve existing component.
```
Input: {
  "userMessage": "Make it more modern",
  "absolutePathToRefiningFile": "/src/Button.tsx"
}
```

### logo_search
Find brand logos.
```
Input: {
  "queries": ["github", "discord"],
  "format": "TSX"
}
```

## Component Types
- Buttons, Forms, Inputs
- Cards, Modals, Dialogs
- Navigation, Headers, Footers
- Tables, Lists, Grids
- Charts, Dashboards
- Landing pages

## Integration with Commands
- `/sg:implement` - UI components
- `/sg:scaffold` - Design system
- @frontend agent - Styling

## Best Practices
- Provide clear descriptions
- Specify framework (React, Vue, etc.)
- Include accessibility requirements
- Refine iteratively
