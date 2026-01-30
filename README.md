<div align="center">

# SuperGravity

### **Framework for Google Antigravity IDE**

<p align="center">
  <img src="https://img.shields.io/pypi/v/supergravity" alt="PyPI">
  <img src="https://img.shields.io/badge/Antigravity-Compatible-green" alt="Antigravity">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/pypi/pyversions/supergravity" alt="Python">
</p>

</div>

---

## Overview

SuperGravity transforms Google Antigravity IDE into a structured development platform with:

- **9 Global Workflows** - Slash commands for common tasks (`/scaffold`, `/deploy`, etc.)
- **Workspace Support** - Initialize projects with `.agent/` structure
- **Integrated Rules** - Code quality and security guidelines in GEMINI.md
- **10 MCP Servers** - Validated tool integrations
- **CLI Tool** - Easy installation and management

---

## Installation

### PyPI (Recommended)

```bash
pip install supergravity
```

### From Source

```bash
git clone https://github.com/mithun50/SuperGravity.git
cd SuperGravity
pip install -e .
```

---

## Quick Start

```bash
# Install SuperGravity to Antigravity IDE
supergravity install

# Initialize workspace with .agent/ structure
supergravity init

# Check installation status
supergravity status

# Add MCP servers
supergravity mcp add context7
supergravity mcp add playwright
```

Then restart Antigravity IDE and use `/scaffold`, `/deploy`, `/test`, etc.

---

## CLI Commands

### Core Commands

| Command | Description |
|---------|-------------|
| `supergravity install` | Install SuperGravity to Antigravity IDE |
| `supergravity install --force` | Force reinstall (overwrites files) |
| `supergravity uninstall` | Remove SuperGravity |
| `supergravity update` | Update workflows and rules |
| `supergravity status` | Check installation status |
| `supergravity init` | Initialize `.agent/` workspace structure |
| `supergravity init --path ./myproject` | Initialize specific directory |

### MCP Commands

| Command | Description |
|---------|-------------|
| `supergravity mcp list` | List all available MCP servers |
| `supergravity mcp list --installed` | List only installed servers |
| `supergravity mcp add <server>` | Install and configure an MCP server |
| `supergravity mcp add <server> -k KEY` | Install with API key |
| `supergravity mcp remove <server>` | Remove an MCP server |
| `supergravity mcp update --all` | Update all installed servers |
| `supergravity mcp verify` | Verify all servers work |
| `supergravity mcp prereq` | Check prerequisites (npm, docker) |
| `supergravity mcp setup` | Interactive MCP setup |
| `supergravity mcp sync` | Sync registry with config |

---

## Workflows

Type `/workflow-name` in Antigravity chat:

| Command | Description |
|---------|-------------|
| `/scaffold` | Generate project structures (Next.js, FastAPI, etc.) |
| `/implement` | Implement features with patterns and validation |
| `/security` | Security audit (OWASP Top 10) |
| `/test` | Generate comprehensive test suites |
| `/deploy` | Deploy applications safely |
| `/review` | Code review with quality checks |
| `/document` | Generate documentation |
| `/refactor` | Safe refactoring with tests |
| `/debug` | Systematic debugging |

### Workflow Examples

```
/scaffold nextjs e-commerce app with auth
/implement user authentication with JWT
/security scan src/ for vulnerabilities
/test generate tests for UserService
/deploy to vercel production
/review the changes in src/api/
```

---

## Workspace Initialization

Initialize a project with Antigravity's `.agent/` structure:

```bash
cd your-project
supergravity init
```

This creates:

```
your-project/
└── .agent/
    ├── rules/
    │   └── workspace.md      # Project-specific rules
    └── workflows/
        ├── dev.md            # /dev - Start dev server
        ├── build.md          # /build - Build project
        └── pr.md             # /pr - Create pull request
```

### Custom Workspace Workflows

Create `.agent/workflows/custom.md`:

```markdown
---
description: My custom workflow
---

1. First step description.

// turbo
2. Run `npm run my-command`

3. Final step.
```

Then use `/custom` in Antigravity.

---

## MCP Servers

### No API Key Required

| Server | Purpose |
|--------|---------|
| `context7` | Framework documentation (React, Next.js, Vue, etc.) |
| `sequential-thinking` | Complex multi-step reasoning |
| `playwright` | Browser automation and E2E testing |
| `filesystem` | File system operations |
| `memory` | Persistent memory across sessions |

### API Key Required

| Server | Key Required | Get Key From |
|--------|--------------|--------------|
| `magic` | `TWENTYFIRST_API_KEY` | [21st.dev](https://21st.dev) |
| `tavily` | `TAVILY_API_KEY` | [tavily.com](https://tavily.com) |
| `firecrawl` | `FIRECRAWL_API_KEY` | [firecrawl.dev](https://firecrawl.dev) |
| `github` | `GITHUB_PERSONAL_ACCESS_TOKEN` | [GitHub Settings](https://github.com/settings/tokens) |
| `postgres` | Connection string | Your database |

### Installing MCP Servers

```bash
# No API key required
supergravity mcp add context7
supergravity mcp add playwright

# With API key (interactive prompt)
supergravity mcp add tavily

# With API key (command line)
supergravity mcp add magic -k YOUR_21ST_DEV_KEY
```

---

## Configuration Files

### Global Configuration

```
~/.gemini/
├── GEMINI.md                    # Global rules (includes SuperGravity rules)
└── antigravity/
    ├── mcp_config.json          # MCP server configuration
    ├── mcp_registry.json        # MCP tracking (auto-generated)
    └── global_workflows/        # Global workflow definitions
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

### Workspace Configuration

```
your-project/
└── .agent/
    ├── rules/                   # Workspace-specific rules
    │   └── *.md
    └── workflows/               # Workspace-specific workflows
        └── *.md
```

---

## Core Rules

SuperGravity enforces these rules (added to GEMINI.md):

1. **Read Before Write** - Understand code before modifying
2. **Verify Before Execute** - Check commands first
3. **Backup Before Destructive** - Backup before deletions
4. **Test After Change** - Run tests after modifications
5. **Document Decisions** - Record technical decisions

Plus code standards for:
- Type safety (TypeScript, Python type hints)
- Error handling
- Security (OWASP guidelines)
- Git safety

---

## Troubleshooting

### Check Installation

```bash
supergravity status
```

### MCP Server Issues

```bash
# Check prerequisites
supergravity mcp prereq

# Verify servers
supergravity mcp verify

# Force reinstall a server
supergravity mcp remove context7
supergravity mcp add context7
```

### Missing Node.js

MCP servers require Node.js 18+. Install from [nodejs.org](https://nodejs.org).

### Missing Docker

GitHub MCP requires Docker. Install from [docker.com](https://docker.com).

---

## Documentation

- [Workflows Guide](docs/workflows.md) - Detailed workflow documentation
- [MCP Servers Guide](docs/mcp-servers.md) - MCP server setup and usage
- [Configuration Reference](docs/configuration.md) - All configuration options
- [Customization Guide](docs/customization.md) - Creating custom workflows and rules

---

## Development

```bash
# Clone repository
git clone https://github.com/mithun50/SuperGravity.git
cd SuperGravity

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black supergravity/
isort supergravity/
```

---

## License

MIT

---

## Disclaimer

This project is not affiliated with or endorsed by Google.
Google Antigravity is a product built by Google.
