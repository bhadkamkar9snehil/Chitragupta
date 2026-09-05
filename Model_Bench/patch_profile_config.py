#!/usr/bin/env python3
"""Idempotently add the L2 typed-tool entries to a Hermes profile config.yaml.

Why this is a targeted text editor and not a YAML round-trip: the live profile
configs carry substantial explanatory comments (the Security/Tirith block, the
fallback-model provider list). Loading and re-dumping them through a YAML
library silently deletes every one of those comments and reflows block lists
into flow style. That is real information loss in a file operators read, so we
edit only the specific list entries we own and leave every other byte alone.

What it guarantees:
  * idempotent -- re-running adds nothing and rewrites nothing
  * comment/format preserving -- untouched lines are byte-identical
  * never writes credentials, ports, dispatch settings, or unrelated keys
  * additive only -- it never removes an existing entry
  * missing section is reported, not silently ignored, but a single missing
    optional section does not abort a whole deployment

Usage:
    python3 patch_profile_config.py <config.yaml> [more configs...]
    python3 patch_profile_config.py --check <config.yaml>   # report only
"""
from __future__ import annotations

import sys
from pathlib import Path

# Terminal transports the L2 agents must never reach for. Mirrors
# xstudio_l2_tools_plugin._BLOCKED_TERMINAL_MARKERS as defense in depth: the
# plugin hook is the enforcing layer, these approval-deny rules are the backstop
# if the plugin is ever disabled on a profile.
DENY_ENTRIES = [
    "'*sqlcmd*'",
    "'*Hermes_Orchestrator.py*'",
    "'*/mnt/c/Python314/python.exe*'",
    "'*python.exe*'",
    "'*pip install*'",
    "'*pip3 install*'",
    "'*python -m pip*'",
    "'*python3 -m pip*'",
    "'*uv pip*'",
]

PLUGIN_ENTRIES = ["xstudio-l2-tools"]
TOOLSET_ENTRIES = ["xstudio_l2"]

SECTIONS: list[tuple[list[str], list[str], bool]] = [
    # (key path, entries to ensure, required)
    (["approvals", "deny"], DENY_ENTRIES, True),
    (["plugins", "enabled"], PLUGIN_ENTRIES, True),
    (["platform_toolsets", "cli"], TOOLSET_ENTRIES, True),
    (["known_plugin_toolsets", "cli"], TOOLSET_ENTRIES, False),
]


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_blank_or_comment(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith("#")


def _normalize(value: str) -> str:
    """Compare list entries ignoring quoting/whitespace differences."""
    return value.strip().strip("'\"").strip()


def _find_key_line(lines: list[str], key: str, start: int, end: int, indent: int | None) -> int:
    """Index of `key:` between [start, end) at the given indent (any if None)."""
    prefix = key + ":"
    for i in range(start, min(end, len(lines))):
        line = lines[i]
        if _is_blank_or_comment(line):
            continue
        if line.strip().startswith(prefix) and (indent is None or _indent_of(line) == indent):
            return i
    return -1


def _block_end(lines: list[str], key_index: int) -> int:
    """First index after the key's nested block."""
    parent_indent = _indent_of(lines[key_index])
    for i in range(key_index + 1, len(lines)):
        if _is_blank_or_comment(lines[i]):
            continue
        if _indent_of(lines[i]) <= parent_indent:
            return i
    return len(lines)


def ensure_entries(text: str, key_path: list[str], entries: list[str]) -> tuple[str, list[str], bool]:
    """Return (new_text, added_entries, section_found)."""
    lines = text.splitlines()

    start, end, indent = 0, len(lines), 0
    key_index = -1
    for depth, key in enumerate(key_path):
        key_index = _find_key_line(lines, key, start, end, indent if depth == 0 else None)
        if key_index < 0:
            return text, [], False
        if depth < len(key_path) - 1:
            start, end = key_index + 1, _block_end(lines, key_index)
            indent = None

    key_line = lines[key_index]
    remainder = key_line.split(":", 1)[1].strip()

    # Flow style: key: [a, b, c]
    if remainder.startswith("["):
        if not remainder.endswith("]"):
            return text, [], False  # multi-line flow sequence: leave it alone
        inner = remainder[1:-1].strip()
        existing = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        existing_norm = {_normalize(x) for x in existing}
        added = [e for e in entries if _normalize(e) not in existing_norm]
        if not added:
            return text, [], True
        merged = existing + added
        lines[key_index] = f"{key_line.split(':', 1)[0]}: [{', '.join(merged)}]"
        return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), added, True

    # Block style: key:\n  - a\n  - b
    section_end = _block_end(lines, key_index)
    item_indices = [i for i in range(key_index + 1, section_end)
                    if not _is_blank_or_comment(lines[i]) and lines[i].strip().startswith("- ")]
    existing_norm = {_normalize(lines[i].strip()[2:]) for i in item_indices}
    added = [e for e in entries if _normalize(e) not in existing_norm]
    if not added:
        return text, [], True

    item_indent = _indent_of(lines[item_indices[0]]) if item_indices else _indent_of(key_line) + 2
    insert_at = (item_indices[-1] + 1) if item_indices else (key_index + 1)
    new_lines = [f"{' ' * item_indent}- {entry}" for entry in added]
    lines[insert_at:insert_at] = new_lines
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), added, True


def patch_file(path: Path, *, check_only: bool = False) -> tuple[bool, list[str], list[str]]:
    """Return (changed, added_entries, warnings)."""
    text = path.read_text(encoding="utf-8")
    original = text
    added_all: list[str] = []
    warnings: list[str] = []

    for key_path, entries, required in SECTIONS:
        text, added, found = ensure_entries(text, key_path, entries)
        if not found:
            message = f"section {'.'.join(key_path)} not found in {path}"
            if required:
                warnings.append("WARNING: " + message + " (skipped; plugin hook still enforces this)")
            continue
        added_all.extend(f"{'.'.join(key_path)}: {a}" for a in added)

    changed = text != original
    if changed and not check_only:
        path.write_text(text, encoding="utf-8")
    return changed, added_all, warnings


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    exit_code = 0
    for path in paths:
        if not path.exists():
            print(f"SKIP (absent): {path}")
            continue
        try:
            changed, added, warnings = patch_file(path, check_only=check_only)
        except Exception as exc:  # never abort a deployment on one config
            print(f"ERROR patching {path}: {type(exc).__name__}: {exc}")
            exit_code = 1
            continue
        for warning in warnings:
            print(warning)
        if added:
            verb = "would add" if check_only else "added"
            print(f"{path}: {verb} {len(added)} entr{'y' if len(added) == 1 else 'ies'}")
            for entry in added:
                print(f"    + {entry}")
        else:
            print(f"{path}: already current")
        if check_only and changed:
            exit_code = max(exit_code, 3)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
