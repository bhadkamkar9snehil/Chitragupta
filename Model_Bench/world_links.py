#!/usr/bin/env python3
"""Load Knowledge/world/links.jsonl into GBrain as typed links, over one `gbrain serve` (MCP stdio) session.

Run in WSL after `gbrain sync --source xstudio-knowledge` has imported Knowledge/world.
Idempotent: GBrain keys links on (from, to, type, source), so a re-run adds nothing new.

    python3 Model_Bench/world_links.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINKS = ROOT / "Knowledge" / "world" / "links.jsonl"
GBRAIN = os.environ.get("GBRAIN_BIN", str(Path.home() / ".bun" / "bin" / "gbrain"))
LINK_SOURCE = "world-build"


class Brain:
    """Minimal MCP stdio client: initialize once, then tools/call."""

    def __init__(self) -> None:
        env = {**os.environ, "GBRAIN_HOME": os.environ.get("GBRAIN_HOME", str(Path.home() / ".hermes" / "xstudio-gbrain")),
               "PATH": f"{Path(GBRAIN).parent}:{os.environ.get('PATH', '')}"}
        self.proc = subprocess.Popen([GBRAIN, "serve"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.DEVNULL, text=True, env=env, bufsize=1)
        self.next_id = 0
        self.request("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                    "clientInfo": {"name": "world_links", "version": "1"}})
        self.notify("notifications/initialized")

    def notify(self, method: str) -> None:
        self.proc.stdin.write(json.dumps({"jsonrpc": "2.0", "method": method}) + "\n")

    def request(self, method: str, params: dict) -> dict:
        self.next_id += 1
        self.proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": self.next_id, "method": method, "params": params}) + "\n")
        while True:
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError("gbrain serve closed the connection")
            msg = json.loads(line)
            if msg.get("id") == self.next_id:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                return msg["result"]

    def call(self, tool: str, **args) -> dict:
        result = self.request("tools/call", {"name": tool, "arguments": args})
        text = "".join(c.get("text", "") for c in result.get("content", []))
        if result.get("isError"):
            raise RuntimeError(text[:300])
        try:
            return json.loads(text)
        except ValueError:
            return {"text": text}


def slugs(brain: Brain) -> dict[str, str]:
    """Our page path (kind/name) -> the slug GBrain assigned, found from the synced pages themselves."""
    out = {}
    for kind in ("table", "view", "procedure", "event", "key", "api"):
        listed = brain.call("list_pages", type=kind, limit=5000)
        for page in listed if isinstance(listed, list) else listed.get("pages", []):
            slug = page["slug"]
            out[f"{kind}/{slug.rsplit('/', 1)[-1]}".lower()] = slug
    return out


def main() -> int:
    links = [json.loads(l) for l in LINKS.read_text(encoding="utf-8").splitlines() if l.strip()]
    brain = Brain()
    by_path = slugs(brain)
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
