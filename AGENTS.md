# Chitragupta Agent Contract

Hermes is the agent harness. GBrain is the shared XStudio organizational brain. Chitragupta is the XStudio/Helpdesk domain application.

## L2 authority

`Model_Bench/l2_pipeline_runtime.py` is the single deterministic Helpdesk/Kanban lifecycle authority:

```text
eligible ticket -> claim -> investigator -> frozen proposal -> reviewer
review approve -> publish
review reject  -> bounded rework -> fresh review
```

Global SQL WIP is 1. Review priority 30 > rework 20 > new investigation 10.

Its public modes are only `scout`, `reconcile` and `status`. Do not add parallel publisher, repair, reject, audit, nudge or lifecycle wrapper jobs.

## GBrain

The shared brain is `~/.hermes/xstudio-gbrain`.

Hermes owns the native GBrain MCP connection. Autonomous L2 workers receive read-only GBrain tools; the main/operator Hermes may use the full installed GBrain surface.

Do not recreate GBrain search/query/page/graph tooling, synchronization, embeddings or maintenance inside Chitragupta.

L1 and L2 must use the same organizational brain.

## Evidence

Live `xstudio_l2` evidence outranks retrieved material for current incidents.

Canonical/reference material and historical cases may guide an investigation but do not prove current state.

The full Helpdesk/XBatch schema and stored-procedure references under `Reference Documents/` are authoritative engineering evidence and must be preserved.

## Worker boundary

`xstudio-l2-tools` exposes only `xstudio_l2`.

The investigator investigates one already-claimed ticket and completes its own Kanban card with the exact `run_id`, `ticket_id`, `response_type` and non-empty `reply_text`.

The reviewer verifies the exact frozen `proposal_json`, then uses `kanban_complete` to approve or `kanban_block` with one actionable reason to reject.

No procedural L2 skills are required; role SOUL + card contract + typed tools are the active instruction surface.

## Repository discipline

Delete obsolete layers rather than preserving compatibility frameworks indefinitely. A surviving file must have a current caller and own a real domain/environment boundary.

`Model_Bench` is historical naming only. Benchmark programs and custom GBrain wrappers are retired. Move the surviving production code to a final `l2/` package only after this cleaned deployment is proven live.

## Validation

Run:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```
