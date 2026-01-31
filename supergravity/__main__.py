#!/usr/bin/env python3
"""
SuperGravity CLI - Command-line interface for SuperGravity framework

Usage:
    supergravity install    Install SuperGravity to Antigravity IDE
    supergravity uninstall  Remove SuperGravity from Antigravity IDE
    supergravity update     Update SuperGravity installation
    supergravity status     Check installation status
    supergravity mcp        Manage MCP server configurations
"""

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm

from supergravity import __version__
from supergravity.setup.services.installer import InstallerService
from supergravity.setup.services.config import ConfigService
from supergravity.setup.services.mcp_installer import MCPInstallerService
from supergravity.setup.utils.paths import get_gemini_dir, get_antigravity_dir, get_skills_dir, get_mcp_config_path

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="SuperGravity")
def main():
    """SuperGravity - Framework for Google Antigravity IDE"""
    pass


@main.command()
@click.option("--force", "-f", is_flag=True, help="Force overwrite existing files")
@click.option("--mcp", "-m", multiple=True, help="MCP servers to install (e.g., -m context7 -m playwright)")
@click.option("--skip-mcp-install", is_flag=True, help="Skip npm/docker package installation")
def install(force: bool, mcp: tuple, skip_mcp_install: bool):
    """Install SuperGravity to Antigravity IDE"""
    console.print(Panel.fit(
        "[bold blue]SuperGravity Installer[/bold blue]\n"
        "Framework for Google Antigravity IDE",
        border_style="blue"
    ))

    installer = InstallerService()

    try:
        result = installer.install(force=force, mcp_servers=list(mcp) if mcp else None)

        if result["success"]:
            console.print("\n[bold green]Installation successful![/bold green]")
            console.print(f"\nInstalled to: {result['install_path']}")

            # Offer to install MCP packages
            if not skip_mcp_install:
                console.print("\n[yellow]MCP Server Setup[/yellow]")
                if Confirm.ask("Install MCP server packages now?", default=True):
                    _interactive_mcp_setup()

            console.print("\n[yellow]Restart Antigravity IDE to load changes.[/yellow]")
        else:
            console.print(f"\n[bold red]Installation failed:[/bold red] {result['error']}")
            sys.exit(1)

    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        sys.exit(1)


def _parse_selection(selection: str, max_count: int) -> list:
    """
    Parse user selection for MCP servers.

    Supports:
    - Space-separated: "1 2 3"
    - Comma-separated: "1,2,3" or "1, 2, 3"
    - Ranges: "1-3" or "1-3, 5"
    - Mixed: "1, 2-4, 6"

    Returns list of 0-indexed integers.
    """
    import re

    indices = set()

    # Normalize: replace commas with spaces
    normalized = selection.replace(",", " ")

    # Split on whitespace
    parts = normalized.split()

    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Check for range (e.g., "1-3")
        if "-" in part and not part.startswith("-"):
            range_match = re.match(r"(\d+)-(\d+)", part)
            if range_match:
                start, end = int(range_match.group(1)), int(range_match.group(2))
                for i in range(start, end + 1):
                    if 1 <= i <= max_count:
                        indices.add(i - 1)  # Convert to 0-indexed
            else:
                raise ValueError(f"Invalid range: {part}")
        else:
            # Single number
            num = int(part)
            if 1 <= num <= max_count:
                indices.add(num - 1)  # Convert to 0-indexed
            else:
                raise ValueError(f"Number {num} out of range (1-{max_count})")

    return sorted(list(indices))


