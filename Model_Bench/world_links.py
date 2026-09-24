#!/usr/bin/env python3
"""Load Knowledge/world/links.jsonl into GBrain as typed links (after the sync imported Knowledge/world).

Runs in WSL from sync_gbrain_knowledge.sh. Idempotent: GBrain keys links on (from, to, type, source).

    python3 Model_Bench/world_links.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from l2_gbrain import Brain  # noqa: E402  (the one GBrain owner)

LINKS = Path(__file__).resolve().parent.parent / "Knowledge" / "world" / "links.jsonl"
LINK_SOURCE = "world-build"


def prune(brain: Brain, pages: list[dict]) -> int:
    """GBrain sync keeps pages whose files were removed on a full import (a key merged away).
    The world is generated, so a world page with no file is stale: soft-delete it."""
    world_dir = LINKS.parent
    files = {("knowledge/world/" + str(p.relative_to(world_dir).with_suffix(""))).lower() for p in world_dir.rglob("*.md")}
    removed = 0
    for slug in (p["slug"] for p in pages if p["slug"].startswith("knowledge/world/") and p["slug"].lower() not in files):
        try:
            brain.call("delete_page", slug=slug)
            removed += 1
        except RuntimeError as exc:
            print(f"could not delete stale page {slug}: {exc}")
    return removed


def main() -> int:
    links = [json.loads(l) for l in LINKS.read_text(encoding="utf-8").splitlines() if l.strip()]
    brain = Brain()
    print(f"stale world pages removed {prune(brain, brain.all_pages())}")
    # Our page path (kind/name) -> the slug GBrain assigned, read from the synced pages themselves.
    by_path = {f"{p.get('type')}/{p['slug'].rsplit('/', 1)[-1]}".lower(): p["slug"] for p in brain.all_pages()}
    added = missing = 0
    for l in links:
        frm, to = by_path.get(l["from"].lower()), by_path.get(l["to"].lower())
        if not frm or not to:
            missing += 1
            continue
        brain.call("add_link", **{"from": frm, "to": to, "link_type": l["type"], "context": l["context"],
                                  "link_source": LINK_SOURCE})
        added += 1
    print(f"links added {added}, endpoints not found {missing}, pages known {len(by_path)}")
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
