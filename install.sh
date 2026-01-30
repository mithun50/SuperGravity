#!/bin/bash
# SuperGravity Installer for Google Antigravity IDE
# APPENDS to existing configs - does not replace

set -e

echo "🪐 SuperGravity Installer for Google Antigravity"
echo "================================================"
echo "Mode: APPEND to existing configuration"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GEMINI_DIR="$HOME/.gemini"
ANTIGRAVITY_DIR="$GEMINI_DIR/antigravity"

# Windows support
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    GEMINI_DIR="$USERPROFILE/.gemini"
    ANTIGRAVITY_DIR="$GEMINI_DIR/antigravity"
fi

echo "Target: $GEMINI_DIR"
echo ""

# Create directories if needed
mkdir -p "$GEMINI_DIR"
mkdir -p "$ANTIGRAVITY_DIR/global_workflows"
mkdir -p "$ANTIGRAVITY_DIR/rules"

# ============================================
# APPEND TO GEMINI.md
# ============================================
echo -e "${YELLOW}Updating GEMINI.md...${NC}"

GEMINI_FILE="$GEMINI_DIR/GEMINI.md"

# Check if SuperGravity section already exists
if [ -f "$GEMINI_FILE" ] && grep -q "SuperGravity" "$GEMINI_FILE"; then
    echo "  SuperGravity section already exists in GEMINI.md"
    echo -n "  Overwrite SuperGravity section? [y/N]: "
    read -r OVERWRITE
    if [[ ! "$OVERWRITE" =~ ^[Yy]$ ]]; then
        echo "  Skipping GEMINI.md update"
    else
        # Remove old SuperGravity section and append new
        sed -i '/# SuperGravity/,/^# [^S]/{ /^# [^S]/!d }' "$GEMINI_FILE" 2>/dev/null || true
        cat >> "$GEMINI_FILE" << 'SGEOF'

# SuperGravity Framework

## Workflows (type /name in Antigravity)

| Command | Description |
|---------|-------------|
| `/scaffold` | Generate project structures |
| `/implement` | Implement features |
| `/security` | Security audit |
| `/test` | Generate tests |
| `/deploy` | Deploy applications |
| `/review` | Code review |
| `/document` | Generate docs |
| `/refactor` | Safe refactoring |
| `/debug` | Debug issues |

## Core Rules

1. **Read Before Write** - Understand code before modifying
2. **Verify Before Execute** - Check commands first
3. **Backup Before Destructive** - Backup before deletions
4. **Test After Change** - Run tests after modifications
5. **Document Decisions** - Record technical decisions

## Code Standards

- TypeScript for JS projects
- Handle all errors with try/catch
- Validate all inputs
- Never hardcode secrets
- Write tests for new code
- Follow OWASP guidelines
SGEOF
        echo "  Updated GEMINI.md"
    fi
else
    # File doesn't exist or no SuperGravity section - append
    cat >> "$GEMINI_FILE" << 'SGEOF'

# SuperGravity Framework

## Workflows (type /name in Antigravity)

| Command | Description |
|---------|-------------|
| `/scaffold` | Generate project structures |
| `/implement` | Implement features |
| `/security` | Security audit |
| `/test` | Generate tests |
| `/deploy` | Deploy applications |
| `/review` | Code review |
| `/document` | Generate docs |
| `/refactor` | Safe refactoring |
| `/debug` | Debug issues |

## Core Rules

1. **Read Before Write** - Understand code before modifying
2. **Verify Before Execute** - Check commands first
3. **Backup Before Destructive** - Backup before deletions
4. **Test After Change** - Run tests after modifications
5. **Document Decisions** - Record technical decisions

## Code Standards

- TypeScript for JS projects
- Handle all errors with try/catch
- Validate all inputs
- Never hardcode secrets
- Write tests for new code
- Follow OWASP guidelines
SGEOF
    echo "  Appended SuperGravity section to GEMINI.md"