def _interactive_mcp_setup():
    """Interactive MCP server setup"""
    mcp_installer = MCPInstallerService()
    config_service = ConfigService()

    # Check prerequisites
    prereqs = mcp_installer.check_prerequisites()
    if prereqs["issues"]:
        console.print("\n[yellow]Prerequisites:[/yellow]")
        for issue in prereqs["issues"]:
            console.print(f"  [red]![/red] {issue}")
        console.print("")

    # Show available servers
    servers = mcp_installer.list_servers()

    console.print("\n[bold]Available MCP Servers:[/bold]")
    console.print("")

    # Group by requires_key
    no_key = [s for s in servers if not s["requires_key"]]
    with_key = [s for s in servers if s["requires_key"]]

    console.print("[green]No API Key Required:[/green]")
    for i, s in enumerate(no_key, 1):
        console.print(f"  {i}. {s['name']:<20} - {s['description']}")

    console.print("\n[yellow]API Key Required:[/yellow]")
    for i, s in enumerate(with_key, len(no_key) + 1):
        key_info = f"({s['key_name']})"
        console.print(f"  {i}. {s['name']:<20} - {s['description']} {key_info}")

    console.print("")

    # Ask which to install
    console.print("[dim]Formats: '1 2 3', '1,2,3', '1-3', 'all', 'skip'[/dim]")
    selection = Prompt.ask(
        "Enter server numbers to install",
        default="all"
    )

    if selection.lower() == "skip":
        return

    if selection.lower() == "all":
        to_install = [s["name"] for s in no_key]
    else:
        try:
            # Parse selection - handle "1 2 3", "1,2,3", "1, 2, 3", "1-3"
            all_servers = no_key + with_key
            indices = _parse_selection(selection, len(all_servers))
            if not indices:
                console.print("[red]Invalid selection[/red]")
                console.print("[dim]Examples: '1 2 3', '1,2,3', '1-3', 'all', 'skip'[/dim]")
                return
            to_install = [all_servers[i]["name"] for i in indices]
        except (ValueError, IndexError) as e:
            console.print(f"[red]Invalid selection:[/red] {e}")
            console.print("[dim]Examples: '1 2 3', '1,2,3', '1-3', 'all', 'skip'[/dim]")
            return

    # Install selected servers
    for server_name in to_install:
        server_info = mcp_installer.get_server_info(server_name)
        api_key = None

        if server_info.get("requires_key"):
            console.print(f"\n[yellow]{server_name} requires {server_info['key_name']}[/yellow]")
            if server_info.get("key_url"):
                console.print(f"  Get key from: {server_info['key_url']}")

            api_key = Prompt.ask(f"  Enter {server_info['key_name']}", default="", show_default=False)
            if not api_key:
                console.print(f"  [dim]Skipping {server_name} (no key provided)[/dim]")
                continue

        console.print(f"\n[blue]Installing {server_name}...[/blue]")

        result = mcp_installer.install_server(
            server_name,
            api_key=api_key,
            install_package=True,
            verbose=True
        )

        if result["success"]:
            # Add to config
            config_service.add_server_config(server_name, result["config"])
            console.print(f"  [green]✓[/green] {server_name} installed")
        else:
            console.print(f"  [red]✗[/red] {server_name}: {result.get('error', 'Failed')}")


@main.command()
@click.option("--keep-config", is_flag=True, help="Keep MCP configuration")
def uninstall(keep_config: bool):
    """Remove SuperGravity from Antigravity IDE"""
    console.print("[yellow]Uninstalling SuperGravity...[/yellow]")

    installer = InstallerService()

    try:
        result = installer.uninstall(keep_config=keep_config)

        if result["success"]:
            console.print("[bold green]Uninstall successful![/bold green]")
        else:
            console.print(f"[bold red]Uninstall failed:[/bold red] {result['error']}")
            sys.exit(1)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)


@main.command()
def update():
    """Update SuperGravity installation"""
    console.print("[yellow]Updating SuperGravity...[/yellow]")

    installer = InstallerService()

    try:
        result = installer.update()

        if result["success"]:
            console.print("[bold green]Update successful![/bold green]")
            if result.get("updated_files"):
                console.print("\nUpdated files:")
                for f in result["updated_files"]:
                    console.print(f"  - {f}")
        else:
            console.print(f"[bold red]Update failed:[/bold red] {result['error']}")
            sys.exit(1)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)


