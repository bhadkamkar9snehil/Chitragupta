"""Bootstrap connection settings: one JSON file, translated into the environment the code already reads.

The Connections panel in the console writes this file; the engine and the API both apply it at start, so a
fresh server launches with nothing configured and is connected afterwards. Secrets live in the file, which the
installer restricts to the service account and administrators (docs/plans/no-hermes-architecture.md, D9).
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Optional

# (section, key) -> environment variable the existing code reads
ENV = {
    ("sql", "server"): "MSSQL_MCP_SERVER",
    ("sql", "user"): "MSSQL_MCP_USER",
    ("sql", "password"): "MSSQL_MCP_PASSWORD",
    ("lm_studio", "base_url"): "LMSTUDIO_BASE_URL",
    ("jev", "api_key"): "TYPESAFE_API_KEY",
    ("jev", "base_url"): "TYPESAFE_BASE_URL",
    ("gbrain", "home"): "CHITRAGUPTA_GBRAIN_HOME",
    ("gbrain", "bin"): "CHITRAGUPTA_GBRAIN_BIN",
}


def config_path() -> Path:
    if os.environ.get("CHITRAGUPTA_CONFIG_FILE"):
        return Path(os.environ["CHITRAGUPTA_CONFIG_FILE"])
    base = Path(os.environ.get("PROGRAMDATA", r"C:\ProgramData")) / "Chitragupta" if os.name == "nt" else Path.home() / ".chitragupta"
    return base / "chitragupta.json"


def apply() -> Optional[float]:
    """Export the file's values (a missing file is fine: first run). Returns its mtime, for change detection."""
    path = config_path()
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        mtime = path.stat().st_mtime
    except (OSError, ValueError):
        return None
    for (section, key), env in ENV.items():
        value = (data.get(section) or {}).get(key)
        if value not in (None, ""):
            os.environ[env] = str(value)
    return mtime
