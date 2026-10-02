"""Bootstrap connection settings: one JSON file, translated into the environment the code already reads.

The Connections panel in the console writes this file; the engine and the API both apply it at start, so a
fresh server launches with nothing configured and is connected afterwards. Secrets live in the file, which the
installer restricts to the service account and administrators (docs/plans/no-hermes-architecture.md, D9).
"""
from __future__ import annotations

import base64
import ctypes
import json
import os
import tempfile
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
    ("gbrain", "url"): "CHITRAGUPTA_GBRAIN_URL",
    ("gbrain", "token"): "CHITRAGUPTA_GBRAIN_TOKEN",
    ("gbrain", "client_id"): "CHITRAGUPTA_GBRAIN_CLIENT_ID",
    ("gbrain", "client_secret"): "CHITRAGUPTA_GBRAIN_CLIENT_SECRET",
    ("gbrain", "home"): "CHITRAGUPTA_GBRAIN_HOME",
    ("gbrain", "bin"): "CHITRAGUPTA_GBRAIN_BIN",
}

SECRETS = {("sql", "password"), ("jev", "api_key"), ("gbrain", "token"), ("gbrain", "client_secret")}
PREFIX = "dpapi:"


def _dpapi(data: bytes, protect: bool) -> bytes:
    """Use Windows' machine-bound DPAPI; the installed SYSTEM/Admin ACL remains mandatory."""
    class Blob(ctypes.Structure):
        _fields_ = [("size", ctypes.c_ulong), ("data", ctypes.c_void_p)]

    buffer = ctypes.create_string_buffer(data)
    source = Blob(len(data), ctypes.cast(buffer, ctypes.c_void_p))
    output = Blob()
    crypt = ctypes.WinDLL("crypt32", use_last_error=True)
    function = crypt.CryptProtectData if protect else crypt.CryptUnprotectData
    function.argtypes = [ctypes.POINTER(Blob), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
                         ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(Blob)]
    function.restype = ctypes.c_int
    if not function(ctypes.byref(source), None, None, None, None, 5 if protect else 1, ctypes.byref(output)):
        raise OSError("Windows could not protect/read Chitragupta credentials")
    try:
        return ctypes.string_at(output.data, output.size)
    finally:
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.LocalFree.argtypes = [ctypes.c_void_p]
        kernel.LocalFree.restype = ctypes.c_void_p
        kernel.LocalFree(output.data)


def unprotect(value: str) -> str:
    if not value.startswith(PREFIX):
        return value
    if os.name != "nt":
        raise OSError("Windows-protected credentials must be configured on this machine")
    return _dpapi(base64.b64decode(value[len(PREFIX):], validate=True), False).decode("utf-8")


def save(settings: dict) -> None:
    """Persist settings atomically; never write plaintext connection secrets on Windows."""
    data = json.loads(json.dumps(settings))
    if os.name == "nt":
        for section, key in SECRETS:
            value = (data.get(section) or {}).get(key)
            if value and not value.startswith(PREFIX):
                data[section][key] = PREFIX + base64.b64encode(_dpapi(value.encode("utf-8"), True)).decode("ascii")
    path = config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=path.name + ".", suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(data, stream, indent=2)
        temporary.replace(path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def data_dir() -> Path:
    """Where the engine keeps logs, traces and its lock: the ProgramData Chitragupta folder on Windows (the installer also sets
    CHITRAGUPTA_DATA machine-wide so the API and the engine agree), ~/.chitragupta elsewhere."""
    if os.environ.get("CHITRAGUPTA_DATA"):
        return Path(os.environ["CHITRAGUPTA_DATA"])
    return Path(os.environ.get("PROGRAMDATA", r"C:\ProgramData")) / "Chitragupta" if os.name == "nt" else Path.home() / ".chitragupta"


def config_path() -> Path:
    return Path(os.environ["CHITRAGUPTA_CONFIG_FILE"]) if os.environ.get("CHITRAGUPTA_CONFIG_FILE") else data_dir() / "chitragupta.json"


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
            os.environ[env] = unprotect(str(value)) if (section, key) in SECRETS else str(value)
        elif key in (data.get(section) or {}):
            os.environ.pop(env, None)
    return mtime
