"""Tests for installer service"""

import pytest
from pathlib import Path
from supergravity.setup.services.installer import InstallerService


def test_installer_init():
    """Test installer initialization"""
    installer = InstallerService()
    assert installer is not None


def test_get_available_servers():
    """Test getting available MCP servers"""
    from supergravity.setup.services.config import ConfigService
    config = ConfigService()
    servers = config.get_available_servers()
    assert len(servers) > 0
    assert any(s["name"] == "context7" for s in servers)
