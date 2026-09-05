---
type: "Mental Model"
title: "Hermes L2 Mental Model"
description: "Current authority split between XStudio Helpdesk, deterministic lifecycle code, read-only L2 workers, review, and publication."
status: current
verified: "2026-09-05"
tags:
  - hermes
  - l2-support
  - mental-model
---

# Hermes L2 Mental Model

## One-line model

```text
XStudio owns L1 and the Helpdesk.
Deterministic code owns claim/review/rework/publication.
Hermes workers investigate and verify live evidence through a typed read-only surface.
Humans act only when the required action is outside L2 authority or the problem genuinely needs L3.
```

Hermes is not a second Helpdesk and the model is not the workflow engine.

## Current runtime shape

```text
Existing XStudio Helpdesk
        |
        v
reconcile-first ticket scout
        |
        v
one claimed SQL run (global WIP = 1)
        |
        v
investigator
  typed xstudio_l2 reads
  + routed project knowledge
  + run ledger
        |
        v
normalize structured completion
        |
        v
deferred reviewer
  frozen proposal_json
  independent live verification
      /       \
 approve     reject
    |          |
    v          v
publisher    rework -> normalize -> fresh reviewer
```

Reviewer cards are not pre-created and are not parent-gated.

## Authority boundaries

### XStudio Helpdesk

`XStudio_Helpdesk.dbo.Complaint_Mst_Tbl` remains the user-visible ticket/workflow record. Existing Helpdesk status and AskStatus semantics are reused rather than replaced.

### Deterministic lifecycle runtime

`Model_Bench/l2_pipeline_runtime.py` owns:

- completion normalization;
- reviewer creation;
- frozen proposal handoff;
- bounded reject/rework cycles;
- approved publication;
- workflow binding;
- orphan recovery;
- WIP admission.

These transitions are not delegated to an LLM.

### Investigator

The investigator is a reasoning/evidence worker. It does not publish tickets and does not own database transport. All database, schema, ticket, and ledger work goes through `xstudio_l2`.

### Reviewer

The reviewer is an independent evidence gate. It approves with `kanban_complete` or rejects with `kanban_block`. It does not publish, reassign, or create rework.

### Publisher

After approval, deterministic code publishes the exact frozen proposal through the audited Hermes SQL path and applies only workflow states allowed by `deploy/helpdesk_workflow_binding.json`.

## L2 database surface is read-only

The worker-facing `xstudio_l2` surface supports bounded reads, discovery, identifier validation, an explicit read-procedure allowlist, ticket/run evidence, and ledger persistence.

It deliberately does **not** expose arbitrary SQL mutation or arbitrary `EXEC`.

If investigation proves that a production/configuration mutation is required:

- return `NEEDS_HUMAN_ACTION` when the cause and required action are known but the worker is not authorized to execute it;
- return `L3_ESCALATION` when the cause remains unresolved or the issue is beyond L2 capability.

A future deterministic corrective-action harness may add explicitly reviewed operations, but a model must never recreate a raw SQL write path itself.

## Knowledge authority

Use sources according to what they are good at:

| Source | Role |
|---|---|
| Live SQL for this ticket | Current incident authority |
| Git-tracked `Knowledge/` | Canonical domain/runtime reference |
| Approved SQL Solution article | Reusable known-issue guidance |
| Problem/ticket history | Episodic and recurring-root-cause evidence |
| mem0 | Compact durable operational heuristics |
| Qdrant | Retrieval index only |

A KB hit, old ticket, snapshot, or memory item is a lead. A current-ticket factual claim must be verified against live evidence when live verification is possible.

## No permanent domain-bot taxonomy

There is one investigator role and one reviewer role. Domain skills route the same workers toward the right evidence surfaces; they do not create a permanent fleet of specialist agents.

## Completion means reviewed publication, not plausible prose

An investigation is not complete because the model says it is done. The lifecycle is complete only when the proposal is structurally reviewable, independently reviewed, and either deterministically published or sent through the bounded rework/escalation path.
