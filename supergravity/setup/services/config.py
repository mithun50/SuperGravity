"""Configuration service for SuperGravity MCP servers"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any

from supergravity import PACKAGE_DIR
from supergravity.setup.utils.paths import get_mcp_config_path, get_antigravity_dir


class ConfigService:
    """Manages MCP server configurations"""

    # Available MCP servers with metadata
    SERVERS = {
        "context7": {
            "name": "context7",
            "description": "Framework documentation - React, Next.js, Vue, etc.",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@upstash/context7-mcp@latest"]
            }
        },
        "sequential-thinking": {
            "name": "sequential-thinking",
            "description": "Complex multi-step reasoning",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
            }
        },
        "magic": {
            "name": "magic",
            "description": "UI component generation from 21st.dev",
            "requires_key": True,
            "key_name": "TWENTYFIRST_API_KEY",
            "config": {
                "command": "npx",
                "args": ["-y", "@21st-dev/magic@latest"],
                "env": {"TWENTYFIRST_API_KEY": ""}
            }
        },
        "playwright": {
            "name": "playwright",
            "description": "Browser automation and E2E testing",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@playwright/mcp@latest"]
            }
        },
        "tavily": {
            "name": "tavily",
            "description": "Web search for research",
            "requires_key": True,
            "key_name": "TAVILY_API_KEY",
            "config": {
                "command": "npx",
                "args": ["-y", "tavily-mcp@latest"],
                "env": {"TAVILY_API_KEY": ""}
            }
        },
        "firecrawl": {
            "name": "firecrawl",
            "description": "Web scraping and content extraction",
            "requires_key": True,
            "key_name": "FIRECRAWL_API_KEY",
            "config": {
                "command": "npx",
                "args": ["-y", "firecrawl-mcp"],
                "env": {"FIRECRAWL_API_KEY": ""}
            }
        },
        "postgres": {
            "name": "postgres",
            "description": "PostgreSQL database operations",
            "requires_key": True,
            "key_name": "POSTGRES_URL",
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
            }
        },
        "filesystem": {
            "name": "filesystem",
            "description": "File system operations",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
            }
        },
        "memory": {
            "name": "memory",
            "description": "Persistent memory across sessions",
            "requires_key": False,
            "config": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-memory"]
            }
        },
        "github": {
            "name": "github",
            "description": "GitHub operations - PRs, issues, repos",
            "requires_key": True,
            "key_name": "GITHUB_PERSONAL_ACCESS_TOKEN",
            "config": {
                "command": "docker",
                "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
                "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": ""}
            }
        }
    }

    def __init__(self):
        self.config_path = get_mcp_config_path()

    def get_available_servers(self) -> List[Dict[str, Any]]:
        """Get list of available MCP servers"""
        return [
            {
                "name": server["name"],
                "description": server["description"],
                "requires_key": server.get("requires_key", False),
            }
            for server in self.SERVERS.values()
        ]

    def get_installed_servers(self) -> List[str]:
        """Get list of installed MCP servers"""
        if not self.config_path.exists():
            return []

        with open(self.config_path) as f:
            config = json.load(f)

        return list(config.get("mcpServers", {}).keys())

    def add_server(
        self,
        server_name: str,
        api_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Add an MCP server to configuration

        Args:
            server_name: Name of the server to add
            api_key: Optional API key for the server

        Returns:
            Dict with success status
        """
        if server_name not in self.SERVERS:
            return {
                "success": False,
                "error": f"Unknown server: {server_name}. Available: {', '.join(self.SERVERS.keys())}"
            }

        server = self.SERVERS[server_name]

        # Check if API key is required
        if server.get("requires_key") and not api_key:
            return {
                "success": False,
                "error": f"Server {server_name} requires API key ({server.get('key_name')})"
            }

        # Load or create config
        if self.config_path.exists():
            with open(self.config_path) as f:
                config = json.load(f)
        else:
            config = {"mcpServers": {}}

        if "mcpServers" not in config:
            config["mcpServers"] = {}

        # Add server config
        server_config = server["config"].copy()

        # Set API key if provided
        if api_key and "env" in server_config:
            key_name = server.get("key_name")
            if key_name:
                server_config["env"][key_name] = api_key

        config["mcpServers"][server_name] = server_config

        # Ensure directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        # Write config
        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=2)

        return {"success": True}

    def remove_server(self, server_name: str) -> Dict[str, Any]:
        """
        Remove an MCP server from configuration

        Args:
            server_name: Name of the server to remove

        Returns:
            Dict with success status
        """
        if not self.config_path.exists():
            return {"success": False, "error": "No MCP configuration found"}

        with open(self.config_path) as f:
            config = json.load(f)

        if server_name not in config.get("mcpServers", {}):
            return {"success": False, "error": f"Server {server_name} not installed"}

        del config["mcpServers"][server_name]

        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=2)

        return {"success": True}

    def add_server_config(self, server_name: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a server with a pre-built config

        Args:
            server_name: Name of the server
            config: Server configuration dict

        Returns:
            Dict with success status
        """
        # Load or create config file
        if self.config_path.exists():
            with open(self.config_path) as f:
                mcp_config = json.load(f)
        else:
            mcp_config = {"mcpServers": {}}

        if "mcpServers" not in mcp_config:
            mcp_config["mcpServers"] = {}

        # Add or update server config
        mcp_config["mcpServers"][server_name] = config

        # Ensure directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        # Write config
        with open(self.config_path, "w") as f:
            json.dump(mcp_config, f, indent=2)

        return {"success": True}

    def update_api_key(self, server_name: str, api_key: str) -> Dict[str, Any]:
        """
        Update API key for an installed MCP server

        Args:
            server_name: Name of the server
            api_key: New API key

        Returns:
            Dict with success status
        """
        if not self.config_path.exists():
            return {"success": False, "error": "No MCP configuration found"}

        with open(self.config_path) as f:
            config = json.load(f)

        if server_name not in config.get("mcpServers", {}):
            return {"success": False, "error": f"Server {server_name} not installed"}

        server_meta = self.SERVERS.get(server_name, {})
        key_name = server_meta.get("key_name")

        if not key_name:
            return {"success": False, "error": f"Server {server_name} doesn't use API keys"}

        if "env" not in config["mcpServers"][server_name]:
            config["mcpServers"][server_name]["env"] = {}

        config["mcpServers"][server_name]["env"][key_name] = api_key

        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=2)

        return {"success": True}
