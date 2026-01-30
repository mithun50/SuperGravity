---
name: fullstack-architect
description: Design and implement complete full-stack applications. Use when user asks to scaffold a project, design architecture, or build end-to-end features.
---

# Full-Stack Architect

## Goal

Design and implement complete full-stack applications with modern patterns, proper architecture, and production-ready code.

## Instructions

1. **Assess Requirements**
   - Understand the project scope and scale
   - Identify team size and expertise
   - Determine performance and security needs

2. **Design Architecture**
   - Choose appropriate frontend framework (React, Next.js, Vue, Svelte)
   - Select backend technology (Node.js, Python, Go)
   - Design database schema (PostgreSQL, MongoDB)
   - Plan API structure (REST, GraphQL, tRPC)

3. **Scaffold Project**
   - Generate complete directory structure
   - Set up configuration files
   - Configure TypeScript, ESLint, Prettier
   - Add Docker and CI/CD

4. **Implement Features**
   - Build with extensibility in mind
   - Follow established patterns
   - Include proper error handling
   - Add authentication if needed

## Examples

**User**: "Create a SaaS starter with Next.js and Stripe"
**Action**: Scaffold Next.js 14 app with App Router, add Stripe integration, set up auth with NextAuth, configure PostgreSQL with Prisma.

**User**: "Design architecture for a real-time chat app"
**Action**: Propose WebSocket-based architecture, recommend tech stack, create component diagram, identify scaling considerations.

## Constraints

- Do NOT over-engineer simple projects
- Do NOT choose technologies based on hype
- Do NOT skip error handling or validation
- Do NOT hardcode secrets or credentials
