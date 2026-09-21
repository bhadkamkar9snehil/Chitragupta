---
type: "Reference"
title: "Hermes L2 Stored Procedure Catalog"
description: "Current catalog of project-local Hermes L2/L3 SQL procedures, separated by worker, deterministic-runtime, and operator authority."
tags:
  - hermes
  - stored-procedure
  - sql
status: current
verified: "2026-09-05"
---

# Hermes L2 Stored Procedure Catalog

This catalog describes SQL package capabilities. It does **not** imply that every procedure is exposed to an LLM worker.

## Read/discovery procedures

| Procedure | Purpose |
|---|---|
| `Hermes_L2_Discover_Helpdesk_Workflow_Usp` | Discover live ticket/workflow values and workflow-touching objects. |
| `Hermes_L2_Get_Candidate_Tickets_Usp` | Return currently eligible unresolved L2 candidates. |
| `Hermes_L2_Get_Ticket_Context_Usp` | Load one ticket plus readable masters and prior Hermes context. |
| `Hermes_L2_Get_Run_Usp` | Load one Hermes run. |
| `Hermes_L2_Get_Reference_Documents_Usp` | Search existing system reference documents. |
| `Hermes_L2_Find_SQL_Objects_Usp` | Discover tables/views/procedures/functions/triggers by name, column, or definition. |
| `Hermes_L2_Get_SQL_Object_Definition_Usp` | Inspect current object metadata, columns, parameters, definition, indexes, and triggers. |
| `Hermes_L2_Get_Run_Actions_Usp` | Return the ordered audited SQL actions for a run. |
| `Hermes_L3_Get_Open_Escalations_Usp` | Read the human L3 queue. |
| `Hermes_Get_Ticket_Activity_Usp` | Return the ticket activity timeline. |

Worker access to these capabilities is normally through typed `xstudio_l2` operations such as `get_ticket_context`, `get_run_actions`, `find_objects`, `get_definition`, `select`, and `query`, not through model-composed shell/CLI transport.

`xstudio_l2.read_procedure` is separately restricted to its explicit reviewed read-only allowlist; the presence of a procedure in this catalog does not automatically expose it through that operation.

## Deterministic L2 runtime procedures

| Procedure | Purpose | Authority |
|---|---|---|
| `Hermes_L2_Claim_Ticket_Usp` | Atomically claim one eligible ticket and create its active run. | Deterministic scout/runtime |
| `Hermes_L2_Recover_Stale_Runs_Usp` | Recover genuinely abandoned active runs. | Deterministic reconciler/operator |
| `Hermes_L2_Start_Investigation_Usp` | Move a claimed run into investigation state. | Harness |
| `Hermes_L2_Save_Investigation_State_Usp` | Persist structured investigation state/heartbeat. | Harness |
| `Hermes_L2_Heartbeat_Usp` | Refresh active-run heartbeat. | Harness |
| `Hermes_L2_Execute_SQL_Usp` | Audited internal SQL execution primitive. | Harness only; not arbitrary worker access |
| `Hermes_L2_Update_SQL_Action_Evidence_Usp` | Attach before/after evidence to an audited SQL action. | Harness |
| `Hermes_L2_Publish_Response_Usp` | Atomically publish the reviewed structured response and allowed Helpdesk workflow changes. | Deterministic publisher |
| `Hermes_L2_Ask_Question_Usp` | QUESTION convenience wrapper. | Deterministic runtime |
| `Hermes_L2_Resolve_Ticket_Usp` | RESOLUTION convenience wrapper using a real bound resolved status. | Deterministic runtime |
| `Hermes_L2_Escalate_L3_Usp` | Create/update the structured L3 handoff path. | Deterministic runtime |
| `Hermes_L2_Fail_Run_Usp` | Fail an active run and make the ticket eligible according to retry policy. | Deterministic runtime |

The current production lifecycle is centralized in `Model_Bench/l2_pipeline_runtime.py`. The LLM investigator/reviewer does not call publication or workflow procedures directly.

## L3 operator procedures