fi

# ============================================
# MERGE MCP CONFIG
# ============================================
echo ""
echo -e "${BLUE}=== MCP Server Configuration ===${NC}"
echo ""

MCP_FILE="$ANTIGRAVITY_DIR/mcp_config.json"

echo "Select MCP servers to add:"
echo ""
echo "  1. context7           - Framework documentation (@upstash/context7-mcp)"
echo "  2. sequential-thinking - Complex reasoning (@modelcontextprotocol/server-sequential-thinking)"
echo "  3. playwright         - Browser testing (@playwright/mcp)"
echo "  4. magic              - UI components (needs API key) (@21st-dev/magic)"
echo "  5. tavily             - Web search (needs API key) (tavily-mcp)"
echo "  6. github             - GitHub ops (needs token) (Docker)"
echo "  7. postgres           - Database (needs URL) (@modelcontextprotocol/server-postgres)"
echo "  8. filesystem         - File operations (@modelcontextprotocol/server-filesystem)"
echo "  9. memory             - Persistent memory (@modelcontextprotocol/server-memory)"
echo "  10. firecrawl         - Web scraping (needs API key) (firecrawl-mcp)"
echo ""
echo "Enter numbers (e.g., '1 2 3') or 'skip' to skip:"
read -r MCP_SELECTION

if [ "$MCP_SELECTION" != "skip" ] && [ -n "$MCP_SELECTION" ]; then
    echo -e "${YELLOW}Adding MCP servers...${NC}"

    # Create temp file for new servers
    TEMP_MCPS=$(mktemp)

    for num in $MCP_SELECTION; do
        case $num in
            1)
                cat >> "$TEMP_MCPS" << 'EOF'
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
EOF
                echo "  + context7"
                ;;
            2)
                cat >> "$TEMP_MCPS" << 'EOF'
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
EOF
                echo "  + sequential-thinking"
                ;;
            3)
                cat >> "$TEMP_MCPS" << 'EOF'
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    },
EOF
                echo "  + playwright"
                ;;
            4)
                echo -n "    21st.dev API key: "
                read -r KEY
                if [ -n "$KEY" ]; then
                    cat >> "$TEMP_MCPS" << EOF
    "magic": {
      "command": "npx",
      "args": ["-y", "@21st-dev/magic@latest"],
      "env": { "TWENTYFIRST_API_KEY": "$KEY" }
    },
EOF
                    echo "  + magic"
                fi
                ;;
            5)
                echo -n "    Tavily API key: "
                read -r KEY
                if [ -n "$KEY" ]; then
                    cat >> "$TEMP_MCPS" << EOF
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": { "TAVILY_API_KEY": "$KEY" }
    },
EOF
                    echo "  + tavily"
                fi
                ;;
            6)
                echo -n "    GitHub token: "
                read -r KEY
                if [ -n "$KEY" ]; then
                    cat >> "$TEMP_MCPS" << EOF
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "$KEY" }
    },
EOF
                    echo "  + github"
                fi
                ;;
            7)
                echo -n "    PostgreSQL URL: "
                read -r KEY
                if [ -n "$KEY" ]; then
                    cat >> "$TEMP_MCPS" << EOF
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "$KEY"]
    },
EOF
                    echo "  + postgres"
                fi
                ;;
            8)
                cat >> "$TEMP_MCPS" << 'EOF'
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
    },
EOF
                echo "  + filesystem"
                ;;
            9)
                cat >> "$TEMP_MCPS" << 'EOF'
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
EOF
                echo "  + memory"
                ;;
            10)
                echo -n "    Firecrawl API key: "
                read -r KEY
                if [ -n "$KEY" ]; then
                    cat >> "$TEMP_MCPS" << EOF
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "$KEY" }
    },
