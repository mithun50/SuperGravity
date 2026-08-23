# MCP Servers Guide

Model Context Protocol (MCP) servers extend Antigravity IDE with additional capabilities. SuperGravity includes 10 validated MCP server configurations.

## What is MCP?

MCP (Model Context Protocol) is a standard that allows AI assistants to interact with external tools and services. Each MCP server provides specific capabilities:

- **context7:** Access framework documentation
- **playwright:** Browser automation
- **memory:** Persistent memory across sessions
- **github:** GitHub operations
- **gbr:** Build Remote Agent phone pairing (`gbr/1`, loopback `:8788` / `gbr-mcp`)

---

## Quick Start

```bash
# Check prerequisites
supergravity mcp prereq

# Install servers (no API key required)
supergravity mcp add context7
supergravity mcp add playwright
supergravity mcp add memory

# Verify installation
supergravity mcp verify
```

---

## Available Servers

### No API Key Required

#### context7

**Purpose:** Access up-to-date framework documentation for React, Next.js, Vue, and more.

```bash
supergravity mcp add context7
```

**Capabilities:**
- Fetch latest documentation
- Get code examples
- Search API references

**Usage in Antigravity:**
```
How do I use React Server Components?
Show me Next.js 14 routing examples
```

---

#### sequential-thinking

**Purpose:** Complex multi-step reasoning and problem-solving.

```bash
supergravity mcp add sequential-thinking
```

**Capabilities:**
- Break down complex problems
- Step-by-step analysis
- Logical reasoning chains

**Usage in Antigravity:**
```
Help me design a scalable authentication system
Analyze this architecture for potential issues
```

---

#### playwright

**Purpose:** Browser automation and E2E testing.

```bash
supergravity mcp add playwright
```

**Capabilities:**
- Automate browser interactions
- Take screenshots
- Run E2E tests
- Navigate web pages

**Usage in Antigravity:**
```
Test the login flow on my app
Take a screenshot of the dashboard
Check if the checkout process works
```

---

#### filesystem

**Purpose:** File system operations.

```bash
supergravity mcp add filesystem
```

**Capabilities:**
- Read/write files
- Create directories
- List directory contents
- Search for files

**Configuration:** Update the path in `mcp_config.json`:
```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/your/project/path"]
  }
}
```

---

#### memory

**Purpose:** Persistent memory across sessions.

```bash
supergravity mcp add memory
```

**Capabilities:**
- Store key-value data
- Retrieve stored information
- Persist context across sessions

**Usage in Antigravity:**
```
Remember that the API uses JWT tokens
What authentication method did we decide on?
```

---

### API Key Required

#### magic (21st.dev)

**Purpose:** AI-powered UI component generation.

```bash
# Interactive (prompts for key)
supergravity mcp add magic

# With key
supergravity mcp add magic -k YOUR_TWENTYFIRST_API_KEY
```

