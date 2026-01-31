"""
SuperGravity - Framework for Google Antigravity IDE

A comprehensive framework providing workflows, rules, and MCP configurations
for enhanced development with Google Antigravity IDE.
"""

__version__ = "1.0.0"
__author__ = "Mithun Gowda B"
__email__ = "mithungowda.b7411@gmail.com"
__license__ = "MIT"

from pathlib import Path

# Package paths
PACKAGE_DIR = Path(__file__).parent
WORKFLOWS_DIR = PACKAGE_DIR / "global_workflows"
RULES_DIR = PACKAGE_DIR / "rules"
MCP_CONFIG = PACKAGE_DIR / "mcp_config.json"

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "PACKAGE_DIR",
    "WORKFLOWS_DIR",
    "RULES_DIR",
    "MCP_CONFIG",
]
