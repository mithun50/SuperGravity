# PostgreSQL MCP Server

**Purpose**: Direct PostgreSQL database operations and queries

## Triggers
- Database schema design or modification
- SQL query execution needs
- Data migration tasks
- Database performance analysis
- Schema introspection requirements

## Choose When
- **For queries**: Running SELECT, INSERT, UPDATE, DELETE
- **For schema**: Creating/modifying tables, indexes, constraints
- **For migrations**: Database schema changes
- **For analysis**: Query performance, explain plans

## Works Best With
- **Sequential**: Plan complex database operations
- **Context7**: Get ORM/database library patterns

## Configuration
Requires `POSTGRES_URL` environment variable (connection string).

## Security Notes
- Use read-only connections when possible
- Never expose credentials in code
- Validate all user inputs before queries
- Use parameterized queries to prevent SQL injection

## Examples
```
"show all tables in the database" → Postgres (schema introspection)
"create a users table" → Postgres (DDL operations)
"find users created last week" → Postgres (query execution)
"optimize this slow query" → Postgres (explain/analyze)
```
