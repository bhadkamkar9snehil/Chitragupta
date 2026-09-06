#!/usr/bin/env python3
"""Synchronize the small trust-separated GBrain source set.

Canonical Knowledge is indexed directly from the Chitragupta Git checkout.
Only runtime-derived facts/solutions/cases live in the local learning-vault Git
repo. GBrain remains disposable derivative state and has no independent
scheduler.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import subprocess
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from l2_gbrain import (
    SOURCE_IDS,
    VAULT_SOURCE_DIRS,
    available,
    knowledge_path,
    run,
    vault_path,
)

GIT_TIMEOUT = 30


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
    path = vault.parent / f".{vault.name}.gbrain-sync.lock"
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
        if proc.returncode:
            raise RuntimeError((proc.stderr or proc.stdout).strip())
    for key, value in (
        ("user.name", "Chitragupta Learning Plane"),
        ("user.email", "chitragupta-learning@local.invalid"),
    ):
        proc = _git(vault, ["config", key, value])
        if proc.returncode:
            raise RuntimeError((proc.stderr or proc.stdout).strip())


def _checkpoint(vault: Path) -> bool:
    """Commit dynamic learning material so GBrain path sources have Git state."""
    _ensure_local_git(vault)
    add = _git(vault, ["add", "-A"])
    if add.returncode:
        raise RuntimeError((add.stderr or add.stdout).strip())
    diff = _git(vault, ["diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        return False
    if diff.returncode != 1:
        raise RuntimeError((diff.stderr or diff.stdout).strip())
    commit = _git(vault, [
        "commit",
        "-m",
        "learning checkpoint " + datetime.now(timezone.utc).isoformat(),
        "--no-gpg-sign",
    ])
    if commit.returncode:
        raise RuntimeError((commit.stderr or commit.stdout).strip())
    return True


def _ensure_brain() -> bool:
    rc, _, _ = run(["doctor", "--json"])
    if rc == 0:
        return False
    rc, out, err = run(["init", "--pglite"], timeout=300)
    if rc:
        raise RuntimeError((err or out).strip() or "failed to initialize isolated GBrain")
    return True


def _sources_list() -> list[dict[str, Any]]:
    rc, out, err = run(["sources", "list", "--json"])
    if rc:
        raise RuntimeError((err or out).strip() or "gbrain sources list failed")
    data = json.loads(out or "[]")
    if isinstance(data, dict):
        rows = data.get("sources") or data.get("results") or []
    else:
        rows = data
    return [row for row in rows if isinstance(row, dict)]


def _source_id(row: dict[str, Any]) -> str:
    return str(row.get("id") or row.get("source_id") or "")


def _source_config(row: dict[str, Any]) -> dict[str, Any]:
    value = row.get("config")
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, dict) else {}
        except json.JSONDecodeError:
            pass
    return {}


def _is_federated(row: dict[str, Any]) -> bool:
    return bool(row.get("federated")) if "federated" in row else bool(_source_config(row).get("federated"))


def _registered_path(row: dict[str, Any]) -> str:
    config = _source_config(row)
    return str(row.get("local_path") or row.get("path") or config.get("local_path") or config.get("path") or "")


def _expected_paths(vault: Path, knowledge: Path | None) -> dict[str, Path | None]:
    paths: dict[str, Path | None] = {"l2-knowledge": knowledge}
    paths.update({source: vault / rel for source, rel in VAULT_SOURCE_DIRS.items()})
    return paths


def _register_missing(
    vault: Path,
    existing: dict[str, dict[str, Any]],
    knowledge: Path | None,
) -> list[str]:
    created: list[str] = []
    for source_id, path in _expected_paths(vault, knowledge).items():
        if source_id in existing:
            continue
        if path is None or not path.is_dir():
            raise RuntimeError(f"source path unavailable for {source_id}: {path}")
        args = ["sources", "add", source_id, "--path", str(path), "--no-federated"]
        # Dynamic lanes may be empty on first deployment. They live inside the
        # checkpointed vault repo but have no tracked file until their first item.
        if source_id != "l2-knowledge":
            args.append("--force")
        rc, out, err = run(args)
        if rc:
            raise RuntimeError((err or out).strip() or f"failed to register {source_id}")
        created.append(source_id)
    return created


def _check_sources(vault: Path, knowledge: Path | None) -> list[str]:
    rows = {_source_id(row): row for row in _sources_list()}
    errors: list[str] = []
    for source_id, expected in _expected_paths(vault, knowledge).items():
        row = rows.get(source_id)
        if row is None:
            errors.append(f"missing GBrain source: {source_id}")
            continue
        if _is_federated(row):
            errors.append(f"GBrain source must be non-federated: {source_id}")
        raw = _registered_path(row)
        if not raw:
            errors.append(f"GBrain source path is not reported for {source_id}")
            continue
        try:
            actual = Path(raw).expanduser().resolve()
        except Exception:
            errors.append(f"invalid GBrain source path for {source_id}: {raw}")
            continue
        if not actual.is_dir():
            errors.append(f"GBrain source path does not exist for {source_id}: {actual}")
        if expected is not None and actual != expected.resolve():
            errors.append(f"GBrain source path mismatch for {source_id}: {actual} != {expected.resolve()}")
    return errors


def _sync_sources() -> list[str]:
    synced: list[str] = []
    for source_id in SOURCE_IDS:
        rc, out, err = run(["sync", "--source", source_id])
        if rc:
            raise RuntimeError((err or out).strip() or f"failed to sync {source_id}")
        synced.append(source_id)
    return synced


def _embed_stale() -> None:
    rc, out, err = run(["embed", "--stale"], timeout=300)
    if rc:
        raise RuntimeError((err or out).strip() or "gbrain embed --stale failed")


def sync_gbrain(
    vault: Path,
    *,
    knowledge: Path | None = None,
    embed: bool = True,
    dry_run: bool = False,
) -> dict[str, Any]:
    knowledge = knowledge if knowledge is not None else knowledge_path()
    if dry_run:
        return {
            "ok": True,
            "dry_run": True,
            "vault": str(vault),
            "knowledge": str(knowledge) if knowledge else None,
            "sources": list(SOURCE_IDS),
            "errors": [],
        }
    if not available():
        return {"ok": False, "errors": ["gbrain is not installed"]}
    for rel in VAULT_SOURCE_DIRS.values():
        (vault / rel).mkdir(parents=True, exist_ok=True)
    with _sync_lock(vault) as acquired:
        if not acquired:
            return {"ok": True, "skipped": "sync_already_running", "errors": []}
        initialized = _ensure_brain()
        checkpointed = _checkpoint(vault)
        existing = {_source_id(row): row for row in _sources_list()}
        created = _register_missing(vault, existing, knowledge)
        errors = _check_sources(vault, knowledge)
        if errors:
            return {
                "ok": False,
                "initialized": initialized,
                "checkpointed": checkpointed,
                "created": created,
                "errors": errors,
            }
        synced = _sync_sources()
        if embed:
            _embed_stale()
        return {
            "ok": True,
            "initialized": initialized,
            "checkpointed": checkpointed,
            "created": created,
            "synced": synced,
            "embedded": embed,
            "errors": [],
        }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--knowledge", default=None)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--no-embed", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ns = ap.parse_args(argv)
    vault = vault_path(ns.vault)
    knowledge = knowledge_path(ns.knowledge)
    if ns.check:
        rc, _, _ = run(["doctor", "--json"])
        errors = [] if rc == 0 else ["isolated GBrain is not initialized/healthy"]
        if not errors:
            errors.extend(_check_sources(vault, knowledge))
        result = {"ok": not errors, "errors": errors, "sources": list(SOURCE_IDS)}
    else:
        result = sync_gbrain(
            vault,
            knowledge=knowledge,
            embed=not ns.no_embed,
            dry_run=ns.dry_run,
        )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
