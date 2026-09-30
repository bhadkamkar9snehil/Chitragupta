# Decision: drop Qdrant and mem0

Date: 2026-09-30. Status: accepted, executed.

## Decision

Remove mem0 (Hermes memory provider) and Qdrant (the vector server that only mem0 used). No replacement.

## Evidence (live instance, 2026-09-30)

- Qdrant held one real collection, `hermes_l2`, with 134 points. `mem0migrations` had 0. Newest point: 2026-09-26.
- Almost all entries were auto-extracted run history ("User completed work kanban task t_...", "blocked because the frozen proposal ..."). That is per-ticket state, which AGENTS.md §8 already forbade in shared mem0. The rest was tool-usage advice that AGENTS.md §8a says belongs in code and config.
- Qdrant served nothing but mem0. GBrain is a separate store and `kb_retrieval.py` states it is not mem0.
- mem0 was the last (5th) tier of the evidence hierarchy: "operational hints".

## Reasons

1. **Redundant.** The lifecycle no longer relies on model recall: probes -> harness fact table -> Jev outcome -> fixed reply; the local model runs only on NEEDS_REASONING. Each run gets a dispatch-time bundle (ticket, candidate tables, prior ledger, known solution articles). Cross-ticket learning is KB Candidate -> Approved curation. mem0 was a weaker third path for the same job.
2. **Noise.** What it stored was forbidden content, not heuristics.
3. **Fragile.** mem0 needed a patch inside Hermes's own venv (`apply_mem0_json_object_patch.py`) that every `hermes update` wiped, plus a daily self-healing cron job. Before Qdrant ran as a server, an embedded-lock bug left memory empty for weeks.
4. **Coupled to LM Studio and Linux.** mem0's extraction call went to LM Studio, and Qdrant was a Linux binary under systemd. Both fight the goal of a portable Windows package that launches with nothing connected.
5. **Cost per install.** One more service to install, configure and monitor on every new server.

## Not established

Whether mem0 ever changed a ticket outcome was never measured. The judgment rests on content, design and cost, not on an A/B run.

## What changed

- Removed `deploy/qdrant/`, `patches/apply_mem0_json_object_patch.py`, the mem0 sections of `patches/POST_UPDATE.md`, the "Reapply mem0" cron entry, and `memory: provider: mem0` from all five profile configs.
- Removed mem0/Qdrant from AGENTS.md, CLAUDE.md, README, the state-machine contract and the runtime DB design. `KB_IMPLEMENTATION_PLAN.md` carries an amendment note; its Qdrant/`hermes_kb_v1` phases are withdrawn.
- KB retrieval stays lexical (`Model_Bench/kb_retrieval.py`) plus Jev applicability judgment.

## Reopen when

A measured retrieval-recall failure that lexical retrieval plus GBrain cannot fix. Then design a fresh index against that failure, not this one.
