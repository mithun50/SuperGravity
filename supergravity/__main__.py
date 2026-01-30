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

from supergravity import __version__
from supergravity.setup.services.installer import InstallerService
from supergravity.setup.services.config import ConfigService
from supergravity.setup.utils.paths import get_gemini_dir, get_antigravity_dir

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="SuperGravity")
def main():
    """SuperGravity - Framework for Google Antigravity IDE"""
    pass


@main.command()
@click.option("--force", "-f", is_flag=True, help="Force overwrite existing files")
@click.option("--mcp", "-m", multiple=True, help="MCP servers to install (e.g., -m context7 -m playwright)")
def install(force: bool, mcp: tuple):
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
            console.print("\n[yellow]Restart Antigravity IDE to load changes.[/yellow]")
        else:
            console.print(f"\n[bold red]Installation failed:[/bold red] {result['error']}")
            sys.exit(1)

    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        sys.exit(1)


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

    # Check rules
    rules_dir = antigravity_dir / "rules"
    if rules_dir.exists():
        count = len(list(rules_dir.glob("*.md")))
        table.add_row("Rules", f"[green]{count} installed[/green]", str(rules_dir))
    else:
        table.add_row("Rules", "[red]Not found[/red]", str(rules_dir))

    # Check MCP config
    mcp_config = antigravity_dir / "mcp_config.json"
    if mcp_config.exists():
        table.add_row("MCP Config", "[green]Installed[/green]", str(mcp_config))
    else:
        table.add_row("MCP Config", "[red]Not found[/red]", str(mcp_config))

    console.print(table)


@main.group()
def mcp():
    """Manage MCP server configurations"""
    pass


@mcp.command("list")
def mcp_list():
    """List available MCP servers"""
    config_service = ConfigService()
    servers = config_service.get_available_servers()

    table = Table(title="Available MCP Servers")
    table.add_column("Server", style="cyan")
    table.add_column("Description", style="white")
    table.add_column("Requires API Key", style="yellow")

    for server in servers:
        table.add_row(
            server["name"],
            server["description"],
            "[yellow]Yes[/yellow]" if server.get("requires_key") else "[green]No[/green]"
        )

    console.print(table)


@mcp.command("add")
@click.argument("server_name")
@click.option("--api-key", "-k", help="API key for the server")
def mcp_add(server_name: str, api_key: str):
    """Add an MCP server to configuration"""
    config_service = ConfigService()

    try:
        result = config_service.add_server(server_name, api_key=api_key)

        if result["success"]:
            console.print(f"[bold green]Added {server_name} to MCP configuration[/bold green]")
        else:
            console.print(f"[bold red]Failed:[/bold red] {result['error']}")
            sys.exit(1)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)


@mcp.command("remove")
@click.argument("server_name")
def mcp_remove(server_name: str):
    """Remove an MCP server from configuration"""
    config_service = ConfigService()

    try:
        result = config_service.remove_server(server_name)

        if result["success"]:
            console.print(f"[bold green]Removed {server_name} from MCP configuration[/bold green]")
        else:
            console.print(f"[bold red]Failed:[/bold red] {result['error']}")
            sys.exit(1)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
