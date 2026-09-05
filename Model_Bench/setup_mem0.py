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
USER_ID = "xstudio-l2-helpdesk"
LLM_MODEL = "qwen/qwen3.5-9b"
EMBEDDER_MODEL = "nomic-embed-text"

PROFILES = ["l2-investigator", "l2-gemma", "l2-reviewer-primary", "l2-reviewer-fallback", "l2-investigator-primary"]

# 2026-09-05: was ONE shared path (~/.hermes/mem0_qdrant) across all 4
# profiles. Real, live bug: Qdrant's local/embedded mode is single-process
# only (a file lock, not a server) -- confirmed live via gateway error
# logs ("Storage folder ... already accessed by another instance") the
# moment two profiles' gateways (both long-running, separate processes)
# tried to touch it around the same time. Since l2-gemma (investigator)
# and l2-gemma-verifier (reviewer) run concurrently by design, this wasn't
# a rare edge case -- it silently broke memory writes/reads for whichever
# profile didn't win the lock, unpredictably. Fix: one embedded Qdrant
# path PER PROFILE. Trade-off: a fact learned by one bot no longer
# automatically appears in another's search results (the "shared
# learning" this project wanted); reliability wins over that until a real
# Qdrant server (multi-process safe) is worth the extra service.

for profile in PROFILES:
    home = HOME / ".hermes" / "profiles" / profile
    if not home.exists():
        print(f"{profile}: SKIP, no profile dir")
        continue

    oss_config = {
        "llm": {
            "provider": "openai",
            "config": {"model": LLM_MODEL, "openai_base_url": LM_STUDIO_URL},
        },
        "embedder": {
            "provider": "ollama",
            "config": {"model": EMBEDDER_MODEL, "ollama_base_url": OLLAMA_URL, "embedding_dims": 768},
        },
        # 2026-09-05: switched from embedded/local-path Qdrant to the real
        # server on 127.0.0.1:6333 (systemd user unit `qdrant.service`, plain
        # binary, no Docker).
        #
        # The per-profile `path` workaround added earlier this session fixed
        # the WRONG level of the problem. It stopped two GATEWAYS fighting
        # over one folder, but kanban workers are separate OS processes from
        # their gateway, so every worker still hit
        #   "Storage folder ... already accessed by another instance of
        #    Qdrant client"
        # and its mem0 tool call failed outright. Confirmed live from a real
        # worker log: the model DID call mem0_search and got that error --
        # memory was never empty because nothing wrote to it, it was empty
        # because every read and write failed on a file lock.
        #
        # A server is multi-process safe by construction, and as a bonus
        # restores the ONE shared store across all profiles (the earlier
        # per-profile split had traded cross-bot learning away for
        # reliability; this needs neither trade).
        "vector_store": {
            "provider": "qdrant",
            # embedding_model_dims must be set explicitly -- mem0 defaults
            # to 1536 (OpenAI's dim) regardless of the embedder section,
            # confirmed live to break search with a shape mismatch once
            # the collection is created at the wrong size.
            # One shared collection on the local server. embedding_model_dims
            # must stay explicit: mem0 defaults it to 1536 (OpenAI's) no matter
            # what embedder is configured, which silently breaks search against
            # nomic-embed-text's 768 once the collection exists at the wrong size.
            "config": {
                "host": "127.0.0.1",
                "port": 6333,
                "collection_name": "hermes_l2",
                "embedding_model_dims": 768,
            },
        },
    }

    mem0_json_path = home / "mem0.json"
    existing = {}
    if mem0_json_path.exists():
        try:
            existing = json.loads(mem0_json_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    existing.update({"mode": "oss", "user_id": USER_ID, "agent_id": "hermes", "oss": oss_config})
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
