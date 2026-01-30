"""
SuperGravity - Framework for Google Antigravity IDE

A comprehensive framework providing workflows, rules, and MCP configurations
for enhanced development with Google Antigravity IDE.
"""

__version__ = "1.0.0"
__author__ = "Mithun"
__license__ = "MIT"

from pathlib import Path

# Package paths
PACKAGE_DIR = Path(__file__).parent
DATA_DIR = PACKAGE_DIR / "data"
SUPERGRAVITY_DIR = PACKAGE_DIR / "SuperGravity"

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "PACKAGE_DIR",
    "DATA_DIR",
    "SUPERGRAVITY_DIR",
]