EOF
                    echo "  + firecrawl"
                fi
                ;;
        esac
    done

    # Merge into existing mcp_config.json
    if [ -f "$MCP_FILE" ]; then
        echo ""
        echo "  Existing mcp_config.json found"

        # Check if it has mcpServers
        if grep -q '"mcpServers"' "$MCP_FILE"; then
            # Insert new servers before the closing brace of mcpServers
            # This is a simple approach - for complex merging, use jq
            echo "  Merging new servers into existing config..."

            # Create backup
            cp "$MCP_FILE" "$MCP_FILE.backup"

            # Read new servers content
            NEW_SERVERS=$(cat "$TEMP_MCPS")

            # Use Python for reliable JSON merge (if available)
            if command -v python3 &> /dev/null; then
                python3 << PYEOF
import json
import sys

# Read existing config
with open('$MCP_FILE', 'r') as f:
    try:
        config = json.load(f)
    except:
        config = {"mcpServers": {}}

if "mcpServers" not in config:
    config["mcpServers"] = {}

# New servers to add
new_servers = """$NEW_SERVERS"""

# Parse each server block (simple parsing)
import re
for match in re.finditer(r'"([^"]+)":\s*\{([^}]+)\}', new_servers):
    name = match.group(1)
    if name not in config["mcpServers"]:
        # Parse the server config
        block = match.group(0)
        try:
            server_json = "{" + block + "}"
            server = json.loads(server_json)
            config["mcpServers"][name] = server[name]
            print(f"  Added: {name}")
        except:
            pass

# Write back
with open('$MCP_FILE', 'w') as f:
    json.dump(config, f, indent=2)
PYEOF
            else
                echo "  Python not found - creating new config"
                cat > "$MCP_FILE" << EOF
{
  "mcpServers": {
$(cat "$TEMP_MCPS" | sed '$ s/,$//')
  }
}
EOF
            fi
        else
            echo "  Invalid config format - creating new"
            cat > "$MCP_FILE" << EOF
{
  "mcpServers": {
$(cat "$TEMP_MCPS" | sed '$ s/,$//')
  }
}
EOF
        fi
    else
        echo "  Creating new mcp_config.json"
        cat > "$MCP_FILE" << EOF
{
  "mcpServers": {
$(cat "$TEMP_MCPS" | sed '$ s/,$//')
  }
}
EOF
    fi

    rm -f "$TEMP_MCPS"
fi

# ============================================
# COPY WORKFLOWS (without overwriting)
# ============================================
echo ""
echo -e "${YELLOW}Installing workflows...${NC}"

for workflow in "$SCRIPT_DIR/global_workflows"/*.md; do
    if [ -f "$workflow" ]; then
        name=$(basename "$workflow")
        target="$ANTIGRAVITY_DIR/global_workflows/$name"

        if [ -f "$target" ]; then
            echo "  /${name%.md} (exists, skipped)"
        else
            cp "$workflow" "$target"
            echo "  /${name%.md} (added)"
        fi
    fi
done

# ============================================
# COPY RULES (without overwriting)
# ============================================
echo -e "${YELLOW}Installing rules...${NC}"

for rule in "$SCRIPT_DIR/rules"/*.md; do
    if [ -f "$rule" ]; then
        name=$(basename "$rule")
        target="$ANTIGRAVITY_DIR/rules/$name"

        if [ -f "$target" ]; then
            echo "  $name (exists, skipped)"
        else
            cp "$rule" "$target"
            echo "  $name (added)"
        fi
    fi
done

# ============================================
# SUMMARY
# ============================================
echo ""
echo -e "${GREEN}✅ SuperGravity installed!${NC}"
echo ""
echo "Updated files:"
echo "  $GEMINI_DIR/GEMINI.md"
echo "  $ANTIGRAVITY_DIR/mcp_config.json"
echo "  $ANTIGRAVITY_DIR/global_workflows/"
echo "  $ANTIGRAVITY_DIR/rules/"
echo ""
echo -e "${YELLOW}Restart Antigravity IDE to load changes.${NC}"
echo ""
