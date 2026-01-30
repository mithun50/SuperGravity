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

- **9 Workflows** - Slash commands for common tasks
- **3 Rule Sets** - Code quality and security guidelines
- **10 MCP Servers** - Tool integrations (validated packages)
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

### Shell Script (Alternative)

```bash
git clone https://github.com/mithun50/SuperGravity.git
cd SuperGravity
./install.sh
```

---

## CLI Usage

```bash
# Install to Antigravity IDE
supergravity install

# Install with specific MCP servers
supergravity install -m context7 -m playwright -m tavily

# Check installation status
supergravity status

# List available MCP servers
supergravity mcp list

# Add an MCP server
supergravity mcp add tavily --api-key YOUR_KEY

# Remove an MCP server
supergravity mcp remove tavily

# Update installation
supergravity update

# Uninstall
supergravity uninstall
```

---

## Workflows

Type `/workflow-name` in Antigravity:

| Command | Description |
|---------|-------------|
| `/scaffold` | Generate project structures |
| `/implement` | Implement features |
| `/security` | Security audit |
| `/test` | Generate tests |
| `/deploy` | Deploy applications |
| `/review` | Code review |
| `/document` | Generate documentation |
| `/refactor` | Safe refactoring |
| `/debug` | Debug issues |

### Examples

```
/scaffold nextjs my-saas-app
/implement user authentication with OAuth
/security
/test UserService --coverage
/deploy staging
/review src/api/
```

---

## MCP Servers

All MCP server packages have been validated and use correct npm/docker packages.

### No API Key Required

| Server | Package | Purpose |
|--------|---------|---------|
| context7 | `@upstash/context7-mcp` | Framework documentation |
| sequential-thinking | `@modelcontextprotocol/server-sequential-thinking` | Complex reasoning |
| playwright | `@playwright/mcp` | Browser testing |
| filesystem | `@modelcontextprotocol/server-filesystem` | File operations |
| memory | `@modelcontextprotocol/server-memory` | Persistent memory |

### API Key Required

| Server | Package | Key Required |
|--------|---------|--------------|
| magic | `@21st-dev/magic` | `TWENTYFIRST_API_KEY` |
| tavily | `tavily-mcp` | `TAVILY_API_KEY` |
| firecrawl | `firecrawl-mcp` | `FIRECRAWL_API_KEY` |
| github | `ghcr.io/github/github-mcp-server` | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| postgres | `@modelcontextprotocol/server-postgres` | `POSTGRES_URL` |

---

## Configuration Files

### Location (macOS/Linux)
```
~/.gemini/
├── GEMINI.md                    # Global rules
└── antigravity/
    ├── mcp_config.json          # MCP server config
    ├── global_workflows/        # Workflow definitions
    │   ├── scaffold.md
    │   ├── implement.md
    │   └── ...
    └── rules/                   # Rule files
```

### Location (Windows)
```
%USERPROFILE%\.gemini\
└── antigravity\
    └── mcp_config.json
```

---

## Core Rules

SuperGravity enforces these rules:

1. **Read Before Write** - Understand code before modifying
2. **Verify Before Execute** - Check commands first
3. **Backup Before Destructive** - Backup before deletions
4. **Test After Change** - Run tests after modifications
5. **Document Decisions** - Record technical decisions

---

## Customization

### Add Custom Workflow

Create `~/.gemini/antigravity/global_workflows/my-workflow.md`:

```markdown
---
name: my-workflow
description: My custom workflow
---

# My Custom Workflow

Instructions for what the agent should do...
```

Then use with `/my-workflow`.

### Add MCP Server via CLI

```bash
supergravity mcp add tavily --api-key YOUR_TAVILY_KEY
```

### Add MCP Server Manually

Edit `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "@my/mcp-server"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

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

## Uninstall

```bash
# Via CLI
supergravity uninstall

# Manual
rm -rf ~/.gemini/antigravity
# Edit ~/.gemini/GEMINI.md to remove SuperGravity section
```

---

## Sources

MCP package information validated from:
- [@upstash/context7-mcp](https://www.npmjs.com/package/@upstash/context7-mcp)
- [@modelcontextprotocol/server-sequential-thinking](https://www.npmjs.com/package/@modelcontextprotocol/server-sequential-thinking)
- [@21st-dev/magic](https://www.npmjs.com/package/@21st-dev/magic)
- [@playwright/mcp](https://www.npmjs.com/package/@playwright/mcp)
- [tavily-mcp](https://www.npmjs.com/package/tavily-mcp)
- [firecrawl-mcp](https://www.npmjs.com/package/firecrawl-mcp)
- [github/github-mcp-server](https://github.com/github/github-mcp-server)
- [@modelcontextprotocol/server-postgres](https://www.npmjs.com/package/@modelcontextprotocol/server-postgres)
- [@modelcontextprotocol/server-filesystem](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem)
- [@modelcontextprotocol/server-memory](https://www.npmjs.com/package/@modelcontextprotocol/server-memory)

---

## License

MIT

---

## Disclaimer

This project is not affiliated with or endorsed by Google.
Google Antigravity is a product built by Google.
