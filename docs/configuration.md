# Configuration Reference

Complete reference for all SuperGravity configuration files and options.

---

## Directory Structure

### Global Configuration (All Projects)

```
~/.gemini/
├── GEMINI.md                         # Global rules
└── antigravity/
    ├── mcp_config.json               # MCP server configuration
    ├── mcp_registry.json             # MCP registry (auto-generated)
    └── global_workflows/             # Global workflows
        ├── scaffold.md
        ├── implement.md
        ├── security.md
        ├── test.md
        ├── deploy.md
        ├── review.md
        ├── document.md
        ├── refactor.md
        └── debug.md
```

### Workspace Configuration (Per Project)

```
your-project/
└── .agent/
    ├── rules/                        # Project-specific rules
    │   └── workspace.md
    └── workflows/                    # Project-specific workflows
        ├── dev.md
        ├── build.md
        └── pr.md
```

---

## GEMINI.md

Global rules file that applies to all projects.

### Location

```
~/.gemini/GEMINI.md
```

### SuperGravity Section

SuperGravity adds this section:

```markdown
# SuperGravity Framework

## Workflows (type /name in Antigravity)

| Command | Description |
|---------|-------------|
| `/scaffold` | Generate project structures |
| `/implement` | Implement features |
| ... | ... |

## Core Rules

1. **Read Before Write** - Understand code before modifying
2. **Verify Before Execute** - Check commands first
3. **Backup Before Destructive** - Backup before deletions
4. **Test After Change** - Run tests after modifications
5. **Document Decisions** - Record technical decisions

## Code Standards
...

## Security Rules
...

## Git Safety
...
```

### Customizing

Add your own rules before or after the SuperGravity section:

```markdown
# My Custom Rules

- Always use feature branches
- Require PR reviews
- Run linting before commits

# SuperGravity Framework
...
```

---

## mcp_config.json

MCP server configuration file.

### Location

```
~/.gemini/antigravity/mcp_config.json
```

### Format

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "package-name"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `command` | Yes | Executable to run (`npx`, `docker`, `node`) |
| `args` | Yes | Command arguments array |
| `env` | No | Environment variables object |

### Default Servers

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "magic": {
      "command": "npx",
      "args": ["-y", "@21st-dev/magic@latest"],
      "env": {
        "TWENTYFIRST_API_KEY": ""
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    },
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": {
        "TAVILY_API_KEY": ""
      }
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": ""
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": ""
      }
    }
  }
}
```

---

## Workflow Files

### Format

```markdown
---
description: Brief description (max 250 chars)
---

1. Step description.

// turbo
2. Run `command here`

3. Another step.

## Section Header

Additional instructions...

## Rules
- Rule 1
- Rule 2
```

### Frontmatter

| Field | Required | Description |
|-------|----------|-------------|
| `description` | Yes | Brief description of the workflow |

### Step Format

```markdown
1. Plain text step description.

// turbo
2. Run `command to auto-execute`

3. Step with substeps:
   - Substep 1
   - Substep 2
```

### Turbo Annotations

| Annotation | Scope | Description |
|------------|-------|-------------|
| `// turbo` | Single step | Auto-execute next command |
| `// turbo-all` | Entire file | Auto-execute all commands |

### Location

| Type | Path |
|------|------|
| Global | `~/.gemini/antigravity/global_workflows/` |
| Workspace | `.agent/workflows/` |

---

## Workspace Rules

### Format

```markdown
# Workspace Rules

> Description of these rules.

## Section

- Rule 1
- Rule 2

## Another Section

Instructions...
```

### Location

```
your-project/.agent/rules/workspace.md
```

### Example

```markdown
# Project Rules

> Rules specific to this project.

## Tech Stack

- Frontend: Next.js 14 with App Router
- Backend: tRPC
- Database: PostgreSQL with Prisma
- Auth: NextAuth.js

## Conventions

- Use `src/` directory structure
- Components in `src/components/`
- API routes in `src/app/api/`

## Important Files

- `src/lib/db.ts` - Database client
- `src/lib/auth.ts` - Auth configuration
- `src/types/` - Shared TypeScript types
```

---

## CLI Options

### supergravity install

```bash
supergravity install [OPTIONS]

Options:
  -f, --force              Overwrite existing files
  -m, --mcp TEXT           MCP servers to install (repeatable)
  --skip-mcp-install       Skip npm/docker package installation
```

### supergravity init

```bash
supergravity init [OPTIONS]

Options:
  -p, --path PATH          Workspace path (default: current directory)
  --rules / --no-rules     Include sample workspace rules (default: yes)
  --workflows / --no-workflows  Include sample workflows (default: yes)
```

### supergravity mcp add

```bash
supergravity mcp add SERVER_NAME [OPTIONS]

Options:
  -k, --api-key TEXT       API key for the server
  --no-install             Skip package installation
```

### supergravity mcp update

```bash
supergravity mcp update [SERVER_NAME] [OPTIONS]

Options:
  -a, --all                Update all installed servers
```

---

## Environment Variables

### Supported by MCP Servers

| Variable | Server | Description |
|----------|--------|-------------|
| `TWENTYFIRST_API_KEY` | magic | 21st.dev API key |
| `TAVILY_API_KEY` | tavily | Tavily search API key |
| `FIRECRAWL_API_KEY` | firecrawl | Firecrawl API key |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | github | GitHub PAT |

### Setting Keys

**Option 1: In mcp_config.json**
```json
{
  "env": {
    "TAVILY_API_KEY": "your-key"
  }
}
```

**Option 2: Via CLI**
```bash
supergravity mcp add tavily -k your-key
```

**Option 3: System Environment**
```bash
export TAVILY_API_KEY=your-key
```

---

## Platform Differences

### macOS / Linux

```
~/.gemini/
└── antigravity/
    ├── mcp_config.json
    └── global_workflows/
```

### Windows

```
%USERPROFILE%\.gemini\
└── antigravity\
    ├── mcp_config.json
    └── global_workflows\
```

---

## Best Practices

1. **Don't Edit Registry:** The `mcp_registry.json` is auto-generated
2. **Backup Before Force:** Use `--force` carefully, it overwrites files
3. **Keep Keys Secure:** Never commit API keys to version control
4. **Use Workspace Config:** Project-specific settings go in `.agent/`
5. **Sync After Manual Edits:** Run `supergravity mcp sync` after editing mcp_config.json
