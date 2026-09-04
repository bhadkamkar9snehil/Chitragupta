---
type: "Reference"
title: "Hermes L2 Stored Procedure Catalog"
description: "Catalog of the project-local stored procedures supplied with the Hermes L2 SQL package."
tags:
  - "hermes"
  - "stored-procedure"
  - "sql"
status: draft
---

# Hermes L2 Stored Procedure Catalog

| Procedure | Purpose | Mode |
|---|---|---|
| `Hermes_L2_Discover_Helpdesk_Workflow_Usp` | Discover live ticket states, ticket-touching SPs/triggers and recent workflow samples | Read |
| `Hermes_L2_Get_Candidate_Tickets_Usp` | Return unresolved L2 candidates in existing priority/age order | Read |
| `Hermes_L2_Claim_Ticket_Usp` | Atomically claim one ticket and create one active Hermes run/response row | Write Helpdesk |
| `Hermes_L2_Recover_Stale_Runs_Usp` | Release abandoned Hermes claims for retry | Write Hermes |
| `Hermes_L2_Get_Ticket_Context_Usp` | Load ticket + readable masters + previous Hermes responses/actions | Read |
| `Hermes_L2_Get_Run_Usp` | Load one Hermes run and its actions | Read |
| `Hermes_L2_Get_Reference_Documents_Usp` | Search existing systemreferencedocuments without a RAG layer | Read |
| `Hermes_L2_Find_SQL_Objects_Usp` | Search current tables/views/SPs/functions/triggers by name, column or definition | Read |
| `Hermes_L2_Get_SQL_Object_Definition_Usp` | Inspect current object metadata, columns, params, definition, indexes and triggers | Read |
| `Hermes_L2_Start_Investigation_Usp` | Move claimed run to investigating | Write Hermes |
| `Hermes_L2_Save_Investigation_State_Usp` | Persist route/findings/root cause/intermediate state and heartbeat | Write Hermes |
| `Hermes_L2_Heartbeat_Usp` | Refresh active-run heartbeat | Write Hermes |
| `Hermes_L2_Execute_SQL_Usp` | Execute arbitrary read/SP/write/DDL SQL against a named current database and audit it | Read/Write |
| `Hermes_L2_Update_SQL_Action_Evidence_Usp` | Attach before/after JSON evidence to an executed SQL action | Write Hermes |
| `Hermes_L2_Get_Run_Actions_Usp` | Return ordered SQL actions for a run | Read |
| `Hermes_L2_Publish_Response_Usp` | Atomic structured response publication + optional existing Helpdesk state update | Write Helpdesk |
| `Hermes_L2_Ask_Question_Usp` | Convenience wrapper for QUESTION | Write Helpdesk |
| `Hermes_L2_Resolve_Ticket_Usp` | Convenience wrapper for RESOLUTION + existing resolved/closed status | Write Helpdesk |
| `Hermes_L2_Escalate_L3_Usp` | Convenience wrapper for L3 escalation + existing L3 status; also snapshots the full investigation package into `Hermes_L3_Escalation_Trn_Tbl` (2026-09-03) | Write Helpdesk |
| `Hermes_L2_Fail_Run_Usp` | Close failed attempt and make it retryable after a delay | Write Hermes |
| `Hermes_L3_Get_Open_Escalations_Usp` | Human L3 work queue: return Open/Assigned/InProgress escalations (or a specific status) with full structured evidence | Read |
| `Hermes_L3_Update_Escalation_Status_Usp` | Human L3 workflow: assign, move status, record remarks/resolution on one escalation row | Write Helpdesk |

