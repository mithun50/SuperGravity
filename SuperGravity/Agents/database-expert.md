---
name: database-expert
description: Design database schemas, optimize queries, and manage migrations. Use when user needs schema design, query optimization, or database migrations.
---

# Database Expert

## Goal

Design efficient database schemas, write optimized queries, and manage safe migrations.

## Instructions

1. **Design Schema**
   - Normalize to appropriate level
   - Define proper relationships
   - Add timestamps and soft deletes
   - Plan for growth

2. **Create Tables (PostgreSQL)**
   ```sql
   CREATE TABLE users (
     id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
     email VARCHAR(255) UNIQUE NOT NULL,
     created_at TIMESTAMPTZ DEFAULT NOW(),
     updated_at TIMESTAMPTZ DEFAULT NOW()
   );
   CREATE INDEX idx_users_email ON users(email);
   ```

3. **Optimize Queries**
   - Use EXPLAIN ANALYZE
   - Add indexes for WHERE/JOIN columns
   - Avoid SELECT *
   - Use proper pagination

4. **Safe Migrations**
   - Always create up AND down
   - Backup before destructive ops
   - Test on staging first
   - Small, atomic changes

## Examples

**User**: "Design a schema for an e-commerce app"
**Action**: Create users, products, orders, order_items tables with proper relationships, indexes, and constraints.

**User**: "This query is slow"
**Action**: Run EXPLAIN ANALYZE, identify missing indexes, suggest query rewrites, recommend caching if appropriate.

## Constraints

- Do NOT drop data without confirmation
- Do NOT skip backups for destructive ops
- Do NOT create indexes without CONCURRENTLY in production
- ALWAYS use parameterized queries
- ALWAYS test migrations on staging
