---
type: "Reference"
title: "Hermes L2 Runtime Database Design"
description: "Current SQL persistence and authority boundaries for the deterministic Hermes L2 runtime."
tags:
  - hermes
  - l2
  - sql
  - runtime
status: current
verified: "2026-09-05"
---

# Hermes L2 Runtime Database Design

## Authority split

`XStudio_Helpdesk.dbo.Complaint_Mst_Tbl` remains the user-visible ticket/workflow record. Hermes adds structured run, evidence, escalation, activity, and governed-knowledge persistence around that existing Helpdesk.

The key boundary is not whether an internal SQL procedure is technically capable of mutation. It is **which actor is allowed to invoke which surface**:

```text
investigator/reviewer
    -> typed xstudio_l2 surface
    -> bounded live reads/discovery + run ledger
    -> no arbitrary SQL write/DDL/EXEC

deterministic lifecycle runtime
    -> claim/recover/publish/fail/workflow procedures
    -> audited harness-owned SQL transport

human/operator maintenance
    -> explicit reviewed L3/admin procedures
```

The model is not the database policy engine and is not the ticket publisher.

## Core run persistence

```text
Complaint_Mst_Tbl                    existing ticket/workflow master
        |
        | ID = TicketID
        v
Hermes_L2_Response_Trn_Tbl           one row per claimed L2 run/response
        |
        | ID = RunID
        v
Hermes_L2_SQL_Action_Trn_Tbl         audited SQL actions performed by harness code
```

A response row also acts as the durable L2 run row. It carries claim/liveness state, structured investigation state, retry eligibility, and eventual response/completion state. This avoids a second queue/run database alongside the Helpdesk.

Kanban is orchestration state in Hermes; SQL remains authoritative for the ticket/run record.

## Additional support persistence

The SQL package also contains supporting structures including:

```text
Hermes_L3_Escalation_Trn_Tbl         structured L3 handoff / human queue
Hermes_Ticket_Activity_Trn_Tbl       timestamped Helpdesk activity history
Hermes_Solution_Article_Mst_Tbl      governed reusable solution knowledge
Hermes_Agent_Trace_Trn_Tbl           platform-level agent/tool trace sink
```

Problem/feedback/linking structures support history and governance. They do not mean every L2 response becomes a Solution article automatically.

## SQL action audit versus worker capability

`Hermes_L2_Execute_SQL_Usp` is an internal audited execution primitive used by harness code. Its existence does **not** grant investigators or reviewers arbitrary SQL mutation rights.

The worker-facing `xstudio_l2` plugin structurally constrains the model:

- `select` and `query` are read-only;
- write/DDL/EXEC SQL is rejected;
- arbitrary stored-procedure execution is unavailable;
- `read_procedure` is restricted to an explicit reviewed read-only allowlist;
- schema/object discovery and definitions are read operations;
- database targets are allowlisted;
- result size and repeated-failure behavior are bounded;
- terminal attempts to recreate Python/pyodbc/sqlcmd transport are blocked.

A required production/configuration mutation therefore becomes `NEEDS_HUMAN_ACTION` when the cause/action are known, or `L3_ESCALATION` when the safe cause/path remains unresolved.

## Typed-tool discovery is deployment infrastructure

A profile-local plugin copy is sufficient for plugin hooks to run, but live testing showed it is **not** sufficient for Hermes to expose the plugin's toolset. The `xstudio-l2-tools` plugin must also be installed in the shared Hermes plugin directory and enabled in the root Hermes config so toolset discovery recognises `xstudio_l2`.

For the small local 9B L2 profiles, deferred `tool_search` is disabled. A mandatory evidence tool should be directly present in the worker's tool list rather than requiring an extra discovery round trip. These requirements are enforced by `Model_Bench/deploy_l2_pipeline_runtime.sh` and its targeted config patchers.

## Deterministic lifecycle ownership

The central lifecycle is owned by `Model_Bench/l2_pipeline_runtime.py`:

```text
claim one ticket
-> investigator [10]
-> normalize structured completion
-> create reviewer [30] with frozen proposal_json
-> approve -> deterministic publish
   reject  -> rework [20] -> normalize -> fresh reviewer
```

`review_cycle` bounds review/rework independently of SQL `AttemptNo`. Reviewer cards are created only after the source completion is reviewable; there is no pre-created or parent-gated reviewer.

Ticket publication uses the audited SQL runtime only after review approval. Model-supplied ticket status is ignored by default.

## Workflow binding

Current deployment binding:

```text
eligible ticket status:       Enter
resolved ticket status:       Closed
waiting-user AskStatus:       Ask
waiting-user ticket status:   unbound
L3 ticket status:             unbound
needs-human-action status:    unbound
```

Canonical file:

```text
deploy/helpdesk_workflow_binding.json
```

`RESOLUTION` publication fails closed if the resolved status is not bound. Null L3/human-action statuses are not replaced with guessed values.

## L3 maintenance boundary

Per-escalation human decisions use `Hermes_L3_Update_Escalation_Status_Usp`.

`Hermes_L3_Release_Defect_Escalations_Usp` is an explicit operator maintenance procedure for releasing stale L3 blocks whose root cause matches known historical harness-defect families. It defaults to dry-run, only targets active escalation states, and is not an investigator/reviewer tool.

This pattern is intentional: corrective administration should be a narrow reviewed deterministic operation with observable effect, not an ad-hoc direct UPDATE or a model-owned write path.

## Live validation lesson

A Git cleanup is not automatically a deployment cleanup. Live validation found retired lifecycle scripts still present under the deployed Hermes scripts directory after they had been deleted from the repository. The deployment script now removes the known retired copies on every deploy, and local validation fails if they reappear.

The live end-to-end run also verified the intended rejection path: the reviewer used `xstudio_l2`, rejected a proposal that mischaracterised a stale scheduler recovery as a database-access failure, and the reconciler created priority-20 rework with an incremented `review_cycle`.

## Knowledge boundary

- Git-tracked `Knowledge/` is canonical domain/runtime reference.
- SQL Solution articles are governed reusable known-issue knowledge.
- Ticket/problem history is episodic evidence.
- mem0 contains compact durable heuristics only.
- Qdrant is retrieval/indexing, not source of truth.

Current-ticket factual claims still require live evidence when live verification is possible.