@main.command()
def status():
    """Check installation status"""
    gemini_dir = get_gemini_dir()
    antigravity_dir = get_antigravity_dir()

    table = Table(title="SuperGravity Installation Status")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Path", style="dim")

    # Check GEMINI.md
    gemini_md = gemini_dir / "GEMINI.md"
    if gemini_md.exists():
        content = gemini_md.read_text()
        if "SuperGravity" in content:
            table.add_row("GEMINI.md", "[green]Installed[/green]", str(gemini_md))
        else:
            table.add_row("GEMINI.md", "[yellow]Exists (no SuperGravity)[/yellow]", str(gemini_md))
    else:
        table.add_row("GEMINI.md", "[red]Not found[/red]", str(gemini_md))

    # Check workflows
    workflows_dir = antigravity_dir / "global_workflows"
    if workflows_dir.exists():
        count = len(list(workflows_dir.glob("*.md")))
        table.add_row("Workflows", f"[green]{count} installed[/green]", str(workflows_dir))
    else:
        table.add_row("Workflows", "[red]Not found[/red]", str(workflows_dir))

    # Check skills
    skills_dir = get_skills_dir()
    if skills_dir.exists():
        count = len([d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()])
        table.add_row("Skills", f"[green]{count} installed[/green]", str(skills_dir))
    else:
        table.add_row("Skills", "[red]Not found[/red]", str(skills_dir))

    # Check MCP config
    mcp_config = antigravity_dir / "mcp_config.json"
    if mcp_config.exists():
        import json
        with open(mcp_config) as f:
            config = json.load(f)
        count = len(config.get("mcpServers", {}))
        table.add_row("MCP Config", f"[green]{count} servers[/green]", str(mcp_config))
    else:
        table.add_row("MCP Config", "[red]Not found[/red]", str(mcp_config))

    console.print(table)

    # Check prerequisites
    mcp_installer = MCPInstallerService()
    prereqs = mcp_installer.check_prerequisites()

    console.print("\n[bold]System Prerequisites:[/bold]")
    console.print(f"  npm/npx: {'[green]✓[/green]' if prereqs['npm'] else '[red]✗[/red]'}")
    console.print(f"  Docker:  {'[green]✓[/green]' if prereqs['docker'] else '[yellow]○[/yellow] (optional)'}")
    if prereqs["node_version"]:
        console.print(f"  Node.js: {prereqs['node_version']}")


