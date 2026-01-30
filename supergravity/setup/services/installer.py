"""Installer service for SuperGravity"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any

from supergravity import PACKAGE_DIR
from supergravity.setup.utils.paths import (
    get_gemini_dir,
    get_antigravity_dir,
    get_workflows_dir,
    get_rules_dir,
    get_mcp_config_path,
    ensure_dirs,
)


class InstallerService:
    """Handles SuperGravity installation, update, and uninstallation"""

    SUPERGRAVITY_MARKER = "# SuperGravity Framework"

    def __init__(self):
        self.package_dir = PACKAGE_DIR
        self.source_workflows = self.package_dir.parent / "global_workflows"
        self.source_rules = self.package_dir.parent / "rules"
        self.source_mcp_config = self.package_dir.parent / "mcp_config.json"

    def install(
        self,
        force: bool = False,
        mcp_servers: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Install SuperGravity to Antigravity IDE

        Args:
            force: Overwrite existing files
            mcp_servers: List of MCP servers to install (None = all)

        Returns:
            Dict with success status and details
        """
        try:
            # Ensure directories exist
            ensure_dirs()

            # Install GEMINI.md section
            self._install_gemini_md(force)

            # Install workflows
            self._install_workflows(force)

            # Install rules
            self._install_rules(force)

            # Install MCP configuration
            self._install_mcp_config(mcp_servers, force)

            return {
                "success": True,
                "install_path": str(get_antigravity_dir()),
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }

    def _install_gemini_md(self, force: bool = False):
        """Install or update GEMINI.md"""
        gemini_md = get_gemini_dir() / "GEMINI.md"

        supergravity_section = '''
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
'''

        if gemini_md.exists():
            content = gemini_md.read_text()

            if self.SUPERGRAVITY_MARKER in content:
                if force:
                    # Remove old section and add new
                    lines = content.split("\n")
                    new_lines = []
                    skip = False

                    for line in lines:
                        if line.startswith(self.SUPERGRAVITY_MARKER):
                            skip = True
                            continue
                        if skip and line.startswith("# ") and "SuperGravity" not in line:
                            skip = False
                        if not skip:
                            new_lines.append(line)

                    content = "\n".join(new_lines).rstrip()
                    content += "\n" + supergravity_section
                    gemini_md.write_text(content)
                # else: already installed, skip
            else:
                # Append section
                content = content.rstrip() + "\n" + supergravity_section
                gemini_md.write_text(content)
        else:
            # Create new file
            gemini_md.write_text(supergravity_section.lstrip())

    def _install_workflows(self, force: bool = False):
        """Install workflow files"""
        target_dir = get_workflows_dir()
        target_dir.mkdir(parents=True, exist_ok=True)

        if not self.source_workflows.exists():
            return

        for workflow in self.source_workflows.glob("*.md"):
            target = target_dir / workflow.name

            if target.exists() and not force:
                continue

            shutil.copy2(workflow, target)

    def _install_rules(self, force: bool = False):
        """Install rule files"""
        target_dir = get_rules_dir()
        target_dir.mkdir(parents=True, exist_ok=True)

        if not self.source_rules.exists():
            return

        for rule in self.source_rules.glob("*.md"):
            target = target_dir / rule.name

            if target.exists() and not force:
                continue

            shutil.copy2(rule, target)

    def _install_mcp_config(
        self,
        servers: Optional[List[str]] = None,
        force: bool = False
    ):
        """Install MCP configuration"""
        target = get_mcp_config_path()

        if not self.source_mcp_config.exists():
            return

        # Load source config
        with open(self.source_mcp_config) as f:
            source_config = json.load(f)

        # Filter servers if specified
        if servers:
            filtered = {}
            for name, config in source_config.get("mcpServers", {}).items():
                if name in servers:
                    filtered[name] = config
            source_config["mcpServers"] = filtered

        if target.exists() and not force:
            # Merge with existing
            with open(target) as f:
                existing = json.load(f)

            if "mcpServers" not in existing:
                existing["mcpServers"] = {}

            for name, config in source_config.get("mcpServers", {}).items():
                if name not in existing["mcpServers"]:
                    existing["mcpServers"][name] = config

            with open(target, "w") as f:
                json.dump(existing, f, indent=2)
        else:
            # Write new config
            with open(target, "w") as f:
                json.dump(source_config, f, indent=2)

    def uninstall(self, keep_config: bool = False) -> Dict[str, Any]:
        """
        Remove SuperGravity from Antigravity IDE

        Args:
            keep_config: Keep MCP configuration

        Returns:
            Dict with success status
        """
        try:
            # Remove SuperGravity section from GEMINI.md
            gemini_md = get_gemini_dir() / "GEMINI.md"
            if gemini_md.exists():
                content = gemini_md.read_text()
                if self.SUPERGRAVITY_MARKER in content:
                    lines = content.split("\n")
                    new_lines = []
                    skip = False

                    for line in lines:
                        if line.startswith(self.SUPERGRAVITY_MARKER):
                            skip = True
                            continue
                        if skip and line.startswith("# ") and "SuperGravity" not in line:
                            skip = False
                        if not skip:
                            new_lines.append(line)

                    gemini_md.write_text("\n".join(new_lines).rstrip())

            # Remove workflows
            workflows_dir = get_workflows_dir()
            if workflows_dir.exists():
                for f in workflows_dir.glob("*.md"):
                    f.unlink()

            # Remove rules
            rules_dir = get_rules_dir()
            if rules_dir.exists():
                for f in rules_dir.glob("*.md"):
                    f.unlink()

            # Optionally remove MCP config
            if not keep_config:
                mcp_config = get_mcp_config_path()
                if mcp_config.exists():
                    mcp_config.unlink()

            return {"success": True}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def update(self) -> Dict[str, Any]:
        """Update SuperGravity installation"""
        return self.install(force=True)
