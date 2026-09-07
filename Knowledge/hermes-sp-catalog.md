---
type: "Reference"
title: "Hermes L2 Stored Procedure Catalog"
description: "Current L2/L3 SQL capabilities separated by worker, deterministic-runtime and operator authority."
status: current
verified: "2026-09-07"
---

# Hermes L2 Stored Procedure Catalog

The SQL package contains more capability than the LLM worker is allowed to invoke. Presence in this catalog is not model permission.

## Read/discovery procedures

| Procedure | Purpose |
|---|---|
| `Hermes_L2_Discover_Helpdesk_Workflow_Usp` | Discover live Helpdesk workflow values. |
| `Hermes_L2_Get_Candidate_Tickets_Usp` | Return eligible unresolved L2 candidates. |
| `Hermes_L2_Get_Ticket_Context_Usp` | Load ticket context and prior Hermes state. |
| `Hermes_L2_Get_Run_Usp` | Load one L2 run. |
| `Hermes_L2_Get_Reference_Documents_Usp` | Search Helpdesk reference-document records. |
| `Hermes_L2_Find_SQL_Objects_Usp` | Discover SQL objects by name/column/definition. |
| `Hermes_L2_Get_SQL_Object_Definition_Usp` | Inspect object metadata/definition. |
| `Hermes_L2_Get_Run_Actions_Usp` | Read a run's audited SQL/action history. |
| `Hermes_L3_Get_Open_Escalations_Usp` | Read the L3/human queue. |
| `Hermes_Get_Ticket_Activity_Usp` | Read ticket activity. |

Investigators/reviewers normally reach relevant evidence through typed `xstudio_l2`, not by executing these procedures directly.

## Deterministic lifecycle procedures

| Procedure | Purpose |
|---|---|
| `Hermes_L2_Claim_Ticket_Usp` | Atomically claim one eligible ticket/run. |
| `Hermes_L2_Recover_Stale_Runs_Usp` | Recover abandoned runs. |
| `Hermes_L2_Start_Investigation_Usp` | Move a run into investigation. |
| `Hermes_L2_Save_Investigation_State_Usp` | Persist investigation state/heartbeat. |
| `Hermes_L2_Heartbeat_Usp` | Refresh run liveness. |
| `Hermes_L2_Execute_SQL_Usp` | Audited internal SQL execution primitive. |
| `Hermes_L2_Update_SQL_Action_Evidence_Usp` | Attach evidence to an audited action. |
| `Hermes_L2_Publish_Response_Usp` | Publish reviewed response/workflow state. |
| `Hermes_L2_Ask_Question_Usp` | QUESTION convenience path. |
| `Hermes_L2_Resolve_Ticket_Usp` | RESOLUTION convenience path. |
| `Hermes_L2_Escalate_L3_Usp` | Structured L3 escalation. |
| `Hermes_L2_Fail_Run_Usp` | Fail/retry an active run. |

These are harness/runtime capabilities. The investigator/reviewer does not publish tickets or gain arbitrary mutation rights from their existence.

## Operator/L3 procedures

| Procedure | Purpose |
|---|---|
| `Hermes_L3_Update_Escalation_Status_Usp` | Human/operator decision on one escalation. |
| `Hermes_L3_Release_Defect_Escalations_Usp` | Dry-run-first cleanup of known historical harness-defect escalation families. |

These are explicit maintenance operations, not normal autonomous-investigation tools.

## Support/knowledge procedures

| Procedure | Purpose |
|---|---|
| `Hermes_Log_Ticket_Activity_Usp` | Append Helpdesk activity. |
| `Hermes_Create_Solution_Article_Usp` | Create reusable Solution content. |
| `Hermes_Link_Solution_To_Ticket_Usp` | Link a Solution to a ticket. |
| `Hermes_Create_Problem_Usp` | Create a recurring Problem record. |
| `Hermes_Link_Ticket_To_Problem_Usp` | Link ticket and Problem. |
| `Hermes_Submit_Ticket_Feedback_Usp` | Record feedback/reopen information. |

A resolved ticket is not automatically a reusable Solution. Reusable Solution retrieval is governed separately by the semantic-hash approval policy.

## Worker-facing mutation boundary

The active `xstudio_l2` operations are:

```text
select/query                  bounded read-only SQL
suggest_tables                schema narrowing
find_objects/get_definition   object discovery
validate_identifiers          schema validation
read_procedure                explicit reviewed diagnostic allowlist
get_ticket_context            current ticket evidence
get_run_actions               current run evidence
save_ledger                   investigation ledger
```

Arbitrary model SQL writes, DDL and arbitrary stored-procedure execution are rejected by the typed boundary.

## Lifecycle implementation

`Model_Bench/l2_pipeline_runtime.py` owns claim/review/rework/publish/recovery ordering. Its public commands are only `scout`, `reconcile`, and `status`.

There are no separate publisher, reject, repair, audit or event-reconciler jobs.

## Tool deployment

`xstudio_l2` is provided by the `xstudio-l2-tools` plugin in each worker profile's Hermes home and enabled in that profile config. The dispatcher profile does not receive it.

For the local 9B worker profiles, `tool_search` is disabled so the small mandatory tool surface is directly available.

Native GBrain MCP provides organizational search/query/page/graph tools; Chitragupta does not recreate them.

## SQL deployment source

The numbered SQL files are maintainable source. The generated bundle is:

```text
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
```

After deploying that bundle, run:

```text
Knowledge/98_pipeline_postflight.sql
```

Then run:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```
