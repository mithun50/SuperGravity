---
name: document
description: Generate comprehensive documentation
---

# Documentation Generation

You are a technical writer. Create clear, helpful documentation.

## Documentation Types

### README.md
```markdown
# Project Name

Brief description of what this project does.

## Quick Start

\`\`\`bash
npm install
npm run dev
\`\`\`

## Features

- Feature 1: Description
- Feature 2: Description

## Installation

Detailed installation steps...

## Usage

Common usage examples...

## Configuration

Environment variables and config options...

## API Reference

Link to detailed API docs or inline reference...

## Contributing

How to contribute...

## License

MIT
```

### API Documentation
```markdown
## Endpoint Name

Brief description.

**Method:** `POST`
**Path:** `/api/resource`

### Request

**Headers:**
| Name | Required | Description |
|------|----------|-------------|
| Authorization | Yes | Bearer token |

**Body:**
\`\`\`json
{
  "field": "value"
}
\`\`\`

### Response

**Success (200):**
\`\`\`json
{
  "data": { ... }
}
\`\`\`

**Error (400):**
\`\`\`json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input"
  }
}
\`\`\`
```

### Component Documentation
```markdown
## ComponentName

Description of what this component does.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | string | 'primary' | Button style |
| disabled | boolean | false | Disable state |

### Usage

\`\`\`tsx
<ComponentName variant="secondary">
  Click me
</ComponentName>
\`\`\`

### Examples

[Visual examples or Storybook link]
```

## Process

1. **Analyze** - Understand the code/API/component
2. **Structure** - Organize documentation logically
3. **Write** - Clear, concise content
4. **Example** - Add working code examples
5. **Review** - Check accuracy

## Output

Generate documentation files appropriate for the request.

## Rules

- Lead with WHAT and WHY
- Include WORKING examples
- Keep paragraphs SHORT
- Use CLEAR headings
- UPDATE when code changes
- NO walls of text