**Views (2026-09-03):** `Hermes_L2_Investigation_Metrics_Vw` (per-run duration, SQL action count, outcome), `Hermes_L2_Worker_Performance_Summary_Vw` (per-WorkerID rollup -- **note: only 3 generic WorkerID values exist today, real per-model bot labels from the Kanban path aren't wired into this column yet**), `Hermes_L3_Escalation_Turnaround_Vw` (human resolution time by L3Status), `Hermes_L2_Ticket_Resolution_Vw` (per-ticket time-to-first-response/time-to-resolve, no invented SLA targets), `Hermes_L2_Resolution_Time_By_Priority_Vw`, `Hermes_L2_Resolution_Time_By_Type_Vw`.

**Advanced Helpdesk enhancements (2026-09-03)** -- modeled on mature ITSM systems (ServiceNow/Zendesk/Jira Service Management class), none of this existed before:

| Procedure | Purpose | Mode |
|---|---|---|
| `Hermes_Log_Ticket_Activity_Usp` | Append one timestamped activity row (Note/StatusChange/Escalation/Resolution/Reopen/SolutionLinked/ProblemLinked) -- the real work-log a human reviewing ticket history needs, replacing the single overwritable `SupportExecutiveRemarks` field | Write Helpdesk |
| `Hermes_Get_Ticket_Activity_Usp` | Full activity timeline for one ticket, ordered | Read |
| `Hermes_Create_Solution_Article_Usp` | Create a reusable knowledge-base entry (problem/root cause/resolution steps), independent of any one ticket | Write Helpdesk |
| `Hermes_Link_Solution_To_Ticket_Usp` | Link a ticket to a solution it used, increments the solution's `UsageCount`, auto-logs a `SolutionLinked` activity | Write Helpdesk |
| `Hermes_Create_Problem_Usp` | Create a Problem record -- one root cause behind N recurring incidents | Write Helpdesk |
| `Hermes_Link_Ticket_To_Problem_Usp` | Link a ticket to a Problem, auto-logs a `ProblemLinked` activity | Write Helpdesk |
| `Hermes_Submit_Ticket_Feedback_Usp` | CSAT rating / reopen record; a reopen auto-logs a customer-visible `Reopen` activity | Write Helpdesk |

New reference tables (no SP wrapper needed, query directly): `Hermes_Root_Cause_Category_Mst_Tbl` (10 seeded categories -- controlled taxonomy replacing free-text `SuspectedCause`), `Hermes_Escalation_Rule_Mst_Tbl` (priority x elapsed-time escalation config -- **not yet wired to any cron/SP, config only for now**).

**2026-09-03, later same day -- CLI access gap closed.** Confirmed real bug: `--query` refuses *any* `EXEC` (including harmless read SPs), so several SPs that already had a working Python client method had **zero way for a bot to actually call them** -- `Hermes_L2_Find_SQL_Objects_Usp`, `Hermes_L2_Get_SQL_Object_Definition_Usp`, `Hermes_L2_Get_Reference_Documents_Usp`, `Hermes_L2_Get_Run_Actions_Usp` were all dead code from the bot's perspective. Added CLI flags for all of them, plus the new advanced-Helpdesk SPs: `--search-solutions`, `--log-activity`, `--create-solution`, `--link-solution`, `--get-activity`, `--list-root-cause-categories`, `--create-problem`, `--link-problem`, `--find-sql-objects` (+`--object-type`, `--target-database`), `--get-sql-object-definition` (+`--schema-name`), `--get-reference-documents` (+`--area`), `--get-run-actions`. All smoke-tested live.

**Wired into the skills (both investigator and reviewer, v0.3.0):**
- Investigator (`xstudio-l2-ticket-workflow`): checks `--search-solutions` before investigating (step 3.5), logs a work-log `Note` via `--log-activity` before every handoff (step 5.5).
- Reviewer (`xstudio-l2-draft-verifier`): mandatory (not conditional) claim verification via `--get-run-actions` (catches a claim with no real query behind it) and `--get-sql-object-definition` (catches a mischaracterized view), plus its own `--search-solutions` check for silent KB contradictions (step 3.5).
- **`Model_Bench/kanban_approval_publisher.py`** (the deterministic, no-LLM publish script) now also logs the activity entry and, on a genuine `RESOLUTION`, creates + links a solution article -- deliberately gated HERE, not in the investigator's own judgment, since the claim isn't verified until it reaches this point (real approval + real publish).

## Deployment order

```text
00_tables_and_indexes.sql
10_helpdesk_discovery.sql
20_ticket_dispatch.sql
30_context_and_live_discovery.sql
40_investigation_runtime.sql
50_response_and_workflow.sql
99_postflight.sql
```

Or deploy:

```text
00_Hermes_L2_FULL_INSTALL.sql
```

in `XStudio_Helpdesk`, then run `99_postflight.sql`.

## Important boundary

These are Hermes support procedures.

They do **not** replace existing XBatch/XMES business procedures. When an incident requires
a business-system correction, Hermes discovers and inspects the current domain SP and can
execute that SP through `Hermes_L2_Execute_SQL_Usp`.

Examples present in the supplied XBatch snapshot include:

```text
XMES_SAP_Posting_Sequence_Usp
XMES_I_API_Transaction_Summary
XMES_Get_API_Transaction_Summary
Xbatch_HEAT_Tracking
XMES_BilletPosting_Validation_Usp
XMES_SAP_*_API_Error_Usp
SP_XBatch_YMS_*
XBatch_RM_*
```

Their live definitions remain the source for what they actually do.
