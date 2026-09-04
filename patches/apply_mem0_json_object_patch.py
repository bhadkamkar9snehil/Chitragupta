#!/usr/bin/env python3
"""Re-apply the mem0 LM-Studio compatibility patch.

Why this exists: mem0's own memory/main.py hardcodes
response_format={"type": "json_object"} for its LLM fact-extraction calls
(two call sites). LM Studio's OpenAI-compatible endpoint rejects that --
it only accepts response_format.type of "json_schema" or "text" -- so
mem0's extraction call 400s against our LLM (LM Studio, reusing the
already-loaded investigation model rather than adding a second model's
worth of VRAM). See deploy/README.md for the full mem0 setup this patch
is part of.

This lives in the pip-installed mem0ai package inside Hermes's own venv,
so it does NOT survive `pip install --upgrade mem0ai` or a Hermes
self-update that rebuilds the venv. Re-run this script any time after
`hermes update` (or after any mem0ai upgrade) to restore it. Idempotent --
safe to run whether or not the patch is already applied.

Usage (from WSL, inside Hermes's own venv):
    source ~/.hermes/hermes-agent/venv/bin/activate
    python3 patches/apply_mem0_json_object_patch.py
"""
import pathlib
import sys

TARGET = pathlib.Path.home() / ".hermes/hermes-agent/venv/lib/python3.11/site-packages/mem0/memory/main.py"

OLD = 'response_format={"type": "json_object"},'
NEW = ('response_format={"type": "text"},  # patched 2026-09-05: LM Studio '
       'rejects json_object (only accepts json_schema/text) -- see '
       'AIHelpdesk/patches/apply_mem0_json_object_patch.py')

def main() -> int:
    if not TARGET.exists():
        print(f"NOT FOUND: {TARGET} -- is mem0ai installed in this venv?", file=sys.stderr)
        return 1

    text = TARGET.read_text(encoding="utf-8")
    already = text.count(NEW)
    remaining = text.count(OLD)

    if remaining == 0:
        print(f"Already patched ({already} occurrence(s)). Nothing to do.")
        return 0

    text = text.replace(OLD, NEW)
    TARGET.write_text(text, encoding="utf-8")
    print(f"Patched {remaining} occurrence(s). ({already} were already patched.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
