#!/usr/bin/env python3
"""Direct mem0 OSS config writer -- bypasses hermes's CLI wrapper, which
doesn't actually pass --mode/--oss-* flags through to the plugin's
parse_flags(sys.argv[1:]) (confirmed live: 'unrecognized arguments' at the
top-level parser, and the plugin's own test suite mocks sys.argv directly
rather than going through the hermes CLI at all). Replicates exactly what
plugins/memory/mem0/_setup.py's _setup_oss() does when driven by flags:
write mem0.json, write .env, flip config.yaml's memory.provider to mem0.
"""
import json
import pathlib
import re
import sys

HOME = pathlib.Path.home()
LM_STUDIO_URL = "http://100.111.69.102:1235/v1"
OLLAMA_URL = "http://100.111.69.102:11434"
QDRANT_PATH = str(HOME / ".hermes" / "mem0_qdrant")
USER_ID = "xstudio-l2-helpdesk"
LLM_MODEL = "gemma-4-e4b-it"
EMBEDDER_MODEL = "nomic-embed-text"

OSS_CONFIG = {
    "llm": {
        "provider": "openai",
        "config": {"model": LLM_MODEL, "openai_base_url": LM_STUDIO_URL},
    },
    "embedder": {
        "provider": "ollama",
        "config": {"model": EMBEDDER_MODEL, "ollama_base_url": OLLAMA_URL, "embedding_dims": 768},
    },
    "vector_store": {
        "provider": "qdrant",
        # mem0's Qdrant config defaults embedding_model_dims to 1536 (OpenAI's
        # text-embedding-3-small) regardless of the embedder section --
        # confirmed live: without this explicit override, the collection gets
        # created at 1536 dims and every real search against our 768-dim
        # nomic-embed-text vectors fails with a shape mismatch.
        "config": {"path": QDRANT_PATH, "embedding_model_dims": 768},
    },
}

PROFILES = ["l2-investigator", "l2-gemma", "l2-gemma-verifier", "l2-qwen-verifier"]

for profile in PROFILES:
    home = HOME / ".hermes" / "profiles" / profile
    if not home.exists():
        print(f"{profile}: SKIP, no profile dir")
        continue

    mem0_json_path = home / "mem0.json"
    existing = {}
    if mem0_json_path.exists():
        try:
            existing = json.loads(mem0_json_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    existing.update({"mode": "oss", "user_id": USER_ID, "agent_id": "hermes", "oss": OSS_CONFIG})
    mem0_json_path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")

    env_path = home / ".env"
    lines = []
    if env_path.exists():
        lines = env_path.read_text(encoding="utf-8-sig").splitlines()
    if not any(l.startswith("OPENAI_API_KEY=") for l in lines):
        lines.append("OPENAI_API_KEY=lm-studio-local")
    env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Text-only patch -- never round-trip the whole file through a YAML
    # dump, which can silently reformat/reorder an already-tuned config.yaml
    # (comments, key order) even when the data is equivalent.
    config_path = home / "config.yaml"
    text = config_path.read_text(encoding="utf-8")
    if re.search(r"^memory:\s*$", text, re.MULTILINE):
        if re.search(r"^memory:\n(?:[ \t].*\n?)*", text, re.MULTILINE):
            block_match = re.search(r"^memory:\n((?:[ \t].*\n?)*)", text, re.MULTILINE)
            block = block_match.group(1)
            if re.search(r"^\s*provider:", block, re.MULTILINE):
                new_block = re.sub(r"^(\s*provider:).*$", r"\1 mem0", block, count=1, flags=re.MULTILINE)
            else:
                new_block = "  provider: mem0\n" + block
            text = text[:block_match.start(1)] + new_block + text[block_match.end(1):]
    else:
        sep = "" if text.endswith("\n") else "\n"
        text = text + sep + "memory:\n  provider: mem0\n"
    config_path.write_text(text, encoding="utf-8")

    print(f"{profile}: mem0.json + .env + config.yaml written")

print("Done. Restart gateways / new kanban tasks will pick this up.")
