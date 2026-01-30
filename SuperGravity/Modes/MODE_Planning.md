---
name: planning
description: Thorough analysis and detailed planning before execution
activation: Complex features, architecture decisions, major changes
---

# Planning Mode

> **Context Framework Note**: Activates for thorough analysis before major work.

## When to Use
- Complex feature implementation
- Architecture decisions
- Major refactoring
- New project setup
- Breaking changes

## Behavioral Changes

### Analysis First
- Gather all requirements
- Research existing patterns
- Identify dependencies
- Map impact areas

### Create Artifacts
- Implementation plans
- Architecture diagrams
- Task breakdowns
- Risk assessments

### Seek Approval
- Present plan before executing
- Get sign-off on approach
- Confirm understanding
- Clarify ambiguities

### Document Decisions
- Record rationale
- Note alternatives considered
- Track constraints
- Update knowledge base

## Artifact Types

### Implementation Plan
```markdown
## Feature: User Authentication

### Requirements
- OAuth2 with Google/GitHub
- Session management
- Role-based access

### Approach
1. Set up NextAuth.js
2. Configure providers
3. Add session middleware
4. Implement role checks

### Risks
- Token refresh complexity
- Session sync across tabs

### Estimated Impact
- 5 new files
- 3 modified files
- ~200 lines
```

## Activation
```
/sg:mode planning
```
Or automatic when:
- "design", "plan", "architect" detected
- Complex scope identified
- Breaking changes involved

## Deactivation
- `/sg:mode fast` for quick mode
- Completion of planning phase
- User switches mode
