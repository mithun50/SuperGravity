# Changelog

All notable changes to SuperGravity will be documented in this file.

## [1.1.0] - 2026-01-30

### Added

#### GitHub Actions CI/CD
- **`.github/workflows/publish.yml`** - Automatic PyPI publishing on GitHub releases
- **`.github/workflows/test.yml`** - Cross-platform testing (Windows, macOS, Linux) with Python 3.8-3.12
- Uses PyPI Trusted Publishing (no API token needed)

#### Documentation
- Windows usage instructions in README and docs
- Interactive MCP setup selection format documentation
- Contributing/publishing guide in README

### Fixed

#### MCP Interactive Setup
- Fixed number selection parsing to support multiple formats:
  - Space-separated: `1 2 3`
  - Comma-separated: `1,2,3` or `1, 2, 3`
  - Ranges: `1-3`
  - Mixed: `1, 3-5, 7`
- Better error messages with format examples

#### Package Configuration
- Fixed `MANIFEST.in` to include correct package data paths
- Fixed `pyproject.toml` package-data configuration
- Updated path constants in `__init__.py`

---

## [1.0.0] - 2026-01-30

### Added

#### Workspace Initialization
- **`supergravity init`** - Initialize `.agent/` workspace structure
- Creates `.agent/rules/`, `.agent/workflows/`, and `.agent/skills/` directories
- Generates sample workspace rules and workflows:
  - `.agent/rules/workspace.md` - Project-specific rules
  - `.agent/workflows/dev.md` - Start dev server
  - `.agent/workflows/build.md` - Build project
  - `.agent/workflows/pr.md` - Create pull request
- Ready for custom workspace-level skills

#### Skills System
- **12 AI Skills** installed to `~/.gemini/antigravity/skills/`
- Skills activate on-demand based on user request
- Includes: fullstack-architect, security-engineer, test-engineer, database-expert, etc.
- Skills use SKILL.md format with Goal, Instructions, Examples, Constraints sections

#### Documentation
- **docs/skills.md** - Complete skills guide (NEW)
- **docs/workflows.md** - Complete workflow guide
- **docs/mcp-servers.md** - MCP server setup and usage
- **docs/configuration.md** - Configuration reference
- **docs/customization.md** - Creating custom workflows and rules

### Changed

#### Workflow Format (Breaking)
- Updated to Antigravity-compatible format
- Changed frontmatter from `name:` + `description:` to `description:` only
- Added numbered step format (1. 2. 3.)
- Added `// turbo` annotations for auto-execution

#### Rules Integration
- Rules now integrated directly into GEMINI.md
- Removed separate `rules/` directory (non-standard location)
- Includes: Core rules, Code standards, Security rules, Git safety

#### MCP Configuration
- Cleaned `mcp_config.json` format
- Removed `$schema` and `description` fields
- Now uses standard Antigravity format: `command`, `args`, `env` only

### Fixed
- Workflow frontmatter format (removed `name:` field)
- MCP config extra fields removed
- Status command no longer references removed rules directory

---

## [1.0.0] - 2026-01-30

### Added

#### Core Features
- **SuperGravity Framework** - Complete framework for Google Antigravity IDE
- **9 Workflows** - scaffold, implement, security, test, deploy, review, document, refactor, debug
- **Integrated Rules** - Code quality and security guidelines in GEMINI.md
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
- docs/ folder with detailed guides

### Technical Details
- Python 3.8+ support
- Cross-platform (macOS, Linux, Windows)
- Interactive CLI with rich formatting
- Config merge (APPEND mode, not replace)
- Registry-based tracking with checksums