@main.command()
@click.option("--path", "-p", type=click.Path(), default=".", help="Workspace path (default: current directory)")
@click.option("--rules/--no-rules", default=True, help="Include sample workspace rules")
@click.option("--workflows/--no-workflows", default=True, help="Include sample workspace workflows")
def init(path: str, rules: bool, workflows: bool):
    """Initialize .agent/ workspace structure for Antigravity IDE

    Creates the workspace-level configuration structure:
    - .agent/rules/      - Workspace-specific rules
    - .agent/workflows/  - Workspace-specific workflows
    - .agent/skills/     - Workspace-specific skills
    """
    workspace = Path(path).resolve()
    agent_dir = workspace / ".agent"

    console.print(Panel.fit(
        "[bold blue]Workspace Initialization[/bold blue]\n"
        f"Path: {workspace}",
        border_style="blue"
    ))

    try:
        # Create .agent directory structure
        (agent_dir / "rules").mkdir(parents=True, exist_ok=True)
        (agent_dir / "workflows").mkdir(parents=True, exist_ok=True)
        (agent_dir / "skills").mkdir(parents=True, exist_ok=True)

        created_files = []

        # Create sample workspace rules
        if rules:
            rules_file = agent_dir / "rules" / "workspace.md"
            if not rules_file.exists():
                rules_file.write_text('''# Workspace Rules

> Project-specific rules for this workspace.

## Project Context

- This is a [describe your project]
- Main technologies: [list technologies]
- Follow existing patterns in the codebase

## Code Style

- Follow the established patterns in this codebase
- Use consistent naming conventions
- Add tests for new features

## Important Files

- `src/` - Main source code
- `tests/` - Test files
- Add your key files here
''')
                created_files.append(str(rules_file.relative_to(workspace)))

        # Create sample workspace workflows
        if workflows:
            # Development workflow
            dev_workflow = agent_dir / "workflows" / "dev.md"
            if not dev_workflow.exists():
                dev_workflow.write_text('''---
description: Start development server and watch for changes
---

// turbo-all

1. Install dependencies if node_modules is missing.
   Run `npm install` or `yarn` or `pnpm install`

2. Start the development server.
   Run `npm run dev` or `yarn dev` or `pnpm dev`
''')
                created_files.append(str(dev_workflow.relative_to(workspace)))

            # Build workflow
            build_workflow = agent_dir / "workflows" / "build.md"
            if not build_workflow.exists():
                build_workflow.write_text('''---
description: Build the project for production
---

1. Run linting checks.
// turbo
   Run `npm run lint`

2. Run type checking.
// turbo
   Run `npm run typecheck` or `npx tsc --noEmit`

3. Run tests.
// turbo
   Run `npm test`

4. Build for production.
// turbo
   Run `npm run build`
''')
                created_files.append(str(build_workflow.relative_to(workspace)))

            # PR workflow
            pr_workflow = agent_dir / "workflows" / "pr.md"
            if not pr_workflow.exists():
                pr_workflow.write_text('''---
description: Prepare and create a pull request
---

1. Ask for the PR title and description.

2. Check for uncommitted changes.
   Run `git status`

3. Stage all changes.
// turbo
   Run `git add -A`

4. Create a commit with the changes.
   Run `git commit -m "[commit message]"`

5. Push to the remote branch.
// turbo
   Run `git push -u origin HEAD`

6. Create the pull request.
   Run `gh pr create --title "[title]" --body "[description]"`
''')
                created_files.append(str(pr_workflow.relative_to(workspace)))

        # Success output
        console.print("\n[bold green]Workspace initialized![/bold green]")
        console.print(f"\nCreated: [cyan]{agent_dir.relative_to(workspace)}/[/cyan]")
        console.print("  ├── rules/      - Workspace-specific rules")
        console.print("  ├── workflows/  - Workspace-specific workflows")
        console.print("  └── skills/     - Workspace-specific skills")

        if created_files:
            console.print("\n[dim]Created files:[/dim]")
            for f in created_files:
                console.print(f"  - {f}")

        console.print("\n[yellow]Tip:[/yellow] Edit files in .agent/ to customize for your project.")
        console.print("[yellow]Tip:[/yellow] Use /dev, /build, /pr in Antigravity to trigger workflows.")
        console.print("[yellow]Tip:[/yellow] Add custom skills in .agent/skills/<name>/SKILL.md")

    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        sys.exit(1)


@main.group()
def mcp():
    """Manage MCP server configurations"""
    pass


@mcp.command("list")
@click.option("--installed", "-i", is_flag=True, help="Show only installed servers")
def mcp_list(installed: bool):
    """List available MCP servers"""
    mcp_installer = MCPInstallerService()
    config_service = ConfigService()

    servers = mcp_installer.list_servers()
    installed_servers = config_service.get_installed_servers()

    table = Table(title="MCP Servers")
    table.add_column("Server", style="cyan")
    table.add_column("Type", style="dim")
    table.add_column("Description", style="white")
    table.add_column("API Key", style="yellow")
    table.add_column("Status", style="green")

    for server in servers:
        if installed and server["name"] not in installed_servers:
            continue

        status = "[green]Installed[/green]" if server["name"] in installed_servers else "[dim]Not installed[/dim]"
        key_status = f"[yellow]{server['key_name']}[/yellow]" if server.get("requires_key") else "[green]No[/green]"

        table.add_row(
            server["name"],
            server["type"],
            server["description"],
            key_status,
            status
        )

    console.print(table)


