---
name: implement
description: Feature and code implementation with intelligent agent coordination
category: workflow
mcp-servers: [context7, sequential, magic, playwright]
agents: [fullstack, frontend, backend, security, tester]
---

# /sg:implement - Feature Implementation

> **Context Framework Note**: Activates when users type `/sg:implement` for feature development.

## Triggers
- `/sg:implement [feature] [--flags]`
- Feature development requests
- Code implementation needs

## Syntax
```
/sg:implement [feature-description] [options]

Options:
  --type component|api|service|feature
  --framework react|vue|nextjs|fastapi
  --safe          Enable safety checks
  --with-tests    Generate tests
  --artifact      Create artifact
```

## Behavioral Flow

1. **Analyze** - Examine requirements, detect tech context
2. **Plan** - Create implementation plan artifact
3. **Coordinate** - Activate relevant agents
4. **Generate** - Create code with best practices
5. **Validate** - Security checks, tests
6. **Document** - Update docs if needed

## Agent Coordination

| Context | Agents Activated |
|---------|-----------------|
| UI Component | @frontend, @tester |
| API Endpoint | @backend, @security |
| Full Feature | @fullstack, @security, @tester |
| Database | @backend, @database |

## MCP Integration
- **Context7**: Framework documentation
- **Magic**: UI component generation
- **Sequential**: Complex multi-step planning
- **Playwright**: E2E test generation

## Examples

### React Component
```
/sg:implement user profile card --type component --framework react
```

### API Endpoint
```
/sg:implement user authentication API --type api --safe --with-tests
```

### Full Feature
```
/sg:implement shopping cart --type feature --with-tests --artifact
```

## Outputs
- Implementation code
- Test files (if --with-tests)
- Documentation updates
- Artifact with plan and diffs

## Boundaries
**Will:** Implement with proper patterns, validation, testing
**Won't:** Skip security, ignore type safety
