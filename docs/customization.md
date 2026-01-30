# Customization Guide

Learn how to create custom workflows, rules, and configure SuperGravity for your needs.

---

## Custom Workflows

### Global Workflows

Global workflows are available in all projects.

**Location:** `~/.gemini/antigravity/global_workflows/`

#### Creating a Global Workflow

1. Create a new file:

```bash
touch ~/.gemini/antigravity/global_workflows/my-workflow.md
```

2. Add workflow content:

```markdown
---
description: My custom workflow for automating X
---

1. Ask the user for the target feature.

2. Read the relevant source files.

3. Analyze the code structure.

// turbo
4. Run `npm run lint`

5. Generate the implementation.

6. Create tests for the implementation.

// turbo
7. Run `npm test`

## Rules
- Follow existing patterns
- Add proper error handling
```

3. Use in Antigravity:

```
/my-workflow
```

---

### Workspace Workflows

Workspace workflows are specific to a project.

**Location:** `.agent/workflows/` in your project

#### Creating a Workspace Workflow

1. Initialize the workspace (if not done):

```bash
supergravity init
```

2. Create a workflow file:

```bash
touch .agent/workflows/custom.md
```

3. Add content:

```markdown
---
description: Project-specific deployment workflow
---

// turbo-all

1. Run linting.
   Run `npm run lint`

2. Run type checking.
   Run `npm run typecheck`

3. Run tests.
   Run `npm test`

4. Build for production.
   Run `npm run build`

5. Deploy to staging.
   Run `npm run deploy:staging`
```

4. Use in Antigravity:

```
/custom
```

---

### Workflow Best Practices

#### Use Clear Step Numbers

```markdown
1. First step.

2. Second step.

3. Third step.
```

#### Add Turbo for Safe Commands

```markdown
// turbo
5. Run `npm run lint`

// turbo
6. Run `npm test`
```

#### Include Rules Section

```markdown
## Rules
- Always validate input
- Check for existing patterns
- Include error handling
```

#### Keep Descriptions Concise

```markdown
---
description: Deploy to production with safety checks (max 250 chars)
---
```

---

## Custom Rules

### Global Rules

Add to `~/.gemini/GEMINI.md`:

```markdown
# My Global Rules

## Code Style
- Use 2-space indentation
- Prefer arrow functions
- Always use const/let, never var

## Project Standards
- All API responses must include status codes
- Log all errors with context
- Use descriptive variable names

# SuperGravity Framework
...
```

### Workspace Rules

Create `.agent/rules/workspace.md`:

```markdown
# Project Rules

> Specific rules for this project.

## Tech Stack
- Next.js 14 with App Router
- TypeScript strict mode
- Tailwind CSS
- Prisma ORM

## File Structure
```
src/
├── app/           # Next.js pages
├── components/    # React components
├── lib/           # Utilities
├── hooks/         # Custom hooks
└── types/         # TypeScript types
```

## Conventions
- Components use PascalCase
- Hooks start with "use"
- API routes in `app/api/`

## Important Patterns
- Use server components by default
- Client components only when needed
- Data fetching in server components
```

---

## Custom MCP Servers

### Adding a Custom Server

1. Edit `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "my-custom-server": {
      "command": "npx",
      "args": ["-y", "@my-org/my-mcp-server"],
      "env": {
        "MY_API_KEY": "your-key"
      }
    }
  }
}
```

2. Sync the registry:

```bash
supergravity mcp sync
```

3. Verify:

```bash
supergravity mcp verify my-custom-server
```

### Server Configuration Options

```json
{
  "my-server": {
    "command": "node",
    "args": ["/path/to/server.js", "--port", "3000"],
    "env": {
      "NODE_ENV": "production",
      "API_KEY": "secret"
    }
  }
}
```

---

## Example Customizations

### Team Workflow: Code Review

`.agent/workflows/team-review.md`:

```markdown
---
description: Team code review workflow with checklist
---

1. Ask which files or PR to review.

2. Read all changed files.

3. Check code quality:
   - Naming conventions
   - Function length
   - Code duplication

4. Check security:
   - Input validation
   - Authentication
   - No hardcoded secrets

5. Check performance:
   - N+1 queries
   - Unnecessary re-renders
   - Large bundle imports

6. Check tests:
   - New code has tests
   - Edge cases covered

7. Generate review summary with:
   - Blocking issues
   - Suggestions
   - Positive feedback

8. Format as GitHub PR comment.
```

### Project Rules: React Native

`.agent/rules/workspace.md`:

```markdown
# React Native Project Rules

## Tech Stack
- React Native 0.73+
- Expo SDK 50
- TypeScript
- React Navigation 6

## File Structure
```
src/
├── screens/       # Screen components
├── components/    # Reusable components
├── navigation/    # Navigation config
├── hooks/         # Custom hooks
├── services/      # API services
├── stores/        # State management
└── utils/         # Utilities
```

## Conventions
- Screens end with "Screen" (HomeScreen.tsx)
- Use StyleSheet.create for styles
- Prefer functional components
- Use React Navigation for routing

## Platform Handling
- Check Platform.OS for platform-specific code
- Use Platform.select for values
- Test on both iOS and Android

## Performance
- Use FlatList for long lists
- Memoize expensive computations
- Avoid inline styles in render
```

### DevOps Workflow: Database Migration

`.agent/workflows/migrate.md`:

```markdown
---
description: Safe database migration workflow
---

1. Ask for migration description.

2. Check current database state.
// turbo
   Run `npx prisma migrate status`

3. Generate migration file.
   Run `npx prisma migrate dev --name [description] --create-only`

4. Review the generated SQL.

5. Ask for approval to apply.

// turbo
6. Run `npx prisma migrate dev`

7. Verify migration applied.
// turbo
   Run `npx prisma migrate status`

8. Generate updated Prisma client.
// turbo
   Run `npx prisma generate`

## Safety Rules
- Always review SQL before applying
- Test migrations on staging first
- Have rollback plan ready
```

---

## Tips

1. **Start Small:** Create simple workflows first, then add complexity

2. **Use Turbo Wisely:** Only auto-execute commands you trust

3. **Document Rules:** Clear rules help the AI make better decisions

4. **Test Workflows:** Try your workflow on a test project first

5. **Share with Team:** Commit `.agent/` to version control for team consistency

6. **Iterate:** Refine workflows based on actual usage

7. **Combine Workflows:** Create meta-workflows that call others

8. **Keep Updated:** Update workflows when your stack changes