| Procedure | Purpose | Safety posture |
|---|---|---|
| `Hermes_L3_Update_Escalation_Status_Usp` | Assign/update/resolve/reject one escalation and record human remarks/resolution. | Explicit per-escalation human/operator action. |
| `Hermes_L3_Release_Defect_Escalations_Usp` | Release active L3 blocks that match named historical harness-defect families. | Operator maintenance; dry-run by default; only closes active escalation states; reports effect. |

`Hermes_L3_Release_Defect_Escalations_Usp` exists so cleanup of stale harness-created L3 blocks is a reviewed repeatable procedure instead of an ad-hoc direct UPDATE. Live validation of the queue-deadlock incident showed hundreds of stale escalations had outlived the harness defects that created them; the release procedure was used to separate those from genuine L3 work. It is not part of normal ticket investigation and is not exposed as a worker mutation tool.

## Advanced Helpdesk / governed knowledge procedures

| Procedure | Purpose |
|---|---|
| `Hermes_Log_Ticket_Activity_Usp` | Append a timestamped Helpdesk activity row. |
| `Hermes_Create_Solution_Article_Usp` | Create a reusable governed Solution article. |
| `Hermes_Link_Solution_To_Ticket_Usp` | Link an approved Solution article to a ticket. |
| `Hermes_Create_Problem_Usp` | Create a recurring-root-cause Problem record. |
| `Hermes_Link_Ticket_To_Problem_Usp` | Link a ticket to a Problem. |
| `Hermes_Submit_Ticket_Feedback_Usp` | Record feedback/reopen information. |
| `Hermes_Log_Agent_Trace_Usp` | Persist platform-level trace events drained from the observer plugin. |

These capabilities are not evidence that every reviewed `RESOLUTION` should create a Solution article. The production pipeline deliberately does **not** create one automatically for each response. Solution/Problem promotion follows its own governed knowledge lifecycle.

## Worker mutation boundary

`Hermes_L2_Execute_SQL_Usp` can support audited harness operations, but the agent-facing `xstudio_l2` contract remains structurally read-only for arbitrary SQL:

```text
select/query                  -> bounded reads
find_objects/get_definition   -> discovery/definition reads
validate_identifiers          -> schema validation
read_procedure                -> explicit reviewed read-only allowlist
get_ticket_context/actions    -> run/ticket evidence
save_ledger                   -> ticket-specific investigation ledger
```

Write/DDL/EXEC SQL is rejected at the worker interface. A required production/configuration correction therefore becomes `NEEDS_HUMAN_ACTION` or `L3_ESCALATION` unless and until a narrow reviewed deterministic operation is explicitly implemented.

## Typed tool deployment contract

`xstudio_l2` is provided by the `xstudio-l2-tools` plugin. Live testing established two deployment requirements that are now part of the normal deploy script:

1. the plugin must exist in the shared Hermes plugin directory and be enabled in the root config so toolset discovery recognises the `xstudio_l2` toolset;
2. for the small local L2 profiles, deferred `tool_search` is disabled so this mandatory evidence tool is directly callable rather than hidden behind a discovery hop.

The live end-to-end validation then showed the reviewer actually calling `xstudio_l2` multiple times with no terminal/pip/pyodbc/sqlcmd attempts, rejecting an evidence-poor escalation, and driving deterministic rework.

## Deployment order

The maintainable source files are the numbered SQL files. The generated complete bundle is:

```text
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
```

It already includes the current dispatch and UPDATE-continuation hardening sources (`25_ticket_dispatch_hardening.sql` and `55_update_retry_hardening.sql`). Do not deploy those a second time merely because their numbered source files exist.

After deploying the generated bundle, run:

```text
Knowledge/98_pipeline_postflight.sql
```

Then run the local Hermes validation procedure documented in `Knowledge/VALIDATION.md`.

## Domain-procedure boundary

XBatch/XMES business procedures remain authoritative for their own business logic. During L2 investigation the worker may discover/read their definitions as evidence, but it does not gain permission to execute an unreviewed mutating domain procedure.

For a future deterministic corrective-action operation, use the official-path-first sequence from `Knowledge/sql-write-model.md`: inspect the live definition/signature, explicitly review/allowlist the operation, capture before state, execute through harness-owned code, and verify after state.
