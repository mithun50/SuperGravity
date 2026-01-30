---
name: implement
description: Implement features with proper patterns and validation
---

# Feature Implementation

You are implementing a feature. Follow this structured approach:

## Process

1. **Understand Requirements**
   - What exactly needs to be built?
   - What's the scope?
   - Are there existing patterns to follow?

2. **Plan Implementation**
   - Create an implementation plan artifact
   - Identify files to create/modify
   - Note dependencies
   - Consider edge cases

3. **Generate Code**
   - Follow existing project patterns
   - Use proper typing
   - Include error handling
   - Add input validation

4. **Validate**
   - Check for security issues
   - Verify types are correct
   - Ensure patterns match codebase

5. **Document**
   - Add necessary comments
   - Update related documentation if needed

## Code Standards

### TypeScript/JavaScript
- Use TypeScript with strict mode
- Define interfaces for data structures
- Handle errors with try/catch
- Use async/await for promises

### React/Next.js
- Use functional components
- Prefer hooks over class components
- Add proper TypeScript types for props
- Include loading and error states

### API Endpoints
- Validate all inputs
- Use proper HTTP methods and status codes
- Return consistent error format
- Add rate limiting considerations

### Database
- Use parameterized queries
- Add proper indexes
- Handle transactions where needed

## Output

Create artifact with:
- Implementation plan
- Code changes with diffs
- Testing recommendations

## Rules

- READ existing code before modifying
- FOLLOW existing patterns
- NEVER skip error handling
- ALWAYS validate inputs
- NO hardcoded secrets
