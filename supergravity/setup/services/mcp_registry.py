"""MCP Server Registry - Manages installed MCP servers with state tracking"""

import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

from supergravity.setup.utils.paths import get_antigravity_dir


class MCPRegistry:
    """
    Registry for tracking installed MCP servers

    Tracks:
    - Installation status
    - Configuration checksums
    - Installation timestamps
    - Version information
    """

    REGISTRY_FILE = "mcp_registry.json"

    def __init__(self):
        self.registry_path = get_antigravity_dir() / self.REGISTRY_FILE
        self._registry = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        """Load the registry from disk"""
        if self.registry_path.exists():
            try:
                with open(self.registry_path) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._create_empty_registry()
        return self._create_empty_registry()

    def _create_empty_registry(self) -> Dict[str, Any]:
        """Create an empty registry structure"""
        return {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "servers": {}
        }

    def _save_registry(self):
        """Save the registry to disk"""
        self._registry["updated_at"] = datetime.now().isoformat()
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.registry_path, "w") as f:
            json.dump(self._registry, f, indent=2)

    def _config_checksum(self, config: Dict[str, Any]) -> str:
        """Generate a checksum for a config"""
        config_str = json.dumps(config, sort_keys=True)
        return hashlib.md5(config_str.encode()).hexdigest()[:8]

    def is_installed(self, server_name: str) -> bool:
        """Check if a server is installed"""
        return server_name in self._registry.get("servers", {})

    def get_server_status(self, server_name: str) -> Optional[Dict[str, Any]]:
        """Get the status of an installed server"""
        return self._registry.get("servers", {}).get(server_name)

    def register_server(
        self,
        server_name: str,
        config: Dict[str, Any],
        package: str,
        server_type: str,
        verified: bool = False
    ) -> Dict[str, Any]:
        """
        Register a server installation

        Args:
            server_name: Name of the server
            config: Server configuration
            package: Package name/image
            server_type: 'npm' or 'docker'
            verified: Whether the installation was verified

        Returns:
            Dict with registration result
        """
        existing = self.get_server_status(server_name)
        new_checksum = self._config_checksum(config)

        if existing:
            # Server already exists - check if config changed
            if existing.get("config_checksum") == new_checksum:
                return {
                    "action": "unchanged",
                    "message": f"{server_name} already installed with same config",
                    "server": server_name
                }
            else:
                # Config changed - update
                action = "updated"
        else:
            action = "installed"

        self._registry["servers"][server_name] = {
            "installed_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "package": package,
            "type": server_type,
            "config_checksum": new_checksum,
            "verified": verified,
            "config": config
        }

        self._save_registry()

        return {
            "action": action,
            "message": f"{server_name} {action} successfully",
            "server": server_name,
            "checksum": new_checksum
        }

    def unregister_server(self, server_name: str) -> Dict[str, Any]:
        """Remove a server from the registry"""
        if server_name not in self._registry.get("servers", {}):
            return {
                "success": False,
                "error": f"{server_name} not found in registry"
            }

        del self._registry["servers"][server_name]
        self._save_registry()

        return {
            "success": True,
            "message": f"{server_name} removed from registry"
        }

    def mark_verified(self, server_name: str, verified: bool = True) -> bool:
        """Mark a server as verified or not"""
        if server_name in self._registry.get("servers", {}):
            self._registry["servers"][server_name]["verified"] = verified
            self._registry["servers"][server_name]["verified_at"] = datetime.now().isoformat()
            self._save_registry()
            return True
        return False

    def get_all_servers(self) -> Dict[str, Dict[str, Any]]:
        """Get all registered servers"""
        return self._registry.get("servers", {})

    def get_installed_names(self) -> List[str]:
        """Get list of installed server names"""
        return list(self._registry.get("servers", {}).keys())

    def get_unverified_servers(self) -> List[str]:
        """Get servers that haven't been verified"""
        return [
            name for name, info in self._registry.get("servers", {}).items()
            if not info.get("verified", False)
        ]

    def has_api_key(self, server_name: str) -> bool:
        """Check if a server has an API key configured"""
        server = self.get_server_status(server_name)
        if not server:
            return False

        config = server.get("config", {})
        env = config.get("env", {})

        # Check if any env value is non-empty
        return any(v for v in env.values() if v)

    def get_servers_needing_keys(self) -> List[str]:
        """Get servers that need API keys but don't have them"""
        result = []
        for name, info in self._registry.get("servers", {}).items():
            config = info.get("config", {})
            env = config.get("env", {})
            # Has env section but values are empty
            if env and not any(v for v in env.values() if v):
                result.append(name)
        return result

    def export_config(self) -> Dict[str, Any]:
        """Export all server configs for mcp_config.json"""
        configs = {}
        for name, info in self._registry.get("servers", {}).items():
            configs[name] = info.get("config", {})
        return configs

    def sync_with_config(self, mcp_config_path: Path) -> Dict[str, Any]:
        """
        Sync registry with actual mcp_config.json

        Returns info about any discrepancies
        """
        if not mcp_config_path.exists():
            return {"in_sync": True, "config_exists": False}

        with open(mcp_config_path) as f:
            file_config = json.load(f)

        file_servers = set(file_config.get("mcpServers", {}).keys())
        registry_servers = set(self.get_installed_names())

        return {
            "in_sync": file_servers == registry_servers,
            "config_exists": True,
            "in_config_only": list(file_servers - registry_servers),
            "in_registry_only": list(registry_servers - file_servers),
            "both": list(file_servers & registry_servers)
        }

    def repair_from_config(self, mcp_config_path: Path) -> Dict[str, Any]:
        """
        Repair registry from mcp_config.json

        Adds servers that exist in config but not registry
        """
        if not mcp_config_path.exists():
            return {"success": False, "error": "Config file not found"}

        with open(mcp_config_path) as f:
            file_config = json.load(f)

        added = []
        for name, config in file_config.get("mcpServers", {}).items():
            if not self.is_installed(name):
                # Determine type from config
                cmd = config.get("command", "")
                server_type = "docker" if "docker" in cmd else "npm"

                # Get package from args
                args = config.get("args", [])
                package = next(
                    (a for a in args if not a.startswith("-")),
                    "unknown"
                )

                self.register_server(
                    name,
                    config,
                    package=package,
                    server_type=server_type,
                    verified=False
                )
                added.append(name)

        return {
            "success": True,
            "added": added,
            "message": f"Added {len(added)} servers to registry"
        }
