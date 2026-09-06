# Chitragupta Agent Contract

Hermes is the agent harness. GBrain is the shared XStudio organizational brain. Chitragupta is the XStudio/Helpdesk domain application.

## Authority

`Model_Bench/l2_pipeline_runtime.py` is the single deterministic Helpdesk/Kanban lifecycle authority:

```text
eligible ticket -> claim -> investigator -> frozen proposal -> reviewer
review approve -> publish
review reject  -> bounded rework -> fresh review
```

Global SQL WIP is 1. Review priority 30 > rework 20 > new investigation 10.

Do not add parallel publisher, repair, review-board, nudge, trace, memory, action-planner or GBrain-synchronizer subsystems.

## GBrain

The shared brain is `~/.hermes/xstudio-gbrain`.

Hermes owns the native GBrain MCP connection. The main/operator Hermes may use the full GBrain surface. Autonomous service workers receive read-only MCP tools only.

Do not recreate GBrain search/query/page/graph tooling as a Chitragupta plugin. `xstudio-l2-tools` exposes only `xstudio_l2`.

L1 and L2 must use the same organizational brain. Do not create an L1 copy of the knowledge corpus.

GBrain owns source synchronization, embeddings, graph extraction, maintenance and dream/autopilot. Chitragupta may materialize reviewed Helpdesk outcomes and governed Solutions for GBrain to ingest.

## Evidence

Live `xstudio_l2` evidence outranks retrieved material for current incidents.

Canonical/reference material and prior cases can guide the investigation but historical similarity is not proof of present state.

The full Helpdesk/XBatch schema and stored-procedure documents under `Reference Documents/` are authoritative engineering evidence. Preserve them.

## SQL boundary

The current Windows bridge is retained because Hermes runs in WSL2 while the proven SQL transport uses Windows Python/pyodbc to the remote SQL Server VM. Do not remove it until a WSL-native SQL path is tested successfully.

The model may not build arbitrary connection strings, run DDL/writes, install drivers, or bypass the typed XStudio interface.

## Repository discipline

Delete obsolete layers rather than retaining compatibility frameworks indefinitely. A surviving file must have a current caller and own a real domain/environment boundary.

`Model_Bench` is historical naming. Once the remaining runtime stabilizes, move production code out of it and remove the directory.

The remaining `l2_gbrain.py`/`kb_retrieval.py` pair is temporary compatibility for dispatch-time prefetch and is an explicit cleanup target.

## Validation

Run:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Update deployment and validation whenever runtime components are removed or consolidated.
