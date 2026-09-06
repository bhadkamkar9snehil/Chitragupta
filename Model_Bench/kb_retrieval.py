#!/usr/bin/env python3
"""Thin Windows↔WSL bridge for dispatch-time GBrain retrieval."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any


def _wsl_path(path: Path) -> str:
    value = str(path.resolve())
    match = re.match(r"^([A-Za-z]):\\(.*)$", value)
    if not match:
        return value.replace("\\", "/")
    return f"/mnt/{match.group(1).lower()}/{match.group(2).replace(chr(92), '/')}"


def _empty(reason: str | None = None) -> dict[str, Any]:
    return {
        "backend": "gbrain",
        "retrieval_degraded": bool(reason),
        "degradation_reason": reason,
        "trusted": [],
        "cases": [],
    }


def _search(query: str, top: int) -> dict[str, Any]:
    from l2_gbrain import available, search

    if not available():
        return _empty("gbrain is not installed or not on PATH")

    trusted = search(query, scope="trusted", limit=top)
    cases = search(query, scope="cases", limit=min(2, top))
    failures = [
        str(result.get("error") or "")
        for result in (trusted, cases)
        if not result.get("ok")
    ]
    return {
        "backend": "gbrain",
        "retrieval_degraded": bool(failures),
        "degradation_reason": "; ".join(filter(None, failures)) or None,
        "trusted": trusted.get("results") if trusted.get("ok") else [],
        "cases": cases.get("results") if cases.get("ok") else [],
        "note": "Reference/history only; current-ticket claims require live xstudio_l2 evidence.",
    }


def _proxy_to_wsl(args: argparse.Namespace) -> dict[str, Any] | None:
    if os.name != "nt" or args.wsl_inner:
        return None
    cmd = [
        "wsl",
        "-d",
        os.environ.get("CHITRAGUPTA_WSL_DISTRO", "Ubuntu"),
        "--",
        "python3",
        _wsl_path(Path(__file__)),
        "--query",
        args.query,
        "--top",
        str(args.top),
        "--wsl-inner",
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return _empty(f"WSL GBrain bridge unavailable: {type(exc).__name__}: {exc}")
    if proc.returncode:
        return _empty(
            (proc.stderr or proc.stdout).strip()[-500:]
            or f"WSL retrieval exited {proc.returncode}"
        )
    try:
        value = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return _empty("WSL retrieval returned invalid JSON")
    return value if isinstance(value, dict) else _empty("WSL retrieval returned a non-object")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top", type=int, default=3)
    # Accepted for compatibility with the dispatcher transport; unused here.
    for flag in ("server", "database", "username", "password"):
        parser.add_argument(f"--{flag}", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--wsl-inner", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    query = " ".join(args.query.split())
    result = (
        _empty()
        if not query
        else (_proxy_to_wsl(args) or _search(query, max(1, min(5, args.top))))
    )
    if not query:
        result["note"] = "No requester-grounded retrieval query was available."

    print(json.dumps(result, ensure_ascii=False, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
