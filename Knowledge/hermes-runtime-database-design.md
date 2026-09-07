---
type: "Reference"
title: "Chitragupta L2 Runtime Database Design"
description: "Current SQL persistence and authority boundaries for deterministic L2."
status: current
verified: "2026-09-07"
---

# Chitragupta L2 Runtime Database Design

## Authority split

`XStudio_Helpdesk.dbo.Complaint_Mst_Tbl` remains the user-visible Helpdesk ticket/workflow record.

Hermes owns agent execution and Kanban state. Chitragupta owns deterministic ticket/run transitions. GBrain owns reusable knowledge/history retrieval.

```text
investigator/reviewer
    -> xstudio_l2
    -> current bounded reads/discovery + investigation ledger
    -> no arbitrary SQL write/DDL/EXEC

deterministic L2 runtime
    -> claim/recover/publish/fail/workflow operations
    -> audited Helpdesk SQL path

human/operator
    -> explicit maintenance/L3 operations when required
```

## Core persistence

```text
Complaint_Mst_Tbl
      |
      | ID = TicketID
      v
Hermes_L2_Response_Trn_Tbl
      |
      | ID = RunID
      v
Hermes_L2_SQL_Action_Trn_Tbl
```

`Hermes_L2_Response_Trn_Tbl` is the durable L2 run/response record. It carries claim/liveness, structured investigation state, retry eligibility and eventual response state.

Kanban does not replace this Helpdesk/run persistence; it drives the investigator/reviewer work around it.

## Supporting persistence

Current domain structures include:

```text
Hermes_L3_Escalation_Trn_Tbl     structured L3/human handoff
Hermes_Ticket_Activity_Trn_Tbl   Helpdesk activity history
Hermes_Solution_Article_Mst_Tbl  governed reusable Solutions
```

Older SQL packages may still contain historical trace/experimental structures. Their presence does not make them part of the current Chitragupta architecture; no custom trace-drain or action-planning subsystem is active.

## Worker evidence boundary

The single Chitragupta Hermes plugin provides `xstudio_l2`.

Model-facing operations are intentionally narrow:

```text
select
query
suggest_tables
find_objects
get_definition
validate_identifiers
read_procedure
get_ticket_context
get_run_actions
save_ledger
```

`select`/`query` are bounded reads. `read_procedure` uses an explicit reviewed diagnostic allowlist. Arbitrary SQL writes, DDL and arbitrary EXEC are unavailable through the worker tool.

A known correction outside this interface becomes `NEEDS_HUMAN_ACTION`; an unresolved/beyond-scope problem becomes `L3_ESCALATION`.

## Lifecycle ownership

`Model_Bench/l2_pipeline_runtime.py` is the sole lifecycle implementation:

```text
claim
-> investigator [10]
-> normalize completion
-> reviewer [30] receives frozen proposal_json
   -> approve -> publish + postcondition verification
   -> reject  -> rework [20] -> normalize -> fresh reviewer
```

Global active SQL WIP is 1. `review_cycle` is bounded independently of SQL attempt count.

Public runtime commands are only:

```text
scout
reconcile
status
```

Publication/rejection/recovery/normalization are internal reconciliation steps rather than separately scheduled commands.

## Workflow binding

Canonical file:

```text
deploy/helpdesk_workflow_binding.json
```

Current observed binding:

```text
eligible:                    Enter
resolved:                    Closed
waiting-user AskStatus:      Ask
waiting-user ticket Status:  unbound
L3 ticket Status:            unbound
human-action ticket Status:  unbound
```

Model-provided status overrides are disabled. A `RESOLUTION` cannot publish if the real resolved status is not bound.

## Knowledge/history boundary

Current live ticket facts come from `xstudio_l2`.

GBrain provides canonical/reference material and labelled historical cases. Prior cases and reusable Solutions can guide a current investigation but do not establish current state.

Reviewed outcomes are materialized outside SQL as approved/rejected/reopened historical pages for GBrain ingestion. Reusable Solution export requires an explicit reviewed semantic hash.

There is no custom Mem0/Qdrant stack, raw-session mirror, candidate miner, action-plan framework or Chitragupta-owned GBrain synchronizer in the current L2 architecture.
