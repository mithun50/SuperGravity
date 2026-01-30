"""Path utilities for SuperGravity"""

import os
import platform
from pathlib import Path


def get_gemini_dir() -> Path:
    """Get the Gemini configuration directory path"""
    system = platform.system()

    if system == "Windows":
        base = os.environ.get("USERPROFILE", os.path.expanduser("~"))
    else:
        base = os.environ.get("HOME", os.path.expanduser("~"))

    return Path(base) / ".gemini"


def get_antigravity_dir() -> Path:
    """Get the Antigravity configuration directory path"""
    return get_gemini_dir() / "antigravity"


def get_workflows_dir() -> Path:
    """Get the global workflows directory path"""
    return get_antigravity_dir() / "global_workflows"


def get_skills_dir() -> Path:
    """Get the global skills directory path"""
    return get_antigravity_dir() / "skills"


def get_mcp_config_path() -> Path:
    """Get the MCP configuration file path"""
    return get_antigravity_dir() / "mcp_config.json"


def ensure_dirs():
    """Ensure all required directories exist"""
    dirs = [
        get_gemini_dir(),
        get_antigravity_dir(),
        get_workflows_dir(),
        get_skills_dir(),
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    return dirs
