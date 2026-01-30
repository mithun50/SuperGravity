---
name: document
description: Generate documentation
category: workflow
agents: [docs]
---

# /sg:document - Documentation Generation

> **Context Framework Note**: Creates comprehensive documentation.

## Triggers
- `/sg:document [target] [--flags]`
- Documentation requests
- README/API doc needs

## Syntax
```
/sg:document [target] [options]

Targets:
  readme      Generate README
  api         API documentation
  component   Component docs
  project     Full project docs

Options:
  --format markdown|html
  --output [path]
  --artifact
```

## Behavioral Flow

1. **Analyze** - Understand codebase
2. **Extract** - Get types, signatures, comments
3. **Generate** - Create documentation
4. **Format** - Apply markdown/HTML
5. **Output** - Save or artifact

## Documentation Types

### README
```markdown
# Project Name

Description of the project.

## Quick Start
\`\`\`bash
npm install
npm run dev
\`\`\`

## Features
- Feature 1
- Feature 2

## API Reference
See [API docs](./docs/api.md)
```

### API Documentation
```markdown
## Users API

### GET /api/users
Returns list of users.

**Response:**
\`\`\`json
{
  "data": [{ "id": "1", "email": "..." }]
}
\`\`\`

### POST /api/users
Create new user.

**Body:**
\`\`\`json
{ "email": "user@example.com" }
\`\`\`
```

### Component Docs
```markdown
## Button Component

Reusable button with variants.

### Props
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | string | 'primary' | Button style |
| size | string | 'md' | Button size |

### Usage
\`\`\`tsx
<Button variant="primary" size="lg">
  Click me
</Button>
\`\`\`
```

## Examples

### Generate README
```
/sg:document readme
```

### API Docs
```
/sg:document api --format markdown
```

### Full Project
```
/sg:document project --output ./docs --artifact
```

## Outputs
- Documentation files
- API references
- Component docs
- Artifact (if requested)

## Boundaries
**Will:** Create accurate, helpful documentation
**Won't:** Generate walls of text, skip examples