@mcp.command("add")
@click.argument("server_name")
@click.option("--api-key", "-k", help="API key for the server")
@click.option("--no-install", is_flag=True, help="Skip package installation")
def mcp_add(server_name: str, api_key: str, no_install: bool):
    """Add and install an MCP server"""
    mcp_installer = MCPInstallerService()
    config_service = ConfigService()

    server_info = mcp_installer.get_server_info(server_name)
    if not server_info:
        console.print(f"[bold red]Unknown server:[/bold red] {server_name}")
        console.print("\nAvailable servers:")
        for s in mcp_installer.list_servers():
            console.print(f"  - {s['name']}")
        sys.exit(1)

    # Prompt for API key if required and not provided
    if server_info.get("requires_key") and not api_key:
        console.print(f"\n[yellow]{server_name} requires {server_info['key_name']}[/yellow]")
        if server_info.get("key_url"):
            console.print(f"Get key from: {server_info['key_url']}")

        api_key = Prompt.ask(f"Enter {server_info['key_name']}")
        if not api_key:
            console.print("[red]API key is required[/red]")
            sys.exit(1)

    console.print(f"\n[blue]Installing {server_name}...[/blue]")

    # Install the server
    result = mcp_installer.install_server(
        server_name,
        api_key=api_key,
        install_package=not no_install,
        verbose=True
    )

    if result["success"]:
        # Add to config
        config_result = config_service.add_server_config(server_name, result["config"])

        if config_result["success"]:
            console.print(f"\n[bold green]✓ {server_name} installed and configured[/bold green]")

            if result.get("steps"):
                for step in result["steps"]:
                    if step.get("success"):
                        console.print(f"  [dim]{step.get('message', step.get('action'))}[/dim]")
        else:
            console.print(f"\n[yellow]Package installed but config failed:[/yellow] {config_result.get('error')}")
    else:
        console.print(f"\n[bold red]Installation failed:[/bold red] {result.get('error')}")
        if result.get("key_info"):
            console.print(f"\n{result['key_info']}")
        sys.exit(1)


@mcp.command("remove")
@click.argument("server_name")
def mcp_remove(server_name: str):
    """Remove an MCP server from configuration"""
    config_service = ConfigService()

    result = config_service.remove_server(server_name)

    if result["success"]:
        console.print(f"[bold green]Removed {server_name} from MCP configuration[/bold green]")
        console.print("[dim]Note: npm packages are cached and not removed[/dim]")
    else:
        console.print(f"[bold red]Failed:[/bold red] {result['error']}")
        sys.exit(1)


@mcp.command("verify")
@click.argument("server_name", required=False)
def mcp_verify(server_name: str):
    """Verify MCP server installation"""
    mcp_installer = MCPInstallerService()
    config_service = ConfigService()

    if server_name:
        servers_to_check = [server_name]
    else:
        servers_to_check = config_service.get_installed_servers()

    if not servers_to_check:
        console.print("[yellow]No MCP servers installed[/yellow]")
        return

    console.print("[bold]Verifying MCP servers...[/bold]\n")

    for name in servers_to_check:
        result = mcp_installer.verify_server(name)

        if result["success"]:
            console.print(f"  [green]✓[/green] {name} ({result.get('type', 'unknown')})")
        else:
            console.print(f"  [red]✗[/red] {name}: {result.get('error', 'verification failed')}")


@mcp.command("setup")
def mcp_setup():
    """Interactive MCP server setup"""
    _interactive_mcp_setup()


