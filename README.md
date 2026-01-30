<div align="center">

# 🪐 SuperGravity

### **Framework for Google Antigravity IDE**

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/Antigravity-Compatible-green" alt="Antigravity">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

</div>

---

## Overview

SuperGravity transforms Google Antigravity IDE into a structured development platform with:

- **9 Workflows** - Slash commands for common tasks
- **3 Rule Sets** - Code quality and security guidelines
- **10 MCP Servers** - Tool integrations
- **Interactive Setup** - Configure what you need

---

## Quick Install

```bash
git clone https://github.com/user/SuperGravity.git
cd SuperGravity
./install.sh
```

The installer will:
1. Create `~/.gemini/GEMINI.md` (global config)
2. Install workflows to `~/.gemini/antigravity/global_workflows/`
3. Configure MCP servers in `~/.gemini/antigravity/mcp_config.json`
4. Set up rules and browser allowlist

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

The installer configures these MCP servers:

### Essential (No API Key)
| Server | Purpose |
|--------|---------|
| context7 | Framework documentation |
| sequential-thinking | Complex reasoning |
| playwright | Browser testing |

### Optional (Require API Keys)
| Server | Purpose | Key Required |
|--------|---------|--------------|
| magic | UI components | 21st.dev API key |
| tavily | Web search | Tavily API key |
| github | GitHub operations | GitHub token |
| postgres | Database operations | PostgreSQL URL |

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
    ├── rules/                   # Rule files
    └── browserAllowlist.txt     # Allowed domains
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

### Add MCP Server

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

## Uninstall

```bash
rm -rf ~/.gemini/antigravity
rm ~/.gemini/GEMINI.md
```

---

## License

MIT

---

## Disclaimer

This project is not affiliated with or endorsed by Google.
Google Antigravity is a product built by Google.
