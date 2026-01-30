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
- **MCP Registry** - Robust tracking and management
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

## Quick Start

```bash
# Install SuperGravity to Antigravity IDE
supergravity install

# Check what's installed
supergravity status

# Add an MCP server
supergravity mcp add context7

# Update all MCP servers
supergravity mcp update --all
```

---

## CLI Reference

### Core Commands

| Command | Description |
|---------|-------------|
| `supergravity install` | Install SuperGravity to Antigravity IDE |
| `supergravity uninstall` | Remove SuperGravity |
| `supergravity update` | Update workflows and rules |
| `supergravity status` | Check installation status |

### MCP Commands

| Command | Description |
|---------|-------------|
| `supergravity mcp list` | List all available MCP servers |
| `supergravity mcp list --installed` | List only installed servers |
| `supergravity mcp add <server>` | Install and configure an MCP server |
| `supergravity mcp add <server> -k KEY` | Install with API key |
| `supergravity mcp add <server> --no-install` | Add to config only |
| `supergravity mcp remove <server>` | Remove an MCP server |
| `supergravity mcp update <server>` | Update a specific server |
| `supergravity mcp update --all` | Update all installed servers |
| `supergravity mcp verify` | Verify all servers work |
| `supergravity mcp verify <server>` | Verify specific server |
| `supergravity mcp prereq` | Check prerequisites (npm, docker) |
| `supergravity mcp setup` | Interactive MCP setup |
| `supergravity mcp sync` | Sync registry with config |
| `supergravity mcp registry` | Show registry status |

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

### Installing MCP Servers

```bash
# No API key required
supergravity mcp add context7
supergravity mcp add playwright
supergravity mcp add memory

# With API key
supergravity mcp add tavily -k YOUR_TAVILY_API_KEY
supergravity mcp add magic -k YOUR_21ST_DEV_KEY

# Interactive (prompts for key)
supergravity mcp add github
```

### MCP Registry

SuperGravity uses a registry to track installed MCP servers:

```bash
# Check registry status
supergravity mcp registry

# Sync registry with config file
supergravity mcp sync

# Verify servers are working
supergravity mcp verify
```

The registry tracks:
- Installation timestamps
- Configuration checksums (detects changes)
- Verification status
- Package versions

---

## Configuration Files

### Location (macOS/Linux)
```
~/.gemini/
├── GEMINI.md                    # Global rules
└── antigravity/
    ├── mcp_config.json          # MCP server config
    ├── mcp_registry.json        # MCP registry (auto-generated)
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
    ├── mcp_config.json
    └── mcp_registry.json
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

Then sync the registry:
```bash
supergravity mcp sync
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

### Build for PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

---

## Troubleshooting

### MCP Server Issues

```bash
# Check prerequisites
supergravity mcp prereq

# Verify specific server
supergravity mcp verify context7

# Force reinstall
supergravity mcp add context7 --force

# Update to latest
supergravity mcp update context7
```

### Registry Out of Sync

```bash
# Check sync status
supergravity mcp sync

# Repair registry from config
supergravity mcp sync  # Then choose "Repair"
```

### Missing Node.js

MCP servers require Node.js. Install from [nodejs.org](https://nodejs.org).

### Missing Docker

GitHub MCP requires Docker. Install from [docker.com](https://docker.com).

---

## Architecture

```
supergravity/
├── __init__.py           # Package info
├── __main__.py           # CLI entry point
└── setup/
    ├── services/
    │   ├── installer.py      # Core installation
    │   ├── config.py         # Config management
    │   ├── mcp_installer.py  # MCP package installation
    │   └── mcp_registry.py   # MCP tracking registry
    └── utils/
        └── paths.py          # Cross-platform paths
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