**Get API Key:** [21st.dev](https://21st.dev)

**Capabilities:**
- Generate React components
- Create UI from descriptions
- Build forms and layouts

**Usage in Antigravity:**
```
Create a pricing table component
Build a user profile card
Generate a contact form
```

---

#### tavily

**Purpose:** Web search for research and information gathering.

```bash
supergravity mcp add tavily -k YOUR_TAVILY_API_KEY
```

**Get API Key:** [tavily.com](https://tavily.com)

**Capabilities:**
- Search the web
- Research topics
- Find documentation
- Get current information

**Usage in Antigravity:**
```
Search for best practices in React error handling
Find the latest TypeScript features
Research authentication libraries for Node.js
```

---

#### firecrawl

**Purpose:** Web scraping and content extraction.

```bash
supergravity mcp add firecrawl -k YOUR_FIRECRAWL_API_KEY
```

**Get API Key:** [firecrawl.dev](https://firecrawl.dev)

**Capabilities:**
- Scrape web pages
- Extract structured data
- Convert pages to markdown

**Usage in Antigravity:**
```
Scrape the documentation from this URL
Extract the API reference from this page
```

---

#### gbr

**Purpose:** Pair a phone running [Build Remote Agent](https://grokbuildremote.com/) to this Antigravity desktop session. Protocol `gbr/1`. Phone is spectator + veto. Independent product — not affiliated with xAI or SpaceX. No API key. Never put mailbox keys in `mcp_config.json`.

Install `gbr-agent` v0.6.0+, then `gbr-agent pair && gbr-agent run`. Attach via stdio `gbr-mcp` (entry below) or HTTP `http://127.0.0.1:8788` (`serverUrl` in Antigravity raw config). Clone https://github.com/LinespottingOrg/GrokBuildRemote-Agents and `npm install` in `mcp/gbr-mcp`.

```json
{
  "gbr": {
    "command": "node",
    "args": ["GrokBuildRemote-Agents/mcp/gbr-mcp/bin/gbr-mcp.js"]
  }
}
```

```bash
curl -sS http://127.0.0.1:8788/health
```

---

#### github

**Purpose:** GitHub operations (PRs, issues, repos).

```bash
supergravity mcp add github -k YOUR_GITHUB_TOKEN
```

**Get Token:** [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)

**Required Scopes:**
- `repo` - Full repository access
- `read:org` - Read organization data

**Capabilities:**
- Create/manage pull requests
- Work with issues
- Access repository information
- Review code changes

**Usage in Antigravity:**
```
Create a PR for my changes
List open issues in this repo
Show me the recent commits
```

**Note:** Requires Docker to be installed and running.

---

#### postgres

**Purpose:** PostgreSQL database operations.

```bash
supergravity mcp add postgres
```

**Configuration:** Update the connection string in `mcp_config.json`:
```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/mydb"]
  }
}
```

**Capabilities:**
- Run SQL queries
- Explore database schema
- Manage data

**Usage in Antigravity:**
```
Show me all users in the database
What tables exist in the database?
Run this migration
```

---

## Interactive Setup

The easiest way to install MCP servers is the interactive setup:

```bash
supergravity mcp setup
```

This shows all available servers and lets you select which to install:

```
Available MCP Servers:

No API Key Required:
  1. context7              - Framework documentation - React, Next.js, Vue, etc.
  2. sequential-thinking   - Complex multi-step reasoning
  3. playwright            - Browser automation and E2E testing
  4. filesystem            - File system operations
  5. memory                - Persistent memory across sessions

API Key Required:
  6. magic                 - UI component generation from 21st.dev (TWENTYFIRST_API_KEY)
  7. tavily                - Web search for research (TAVILY_API_KEY)
  8. firecrawl             - Web scraping and content extraction (FIRECRAWL_API_KEY)
  9. github                - GitHub operations - PRs, issues, repos (GITHUB_PERSONAL_ACCESS_TOKEN)
  10. postgres             - PostgreSQL database operations (POSTGRES_URL)

Formats: '1 2 3', '1,2,3', '1-3', 'all', 'skip'
Enter server numbers to install [all]:
```

### Selection Formats

| Format | Example | Installs |
|--------|---------|----------|
| Space-separated | `1 2 3` | Servers 1, 2, 3 |
| Comma-separated | `1,2,3` | Servers 1, 2, 3 |
| Comma with spaces | `1, 2, 3` | Servers 1, 2, 3 |
| Ranges | `1-3` | Servers 1, 2, 3 |
| Mixed | `1, 3-5, 7` | Servers 1, 3, 4, 5, 7 |
| All no-key servers | `all` | Servers 1-5 |
| Skip installation | `skip` | None |

---

## Managing MCP Servers

### List Servers

```bash
# List all available
supergravity mcp list

# List only installed
supergravity mcp list --installed
```

### Add Server

```bash
# No API key required
supergravity mcp add context7

# With API key (interactive)
supergravity mcp add tavily

# With API key (command line)
supergravity mcp add tavily -k YOUR_API_KEY

# Add to config only (skip npm install)
supergravity mcp add context7 --no-install
```

### Remove Server

```bash
supergravity mcp remove context7
```

### Update Servers

```bash
# Update specific server
supergravity mcp update context7

# Update all servers
supergravity mcp update --all
```

### Verify Servers

```bash
# Verify all
supergravity mcp verify

# Verify specific
supergravity mcp verify context7
```

---

## Configuration

### File Location

```
~/.gemini/antigravity/mcp_config.json
```

### Format

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": {
        "TAVILY_API_KEY": "your-key-here"
      }
    }
  }
}
```

### Manual Configuration

Edit `~/.gemini/antigravity/mcp_config.json` directly, then sync:

```bash
supergravity mcp sync
```

---

## MCP Registry

SuperGravity maintains a registry to track installed servers:

```bash
# View registry
supergravity mcp registry

# Sync registry with config
supergravity mcp sync
```

**Registry Location:** `~/.gemini/antigravity/mcp_registry.json`

**Tracked Information:**
- Installation timestamps
- Package versions
- Configuration checksums
- Verification status

---

## Troubleshooting

### Check Prerequisites

```bash
supergravity mcp prereq
```

**Requirements:**
- Node.js 18+ (for npm-based servers)
- Docker (for GitHub MCP only)

### Server Not Working

```bash
# Verify the server
supergravity mcp verify context7

# Remove and reinstall
supergravity mcp remove context7
supergravity mcp add context7

# Check for updates
supergravity mcp update context7
```

### API Key Issues

1. Verify the key is correct
2. Check the key has required permissions
3. Ensure the key hasn't expired

```bash
# Re-add with new key
supergravity mcp remove tavily
supergravity mcp add tavily -k NEW_API_KEY
```

### Docker Not Running (GitHub MCP)

```bash
# Start Docker
docker info

# If not installed, get from docker.com
```

### Registry Out of Sync

```bash
supergravity mcp sync
# Choose "Repair" when prompted
```

---

## Best Practices

1. **Start Simple:** Install `context7` and `memory` first
2. **Add As Needed:** Only install servers you'll use
3. **Keep Updated:** Run `supergravity mcp update --all` periodically
4. **Verify After Install:** Always run `supergravity mcp verify`
5. **Secure Keys:** Never commit API keys to git
