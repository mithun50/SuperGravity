# SuperGravity Rules

> Global rules for Google Antigravity IDE. Always active.

## Core Rules

### 1. Read Before Write
Always read and understand existing code before modifying it. Never propose changes to code you haven't examined.

### 2. Verify Before Execute
Check that commands, paths, and parameters are correct before executing. Use file reads or `ls` to confirm.

### 3. Backup Before Destructive
Create backups or confirmation before any destructive operation: file deletion, database migration, git reset.

### 4. Test After Change
Verify changes work by running tests or manual checks after implementation.

### 5. Document Decisions
Record significant technical decisions with rationale.

## Code Standards

### Type Safety
- Use TypeScript for JavaScript projects
- Use type hints for Python
- Avoid `any` types
- Define interfaces for data structures

### Error Handling
- Wrap external calls in try/catch
- Provide meaningful error messages
- Never swallow exceptions silently

### Security
- Never hardcode secrets
- Validate and sanitize all inputs
- Use parameterized queries
- Follow OWASP guidelines

### Naming
- Descriptive, searchable names
- Follow language conventions
- Avoid abbreviations

## Git Safety
- Meaningful commit messages
- One logical change per commit
- Never commit secrets
- Never force push to main/master
- Create feature branches

## Artifact Usage
- Create implementation plans before major changes
- Generate diffs for code reviews
- Screenshot/record UI changes
- Document test results
