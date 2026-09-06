#!/usr/bin/env python3
"""Synchronize Chitragupta's canonical local corpus into the shared zvec vault.

This script copies only governed/reference material. It never touches sessions,
facts, candidates, approved SQL-solution exports, or archives.

The copied files are a retrieval mirror, not a new source of truth. Git remains
canonical for project/reference knowledge. The zvec index is disposable.
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


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _sources() -> list[tuple[Path, Path]]:
    items: list[tuple[Path, Path]] = []

    for name in ("AGENTS.md", "README.md"):
        src = ROOT / name
        if src.exists():
            items.append((src, Path("knowledge/contracts") / name))

    knowledge = ROOT / "Knowledge"
    if knowledge.exists():
        for src in sorted(knowledge.rglob("*.md")):
            rel = src.relative_to(knowledge)
            items.append((src, Path("knowledge/git") / rel))

    skills = ROOT / "deploy" / "skills" / "xstudio"
    if skills.exists():
        for src in sorted(skills.glob("*/SKILL.md")):
            items.append((src, Path("knowledge/skills") / f"{src.parent.name}.md"))

    return items


def _manifest_for(items: list[tuple[Path, Path]]) -> dict:
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(ROOT),
        "authority": "Git sources listed below; this vault copy is a disposable retrieval mirror",
        "files": [
            {
                "source": str(src.relative_to(ROOT)),
                "vault_path": str(dst).replace("\\", "/"),
                "sha256": _sha256(src),
                "bytes": src.stat().st_size,
            }
            for src, dst in items
        ],
    }


def _expected_signature(manifest: dict) -> list[tuple[str, str, str]]:
    return sorted(
        (str(x.get("source")), str(x.get("vault_path")), str(x.get("sha256")))
        for x in manifest.get("files", [])
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
    if _expected_signature(actual) != _expected_signature(expected):
        print("FAIL: learning corpus mirror is stale; run sync_l2_learning_corpus.py")
        return 1
    missing = [x["vault_path"] for x in actual.get("files", []) if not (vault / x["vault_path"]).exists()]
    if missing:
        print(f"FAIL: {len(missing)} mirrored corpus file(s) missing")
        for rel in missing[:20]:
            print(f"  - {rel}")
        return 1
    print(f"learning corpus mirror current: {len(actual.get('files', []))} files")
    return 0


def _sync(vault: Path, items: list[tuple[Path, Path]], manifest: dict) -> None:
    for rel in ("knowledge/git", "knowledge/skills", "knowledge/contracts"):
        dst = vault / rel
        if dst.exists():
            shutil.rmtree(dst)
        dst.mkdir(parents=True, exist_ok=True)

    for src, rel in items:
        dst = vault / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    for rel in ("sessions", "facts", "candidates", "solutions/approved", "archive"):
        (vault / rel).mkdir(parents=True, exist_ok=True)

    (vault / "corpus_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _index(vault: Path, embedding: str, rebuild: bool) -> int:
    zg = os.environ.get("CHITRAGUPTA_ZG_BIN", "zg")
    if not shutil.which(zg):
        print("FAIL: zg not found. Install Node.js 22+ and npm install -g @zvec/zvec-grep", file=sys.stderr)
        return 2
    cmd = [zg, "index"]
    if rebuild:
        cmd.append("--rebuild")
    cmd += ["--embedding", embedding, str(vault)]
    print("indexing learning vault:", " ".join(cmd))
    result = subprocess.run(cmd, text=True)
    return int(result.returncode)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", str(DEFAULT_VAULT)))
    ap.add_argument("--embedding", default=os.environ.get("CHITRAGUPTA_ZVEC_EMBEDDING", DEFAULT_EMBEDDING))
    ap.add_argument("--check", action="store_true", help="verify mirror freshness without writing")
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
    if args.no_index:
        return 0
    return _index(vault, args.embedding, args.rebuild)


if __name__ == "__main__":
    raise SystemExit(main())
