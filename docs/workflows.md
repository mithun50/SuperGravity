# Workflows Guide

SuperGravity provides 9 global workflows that automate common development tasks in Google Antigravity IDE.

## How Workflows Work

Workflows are triggered by typing `/workflow-name` in the Antigravity chat. They guide the AI agent through a structured series of steps to accomplish a task.

### Workflow Format

Workflows use Markdown with YAML frontmatter:

```markdown
---
description: Brief description of what this workflow does
---

1. First step description.

// turbo
2. Run `command here`

3. Next step.
```

### Turbo Mode

- `// turbo` - Auto-execute the next command without confirmation
- `// turbo-all` - Auto-execute all commands in the workflow

---

## Available Workflows

### /scaffold

**Purpose:** Generate complete project structures for various technology stacks.

**Usage:**
```
/scaffold
/scaffold nextjs e-commerce app
/scaffold fastapi backend with postgres
/scaffold react typescript with tailwind
```

**Steps:**
1. Asks for project type (Next.js, React, Vue, FastAPI, Django, Express)
2. Detects requirements (frontend, backend, database, auth)
3. Generates directory structure
4. Creates configuration files (package.json, tsconfig, etc.)
5. Sets up Docker and CI/CD
6. Generates README with setup instructions

**Supports:**
- Next.js / React / Vue / Svelte
- FastAPI / Django / Express
- PostgreSQL / MySQL / MongoDB / SQLite
- TypeScript / ESLint / Prettier
- Docker / GitHub Actions

---

### /implement

**Purpose:** Implement features with proper patterns, validation, and testing.

**Usage:**
```
/implement
/implement user authentication with JWT
/implement shopping cart functionality
/implement dark mode toggle
```

**Steps:**
1. Asks for feature description
2. Reads existing code to understand patterns
3. Creates implementation plan
4. Generates code following project patterns
5. Adds TypeScript types and error handling
6. Suggests test cases

**Best Practices Applied:**
- Follows existing project patterns
- TypeScript strict mode
- Error handling with try/catch
- Input validation
- Security checks

---

### /security

**Purpose:** Perform security audit scanning for OWASP Top 10 vulnerabilities.

**Usage:**
```
/security
/security scan src/api/
/security check authentication code
```

**Scans For:**

| Category | Vulnerabilities |
|----------|-----------------|
| A01 | Broken Access Control, IDOR, Path Traversal |
| A02 | Weak Hashing, Hardcoded Secrets, Missing Encryption |
| A03 | SQL Injection, XSS, Command Injection |
| A05 | Debug Mode, Default Credentials, Missing Headers |
| A07 | Weak Passwords, Missing Rate Limiting |

**Output:**
- Severity ratings (CRITICAL, HIGH, MEDIUM, LOW)
- File locations and line numbers
- Vulnerable code snippets
- Remediation code examples

---

### /test

**Purpose:** Generate comprehensive test suites for code coverage.

**Usage:**
```
/test
/test UserService
/test src/components/Button.tsx
/test api endpoints
```

**Generates:**
- **Unit Tests:** Individual function testing
- **Integration Tests:** API endpoint testing
- **E2E Tests:** User flow testing with Playwright

**Coverage:**
- Happy path (normal operation)
- Edge cases (empty, null, boundary)
- Error cases (invalid input, failures)
- Async behavior (loading, success, error states)

**Frameworks Supported:**
- Jest / Vitest (JavaScript/TypeScript)
- Pytest (Python)
- Playwright (E2E)

---

### /deploy

**Purpose:** Deploy applications safely with proper checks and rollback plans.

**Usage:**
```
/deploy
/deploy to vercel
/deploy staging
/deploy production with docker
```

**Pre-Deployment Checklist:**
- All tests passing
- Build succeeds
- No security vulnerabilities
- Environment variables configured
- Database migrations ready

**Deployment Targets:**
- Vercel
- Docker / Kubernetes
- AWS / GCP / Azure
- Railway / Render / Fly.io
- GitHub Actions CI/CD

**Steps:**
1. Runs tests and build verification
2. Creates deployment plan
3. Deploys to staging first
4. Verifies staging deployment
5. Gets approval for production
6. Deploys to production
7. Monitors for issues

---

### /review

**Purpose:** Perform code review with security, quality, and performance checks.

**Usage:**
```
/review
/review src/api/users.ts
/review the latest changes
```

**Review Categories:**

| Icon | Category | Description |
|------|----------|-------------|
| 🚨 | Blocking | Must fix (security issues, bugs) |
| 💡 | Suggestion | Should consider (improvements) |
| ❓ | Question | Need clarification |
| ✨ | Praise | Good patterns to highlight |

**Checks:**
- Security (secrets, injection, auth)
- Code quality (naming, complexity, duplication)
- Performance (N+1 queries, memory leaks)
- Test coverage

**Output:**
- Summary with counts per category
- Detailed findings with file locations
- Verdict (Approved / Changes Requested)

---

### /document

**Purpose:** Generate comprehensive documentation for code, APIs, and components.

**Usage:**
```
/document
/document README for this project
/document API endpoints
/document React components
```

**Documentation Types:**

| Type | Contents |
|------|----------|
| README.md | Project overview, installation, usage |
| API Docs | Endpoints, request/response schemas |
| Component Docs | Props, usage examples, Storybook |
| Architecture | System overview, data flow, decisions |

**Features:**
- Working code examples
- Request/response examples
- Props tables for components
- Clear headings and structure

---

### /refactor

**Purpose:** Safely refactor code to improve structure without changing behavior.

**Usage:**
```
/refactor
/refactor UserService for better readability
/refactor extract common logic
```

**Safety Measures:**
1. Checks for existing tests first
2. Suggests writing tests if none exist
3. Makes small, atomic changes
4. Runs tests after each change
5. Creates before/after comparisons

**Common Refactors:**
- Extract function
- Rename for clarity
- Simplify conditionals
- Remove duplication
- Reduce nesting

---

### /debug

**Purpose:** Debug issues systematically with root cause analysis.

**Usage:**
```
/debug
/debug TypeError in UserService
/debug API returning 500 error
```

**Debug Process:**
1. Understand the problem (expected vs actual)
2. Gather information (errors, logs, changes)
3. Form hypothesis
4. Add strategic logging
5. Test hypothesis
6. Implement fix
7. Write regression test
8. Verify fix

**Common Patterns:**
- Undefined/null errors
- Async/promise issues
- API errors
- Database issues

---

## Creating Custom Workflows

### Global Workflows

Create `~/.gemini/antigravity/global_workflows/my-workflow.md`:

```markdown
---
description: My custom workflow for [purpose]
---

1. First step description.

2. Ask user for input.

// turbo
3. Run `npm run my-command`

4. Verify the result.

## Rules
- Rule 1
- Rule 2
```

### Workspace Workflows

Create `.agent/workflows/my-workflow.md` in your project:

```markdown
---
description: Project-specific workflow
---

// turbo-all

1. Install dependencies.
   Run `npm install`

2. Start development server.
   Run `npm run dev`
```

---

## Tips

1. **Be Specific:** Include context in your workflow request
   - Good: `/scaffold nextjs e-commerce with stripe`
   - Basic: `/scaffold`

2. **Combine Workflows:** Use multiple workflows in sequence
   - `/scaffold` → `/implement` → `/test` → `/deploy`

3. **Use Turbo Mode:** Add `// turbo` for commands you trust

4. **Workspace Workflows:** Create project-specific workflows in `.agent/workflows/`

5. **Review Output:** Always review generated code before committing
