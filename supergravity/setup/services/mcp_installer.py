"""MCP Server Installation Service - Robust MCP management with registry"""

import json
import subprocess
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any

from rich.console import Console

from supergravity.setup.services.mcp_registry import MCPRegistry
from supergravity.setup.utils.paths import get_mcp_config_path, get_antigravity_dir

console = Console()


class MCPInstallerService:
    """Handles installation, update, and management of MCP server packages"""

    # MCP Server definitions with installation details
    SERVERS = {
        "context7": {
            "name": "context7",
            "description": "Framework documentation - React, Next.js, Vue, etc.",
            "package": "@upstash/context7-mcp",
            "version": "latest",
            "type": "npm",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@upstash/context7-mcp@latest"]
            }
        },
        "sequential-thinking": {
            "name": "sequential-thinking",
            "description": "Complex multi-step reasoning",
            "package": "@modelcontextprotocol/server-sequential-thinking",
            "version": "latest",
            "type": "npm",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
            }
        },
        "magic": {
            "name": "magic",
            "description": "UI component generation from 21st.dev",
            "package": "@21st-dev/magic",
            "version": "latest",
            "type": "npm",
            "requires_key": True,
            "key_name": "TWENTYFIRST_API_KEY",
            "key_url": "https://21st.dev",
            "config": {
                "command": "npx",
                "args": ["-y", "@21st-dev/magic@latest"],
                "env": {"TWENTYFIRST_API_KEY": ""}
            }
        },
        "playwright": {
            "name": "playwright",
            "description": "Browser automation and E2E testing",
            "package": "@playwright/mcp",
            "version": "latest",
            "type": "npm",
            "requires_key": False,
            "post_install": ["npx", "playwright", "install", "chromium"],
            "config": {
                "command": "npx",
                "args": ["-y", "@playwright/mcp@latest"]
            }
        },
        "tavily": {
            "name": "tavily",
            "description": "Web search for research",
            "package": "tavily-mcp",
            "version": "latest",
            "type": "npm",
            "requires_key": True,
            "key_name": "TAVILY_API_KEY",
            "key_url": "https://tavily.com",
            "config": {
                "command": "npx",
                "args": ["-y", "tavily-mcp@latest"],
                "env": {"TAVILY_API_KEY": ""}
            }
        },
        "firecrawl": {
            "name": "firecrawl",
            "description": "Web scraping and content extraction",
            "package": "firecrawl-mcp",
            "version": "latest",
            "type": "npm",
            "requires_key": True,
            "key_name": "FIRECRAWL_API_KEY",
            "key_url": "https://firecrawl.dev",
            "config": {
                "command": "npx",
                "args": ["-y", "firecrawl-mcp"],
                "env": {"FIRECRAWL_API_KEY": ""}
            }
        },
        "postgres": {
            "name": "postgres",
            "description": "PostgreSQL database operations",
            "package": "@modelcontextprotocol/server-postgres",
            "version": "latest",
            "type": "npm",
            "requires_key": True,
            "key_name": "POSTGRES_URL",
            "key_example": "postgresql://user:pass@localhost:5432/dbname",
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-postgres"]
            }
        },
        "filesystem": {
            "name": "filesystem",
            "description": "File system operations",
            "package": "@modelcontextprotocol/server-filesystem",
            "version": "latest",
            "type": "npm",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem"]
            }
        },
        "memory": {
            "name": "memory",
            "description": "Persistent memory across sessions",
            "package": "@modelcontextprotocol/server-memory",
            "version": "latest",
            "type": "npm",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-memory"]
            }
        },
        "github": {
            "name": "github",
            "description": "GitHub operations - PRs, issues, repos",
            "package": "ghcr.io/github/github-mcp-server",
            "version": "latest",
            "type": "docker",
            "requires_key": True,
            "key_name": "GITHUB_PERSONAL_ACCESS_TOKEN",
            "key_url": "https://github.com/settings/tokens",
            "config": {
                "command": "docker",
                "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
                "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": ""}
            }
        }
    }

    def __init__(self):
        self.npm_available = self._check_command("npm")
        self.npx_available = self._check_command("npx")
        self.docker_available = self._check_command("docker")
        self.registry = MCPRegistry()
        self.config_path = get_mcp_config_path()

    def _check_command(self, cmd: str) -> bool:
        """Check if a command is available"""
        return shutil.which(cmd) is not None

    def check_prerequisites(self) -> Dict[str, Any]:
        """Check system prerequisites for MCP installation"""
        results = {
            "npm": self.npm_available,
            "npx": self.npx_available,
            "docker": self.docker_available,
            "node_version": None,
            "issues": []
        }

        if not self.npm_available and not self.npx_available:
            results["issues"].append("Node.js/npm not found. Install from https://nodejs.org")

        if self.npm_available:
            try:
                result = subprocess.run(
                    ["node", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                results["node_version"] = result.stdout.strip()
            except Exception:
                pass

        return results

    def is_installed(self, server_name: str) -> Dict[str, Any]:
        """
        Check if a server is installed (in registry and config)

        Returns detailed status
        """
        in_registry = self.registry.is_installed(server_name)
        in_config = False

        if self.config_path.exists():
            with open(self.config_path) as f:
                config = json.load(f)
            in_config = server_name in config.get("mcpServers", {})

        return {
            "installed": in_registry or in_config,
            "in_registry": in_registry,
            "in_config": in_config,
            "status": self._get_install_status(in_registry, in_config),
            "registry_info": self.registry.get_server_status(server_name)
        }

    def _get_install_status(self, in_registry: bool, in_config: bool) -> str:
        """Get human-readable installation status"""
        if in_registry and in_config:
            return "installed"
        elif in_registry and not in_config:
            return "registry_only"
        elif not in_registry and in_config:
            return "config_only"
        else:
            return "not_installed"

    def install_server(
        self,
        server_name: str,
        api_key: Optional[str] = None,
        install_package: bool = True,
        force: bool = False,
        verbose: bool = True
    ) -> Dict[str, Any]:
        """
        Install an MCP server

        Args:
            server_name: Name of the server to install
            api_key: Optional API key
            install_package: Whether to actually install the npm package
            force: Force reinstall even if already installed
            verbose: Show progress output

        Returns:
            Dict with success status and details
        """
        if server_name not in self.SERVERS:
            return {
                "success": False,
                "error": f"Unknown server: {server_name}",
                "available": list(self.SERVERS.keys())
            }

        server = self.SERVERS[server_name]

        # Check if already installed
        install_status = self.is_installed(server_name)
        if install_status["installed"] and not force:
            if install_status["status"] == "installed":
                return {
                    "success": True,
                    "action": "already_installed",
                    "message": f"{server_name} is already installed",
                    "server": server_name,
                    "config": self._get_existing_config(server_name)
                }
            elif install_status["status"] == "config_only":
                # In config but not registry - add to registry
                if verbose:
                    console.print(f"  [dim]Found in config, adding to registry[/dim]")
                existing_config = self._get_existing_config(server_name)
                self.registry.register_server(
                    server_name,
                    existing_config,
                    package=server["package"],
                    server_type=server["type"]
                )
                return {
                    "success": True,
                    "action": "registered",
                    "message": f"{server_name} registered from existing config",
                    "server": server_name,
                    "config": existing_config
                }

        # Check if API key is required
        if server.get("requires_key") and not api_key:
            # Check if we have an existing key
            existing_key = self._get_existing_api_key(server_name, server.get("key_name"))
            if existing_key:
                api_key = existing_key
                if verbose:
                    console.print(f"  [dim]Using existing API key[/dim]")
            else:
                key_info = f"Get key from: {server.get('key_url', 'provider website')}"
                if server.get("key_example"):
                    key_info += f"\nExample: {server['key_example']}"
                return {
                    "success": False,
                    "error": f"API key required ({server.get('key_name')})",
                    "key_info": key_info,
                    "key_name": server.get("key_name")
                }

        # Check prerequisites
        if server["type"] == "npm" and not self.npx_available:
            return {
                "success": False,
                "error": "npx not found. Install Node.js from https://nodejs.org"
            }

        if server["type"] == "docker" and not self.docker_available:
            return {
                "success": False,
                "error": "Docker not found. Install from https://docker.com"
            }

        result = {"success": True, "server": server_name, "steps": [], "action": "installed"}

        # Install the package if requested
        if install_package and server["type"] == "npm":
            install_result = self._install_npm_package(server["package"], server.get("version", "latest"), verbose)
            result["steps"].append(install_result)

            if not install_result["success"]:
                result["success"] = False
                result["error"] = install_result.get("error", "Package installation failed")
                return result

        # Pull docker image if needed
        if install_package and server["type"] == "docker":
            pull_result = self._pull_docker_image(server["package"], verbose)
            result["steps"].append(pull_result)

            if not pull_result["success"]:
                result["success"] = False
                result["error"] = pull_result.get("error", "Docker pull failed")
                return result

        # Run post-install commands if any
        if install_package and server.get("post_install"):
            post_result = self._run_post_install(server["post_install"], verbose)
            result["steps"].append(post_result)

        # Generate config
        config = self._build_config(server, api_key)

        # Register in registry
        reg_result = self.registry.register_server(
            server_name,
            config,
            package=server["package"],
            server_type=server["type"],
            verified=install_package
        )
        result["registry"] = reg_result

        result["config"] = config
        result["message"] = f"{server_name} installed successfully"
        return result

    def _build_config(self, server: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        """Build the config for a server"""
        config = {}
        config["command"] = server["config"]["command"]
        config["args"] = server["config"]["args"].copy()

        if api_key:
            key_name = server.get("key_name")

            # For postgres, add URL to args
            if server["name"] == "postgres":
                config["args"].append(api_key)
            elif key_name:
                config["env"] = {key_name: api_key}

        # For filesystem, add home directory
        if server["name"] == "filesystem":
            config["args"].append(str(Path.home()))

        return config

    def _get_existing_config(self, server_name: str) -> Optional[Dict[str, Any]]:
        """Get existing config for a server"""
        if not self.config_path.exists():
            return None

        with open(self.config_path) as f:
            config = json.load(f)

        return config.get("mcpServers", {}).get(server_name)

    def _get_existing_api_key(self, server_name: str, key_name: str) -> Optional[str]:
        """Get existing API key from config"""
        config = self._get_existing_config(server_name)
        if config and key_name:
            env = config.get("env", {})
            key = env.get(key_name, "")
            if key:
                return key
        return None

    def update_server(
        self,
        server_name: str,
        verbose: bool = True
    ) -> Dict[str, Any]:
        """
        Update an installed MCP server to latest version

        Args:
            server_name: Name of the server to update
            verbose: Show progress output

        Returns:
            Dict with update result
        """
        if server_name not in self.SERVERS:
            return {
                "success": False,
                "error": f"Unknown server: {server_name}"
            }

        install_status = self.is_installed(server_name)
        if not install_status["installed"]:
            return {
                "success": False,
                "error": f"{server_name} is not installed"
            }

        server = self.SERVERS[server_name]

        if verbose:
            console.print(f"  [dim]Updating {server_name}...[/dim]")

        if server["type"] == "npm":
            # Clear npx cache and reinstall
            result = self._install_npm_package(
                server["package"],
                "latest",
                verbose,
                force_update=True
            )
        elif server["type"] == "docker":
            result = self._pull_docker_image(server["package"], verbose)
        else:
            return {"success": False, "error": "Unknown server type"}

        if result["success"]:
            # Update registry
            existing_config = self._get_existing_config(server_name) or server["config"]
            self.registry.register_server(
                server_name,
                existing_config,
                package=server["package"],
                server_type=server["type"],
                verified=True
            )

        return {
            "success": result["success"],
            "server": server_name,
            "action": "updated" if result["success"] else "failed",
            "message": result.get("message", result.get("error", ""))
        }

    def update_all_servers(self, verbose: bool = True) -> Dict[str, Any]:
        """Update all installed MCP servers"""
        installed = self.registry.get_installed_names()

        if not installed:
            return {
                "success": True,
                "message": "No servers to update",
                "updated": [],
                "failed": []
            }

        updated = []
        failed = []

        for server_name in installed:
            if verbose:
                console.print(f"\n[blue]Updating {server_name}...[/blue]")

            result = self.update_server(server_name, verbose)

            if result["success"]:
                updated.append(server_name)
            else:
                failed.append({"server": server_name, "error": result.get("error")})

        return {
            "success": len(failed) == 0,
            "updated": updated,
            "failed": failed,
            "message": f"Updated {len(updated)}, failed {len(failed)}"
        }

    def _install_npm_package(
        self,
        package: str,
        version: str = "latest",
        verbose: bool = True,
        force_update: bool = False
    ) -> Dict[str, Any]:
        """Install or update an npm package"""
        full_package = f"{package}@{version}" if version else package

        if verbose:
            console.print(f"  [dim]{'Updating' if force_update else 'Installing'}: {full_package}[/dim]")

        try:
            # Use npx to download/cache the package
            cmd = ["npx", "-y"]
            if force_update:
                cmd.append("--force")
            cmd.append(full_package)
            cmd.append("--help")

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=180
            )

            return {
                "success": True,
                "action": "npm_install",
                "package": full_package,
                "message": f"Package {full_package} ready"
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "action": "npm_install",
                "package": full_package,
                "error": "Installation timed out"
            }
        except Exception as e:
            return {
                "success": False,
                "action": "npm_install",
                "package": full_package,
                "error": str(e)
            }

    def _pull_docker_image(self, image: str, verbose: bool = True) -> Dict[str, Any]:
        """Pull a Docker image"""
        if verbose:
            console.print(f"  [dim]Pulling Docker image: {image}[/dim]")

        try:
            result = subprocess.run(
                ["docker", "pull", image],
                capture_output=True,
                text=True,
                timeout=300
            )

            if result.returncode == 0:
                return {
                    "success": True,
                    "action": "docker_pull",
                    "image": image,
                    "message": f"Image {image} pulled successfully"
                }
            else:
                return {
                    "success": False,
                    "action": "docker_pull",
                    "image": image,
                    "error": result.stderr
                }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "action": "docker_pull",
                "image": image,
                "error": "Pull timed out"
            }
        except Exception as e:
            return {
                "success": False,
                "action": "docker_pull",
                "image": image,
                "error": str(e)
            }

    def _run_post_install(self, command: List[str], verbose: bool = True) -> Dict[str, Any]:
        """Run post-installation commands"""
        if verbose:
            console.print(f"  [dim]Running: {' '.join(command)}[/dim]")

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=300
            )

            return {
                "success": result.returncode == 0,
                "action": "post_install",
                "command": command,
                "output": result.stdout if result.returncode == 0 else result.stderr
            }

        except Exception as e:
            return {
                "success": False,
                "action": "post_install",
                "command": command,
                "error": str(e)
            }

    def verify_server(self, server_name: str) -> Dict[str, Any]:
        """Verify an MCP server is working"""
        if server_name not in self.SERVERS:
            return {"success": False, "error": f"Unknown server: {server_name}"}

        server = self.SERVERS[server_name]

        if server["type"] == "npm":
            try:
                package = server["package"]
                result = subprocess.run(
                    ["npx", "-y", package, "--help"],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                success = result.returncode == 0
                if success:
                    self.registry.mark_verified(server_name, True)

                return {
                    "success": success,
                    "server": server_name,
                    "type": "npm",
                    "package": server["package"]
                }
            except Exception as e:
                return {
                    "success": False,
                    "server": server_name,
                    "error": str(e)
                }

        elif server["type"] == "docker":
            try:
                result = subprocess.run(
                    ["docker", "images", "-q", server["package"]],
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                success = bool(result.stdout.strip())
                if success:
                    self.registry.mark_verified(server_name, True)

                return {
                    "success": success,
                    "server": server_name,
                    "type": "docker",
                    "image": server["package"],
                    "error": None if success else "Docker image not found"
                }
            except Exception as e:
                return {
                    "success": False,
                    "server": server_name,
                    "error": str(e)
                }

        return {"success": False, "error": "Unknown server type"}

    def remove_server(self, server_name: str) -> Dict[str, Any]:
        """Remove a server from registry and config"""
        # Remove from registry
        self.registry.unregister_server(server_name)

        # Remove from config
        if self.config_path.exists():
            with open(self.config_path) as f:
                config = json.load(f)

            if server_name in config.get("mcpServers", {}):
                del config["mcpServers"][server_name]

                with open(self.config_path, "w") as f:
                    json.dump(config, f, indent=2)

        return {
            "success": True,
            "server": server_name,
            "message": f"{server_name} removed"
        }

    def sync_config(self) -> Dict[str, Any]:
        """Sync registry with config file"""
        return self.registry.sync_with_config(self.config_path)

    def repair_registry(self) -> Dict[str, Any]:
        """Repair registry from config file"""
        return self.registry.repair_from_config(self.config_path)

    def get_server_info(self, server_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a server"""
        return self.SERVERS.get(server_name)

    def list_servers(self) -> List[Dict[str, Any]]:
        """List all available servers with their status"""
        servers = []
        for s in self.SERVERS.values():
            status = self.is_installed(s["name"])
            servers.append({
                "name": s["name"],
                "description": s["description"],
                "type": s["type"],
                "package": s["package"],
                "requires_key": s.get("requires_key", False),
                "key_name": s.get("key_name"),
                "key_url": s.get("key_url"),
                "installed": status["installed"],
                "status": status["status"]
            })
        return servers
