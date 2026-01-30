---
name: api-designer
description: Design clean, consistent, well-documented APIs. Use when user needs API design, OpenAPI specs, GraphQL schemas, or API documentation.
---

# API Designer

## Goal

Design consumer-friendly, consistent, well-documented APIs that are easy to use and maintain.

## Instructions

1. **Understand Consumer Needs**
   - Who will use this API?
   - What operations do they need?
   - What data format is preferred?

2. **Design REST Resources**
   ```
   GET    /users           # List users
   POST   /users           # Create user
   GET    /users/:id       # Get user
   PUT    /users/:id       # Update user
   DELETE /users/:id       # Delete user
   GET    /users/:id/posts # User's posts
   ```

3. **Use Proper Status Codes**
   - 200 OK - Success
   - 201 Created - Resource created
   - 400 Bad Request - Invalid input
   - 401 Unauthorized - Auth required
   - 404 Not Found - Resource missing
   - 500 Server Error - Bug

4. **Define Error Format**
   ```json
   {
     "error": {
       "code": "VALIDATION_ERROR",
       "message": "Invalid email format",
       "details": [{ "field": "email", "message": "Must be valid email" }]
     }
   }
   ```

5. **Document with OpenAPI/GraphQL SDL**

## Examples

**User**: "Design an API for a blog platform"
**Action**: Define resources (posts, users, comments), create OpenAPI spec, design error responses, plan versioning strategy.

**User**: "Convert this REST API to GraphQL"
**Action**: Create type definitions, design queries and mutations, implement pagination with connections.

## Constraints

- Do NOT create inconsistent patterns
- Do NOT skip documentation
- Do NOT mix naming conventions
- ALWAYS use proper HTTP methods
- ALWAYS include pagination for lists
