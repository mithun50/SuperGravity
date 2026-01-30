---
description: Implement features with proper patterns, validation, and testing
---

1. Ask the user to describe the feature they want to implement.

2. Understand the requirements:
   - What exactly needs to be built?
   - What is the scope?
   - Are there existing patterns to follow?

3. Read existing code in the affected areas to understand current patterns.

4. Create an implementation plan identifying:
   - Files to create or modify
   - Dependencies needed
   - Edge cases to handle

5. Generate the code following existing project patterns.

6. Add proper TypeScript types and interfaces for data structures.

7. Implement error handling with try/catch blocks.

8. Add input validation for all user inputs and API endpoints.

9. Check for security issues (injection, XSS, authentication).

10. Add necessary comments explaining complex logic.

11. Update related documentation if needed.

12. Suggest test cases for the implementation.

## Code Standards

### TypeScript/JavaScript
- Use TypeScript with strict mode
- Define interfaces for data structures
- Handle errors with try/catch
- Use async/await for promises

### React/Next.js
- Use functional components with hooks
- Add proper TypeScript types for props
- Include loading and error states

### API Endpoints
- Validate all inputs
- Use proper HTTP methods and status codes
- Return consistent error format

### Database
- Use parameterized queries
- Handle transactions where needed

## Rules
- READ existing code before modifying
- FOLLOW existing patterns
- NEVER skip error handling
- ALWAYS validate inputs
- NO hardcoded secrets
