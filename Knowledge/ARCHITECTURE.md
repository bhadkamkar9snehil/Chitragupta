# Chitragupta Architecture

Status: current L2 production contract.

## Ownership

Hermes is the only agent harness. It owns model execution, sessions, Kanban, gateways, MCP, profiles and scheduling.

GBrain is the shared XStudio organizational brain. It owns retrieval, embeddings, graph/link processing, ingestion and maintenance/autopilot.

Chitragupta owns only XStudio/Helpdesk-specific behavior:

- deterministic L2 ticket lifecycle;
- typed live XStudio/Helpdesk evidence through `xstudio_l2`;
- reviewed outcome materialization;
- governed reusable Helpdesk Solution export.

## L2 lifecycle

```text
eligible Helpdesk ticket
  -> deterministic claim
  -> investigator
  -> normalized structured proposal
  -> reviewer receives frozen proposal_json
     -> approve -> deterministic publish + postcondition check
     -> reject  -> bounded rework -> fresh reviewer
```

Global active SQL WIP is 1. Priorities are review 30, rework 20, new investigation 10. Review/rework is bounded to three cycles total.

`Model_Bench/l2_pipeline_runtime.py` is the single lifecycle implementation. Its public modes are only `scout`, `reconcile`, and `status`.

## Worker responsibilities

Investigator:
- receives one already-claimed ticket/run;
- uses `xstudio_l2` for current live evidence;
- uses native GBrain MCP when reusable knowledge/history helps;
- completes its own Kanban card with structured proposal metadata.

Reviewer:
- reviews the exact frozen proposal;
- independently verifies the smallest sufficient current evidence set;
- approves with `kanban_complete` or rejects with `kanban_block` and one actionable reason.

Neither worker publishes Helpdesk state.

## GBrain

Shared brain:

```text
~/.hermes/xstudio-gbrain
```

The operator/default Hermes may use the full installed GBrain surface. Autonomous L2 workers receive a filtered read surface through native Hermes MCP.

There is no Chitragupta GBrain search wrapper, custom MCP proxy, embedding service, synchronizer, candidate-memory framework, Mem0/Qdrant stack, or raw-session mirror.

Authoritative searchable material includes:
- committed `Knowledge/`;
- `Reference Documents/`, including full Helpdesk/XBatch schemas and stored procedures;
- governed reusable Solutions;
- approved/rejected/reopened reviewed cases.

Historical material is a lead, not current-ticket proof.

## XStudio tool boundary

The one Chitragupta Hermes plugin is `xstudio-l2-tools`. It registers only `xstudio_l2`.

The typed interface exposes bounded reads/discovery and run-ledger operations. Arbitrary SQL mutation, DDL and arbitrary stored-procedure execution are not model-facing capabilities.

## Profiles

- `l2-investigator`: Kanban dispatcher only.
- `l2-investigator-primary`: investigator worker with Kanban, `xstudio_l2`, and native read-only GBrain MCP.
- `l2-reviewer-primary`: reviewer worker with Kanban, `xstudio_l2`, and native read-only GBrain MCP.

The retired reviewer-fallback profile is not part of the current topology.

## Scheduling

The only scheduled Chitragupta lifecycle command is:

```text
l2_pipeline_runtime.py scout
```

Scout reconciles existing work before claiming anything new. Publication, rejection handling, completion normalization and orphan recovery are internal lifecycle steps, not separate jobs.

GBrain owns its own maintenance scheduling.

## Outcome history

`sync_l2_outcomes.py` materializes reviewer/publisher outcomes as explicitly labelled approved, rejected and reopened historical cases.

`sync_l2_approved_solutions.py` exports only Solutions whose live semantic content hash matches the reviewed Git policy.

Neither mechanism grants historical content authority over current live evidence.

## Future L1

L1 will be another application/profile layer over the same Hermes + GBrain foundation. It will not get a duplicate RAG stack or duplicate organizational brain.
