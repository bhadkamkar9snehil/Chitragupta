# Chitragupta — XStudio Support on Hermes

Chitragupta is the XStudio/Helpdesk domain layer running on the Hermes agent harness.

## Physical topology

```text
Laptop Windows
  Hermes Web/Desktop UI

Laptop WSL2
  Hermes backend
  Chitragupta runtime
  GBrain MCP server/client
  ~/.hermes/xstudio-gbrain

Desktop Windows
  LM Studio

Remote Windows VM
  XStudio / Helpdesk SQL Server
```

Hermes owns agent/session lifecycle, Kanban dispatch, gateways, MCP, skills and scheduling.
GBrain owns organizational retrieval, embeddings, graph, ingestion and maintenance.
Chitragupta owns Helpdesk lifecycle semantics and typed XStudio evidence.

## Support flow

```text
L1 (planned)
  shared XStudio GBrain
  known-answer / documentation / known-resolution support
  unresolved -> Helpdesk ticket

L2
  deterministic claim
  -> investigator
  -> frozen proposal
  -> independent reviewer
     -> approve -> deterministic publish
     -> reject  -> bounded rework
```

L1 and L2 share the same organizational GBrain. Do not create separate duplicate knowledge bases.

## GBrain

The installed brain is:

```text
~/.hermes/xstudio-gbrain
```

The main/operator Hermes has the full GBrain MCP surface. Autonomous L2 workers use the same native MCP server with a read-only tool allow-list (`search`, `query`, page/chunk reads, links/backlinks/timeline/graph and read-only diagnostics).

`xstudio-l2-tools` no longer wraps GBrain. It exposes only `xstudio_l2`.

Canonical sources include committed `Knowledge/`, full `Reference Documents/`, governed reusable Solutions and reviewed approved/rejected/reopened historical cases. Full schema and stored-procedure Markdown references are authoritative and must not be deleted.

GBrain maintenance/autopilot owns index/embedding/graph convergence. Chitragupta only materializes domain data that GBrain should ingest.

## Live evidence

Current-ticket truth comes from `xstudio_l2`.

The current Windows bridge remains intentionally because the working SQL transport is:

```text
Hermes in WSL2 -> Windows Python/pyodbc -> remote SQL Server VM
```

It should be removed only after WSL-native SQL connectivity is proven equivalent.

## Learning

Reviewed Helpdesk outcomes are materialized as labelled historical cases. GBrain indexes those cases directly. Chitragupta no longer maintains a candidate-miner/curator pipeline or a second GBrain synchronization framework.

Helpdesk Solutions enter reusable retrieval only when their semantic hash matches `deploy/solution_export_policy.json`.

## Current temporary compatibility

`Model_Bench/l2_gbrain.py` and `kb_retrieval.py` remain only for the old dispatch-time prefetch path in `l2_pipeline_runtime.py`. Workers themselves use native GBrain MCP. These two files are next cleanup targets.

## Profiles

```text
l2-investigator          Kanban dispatcher only
l2-investigator-primary  investigator worker: Kanban + xstudio_l2 + read-only GBrain MCP
l2-reviewer-primary      reviewer worker: Kanban + xstudio_l2 + read-only GBrain MCP
```

## Deployment

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

## Validation

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

## Rule

Keep one owner for each responsibility. Do not recreate Hermes or GBrain features inside Chitragupta.
