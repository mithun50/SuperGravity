# Changelog

All notable changes to SuperGravity will be documented in this file.

## [1.0.0] - 2026-01-30

### Added

#### Core Features
- **SuperGravity Framework** - Complete framework for Google Antigravity IDE
- **9 Workflows** - scaffold, implement, security, test, deploy, review, document, refactor, debug
- **3 Rule Sets** - supergravity core rules, security guidelines, code quality standards
- **PyPI Package** - Install via `pip install supergravity`

#### CLI Tool
- `supergravity install` - Install to Antigravity IDE
- `supergravity uninstall` - Remove SuperGravity
- `supergravity update` - Update workflows and rules
- `supergravity status` - Check installation status

#### MCP Management
- **10 MCP Servers** - context7, sequential-thinking, magic, playwright, tavily, firecrawl, postgres, filesystem, memory, github
- **MCP Registry** - Tracks installed servers with checksums
- `supergravity mcp list` - List available servers
- `supergravity mcp add` - Install MCP servers
- `supergravity mcp remove` - Remove MCP servers
- `supergravity mcp update` - Update to latest versions
- `supergravity mcp verify` - Verify servers work
- `supergravity mcp sync` - Sync registry with config
- `supergravity mcp prereq` - Check prerequisites

#### MCP Packages (Validated)
- context7: `@upstash/context7-mcp`
- sequential-thinking: `@modelcontextprotocol/server-sequential-thinking`
- magic: `@21st-dev/magic`
- playwright: `@playwright/mcp`
- tavily: `tavily-mcp`
- firecrawl: `firecrawl-mcp`
- postgres: `@modelcontextprotocol/server-postgres`
- filesystem: `@modelcontextprotocol/server-filesystem`
- memory: `@modelcontextprotocol/server-memory`
- github: `ghcr.io/github/github-mcp-server`

#### Documentation
- Comprehensive README with CLI reference
- MCP server documentation in SuperGravity/MCP/
- Agent profiles in SuperGravity/Agents/
- Command references in SuperGravity/Commands/
- Mode definitions in SuperGravity/Modes/

### Technical Details
- Python 3.8+ support
- Cross-platform (macOS, Linux, Windows)
- Interactive CLI with rich formatting
- Config merge (APPEND mode, not replace)
- Registry-based tracking with checksums
