#!/usr/bin/env python3
"""Disable deferred tool-search for the L2 profiles.

Why: Hermes defers part of the tool surface behind `tool_search` once the
listing budget is exceeded, so the model must discover a tool before it can call
it. That round trip is fine for a large model and fatal for the 9B local model
running L2. Observed live on Ticket_360: the worker searched, found `xstudio_l2`,
wrote a comment saying it would use it -- and then completed with
"database access unavailable ... requires pyodbc installation" without ever
calling the tool it had just located.

The L2 profiles carry a deliberately small toolset (about a dozen entries), so
listing all of them directly costs little and removes the discovery step
entirely. `xstudio_l2` is the tool these workers must reach for; it should never
be something they have to go looking for.

Targeted, idempotent, comment-preserving -- same discipline as
patch_profile_config.py. Adds only:

    tools:
      tool_search:
        enabled: off

Usage:
    python3 patch_tool_search_off.py <config.yaml> [more...] [--check]
"""
from __future__ import annotations

import sys
from pathlib import Path

BLOCK = "tools:\n  tool_search:\n    enabled: off\n"


def _has_tool_search_off(text: str) -> bool:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() != "tool_search:":
            continue
        for follow in lines[i + 1:]:
            stripped = follow.strip()
            if not stripped or stripped.startswith("#"):
                continue
            indent = len(follow) - len(follow.lstrip(" "))
            if indent <= (len(line) - len(line.lstrip(" "))):
                break
            if stripped.replace(" ", "").lower() in ("enabled:off", "enabled:'off'", 'enabled:"off"'):
                return True
    return False


def patch(path: Path, *, check_only: bool = False) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    if _has_tool_search_off(text):
        return False, "already current"

    lines = text.splitlines()
    top_tools = next((i for i, l in enumerate(lines) if l.rstrip() == "tools:"), -1)

    if top_tools < 0:
        new_text = text if text.endswith("\n") else text + "\n"
        new_text += BLOCK
        note = "added tools.tool_search.enabled: off"
    else:
        # A tools: block exists; insert/replace the tool_search subtree conservatively.
        end = len(lines)
        for i in range(top_tools + 1, len(lines)):
            l = lines[i]
            if l.strip() and not l.startswith(" ") and not l.strip().startswith("#"):
                end = i
                break
        block = lines[top_tools + 1:end]
        has_ts = any(l.strip() == "tool_search:" for l in block)
        if has_ts:
            out = []
            skipping = False
            for l in lines[top_tools + 1:end]:
                if l.strip() == "tool_search:":
                    out.append("  tool_search:")
                    out.append("    enabled: off")
                    skipping = True
                    continue
                if skipping:
                    indent = len(l) - len(l.lstrip(" "))
                    if l.strip() and indent > 2:
                        continue
                    skipping = False
                out.append(l)
            lines[top_tools + 1:end] = out
            note = "set existing tools.tool_search.enabled: off"
        else:
            lines.insert(top_tools + 1, "    enabled: off")
            lines.insert(top_tools + 1, "  tool_search:")
            note = "added tool_search.enabled: off under existing tools:"
        new_text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    if not check_only:
        path.write_text(new_text, encoding="utf-8")
    return True, note


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    for path in paths:
        if not path.exists():
            print(f"SKIP (absent): {path}")
            continue
        try:
            changed, note = patch(path, check_only=check_only)
        except Exception as exc:
            print(f"ERROR patching {path}: {type(exc).__name__}: {exc}")
            continue
        print(f"{path}: {note}" if changed else f"{path}: already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
