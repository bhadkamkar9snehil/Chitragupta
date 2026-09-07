# Chitragupta — XStudio Support on Hermes

Chitragupta is the XStudio/Helpdesk domain layer running on Hermes.

## Architecture

```text
Laptop Windows
  Hermes Web/Desktop UI

Laptop WSL2
  Hermes backend
  Chitragupta L2 lifecycle
  native GBrain MCP
  ~/.hermes/xstudio-gbrain

Desktop Windows
  LM Studio

Remote Windows VM
  XStudio / Helpdesk SQL Server
```

Hermes owns agent/session lifecycle, Kanban dispatch, gateways, MCP and scheduling.
GBrain owns organizational retrieval, embeddings, graph, ingestion and maintenance.
Chitragupta owns Helpdesk lifecycle semantics and typed XStudio evidence.

## L2

```text
eligible Helpdesk ticket
  -> deterministic claim
  -> investigator
  -> frozen proposal
  -> independent reviewer
     -> approve -> deterministic publish
     -> reject  -> bounded rework -> fresh review
```

Global active SQL WIP is 1. Review priority is 30, rework 20, new investigation 10.

The only scheduled Chitragupta lifecycle command is:

```bash
python3 Model_Bench/l2_pipeline_runtime.py scout
```

The public operator modes are only:

```text
scout
reconcile
status
```

## GBrain

The shared organizational brain is:

```text
~/.hermes/xstudio-gbrain
```

The main/operator Hermes may use the full native GBrain MCP surface. L2 workers use a filtered read surface for search, hybrid query, page/chunk retrieval, links/backlinks, graph/timeline and read-only diagnostics.

There is no Chitragupta GBrain search wrapper, synchronizer or MCP proxy.

L1 and L2 will use this same organizational brain.

## Evidence

Current-ticket truth comes from `xstudio_l2`. GBrain material is reusable reference/history and must not be treated as proof of current state.

The full schema and stored-procedure references under `Reference Documents/` are authoritative engineering evidence and must be preserved.

## History and reusable Solutions

Reviewed approved/rejected/reopened outcomes are materialized as labelled historical cases for GBrain ingestion.

Helpdesk Solutions enter reusable retrieval only when their semantic hash matches `deploy/solution_export_policy.json`.

## Profiles

```text
l2-investigator          Kanban dispatcher only
l2-investigator-primary  investigator: Kanban + xstudio_l2 + native read-only GBrain MCP
l2-reviewer-primary      reviewer: Kanban + xstudio_l2 + native read-only GBrain MCP
```

## Deployment

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

## Validation

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

`Model_Bench` is now only a historical directory name. The benchmark programs are gone. After this cleaned L2 deployment is proven live, the surviving production files can be moved to a final `l2/` package without changing architecture.

## Rule

One owner per responsibility. Do not recreate Hermes or GBrain features inside Chitragupta.
