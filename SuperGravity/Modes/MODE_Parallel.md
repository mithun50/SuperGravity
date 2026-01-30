---
name: parallel
description: Multi-agent coordination for large tasks
activation: Large features, multi-file changes, complex projects
---

# Parallel Mode

> **Context Framework Note**: Coordinates multiple agents for large tasks.

## When to Use
- Large feature implementation
- Multi-file refactoring
- Full-stack development
- Project-wide changes
- Complex migrations

## Behavioral Changes

### Multi-Agent Coordination
- Spawn specialized agents
- Divide work by domain
- Coordinate dependencies
- Merge results

### Task Distribution
- Frontend agent for UI
- Backend agent for API
- Test agent for testing
- Each works in parallel

### Manager View Integration
- Track all agents
- Monitor progress
- Handle conflicts
- Coordinate completion

### Artifact Aggregation
- Combine outputs
- Resolve conflicts
- Unified reporting
- Coherent result

## Agent Coordination

```
┌─────────────────────────────────────┐
│           Manager View              │
│  ┌─────────┐ ┌─────────┐ ┌───────┐  │
│  │Frontend │ │Backend  │ │Tester │  │
│  │ Agent   │ │ Agent   │ │Agent  │  │
│  └────┬────┘ └────┬────┘ └───┬───┘  │
│       │           │          │      │
│       └───────────┼──────────┘      │
│                   │                 │
│            Coordinated              │
│              Output                 │
└─────────────────────────────────────┘
```

## Example Flow

```
User: Implement user dashboard with API and tests

Agent: [Parallel Mode Active]

Spawning agents:
- @frontend: Dashboard UI components
- @backend: User API endpoints
- @tester: Unit and integration tests

Progress:
- Frontend: ████████░░ 80%
- Backend:  ██████████ 100%
- Testing:  ██████░░░░ 60%

Coordination:
- API types shared with frontend ✓
- Test mocks aligned with API ✓
- Component props match data ✓
```

## Task Division

| Agent | Responsibility |
|-------|---------------|
| @fullstack | Architecture, coordination |
| @frontend | UI components, styling |
| @backend | API, database, services |
| @tester | Tests, coverage |
| @devops | Deployment, CI |

## Activation
```
/sg:mode parallel
```
Or use `--parallel` flag:
```
/sg:implement full feature --parallel
```

## Deactivation
- Task completion
- `/sg:mode planning` or `/sg:mode fast`
- Single-domain work
