#!/usr/bin/env python3
"""Idempotently patch Chitragupta L2 Hermes configs without YAML round-tripping.

For root config bootstrap this module only enables Chitragupta plugins.

For autonomous L2 service profiles it owns:
- Chitragupta plugin/toolset presence;
- retired raw-SQL terminal deny backstops;
- explicit disabling of built-in/user-profile/external Mem0 memory;
- suppression of worker memory/session-search/generic skill-management toolsets;
- skill write approval as defense in depth.

Pinned Kanban skills remain enabled by Hermes task dispatch. Removing the generic
``skills`` toolset does not remove harness-selected task skill loading.
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
DISABLED_WORKER_TOOLSETS = ["memory", "session_search", "skills"]
PROFILE_ADD_SECTIONS: list[tuple[list[str], list[str], bool]] = [
    (["approvals", "deny"], DENY_ENTRIES, True),
    (["plugins", "enabled"], PLUGIN_ENTRIES, True),
    (["platform_toolsets", "cli"], TOOLSET_ENTRIES, True),
    (["known_plugin_toolsets", "cli"], TOOLSET_ENTRIES, False),
]


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_blank_or_comment(line: str) -> bool:
    return not line.strip() or line.strip().startswith("#")


def _normalize(value: str) -> str:
    return value.strip().strip("'\"").strip()


def _find_key_line(
    lines: list[str], key: str, start: int, end: int, indent: int | None
) -> int:
    prefix = key + ":"
    for i in range(start, min(end, len(lines))):
        line = lines[i]
        if _is_blank_or_comment(line):
            continue
        if line.strip().startswith(prefix) and (indent is None or _indent_of(line) == indent):
            return i
    return -1


def _block_end(lines: list[str], key_index: int) -> int:
    parent_indent = _indent_of(lines[key_index])
    for i in range(key_index + 1, len(lines)):
        if _is_blank_or_comment(lines[i]):
            continue
        if _indent_of(lines[i]) <= parent_indent:
            return i
    return len(lines)


def ensure_entries(
    text: str, key_path: list[str], entries: list[str]
) -> tuple[str, list[str], bool]:
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
    if remainder.startswith("["):
        if not remainder.endswith("]"):
            return text, [], False
        inner = remainder[1:-1].strip()
        existing = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        existing_norm = {_normalize(x) for x in existing}
        added = [e for e in entries if _normalize(e) not in existing_norm]
        if not added:
            return text, [], True
        lines[key_index] = f"{key_line.split(':', 1)[0]}: [{', '.join(existing + added)}]"
        return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), added, True
    section_end = _block_end(lines, key_index)
    item_indices = [
        i for i in range(key_index + 1, section_end)
        if not _is_blank_or_comment(lines[i]) and lines[i].strip().startswith("- ")
    ]
    existing_norm = {_normalize(lines[i].strip()[2:]) for i in item_indices}
    added = [e for e in entries if _normalize(e) not in existing_norm]
    if not added:
        return text, [], True
    item_indent = _indent_of(lines[item_indices[0]]) if item_indices else _indent_of(key_line) + 2
    insert_at = item_indices[-1] + 1 if item_indices else key_index + 1
    lines[insert_at:insert_at] = [f"{' ' * item_indent}- {entry}" for entry in added]
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), added, True


def remove_entries(
    text: str, key_path: list[str], entries: list[str]
) -> tuple[str, list[str], bool]:
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
    section_end = _block_end(lines, key_index)
    wanted = {_normalize(v) for v in entries}
    removed: list[str] = []
    keep: list[str] = []
    for i, line in enumerate(lines):
        if key_index < i < section_end and not _is_blank_or_comment(line) and line.strip().startswith("- "):
            value = _normalize(line.strip()[2:])
            if value in wanted:
                removed.append(value)
                continue
        keep.append(line)
    return "\n".join(keep) + ("\n" if text.endswith("\n") else ""), removed, True


def _ensure_root_block(text: str, key: str) -> tuple[str, int]:
    lines = text.splitlines()
    idx = _find_key_line(lines, key, 0, len(lines), 0)
    if idx >= 0:
        if lines[idx].split(":", 1)[1].strip():
            raise ValueError(f"root {key} key uses scalar/inline form")
        return text, idx
    if lines and lines[-1].strip():
        lines.append("")
    lines.append(f"{key}:")
    out = "\n".join(lines) + ("\n" if text.endswith("\n") or text else "")
    return out, len(lines) - 1


def set_nested_scalar(text: str, parent: str, key: str, value: str) -> tuple[str, bool]:
    text, _ = _ensure_root_block(text, parent)
    lines = text.splitlines()
    pidx = _find_key_line(lines, parent, 0, len(lines), 0)
    pend = _block_end(lines, pidx)
    kidx = _find_key_line(lines, key, pidx + 1, pend, _indent_of(lines[pidx]) + 2)
    target = f"{' ' * (_indent_of(lines[pidx]) + 2)}{key}: {value}"
    if kidx >= 0:
        if lines[kidx] == target:
            return text, False
        lines[kidx] = target
    else:
        insert_at = pidx + 1
        # put memory/skills policy near the top of its block, before comments/children
        lines.insert(insert_at, target)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), True


def ensure_nested_list(
    text: str, parent: str, key: str, entries: list[str]
) -> tuple[str, list[str]]:
    text, _ = _ensure_root_block(text, parent)
    lines = text.splitlines()
    pidx = _find_key_line(lines, parent, 0, len(lines), 0)
    pend = _block_end(lines, pidx)
    kidx = _find_key_line(lines, key, pidx + 1, pend, _indent_of(lines[pidx]) + 2)
    if kidx < 0:
        insert_at = pidx + 1
        block = [
            f"{' ' * (_indent_of(lines[pidx]) + 2)}{key}:",
            *[f"{' ' * (_indent_of(lines[pidx]) + 4)}- {v}" for v in entries],
        ]
        lines[insert_at:insert_at] = block
        return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), list(entries)
    updated = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    updated, added, _ = ensure_entries(updated, [parent, key], entries)
    return updated, added


def _ensure_root_plugins_enabled(text: str) -> tuple[str, list[str]]:
    updated, added, found = ensure_entries(text, ["plugins", "enabled"], PLUGIN_ENTRIES)
    if found:
        return updated, added
    lines = text.splitlines()
    plugins_idx = _find_key_line(lines, "plugins", 0, len(lines), 0)
    if plugins_idx >= 0:
        if lines[plugins_idx].split(":", 1)[1].strip():
            raise ValueError("root plugins key uses inline/scalar form")
        lines[plugins_idx + 1:plugins_idx + 1] = [
            "  enabled:", *[f"    - {entry}" for entry in PLUGIN_ENTRIES]
        ]
    else:
        if lines and lines[-1].strip():
            lines.append("")
        lines.extend(["plugins:", "  enabled:", *[f"    - {entry}" for entry in PLUGIN_ENTRIES]])
    return "\n".join(lines) + ("\n" if text.endswith("\n") or not text else ""), list(PLUGIN_ENTRIES)


def harden_l2_worker(text: str) -> tuple[str, list[str], list[str]]:
    changed: list[str] = []
    errors: list[str] = []

    for parent, key, value in (
        ("memory", "provider", "''"),
        ("memory", "memory_enabled", "false"),
        ("memory", "user_profile_enabled", "false"),
        ("memory", "write_approval", "true"),
        ("skills", "write_approval", "true"),
    ):
        text, did = set_nested_scalar(text, parent, key, value)
        if did:
            changed.append(f"{parent}.{key}: {value}")

    text, added = ensure_nested_list(text, "agent", "disabled_toolsets", DISABLED_WORKER_TOOLSETS)
    changed.extend(f"agent.disabled_toolsets: {v}" for v in added)

    text, removed, found = remove_entries(text, ["platform_toolsets", "cli"], DISABLED_WORKER_TOOLSETS)
    if not found:
        errors.append("required section platform_toolsets.cli not found")
    changed.extend(f"platform_toolsets.cli removed: {v}" for v in removed)
    return text, changed, errors


def patch_file(
    path: Path,
    *,
    check_only: bool = False,
    bootstrap_root_plugins: bool = False,
) -> tuple[bool, list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    original = text
    added_all: list[str] = []
    errors: list[str] = []

    if bootstrap_root_plugins:
        text, added = _ensure_root_plugins_enabled(text)
        added_all.extend(f"plugins.enabled: {a}" for a in added)
    else:
        for key_path, entries, required in PROFILE_ADD_SECTIONS:
            text, added, found = ensure_entries(text, key_path, entries)
            if not found:
                if required:
                    errors.append(f"required section {'.'.join(key_path)} not found in {path}")
                continue
            added_all.extend(f"{'.'.join(key_path)}: {a}" for a in added)
        text, hardening, hardening_errors = harden_l2_worker(text)
        added_all.extend(hardening)
        errors.extend(hardening_errors)

    changed = text != original
    if changed and not check_only and not errors:
        path.write_text(text, encoding="utf-8")
    return changed, added_all, errors


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    plugin_only = "--enable-plugin-only" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    exit_code = 0
    for path in paths:
        if not path.exists():
            if plugin_only and not check_only:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("", encoding="utf-8")
            else:
                print(f"ERROR: missing required config: {path}")
                exit_code = 1
                continue
        try:
            changed, added, errors = patch_file(
                path, check_only=check_only, bootstrap_root_plugins=plugin_only
            )
        except Exception as exc:
            print(f"ERROR patching {path}: {type(exc).__name__}: {exc}")
            exit_code = 1
            continue
        for error in errors:
            print("ERROR:", error)
        if errors:
            exit_code = 1
            continue
        if added:
            verb = "would change" if check_only else "changed"
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
