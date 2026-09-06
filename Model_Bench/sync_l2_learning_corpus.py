#!/usr/bin/env python3
"""Synchronize canonical Chitragupta reference material into the zvec vault.

Only the disposable canonical mirror under `knowledge/` is rebuilt. Runtime
experience, governed Solution exports, promoted facts, candidates, action plans
and replay data are separate planes and are never rewritten here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
DEFAULT_EMBEDDING = "local/potion-retrieval-32m"

RUNTIME_DIRS = (
    "sessions",
    "cases/approved",
    "cases/rejected",
    "cases/reopened",
    "facts",
    "candidates",
    "solutions/approved",
    "actions/plans",
    "actions/candidates",
    "eval",
    "archive/candidates/promoted",
    "archive/candidates/rejected",
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sources() -> list[tuple[Path, Path]]:
    items: list[tuple[Path, Path]] = []
    for name in ("AGENTS.md", "README.md"):
        source = ROOT / name
        if source.exists():
            items.append((source, Path("knowledge/contracts") / name))

    knowledge = ROOT / "Knowledge"
    if knowledge.exists():
        for source in sorted(knowledge.rglob("*.md")):
            items.append((source, Path("knowledge/git") / source.relative_to(knowledge)))

    skills = ROOT / "deploy" / "skills" / "xstudio"
    if skills.exists():
        for source in sorted(skills.glob("*/SKILL.md")):
            items.append((source, Path("knowledge/skills") / f"{source.parent.name}.md"))
    return items


def _manifest_for(items: list[tuple[Path, Path]]) -> dict:
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(ROOT),
        "authority": "Git is canonical; this vault copy is a disposable retrieval mirror",
        "files": [{
            "source": str(source.relative_to(ROOT)),
            "vault_path": str(target).replace("\\", "/"),
            "sha256": _sha256(source),
            "bytes": source.stat().st_size,
        } for source, target in items],
    }


def _signature(manifest: dict) -> list[tuple[str, str, str]]:
    return sorted(
        (str(item.get("source")), str(item.get("vault_path")), str(item.get("sha256")))
        for item in manifest.get("files", [])
    )


def _check(vault: Path, expected: dict) -> int:
    path = vault / "corpus_manifest.json"
    if not path.exists():
        print(f"FAIL: missing {path}")
        return 1
    try:
        actual = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: invalid {path}: {exc}")
        return 1
    if _signature(actual) != _signature(expected):
        print("FAIL: learning corpus mirror is stale; run sync_l2_learning_corpus.py")
        return 1

    missing = [
        item["vault_path"]
        for item in actual.get("files", [])
        if not (vault / item["vault_path"]).exists()
    ]
    if missing:
        print(f"FAIL: {len(missing)} mirrored corpus file(s) missing")
        for rel in missing[:20]:
            print(f"  - {rel}")
        return 1
    print(f"learning corpus mirror current: {len(actual.get('files', []))} files")
    return 0


def _sync(vault: Path, items: list[tuple[Path, Path]], manifest: dict) -> None:
    for rel in ("knowledge/git", "knowledge/skills", "knowledge/contracts"):
        target = vault / rel
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)

    for source, rel in items:
        target = vault / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    for rel in RUNTIME_DIRS:
        (vault / rel).mkdir(parents=True, exist_ok=True)

    (vault / "corpus_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _index(vault: Path, embedding: str, rebuild: bool) -> int:
    zg = os.environ.get("CHITRAGUPTA_ZG_BIN", "zg")
    if not shutil.which(zg):
        print(
            "FAIL: zg not found. Run: bash Model_Bench/install_l2_learning_prereqs.sh",
            file=sys.stderr,
        )
        return 2
    cmd = [zg, "index"]
    if rebuild:
        cmd.append("--rebuild")
    cmd += ["--embedding", embedding, str(vault)]
    print("indexing learning vault:", " ".join(cmd))
    return int(subprocess.run(cmd, text=True).returncode)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--vault",
        default=os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", str(DEFAULT_VAULT)),
    )
    ap.add_argument(
        "--embedding",
        default=os.environ.get("CHITRAGUPTA_ZVEC_EMBEDDING", DEFAULT_EMBEDDING),
    )
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--no-index", action="store_true")
    ap.add_argument("--rebuild", action="store_true")
    args = ap.parse_args(argv)

    vault = Path(args.vault).expanduser()
    items = _sources()
    manifest = _manifest_for(items)
    if args.check:
        return _check(vault, manifest)

    vault.mkdir(parents=True, exist_ok=True)
    _sync(vault, items, manifest)
    print(f"mirrored {len(items)} canonical files into {vault}")
    return 0 if args.no_index else _index(vault, args.embedding, args.rebuild)


if __name__ == "__main__":
    raise SystemExit(main())
