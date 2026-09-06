#!/usr/bin/env python3
"""Thin GBrain retrieval bridge for the Chitragupta L2 dispatcher.

Hermes remains the agent harness. This module only bridges the Windows-hosted
Helpdesk dispatcher to the isolated GBrain running in WSL and returns a small,
trust-scoped set of retrieval leads for the investigator task body.
"""
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


def _search(query: str, top: int) -> dict[str, Any]:
    from l2_gbrain import available, search

    if not available():
        return {
            "backend": "gbrain",
            "retrieval_degraded": True,
            "degradation_reason": "gbrain is not installed or not on PATH",
            "trusted": [],
            "cases": [],
        }

    trusted = search(query, scope="trusted", limit=top, automatic=True)
    cases = search(query, scope="cases", limit=min(2, top), automatic=True)
    degraded = not trusted.get("ok") or not cases.get("ok")
    reasons = [
        str(result.get("error") or "")
        for result in (trusted, cases)
        if not result.get("ok") and result.get("error")
    ]
    return {
        "backend": "gbrain",
        "retrieval_degraded": degraded,
        "degradation_reason": "; ".join(reasons) if reasons else None,
        "trusted": trusted.get("results") if trusted.get("ok") else [],
        "cases": cases.get("results") if cases.get("ok") else [],
        "note": "Retrieved material is guidance/history only; current-ticket claims require live xstudio_l2 evidence.",
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
        return {
            "backend": "gbrain",
            "retrieval_degraded": True,
            "degradation_reason": f"WSL GBrain bridge unavailable: {type(exc).__name__}: {exc}",
            "trusted": [],
            "cases": [],
        }
    if proc.returncode != 0:
        return {
            "backend": "gbrain",
            "retrieval_degraded": True,
            "degradation_reason": (proc.stderr or proc.stdout).strip()[-500:] or f"WSL retrieval exited {proc.returncode}",
            "trusted": [],
            "cases": [],
        }
    try:
        value = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            "backend": "gbrain",
            "retrieval_degraded": True,
            "degradation_reason": "WSL retrieval returned invalid JSON",
            "trusted": [],
            "cases": [],
        }
    return value if isinstance(value, dict) else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top", type=int, default=3)
    # The dispatcher still supplies its standard SQL transport arguments. They are
    # accepted here only so retrieval remains decoupled from that transport.
    for flag in ("server", "database", "username", "password"):
        parser.add_argument(f"--{flag}", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--wsl-inner", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    query = " ".join(args.query.split())
    if not query:
        result = {
            "backend": "gbrain",
            "retrieval_degraded": False,
            "trusted": [],
            "cases": [],
            "note": "No requester-grounded retrieval query was available.",
        }
    else:
        result = _proxy_to_wsl(args) or _search(query, max(1, min(5, args.top)))

    print(json.dumps(result, ensure_ascii=False, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
