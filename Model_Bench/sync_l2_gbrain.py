#!/usr/bin/env python3
"""Synchronize Chitragupta's trust-separated learning corpus into GBrain.

The learning vault remains source material. GBrain is disposable derivative
state. Each trust lane is a non-federated source and every read names its source.

The vault gets local-only Git checkpoints because GBrain path sources reconcile
from Git state. No remote is created or pushed. `--watch` is the single freshness
loop used by the deployed user service; it does not participate in ticket
lifecycle correctness.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import subprocess
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from l2_gbrain import SOURCE_DIRS, available, run, vault_path

GIT_TIMEOUT = 30
DEFAULT_INTERVAL = 900


def _git(vault: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(vault), *args],
        capture_output=True,
        text=True,
        timeout=GIT_TIMEOUT,
    )


@contextmanager
def _sync_lock(vault: Path) -> Iterator[bool]:
    vault.mkdir(parents=True, exist_ok=True)
    path = vault / ".gbrain-sync.lock"
    with path.open("a+", encoding="utf-8") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            yield False
            return
        try:
            yield True
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _ensure_local_git(vault: Path) -> None:
    vault.mkdir(parents=True, exist_ok=True)
    if not (vault / ".git").exists():
        proc = _git(vault, ["init"])
        if proc.returncode != 0:
            raise RuntimeError((proc.stderr or proc.stdout).strip())
    for key, value in (("user.name", "Chitragupta Learning Plane"),
                       ("user.email", "chitragupta-learning@local.invalid")):
        proc = _git(vault, ["config", key, value])
        if proc.returncode != 0:
            raise RuntimeError((proc.stderr or proc.stdout).strip())


def _checkpoint(vault: Path) -> bool:
    _ensure_local_git(vault)
    add = _git(vault, ["add", "-A"])
    if add.returncode != 0:
        raise RuntimeError((add.stderr or add.stdout).strip())
    diff = _git(vault, ["diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        return False
    if diff.returncode != 1:
        raise RuntimeError((diff.stderr or diff.stdout).strip())
    message = "learning checkpoint " + datetime.now(timezone.utc).isoformat()
    commit = _git(vault, ["commit", "-m", message, "--no-gpg-sign"])
    if commit.returncode != 0:
        raise RuntimeError((commit.stderr or commit.stdout).strip())
    return True


def _sources_list() -> list[dict[str, Any]]:
    rc, out, err = run(["sources", "list", "--json"])
    if rc != 0:
        raise RuntimeError((err or out).strip() or "gbrain sources list failed")
    data = json.loads(out or "[]")
    rows = data.get("sources") or data.get("results") or [] if isinstance(data, dict) else data
    return [row for row in rows if isinstance(row, dict)]


def _source_id(row: dict[str, Any]) -> str:
    return str(row.get("id") or row.get("source_id") or "")


def _source_config(row: dict[str, Any]) -> dict[str, Any]:
    config = row.get("config")
    if isinstance(config, dict):
        return config
    if isinstance(config, str):
        try:
            parsed = json.loads(config)
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}
    return {}


def _is_federated(row: dict[str, Any]) -> bool:
    if "federated" in row:
        return bool(row.get("federated"))
    return bool(_source_config(row).get("federated"))


def _registered_path(row: dict[str, Any]) -> str:
    return str(row.get("local_path") or row.get("path") or _source_config(row).get("local_path") or "")


def _register_missing(vault: Path, existing: dict[str, dict[str, Any]]) -> list[str]:
    created: list[str] = []
    for source_id, rel in SOURCE_DIRS.items():
        path = vault / rel
        path.mkdir(parents=True, exist_ok=True)
        if source_id in existing:
            continue
        rc, out, err = run([
            "sources", "add", source_id,
            "--path", str(path),
            "--no-federated",
            "--force",
        ])
        if rc != 0:
            raise RuntimeError((err or out).strip() or f"failed to register {source_id}")
        created.append(source_id)
    return created


def _sync_sources() -> list[str]:
    synced: list[str] = []
    for source_id in SOURCE_DIRS:
        rc, out, err = run(["sync", "--source", source_id])
        if rc != 0:
            raise RuntimeError((err or out).strip() or f"failed to sync {source_id}")
        synced.append(source_id)
    return synced


def _check_sources(vault: Path) -> list[str]:
    rows = _sources_list()
    by_id = {_source_id(row): row for row in rows}
    errors: list[str] = []
    for source_id, rel in SOURCE_DIRS.items():
        expected = (vault / rel).resolve()
        row = by_id.get(source_id)
        if row is None:
            errors.append(f"missing GBrain source: {source_id}")
            continue
        if _is_federated(row):
            errors.append(f"GBrain source must be non-federated: {source_id}")
        registered = _registered_path(row)
        if registered:
            try:
                if Path(registered).expanduser().resolve() != expected:
                    errors.append(f"GBrain source path mismatch for {source_id}: {registered} != {expected}")
            except Exception:
                errors.append(f"invalid GBrain source path for {source_id}: {registered}")
        if not expected.is_dir():
            errors.append(f"missing vault source directory: {rel}")
    return errors


def _embed_stale() -> None:
    # GBrain documents bare `embed --stale` as safe on keyless brains: it exits
    # cleanly and leaves keyword search available.
    rc, out, err = run(["embed", "--stale"], timeout=300)
    if rc != 0:
        raise RuntimeError((err or out).strip() or "gbrain embed --stale failed")


def sync_gbrain(vault: Path, *, embed: bool = True) -> dict[str, Any]:
    if not available():
        return {"ok": False, "errors": ["gbrain is not installed"]}
    with _sync_lock(vault) as acquired:
        if not acquired:
            return {"ok": True, "skipped": "sync_already_running", "errors": []}
        checkpointed = _checkpoint(vault)
        rows = _sources_list()
        existing = {_source_id(row): row for row in rows}
        created = _register_missing(vault, existing)
        errors = _check_sources(vault)
        if errors:
            return {"ok": False, "checkpointed": checkpointed, "created": created, "errors": errors}
        synced = _sync_sources()
        if embed:
            _embed_stale()
        return {
            "ok": True,
            "checkpointed": checkpointed,
            "created": created,
            "synced": synced,
            "embedded": embed,
            "errors": [],
        }


def _watch(vault: Path, interval: int, *, embed: bool) -> int:
    delay = max(60, interval)
    while True:
        try:
            result = sync_gbrain(vault, embed=embed)
            print(json.dumps(result, ensure_ascii=False), flush=True)
        except Exception as exc:
            print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), flush=True)
        time.sleep(delay)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--no-embed", action="store_true")
    ap.add_argument("--watch", action="store_true")
    ap.add_argument("--interval", type=int, default=DEFAULT_INTERVAL)
    ns = ap.parse_args(argv)
    vault = vault_path(ns.vault)
    if ns.watch:
        return _watch(vault, ns.interval, embed=not ns.no_embed)
    if not available():
        result = {"ok": False, "errors": ["gbrain is not installed"]}
    elif ns.check:
        errors = _check_sources(vault)
        result = {"ok": not errors, "errors": errors, "sources": list(SOURCE_DIRS)}
    else:
        result = sync_gbrain(vault, embed=not ns.no_embed)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
