#!/usr/bin/env python3
"""Idempotently add Chitragupta L2 plugin/toolset entries to Hermes config.yaml.

Why this is a targeted text editor and not a YAML round-trip: the live profile
configs carry substantial explanatory comments. This patcher owns only:
- xstudio-l2-tools / xstudio_l2
- xstudio-l2-identity (cross-cutting harness-owned run/ticket binding)
- xstudio-l2-learning / l2_learning
- xstudio-l2-actions / l2_actions
- terminal-deny backstops for retired SQL transport

It deliberately does NOT switch the active Hermes memory provider. mem0,
experience retrieval, and action planning are orthogonal.
"""
from __future__ import annotations

import sys
from pathlib import Path

DENY_ENTRIES = [
    "'*sqlcmd*'", "'*Hermes_Orchestrator.py*'", "'*/mnt/c/Python314/python.exe*'",
    "'*python.exe*'", "'*pip install*'", "'*pip3 install*'", "'*python -m pip*'",
    "'*python3 -m pip*'", "'*uv pip*'",
]
PLUGIN_ENTRIES = [
    "xstudio-l2-tools",
    "xstudio-l2-identity",
    "xstudio-l2-learning",
    "xstudio-l2-actions",
]
TOOLSET_ENTRIES = ["xstudio_l2", "l2_learning", "l2_actions"]
PROFILE_SECTIONS: list[tuple[list[str], list[str], bool]] = [
    (["approvals", "deny"], DENY_ENTRIES, True),
    (["plugins", "enabled"], PLUGIN_ENTRIES, True),
    (["platform_toolsets", "cli"], TOOLSET_ENTRIES, True),
    (["known_plugin_toolsets", "cli"], TOOLSET_ENTRIES, False),
]


def _indent_of(line: str) -> int: return len(line) - len(line.lstrip(" "))
def _is_blank_or_comment(line: str) -> bool: return not line.strip() or line.strip().startswith("#")
def _normalize(value: str) -> str: return value.strip().strip("'\"").strip()


def _find_key_line(lines: list[str], key: str, start: int, end: int, indent: int | None) -> int:
    prefix = key + ":"
    for i in range(start, min(end, len(lines))):
        line = lines[i]
        if _is_blank_or_comment(line): continue
        if line.strip().startswith(prefix) and (indent is None or _indent_of(line) == indent): return i
    return -1


def _block_end(lines: list[str], key_index: int) -> int:
    parent_indent = _indent_of(lines[key_index])
    for i in range(key_index + 1, len(lines)):
        if _is_blank_or_comment(lines[i]): continue
        if _indent_of(lines[i]) <= parent_indent: return i
    return len(lines)


def ensure_entries(text: str, key_path: list[str], entries: list[str]) -> tuple[str, list[str], bool]:
    lines = text.splitlines(); start, end, indent = 0, len(lines), 0; key_index = -1
    for depth, key in enumerate(key_path):
        key_index = _find_key_line(lines, key, start, end, indent if depth == 0 else None)
        if key_index < 0: return text, [], False
        if depth < len(key_path) - 1:
            start, end = key_index + 1, _block_end(lines, key_index); indent = None
    key_line = lines[key_index]; remainder = key_line.split(":", 1)[1].strip()
    if remainder.startswith("["):
        if not remainder.endswith("]"): return text, [], False
        inner = remainder[1:-1].strip(); existing = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        existing_norm = {_normalize(x) for x in existing}; added = [e for e in entries if _normalize(e) not in existing_norm]
        if not added: return text, [], True
        lines[key_index] = f"{key_line.split(':', 1)[0]}: [{', '.join(existing + added)}]"
        return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), added, True
    section_end = _block_end(lines, key_index)
    item_indices = [i for i in range(key_index + 1, section_end) if not _is_blank_or_comment(lines[i]) and lines[i].strip().startswith("- ")]
    existing_norm = {_normalize(lines[i].strip()[2:]) for i in item_indices}; added = [e for e in entries if _normalize(e) not in existing_norm]
    if not added: return text, [], True
    item_indent = _indent_of(lines[item_indices[0]]) if item_indices else _indent_of(key_line) + 2
    insert_at = item_indices[-1] + 1 if item_indices else key_index + 1
    lines[insert_at:insert_at] = [f"{' ' * item_indent}- {entry}" for entry in added]
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), added, True


def _ensure_root_plugins_enabled(text: str) -> tuple[str, list[str]]:
    updated, added, found = ensure_entries(text, ["plugins", "enabled"], PLUGIN_ENTRIES)
    if found: return updated, added
    lines = text.splitlines(); plugins_idx = _find_key_line(lines, "plugins", 0, len(lines), 0)
    if plugins_idx >= 0:
        if lines[plugins_idx].split(":", 1)[1].strip():
            raise ValueError("root plugins key uses inline/scalar form; cannot safely patch comment-preserving text")
        lines[plugins_idx + 1:plugins_idx + 1] = ["  enabled:", *[f"    - {entry}" for entry in PLUGIN_ENTRIES]]
    else:
        if lines and lines[-1].strip(): lines.append("")
        lines.extend(["plugins:", "  enabled:", *[f"    - {entry}" for entry in PLUGIN_ENTRIES]])
    suffix = "\n" if text.endswith("\n") or not text else ""
    return "\n".join(lines) + suffix, list(PLUGIN_ENTRIES)


def patch_file(path: Path, *, check_only: bool = False, bootstrap_root_plugins: bool = False) -> tuple[bool, list[str], list[str]]:
    text = path.read_text(encoding="utf-8"); original = text; added_all: list[str] = []; errors: list[str] = []
    if bootstrap_root_plugins:
        text, added = _ensure_root_plugins_enabled(text); added_all.extend(f"plugins.enabled: {a}" for a in added)
    else:
        for key_path, entries, required in PROFILE_SECTIONS:
            text, added, found = ensure_entries(text, key_path, entries)
            if not found:
                if required: errors.append(f"required section {'.'.join(key_path)} not found in {path}")
                continue
            added_all.extend(f"{'.'.join(key_path)}: {a}" for a in added)
    changed = text != original
    if changed and not check_only and not errors: path.write_text(text, encoding="utf-8")
    return changed, added_all, errors


def main(argv: list[str]) -> int:
    check_only = "--check" in argv; plugin_only = "--enable-plugin-only" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths: print(__doc__); return 2
    exit_code = 0
    for path in paths:
        if not path.exists():
            if plugin_only and not check_only:
                path.parent.mkdir(parents=True, exist_ok=True); path.write_text("", encoding="utf-8")
            else:
                print(f"ERROR: missing required config: {path}"); exit_code = 1; continue
        try:
            changed, added, errors = patch_file(path, check_only=check_only, bootstrap_root_plugins=plugin_only)
        except Exception as exc:
            print(f"ERROR patching {path}: {type(exc).__name__}: {exc}"); exit_code = 1; continue
        for error in errors: print("ERROR:", error)
        if errors: exit_code = 1; continue
        if added:
            verb = "would add" if check_only else "added"; print(f"{path}: {verb} {len(added)} entr{'y' if len(added) == 1 else 'ies'}")
            for entry in added: print(f"    + {entry}")
        else: print(f"{path}: already current")
        if check_only and changed: exit_code = max(exit_code, 3)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