@mcp.command("prereq")
def mcp_prereq():
    """Check MCP prerequisites"""
    mcp_installer = MCPInstallerService()
    prereqs = mcp_installer.check_prerequisites()

    console.print("[bold]MCP Prerequisites Check[/bold]\n")

    table = Table()
    table.add_column("Requirement", style="cyan")
    table.add_column("Status")
    table.add_column("Notes", style="dim")

    table.add_row(
        "Node.js/npm",
        "[green]✓ Installed[/green]" if prereqs["npm"] else "[red]✗ Missing[/red]",
        prereqs.get("node_version", "https://nodejs.org")
    )

    table.add_row(
        "npx",
        "[green]✓ Available[/green]" if prereqs["npx"] else "[red]✗ Missing[/red]",
        "Comes with npm"
    )

    table.add_row(
        "Docker",
        "[green]✓ Installed[/green]" if prereqs["docker"] else "[yellow]○ Optional[/yellow]",
        "Required for GitHub MCP"
    )

    console.print(table)

    if prereqs["issues"]:
        console.print("\n[yellow]Issues:[/yellow]")
        for issue in prereqs["issues"]:
            console.print(f"  • {issue}")


@mcp.command("update")
@click.argument("server_name", required=False)
@click.option("--all", "-a", "update_all", is_flag=True, help="Update all installed servers")
def mcp_update(server_name: str, update_all: bool):
    """Update MCP server(s) to latest version"""
    mcp_installer = MCPInstallerService()

    if update_all or not server_name:
        console.print("[bold]Updating all MCP servers...[/bold]")
        result = mcp_installer.update_all_servers(verbose=True)

        if result["updated"]:
            console.print(f"\n[green]Updated:[/green] {', '.join(result['updated'])}")
        if result["failed"]:
            console.print(f"\n[red]Failed:[/red]")
            for f in result["failed"]:
                console.print(f"  - {f['server']}: {f['error']}")

        if not result["updated"] and not result["failed"]:
            console.print("[yellow]No servers to update[/yellow]")
    else:
        console.print(f"[blue]Updating {server_name}...[/blue]")
        result = mcp_installer.update_server(server_name, verbose=True)

        if result["success"]:
            console.print(f"\n[bold green]✓ {server_name} updated[/bold green]")
        else:
            console.print(f"\n[bold red]Failed:[/bold red] {result.get('error')}")
            sys.exit(1)


@mcp.command("sync")
def mcp_sync():
    """Sync MCP registry with config file"""
    mcp_installer = MCPInstallerService()

    console.print("[bold]Syncing MCP registry...[/bold]\n")

    sync_result = mcp_installer.sync_config()

    if sync_result["in_sync"]:
        console.print("[green]✓ Registry and config are in sync[/green]")
    else:
        if sync_result.get("in_config_only"):
            console.print(f"[yellow]In config only:[/yellow] {', '.join(sync_result['in_config_only'])}")
        if sync_result.get("in_registry_only"):
            console.print(f"[yellow]In registry only:[/yellow] {', '.join(sync_result['in_registry_only'])}")

        if Confirm.ask("Repair registry from config?", default=True):
            repair_result = mcp_installer.repair_registry()
            if repair_result["success"]:
                console.print(f"[green]✓ Added to registry:[/green] {', '.join(repair_result.get('added', []))}")
            else:
                console.print(f"[red]Repair failed:[/red] {repair_result.get('error')}")


@mcp.command("registry")
def mcp_registry():
    """Show MCP registry status"""
    mcp_installer = MCPInstallerService()

    registry = mcp_installer.registry.get_all_servers()

    if not registry:
        console.print("[yellow]No servers in registry[/yellow]")
        console.print("\nRun [cyan]supergravity mcp sync[/cyan] to import from config")
        return

    table = Table(title="MCP Registry")
    table.add_column("Server", style="cyan")
    table.add_column("Type", style="dim")
    table.add_column("Package", style="white")
    table.add_column("Verified", style="green")
    table.add_column("Installed", style="dim")

    for name, info in registry.items():
        table.add_row(
            name,
            info.get("type", "unknown"),
            info.get("package", "unknown"),
            "[green]✓[/green]" if info.get("verified") else "[yellow]○[/yellow]",
            info.get("installed_at", "unknown")[:10] if info.get("installed_at") else "unknown"
        )

    console.print(table)


if __name__ == "__main__":
    main()
