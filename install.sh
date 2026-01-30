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
echo "  1. context7           - Framework documentation"
echo "  2. sequential-thinking - Complex reasoning"
echo "  3. playwright         - Browser testing"
echo "  4. magic              - UI components (needs API key)"
echo "  5. tavily             - Web search (needs API key)"
echo "  6. github             - GitHub ops (needs token)"
echo "  7. postgres           - Database (needs URL)"
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
      "args": ["-y", "@context7/mcp"]
    },
EOF
                echo "  + context7"
                ;;
            2)
                cat >> "$TEMP_MCPS" << 'EOF'
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-sequential-thinking"]
    },
EOF
                echo "  + sequential-thinking"
                ;;
            3)
                cat >> "$TEMP_MCPS" << 'EOF'
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-playwright"]
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
      "args": ["-y", "@21st/magic-mcp"],
      "env": { "TWENTY_FIRST_API_KEY": "$KEY" }
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
      "args": ["-y", "@anthropic/mcp-tavily"],
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
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-github"],
      "env": { "GITHUB_TOKEN": "$KEY" }
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
      "args": ["-y", "@anthropic/mcp-postgres"],
      "env": { "POSTGRES_URL": "$KEY" }
    },
EOF
                    echo "  + postgres"
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
