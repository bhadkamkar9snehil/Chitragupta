# Chitragupta Architecture

Status: current cleanup branch contract.

## Boundaries

Hermes is the agent harness.

GBrain is the shared XStudio organizational knowledge platform.

Chitragupta owns only:
- deterministic Helpdesk claim/review/rework/publication semantics;
- typed live XStudio/Helpdesk evidence;
- materialization of reviewed support outcomes;
- governed reusable Solution export.

## Runtime

```text
Helpdesk ticket
  -> deterministic claim
  -> investigator
  -> frozen proposal
  -> independent reviewer
     -> approve -> deterministic publish
     -> reject  -> bounded rework
```

`Model_Bench/l2_pipeline_runtime.py` owns these transitions.

## GBrain

The shared brain lives at:

```text
~/.hermes/xstudio-gbrain
```

It is a full GBrain installation using the native Hermes MCP integration.

The operator/default Hermes may use the full surface. L1/L2 service workers use read-only tool filtering through Hermes `mcp_servers.<name>.tools.include`.

Workers can use lexical/hybrid retrieval, page/chunk reads and graph/history reads without receiving page writes, deletes, source administration or brain administration.

GBrain owns its own:
- source synchronization;
- embeddings;
- graph/link extraction;
- maintenance/doctor;
- dream/autopilot.

Chitragupta must not wrap those capabilities in another plugin or scheduler.

## Knowledge sources

Authoritative sources include:
- committed `Knowledge/`;
- `Reference Documents/`, including the full Helpdesk/XBatch schema and stored-procedure Markdown;
- governed reusable Solutions;
- approved/rejected/reopened reviewed historical cases.

Raw source files remain preserved where they provide provenance. Searchable normalized representations should coexist with raw binaries where needed.

L1 and L2 use this same brain.

## Model-facing domain plugin

There is one Chitragupta plugin: `xstudio-l2-tools`.

It registers only:

- `xstudio_l2` — typed XStudio/Helpdesk evidence and investigation-ledger operations.

GBrain tools come directly from Hermes MCP.

## SQL transport

Today the proven path is:

```text
Hermes WSL2 -> Windows Python/pyodbc -> remote SQL Server VM
```

That bridge is a real current environment boundary. It is not deleted until WSL-native ODBC connectivity is demonstrated and tested against both Helpdesk and XBatch access.

## Outcome history

`sync_l2_outcomes.py` materializes reviewed/published/reopened outcomes into labelled historical material.

There is no candidate-mining/curation framework. GBrain can retrieve historical experience directly.

`sync_l2_approved_solutions.py` exports only semantic-hash-approved reusable Helpdesk Solutions.

## Temporary compatibility

The old dispatch-time prefetch still passes through:

```text
l2_pipeline_runtime.py -> Windows kb_retrieval.py -> WSL l2_gbrain.py -> shared GBrain
```

This is explicitly temporary. It is the next retrieval cleanup target because workers now have native GBrain MCP.

## Profiles

- `l2-investigator`: Kanban dispatcher only.
- `l2-investigator-primary`: investigator + typed XStudio + read-only GBrain MCP.
- `l2-reviewer-primary`: reviewer + typed XStudio + read-only GBrain MCP.

## Future L1

L1 should be implemented as another Hermes service profile/application layer using the same GBrain read surface. Its responsibility is conversational support and known-resolution matching, escalating unresolved issues into the existing Helpdesk/L2 lifecycle.

Do not build a separate L1 RAG stack.
