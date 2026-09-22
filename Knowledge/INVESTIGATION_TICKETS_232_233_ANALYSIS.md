# Deep-Dive Investigation: Live Database Execution Audit for Ticket_232 and Ticket_233

**Database:** `10.2.6.204/XStudio_Helpdesk`  
**Target Tickets:** `Ticket_232`, `Ticket_233`  
**Execution Timestamp:** `2026-09-21 22:14:50 IST` (Database UTC: `2026-09-21 16:44:50`)  
**Repository Branch:** `feature/jev-parallel-pipeline-serialized-qwen`  

---

## 1. Ticket Identification & Helpdesk Context

### Ticket Resolution
- **`Ticket_232`**: ID = `E2A0AB2F-5993-40C4-8BDB-721039B00381`
  - **Brief Details:** EAF Power-On time discrepancy reported for Heat 1604015.
  - **Description:** Shift log shows Heat 1604015 completed melting with recorded `PowerOnTime 47:21` and `PowerOffTime 8:34`. Daily energy dashboard indicates higher than normal electrical consumption. Verification requested for `PowerOnTime`, `PowerOffTime`, and `HeatTime`.
  - **Extracted Entities:** `{"HeatNo": "1604015", "Area": "EAF"}`.
  - **Status in Helpdesk:** `Status = 'Enter'`, `AskStatus = 'Enter'`.
- **`Ticket_233`**: ID = `0F8299FE-9D97-4948-B90B-E6B7956F4346`
  - **Brief Details:** EAF Power-On time discrepancy reported for Heat 1604014.
  - **Description:** Shift log shows Heat 1604014 completed melting with recorded `PowerOnTime 47:35` and `PowerOffTime 7:55`. Verification requested for `PowerOnTime`, `PowerOffTime`, and `HeatTime`.
  - **Extracted Entities:** `{"HeatNo": "1604014", "Area": "EAF"}`.
  - **Status in Helpdesk:** `Status = 'Enter'`, `AskStatus = 'Enter'`.

> [!NOTE]
> In the current 56-ticket Helpdesk population (`Ticket_232` through `Ticket_287`), `Ticket_224` through `Ticket_231` do not exist. Only `Ticket_232` and `Ticket_233` are present.

---

## 2. Per-Run Workload Breakdown

Neither ticket is currently active (`IsActive = 0`). Both completed earlier in the day across multiple attempts.

| TicketNo | RunID | Att | ProcessStatus | ResponseType | Trace Events | API Requests | xstudio_l2 Calls | OK | Error | Blocked | Jev Reviews | ClaimedOn (UTC) | CompletedOn (UTC) |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Ticket_232** | `AF09FCF7...` | 1 | `COMPLETED` | `UPDATE` | 116 | 36 | 31 | 13 | 15 | 3 | 1 | 2026-09-21 16:27:31 | 2026-09-21 16:33:32 |
| **Ticket_232** | `0A57570B...` | 2 | `COMPLETED` | `UPDATE` | 322 | 92 | 83 | 46 | 29 | 8 | 3 | 2026-09-21 16:50:43 | 2026-09-21 17:07:50 |
| **Ticket_232** | `9A2AD1F3...` | 3 | `COMPLETED` | `UPDATE` | 144 | 41 | 32 | 20 | 11 | 1 | 2 | 2026-09-21 17:37:51 | 2026-09-21 17:46:32 |
| **Ticket_232** | `CE0CAD78...` | 4 | `COMPLETED` | `UPDATE` | 124 | 38 | 30 | 13 | 15 | 2 | 1 | 2026-09-21 18:03:41 | 2026-09-21 18:12:15 |
| **Ticket_232** | `1DE39483...` | 5 | `FAILED` | *NULL* | 289 | 83 | 68 | 27 | 36 | 5 | 3 | 2026-09-21 18:30:36 | 2026-09-21 18:44:10 |
| **Ticket_233** | `CCB093C7...` | 1 | `COMPLETED` | `UPDATE` | 341 | 95 | 89 | 33 | 48 | 8 | 3 | 2026-09-21 16:33:35 | 2026-09-21 16:50:40 |
| **Ticket_233** | `B73D0A74...` | 2 | `COMPLETED` | `UPDATE` | 133 | 39 | 24 | 17 | 7 | 0 | 1 | 2026-09-21 17:07:52 | 2026-09-21 17:37:49 |
| **Ticket_233** | `456FA356...` | 3 | `COMPLETED` | `L3_ESCALATION` | 92 | 26 | 22 | 12 | 9 | 1 | 1 | 2026-09-21 17:57:12 | 2026-09-21 18:03:38 |

**Totals:**
- `Ticket_232`: 5 runs, 995 trace events, 290 API requests, 244 tool calls (119 OK, 106 error, 19 blocked), 10 Jev primary reviews.
- `Ticket_233`: 3 runs, 566 trace events, 160 API requests, 135 tool calls (62 OK, 64 error, 9 blocked), 5 Jev primary reviews.

---

## 3. Grouped Failure Signatures & Repetition Analysis

The audit identified 198 tool call failure and blocked events across both tickets. Grouping by exact signature surfaces the worker's operational bottlenecks:

| TicketNo | Status | Failure Signature | Count | First Seen (UTC) | Last Seen (UTC) |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Ticket_232** | `error` | `ValueError: database is required` | **47** | 2026-09-21 10:59:51 | 2026-09-21 13:14:29 |
| **Ticket_232** | `blocked` | `L2 investigation budget exhausted (14 xstudio_l2 calls this session). Stop querying...` | **18** | 2026-09-21 11:00:05 | 2026-09-21 13:14:32 |
| **Ticket_232** | `error` | `ProgrammingError: ('42000', '[SQL Server]Object not found in requested database.')` | **10** | 2026-09-21 11:37:13 | 2026-09-21 13:14:12 |
| **Ticket_232** | `error` | `ValueError: table is required for operation=validate_identifiers` | **10** | 2026-09-21 10:59:27 | 2026-09-21 13:14:23 |
| **Ticket_232** | `error` | `ValueError: search is required for operation=suggest_tables` | **5** | 2026-09-21 11:27:17 | 2026-09-21 13:11:09 |
| **Ticket_232** | `error` | `ValueError: run_id is required for operation=save_ledger` | **4** | 2026-09-21 12:10:16 | 2026-09-21 13:11:38 |
| **Ticket_232** | `error` | `ProgrammingError: ('42S02', "[SQL Server]Invalid object name 'dbo.EAF_PER_HEAT'.")` | **3** | 2026-09-21 10:59:22 | 2026-09-21 12:41:07 |
| **Ticket_232** | `error` | `ValueError: table is required for operation=select` | **3** | 2026-09-21 12:40:38 | 2026-09-21 13:14:17 |
| **Ticket_232** | `error` | `ValueError: columns is required for operation=select` | **3** | 2026-09-21 11:32:51 | 2026-09-21 13:11:19 |
| **Ticket_232** | `error` | `Table/view 'EAF_PER_HEAT' does not exist in the live schema.` | **2** | 2026-09-21 11:25:44 | 2026-09-21 11:37:08 |
| **Ticket_232** | `error` | `Column(s) ['*'] do not exist on dbo.UAT_EAF_ELECTRODECONSUMPTIONPERHEAT.` | **2** | 2026-09-21 11:27:38 | 2026-09-21 11:32:54 |
| **Ticket_232** | `error` | `ProgrammingError: ('42000', '[SQL Server]An expression of non-boolean type... near \'{"column": "HeatID"...\'')` | **2** | 2026-09-21 10:59:18 | 2026-09-21 10:59:44 |
| **Ticket_232** | `blocked` | `Repeated-failure guard: this exact xstudio_l2 call already failed 2 times...` | **1** | 2026-09-21 13:06:50 | 2026-09-21 13:06:50 |
| **Ticket_232** | `error` | Column validation errors (`Duration`, `EnergyKWH`, `HeatNo`, `HeatStartTimeHHMM`) | **7** | 2026-09-21 10:59:12 | 2026-09-21 13:10:08 |
| **Ticket_233** | `error` | `ValueError: database is required` | **26** | 2026-09-21 11:05:40 | 2026-09-21 12:06:13 |
| **Ticket_233** | `blocked` | `L2 investigation budget exhausted (14 xstudio_l2 calls this session). Stop querying...` | **8** | 2026-09-21 11:09:21 | 2026-09-21 12:32:49 |
| **Ticket_233** | `error` | `ValueError: object_name is required for operation=get_definition` | **8** | 2026-09-21 11:14:04 | 2026-09-21 11:19:33 |
| **Ticket_233** | `error` | `ProgrammingError: ('42000', '[SQL Server]Object not found in requested database.')` | **7** | 2026-09-21 11:10:54 | 2026-09-21 12:29:19 |
| **Ticket_233** | `error` | `ValueError: search is required for operation=suggest_tables` | **5** | 2026-09-21 11:10:38 | 2026-09-21 12:31:45 |
| **Ticket_233** | `error` | `ValueError: run_id is required for operation=save_ledger` | **4** | 2026-09-21 11:06:30 | 2026-09-21 12:29:33 |
| **Ticket_233** | `error` | `ValueError: search is required for operation=find_objects` | **3** | 2026-09-21 11:11:06 | 2026-09-21 12:29:17 |
| **Ticket_233** | `error` | `ValueError: table is required for operation=validate_identifiers` | **2** | 2026-09-21 11:09:15 | 2026-09-21 11:11:22 |
| **Ticket_233** | `blocked` | `Repeated-failure guard: this exact xstudio_l2 call already failed 2 times...` | **1** | 2026-09-21 11:16:07 | 2026-09-21 11:16:07 |
| **Ticket_233** | `error` | Column validation errors (`*`, `HeatID`, `HeatNumber`, `PowerOnTime` on wrong tables) | **7** | 2026-09-21 11:08:37 | 2026-09-21 12:32:42 |

### Key Diagnostic Observations:
1. **Primary Operational Mistake (`ValueError: database is required` - 73 total):**  
   The investigator model repeatedly called `xstudio_l2` operations (`query`, `select`, `find_objects`) without explicitly providing the `database` parameter (`XStudio_Xbatch` vs `XStudio_Helpdesk`).
2. **Harness Tool Budget Protection (26 blocks):**  
   When the worker entered unguided query retry loops, the 14-call session budget tripped, preventing context window exhaustion and forcing completion with verified facts.
3. **Database Misdirection (`Object not found in requested database` / `Table does not exist in live schema`):**  
   The model repeatedly searched for plant tables (`dbo.EAF_PER_HEAT`, `dbo.Vw_EAF_Per_Heat_Report_Data`) inside `XStudio_Helpdesk` rather than `XStudio_Xbatch`.
4. **Repeated-Failure Guard Triggers (2 blocks):**  
   The guard prevented infinite loops on identical malformed payloads.

---

## 4. Jev System One Decision Trail

Across all attempts, Jev System One performed semantic triage, execution planning, and primary proposal reviews:

| TicketNo | Att | Recommended Mode | Rec Conf | Evid Suff | Needs Local | Decision | Rev Conf | Risk Score | Reply / Outcome Summary |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Ticket_232** | 1 | *NULL* | *NULL* | *NULL* | *NULL* | `REWORK` | 0.06 | 1.29 | Reply noted schema resolution issues with `dbo.EAF_PER_HEAT`. Jev requested rework. |
| **Ticket_232** | 2 | `FOCUSED_REASONING` | 0.49 | 0.22 | 0.61 | `APPROVE`* | 0.08 | 0.97 | Reply noted `dbo.EAF_PER_HEAT` not in `XStudio_Helpdesk`. Raw Jev choice was APPROVE, but failed safety gates -> local reviewer card dispatched -> local reviewer approved. |
| **Ticket_232** | 3 | `FOCUSED_REASONING` | 0.74 | 0.34 | 0.77 | `REWORK` | 0.20 | 0.92 | Addressed overclaiming certainty. Jev requested rework. |
| **Ticket_232** | 4 | `FOCUSED_REASONING` | 0.36 | 0.49 | 0.72 | `APPROVE`* | 0.25 | 0.94 | Confirmed `dbo.EAF_PER_HEAT` in `XStudio_Xbatch` contains `HeatTime`. Raw Jev choice APPROVE failed safety gates -> local reviewer card dispatched -> local reviewer approved. |
| **Ticket_232** | 5 | `FOCUSED_REASONING` | 0.64 | 0.40 | 0.78 | `REWORK` | 0.66 | 2.66 | **FAILED.** Hit review cycle cap: `"Automated review cycle cap reached after 3 cycles. Proposal overclaims schema verification"`. Escalated to L3. |
| **Ticket_233** | 1 | `FOCUSED_REASONING` | 0.22 | 0.31 | 0.40 | `L3_ESCALATION` | 0.11 | 2.59 | Discovered requested table not accessible in `XStudio_Helpdesk`. Recommended L3. |
| **Ticket_233** | 2 | `FOCUSED_REASONING` | 0.38 | 0.28 | 0.76 | `L3_ESCALATION` | 0.20 | 1.52 | Key finding: data source not accessible in Helpdesk DB; only logbook tables exist. Recommended L3. |
| **Ticket_233** | 3 | `FOCUSED_REASONING` | 0.23 | 0.33 | 0.74 | `REWORK` $\rightarrow$ `L3` | 0.46 | 2.94 | Confirmed `PowerOnTime=47:35`, `PowerOffTime=7:55`, `HeatTime=55:30`. Completed as `L3_ESCALATION`. |

> [!IMPORTANT]
> ***Critical Distinction: Raw Jev Decision vs. Effective Deterministic Action**  
> `Hermes_L2_Response_Trn_Tbl.JevReviewDecision` records the raw choice returned by the TypeSafe Jev API (`answers["decision"]["choice"]`). For Ticket_232 Attempt 2 (conf 0.08, risk 0.97) and Attempt 4 (conf 0.25, risk 0.94), Jev returned `APPROVE`.  
> However, under `Model_Bench/l2_pipeline_runtime.py` (`_jev_primary_review`), direct approval (`safe_approve`) requires:
> - `confidence >= 0.82` (Attempt 2: 0.08, Attempt 4: 0.25)
> - `risk_score <= 0.85` (Attempt 2: 0.97, Attempt 4: 0.94)
> - `evidence_sufficiency >= 0.80` (Attempt 2: 0.22, Attempt 4: 0.49)
> - `overclaiming_risk <= 0.20`  
> Because both attempts failed these deterministic thresholds, direct publication was vetoed. The runtime set `action = "LOCAL_REVIEW"`, creating a local Qwen reviewer card (`l2-reviewer-primary` / `l2-reviewer-fallback`). The *local reviewer* performed independent verification and approved the proposal via `kanban_complete`, which the deterministic publisher then published. Jev did not directly publish these proposals.

---

## 5. Candidate Re-Dispatch Eligibility

Execution of `dbo.Hermes_L2_Get_Candidate_Tickets_Usp @EligibleStatusCsv = 'Enter', @BatchSize = 100` confirmed that **neither ticket is eligible to be picked up again**:

1. **`Ticket_232`**:  
   - Terminal status on Attempt 5: `ProcessStatus = 'FAILED'`.
   - `NextEligibleOn` was set to **`2028-08-16 05:23:10.860`**.  
     *Mechanism:* In `l2_pipeline_runtime.py:1913`, when the review cycle cap (`MAX_REVIEW_CYCLES = 3`) is reached, `_escalate_run` terminates the run by calling `--fail-run --retry-after-minutes 999999`. 999,999 minutes = 694.4 days (~1.9 years), which purposefully places `NextEligibleOn` in August 2028 as an intentional sentinel to prevent the ticket scout from perpetually re-polling the unresolvable incident.
2. **`Ticket_233`**:  
   - Terminal status on Attempt 3: `ProcessStatus = 'COMPLETED'`, `ResponseType = 'L3_ESCALATION'`, `EscalateToL3 = 1`.
   - Tickets with an active escalation or terminal response are excluded by the candidate stored procedure.

---

## 6. L3 Escalation Records

Four escalation records exist across the two tickets in `dbo.Hermes_L3_Escalation_Trn_Tbl`:

| TicketNo | EscalationID | RunID | L3Status | EscalatedOn (UTC) | Problem Summary | Root Cause & Failure Reason |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ticket_232** | `88529FD3...` | `1DE39483...` (Att 5) | `Open` | 2026-09-21 18:44:11 | Questioning electrical consumption and power timing for Heat 1604015. | **Automated review cycle cap reached after 3 cycles.** Proposal overclaims schema verification: cannot verify columns via `xstudio_l2`. |
| **Ticket_232** | `C9649A21...` | `0A57570B...` (Att 2) | `Open` | 2026-09-21 19:40:51 | Questioning electrical consumption and power timing for Heat 1604015. | Reply text claimed verified data in `dbo.EAF_PER_HEAT`, but table does not exist in `XStudio_Helpdesk`. Overclaim caught by review audit. |
| **Ticket_233** | `F9BF1D4F...` | `456FA356...` (Att 3) | `Open` | 2026-09-21 18:03:38 | Discrepancy reported for Heat 1604014. | Verified timings in plant DB; escalated to L3 engineering for operational review. |
| **Ticket_233** | `B2E86524...` | `CCB093C7...` (Att 1) | `Open` | 2026-09-21 19:40:51 | Questioning electrical consumption and power timing for Heat 1604014. | Frozen proposal claimed verification via `xstudio_l2` queries on `EAF_PER_HEAT`, but table does not exist in `XStudio_Helpdesk`. Caught by review audit. |

---

## 7. Conclusions & Harness Validation

1. **Lifecycle Invariant Resilience:** The pipeline correctly prevented infinite loops. When the worker repeatedly failed to resolve the schema across 3 review cycles, the deterministic controller terminated the attempt, marked the run as `FAILED`, persisted the escalation, and backed off `NextEligibleOn` to 2028 (via the 999,999-minute backoff sentinel).
2. **Tool Guard Efficacy:** The 14-call session budget and the 2-strike repeated-failure guard successfully blocked 28 rogue queries, protecting both SQL Server and the LLM context window.
3. **Database Misdirection vs. Evidence Availability:** Early attempts reported that plant data was "unavailable" or "not present in the live schema". This was a false conclusion caused by searching in `XStudio_Helpdesk` rather than `XStudio_Xbatch`. In `XStudio_Xbatch`, `dbo.EAF_PER_HEAT` exists and contains `HeatID` (matching `HeatNo`) and `HeatTime`. The evidence was available; the worker simply searched the wrong database.

---

## 8. Interface Hardening & Before/After Comparison

To eliminate the 198 tool errors and blocked calls exposed by this audit, the `xstudio_l2` contract, bridge validation, and model guidance were hardened:

| Category | Observed in Ticket 232 / 233 (Before) | Hardened Interface (After) | Verification |
| :--- | :--- | :--- | :--- |
| **Missing `database`** | 73 failures (`ValueError: database is required`) | `database` description lists routing rules; turn-level `_pre_llm_call` injects routing guidance; bridge rejects missing `database` with operation-specific error before SQL. | Verified in `test_operations_reject_missing_database_before_sql` |
| **Wrong Database for Plant Data** | Repeated searches for `dbo.EAF_PER_HEAT` in `XStudio_Helpdesk` | Explicit instruction in schema and SOUL: *"Do NOT query XStudio_Helpdesk for plant/EAF/heat data. Use XStudio_Xbatch."* | Added to all 5 SOUL files and turn-level system message |
| **Missing `identifiers`** | 12 calls to `validate_identifiers` without column list | Bridge `_validate_identifiers` requires non-empty `identifiers` (or `columns`) list, raising `ValueError` immediately. | Verified in `test_operations_reject_missing_required_arguments_before_sql` |
| **Missing `ticket` / `parameters`** | Incomplete payloads for `probe_table` and `read_procedure` | Bridge requires `ticket` dict for `probe_table` and `parameters` dict for `read_procedure`. | Verified in unit tests and manual CLI invocation |
| **Missing Operation Fields** | `table`, `columns`, `search`, `object_name`, `run_id` omitted | Comprehensive operation-by-operation required fields documented in schema `operation` description and enforced by bridge `_require`. | 41 unit tests in `Model_Bench/test_xstudio_l2_tools_plugin.py` |
| **LM Studio Tool Compatibility** | Risk of schema rejection with complex JSON schema keywords | Empirical testing confirmed LM Studio rejects `oneOf`/`anyOf` with HTTP 400. Schema preserved as standard flat JSON object with turn-level injection. | Verified in `test_tool_schema_describes_database_routing_and_operation_contracts` |

---

## 9. Post-Fix Live Canary Verification

Following the deployment of the hardened `xstudio_l2` contract, bridge parameter validation, and turn-level database routing instructions (`cca83df`), live canary runs were monitored on the production helpdesk instance to verify behavior in real operational conditions.

### Canary Target Runs

| TicketNo | TicketID | RunID | Attempt | LocalModel TaskID | Role / Stage | Status | Effective Outcome |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **Ticket_241** | `739D297C-C8D6-470D-BCAC-C18ED64A7312` | `F2DB9885-2943-4E89-ABC9-664FF2FACCA9` | 2 | `t_c28297e3` | `l2-jev-investigator` | `COMPLETED` | Direct live query on `XStudio_Xbatch.dbo.LRF_Per_Heat` for Heat 1604013. 2 tool calls, 0 errors. Completed with `kanban_complete`. |
| **Ticket_241** | `739D297C-C8D6-470D-BCAC-C18ED64A7312` | `F2DB9885-2943-4E89-ABC9-664FF2FACCA9` | 2 | `t_1e014b2a` | `l2-reviewer-primary` | `COMPLETED` | Jev primary review requested local review fallback. Reviewer verified live values in `XStudio_Xbatch`, confirmed match, approved via `kanban_complete`. Deterministic publisher published `UPDATE` to SQL. |
| **Ticket_242** | `E1835201-9F31-473D-9F59-E3CFF1654D28` | `7698DD3A-02E7-4417-B0F1-16136D5364E0` | 2 | `t_87dea97f` | `l2-jev-investigator` | `done` | Investigator targeted `XStudio_Xbatch`, retrieved Heat 1604012 timings via `select`, completed cleanly with 0 missing-argument errors. |
| **Ticket_242** | `E1835201-9F31-473D-9F59-E3CFF1654D28` | `7698DD3A-02E7-4417-B0F1-16136D5364E0` | 2 | `t_64e658c1` | `l2-reviewer-primary` | `blocked` | Reviewer called `select` with `HeatNo`. Bridge returned fuzzy suggestion `HeatID`; model immediately corrected. Reviewer blocked with `kanban_block` citing an `ACTION_AUTHORITY` mismatch: `get_run_actions` returned no auditable record of the claimed verification. |
| **Ticket_242** | `E1835201-9F31-473D-9F59-E3CFF1654D28` | `7698DD3A-02E7-4417-B0F1-16136D5364E0` | 2 | `t_2e3cd3ae` (rework cycle 1) | `l2-jev-investigator` (Rework) | `done` | Reconciler converted block to priority-20 rework. Missing `database` on 2 probe calls (`find_objects`, `suggest_tables`) intercepted immediately by bridge before SQL; the resulting retry churn tripped the 14-call session budget block. |
| **Ticket_242** | `E1835201-9F31-473D-9F59-E3CFF1654D28` | `7698DD3A-02E7-4417-B0F1-16136D5364E0` | 2 | `t_e339de75` (rework cycle 2) | `l2-jev-investigator` (Rework) | `done` | 2 clean tool calls, 0 missing-database errors. Reasserted the same `ACTION_AUTHORITY` claim without new corroborating audit evidence. |
| **Ticket_242** | `E1835201-9F31-473D-9F59-E3CFF1654D28` | `7698DD3A-02E7-4417-B0F1-16136D5364E0` | 2 | `t_7cf7b8e1` | `l2-reviewer-primary` | `blocked` | Reviewer re-probed schema (`Hermes_Runs`, `Hermes_L2_SQL_Action_Trn_Tbl` column mismatches), still found no action-trail evidence. Jev primary review issued a 3rd `REWORK`, which hit `MAX_REVIEW_CYCLES = 3` and escalated to L3 at `2026-09-22 07:27:37 UTC` (`Hermes_L3_Escalation_Trn_Tbl.ID = 396CAF39-B5B6-4BCA-9EB0-B85D1CE5D8BB`). This terminal outcome was reached *after* this document's original canary snapshot and is unrelated to the `xstudio_l2` contract defect this audit tracks — see §10 for the full diagnosis. |

### Quantitative Comparison: Pre-Fix (Tickets 232/233) vs. Post-Fix (Canary 241/242)

Aggregated metrics from `dbo.Hermes_Agent_Trace_Trn_Tbl` across all attempts:

> [!IMPORTANT]
> **Corrected 2026-09-22.** The figures below are re-derived directly from `dbo.Hermes_Agent_Trace_Trn_Tbl` with
> `EventType = 'post_tool_call' AND ToolName = 'xstudio_l2'` (one row per actual invocation). The original
> version of this table counted both `pre_tool_call` and `post_tool_call` trace rows for the same invocations,
> doubling the pre/post-fix call counts (758/68), and the missing-required-argument category list summed to
> 47/42 instead of the stated total. The corrected numbers are reproducible with the query in the appendix at
> the end of this section.

| Metric | Pre-Fix Baseline (`Ticket_232` & `Ticket_233`) | Post-Fix Canary (`Ticket_241` & `Ticket_242` Att 2, full RunID scope) | Impact / Assessment |
| :--- | :---: | :---: | :--- |
| **`xstudio_l2` Tool Invocations** (`post_tool_call` only) | **379** (Ticket_232: 244, Ticket_233: 135) | **46** (Ticket_241: 9, Ticket_242 Att2: 37) | Efficient, bounded investigations replacing run-away loops. |
| **OK / Error / Blocked** | 181 / 170 / 28 | 31 / 14 / 1 | Consistent with the reduction above. |
| **Missing `database` Errors** | **73** (`ValueError: database is required`) | **2**, both on the first rework cycle (`t_2e3cd3ae`: one `find_objects`, one `suggest_tables` call); **0** in the fresh investigation, the second rework cycle, or either reviewer stage | **97.3% reduction**; intercepted by bridge before SQL in every case (never reached SQL Server). |
| **Missing Required Argument Errors** (non-`database`) | **49** (`validate_identifiers` table: 12, `select` table: 3 &rarr; table 15; `suggest_tables` search: 10, `find_objects` search: 4 &rarr; search 14; `get_definition` object_name: 8; `save_ledger` run_id: 8; `select` columns: 4) | **0** | **100% elimination** across all investigator and reviewer calls. |
| **Tool Budget / Breaker Blocks** | **28** (26 budget exhausted, 2 repeated-failure breaker) | **1** (single rework-cycle-1 budget cap hit, directly downstream of the 2 missing-`database` retries above; 0 breaker blocks) | Normal sessions use 2–6 calls (well under 14-call cap). |
| **Plant Database Routing Accuracy** | Misdirected to `XStudio_Helpdesk` (reporting tables missing) | All plant/heat queries that reached SQL used `XStudio_Xbatch`. Two bounded-rework tool attempts (`t_2e3cd3ae`) omitted `database` entirely and were rejected by the bridge before SQL execution — see §10. | Correct database selected on first turn in every call that specified one. |
| **Live Evidence Retrieval** | Failed or erroneously concluded tables missing | **100% Success** (`LRF_Per_Heat` retrieved for Heats 1604013 & 1604012) | Real plant records fetched in < 350 ms. |
| **Full Lifecycle Completion** | Blocked on malformed payloads / loop exhaustion | Ticket_241: **Full Success**, published (`COMPLETED`, `UPDATE`). Ticket_242 Att2: reached `MAX_REVIEW_CYCLES = 3` on an unrelated `ACTION_AUTHORITY` audit-trail objection and escalated to L3 — see §10. | The `xstudio_l2` contract defect this audit tracks is resolved independent of Ticket_242's final escalation reason. |

<details>
<summary>Appendix: read-only queries used for the corrected metrics (run via <code>Hermes_Orchestrator.py --query</code>, `XStudio_Helpdesk`)</summary>

```sql
-- Actual invocation counts (post_tool_call only), by ticket/run
SELECT TicketID, COUNT(*) AS PostToolCallCount,
       SUM(CASE WHEN Status='ok' THEN 1 ELSE 0 END) AS OK,
       SUM(CASE WHEN Status='error' THEN 1 ELSE 0 END) AS ErrorCt,
       SUM(CASE WHEN Status='blocked' THEN 1 ELSE 0 END) AS BlockedCt
FROM dbo.Hermes_Agent_Trace_Trn_Tbl
WHERE ToolName='xstudio_l2' AND EventType='post_tool_call'
  AND TicketID IN ('E2A0AB2F-5993-40C4-8BDB-721039B00381','0F8299FE-9D97-4948-B90B-E6B7956F4346')
GROUP BY TicketID;

-- Exact failure-signature counts
SELECT SUBSTRING(ErrorMessage,1,80) AS ErrSig, COUNT(*) AS Cnt
FROM dbo.Hermes_Agent_Trace_Trn_Tbl
WHERE ToolName='xstudio_l2' AND EventType='post_tool_call' AND Status IN ('error','blocked')
  AND TicketID IN ('E2A0AB2F-5993-40C4-8BDB-721039B00381','0F8299FE-9D97-4948-B90B-E6B7956F4346')
GROUP BY SUBSTRING(ErrorMessage,1,80) ORDER BY Cnt DESC;
```

</details>

### Key Observations from Canary Telemetry

1. **Elimination of Database Misdirection:**
   In Ticket_241 (`t_c28297e3`), the investigator immediately issued:
   ```json
   {"operation": "select", "database": "XStudio_Xbatch", "table": "dbo.LRF_Per_Heat", "columns": ["HeatID", "ArcingTime", "PowerONTime", "PowerOFFTime"]}
   ```
   The query executed in 320 ms and retrieved the exact operational metrics:
   `ArcingTime = 22.0000`, `PowerONTime = 25.0000`, `PowerOFFTime = 28.0000`.
   The model did not attempt to query `XStudio_Helpdesk` for plant records.

2. **Self-Correcting Schema Guidance:**
   In Ticket_242 (`t_64e658c1`), the reviewer attempted a `select` using `columns: ["HeatNo"]`. Instead of a generic crash or unhandled SQL exception, the bridge returned:
   ```text
   Column(s) ['HeatNo'] do not exist on dbo.LRF_Per_Heat. Suggestions: {'HeatNo': ['HeatID']}
   ```
   The model immediately self-corrected on the next turn, requesting `["HeatID", "ArcingTime", "PowerONTime", "PowerOFFTime"]`, which executed cleanly in 343 ms.

3. **Autonomous End-to-End Lifecycle Execution:**
   Ticket_241 demonstrated the full intended lifecycle:
   - Investigator retrieved evidence and saved ledger in 2 tool calls.
   - Jev primary review evaluated the proposal: raw choice `REWORK` (`ACTION_AUTHORITY`, confidence 0.75, risk 2.85). Deterministic safety gates vetoed direct approval and correctly dispatched a local reviewer card (`l2-reviewer-primary`, Priority 30).
   - Local reviewer independently verified the evidence in `XStudio_Xbatch`, confirmed accuracy, and completed via `kanban_complete`.
   - The deterministic reconciler and publisher successfully published the response to SQL Server (`Hermes_L2_Response_Trn_Tbl.ProcessStatus = 'COMPLETED'`, `ResponseType = 'UPDATE'`, `IsActive = 0`).

---

## 10. Residual Rework-Only `database` Omission (Ticket_242) — Root Cause and Fix

### 10.1 Exact task chain

RunID `7698DD3A-02E7-4417-B0F1-16136D5364E0` (Ticket_242, Attempt 2):

| TaskID | Role | Stage | Outcome |
| :--- | :--- | :--- | :--- |
| `t_87dea97f` | `l2-jev-investigator` | investigation | `done` — 4 clean `xstudio_l2` calls, 0 errors, verified `XStudio_Xbatch.dbo.LRF_Per_Heat` for Heat 1604012. |
| `t_64e658c1` | `l2-reviewer-primary` | review (cycle 0) | `blocked` — self-corrected a `HeatNo`/`HeatID` column typo, then rejected the proposal on `ACTION_AUTHORITY`: `get_run_actions` showed no audit record of the claimed verification. |
| `t_2e3cd3ae` | `l2-jev-investigator` (rework) | rework (cycle 1) | `done`, but 2 of its `xstudio_l2` calls (`find_objects`, `suggest_tables`) omitted `database` and were rejected by the bridge before SQL; the resulting retries tripped the 14-call session budget block. |
| `t_e339de75` | `l2-jev-investigator` (rework) | rework (cycle 2) | `done` — 2 clean calls, 0 missing-`database` errors; reasserted the same claim without new audit-trail evidence. |
| `t_7cf7b8e1` | `l2-reviewer-primary` | review (cycle 2) | `blocked` — found no new audit-trail evidence either; Jev issued a 3rd `REWORK`, which hit `MAX_REVIEW_CYCLES = 3` and escalated to L3 (`Hermes_L3_Escalation_Trn_Tbl.ID = 396CAF39-B5B6-4BCA-9EB0-B85D1CE5D8BB`, `2026-09-22 07:27:37 UTC`). |

The eventual L3 escalation was for a **different, genuine reason** (an `ACTION_AUTHORITY` audit-trail gap — the reviewer could not find a `Hermes_L2_SQL_Action_Trn_Tbl` record proving the investigator's claimed SQL query actually ran) and is **not** part of the `xstudio_l2` contract defect this audit tracks. It is documented here only because it is the terminal outcome of the same RunID and because the missing-`database` rework failures directly contributed to it: the two rejected calls and the budget block they triggered consumed rework cycle 1 without adding new evidence, which is part of why cycle 2 also had nothing new to show the reviewer.

### 10.2 Context present before rework vs. inside rework

The original investigation task body (`t_87dea97f`) is a Jev-compiled bundle containing pinned live-evidence context plus this closing block (function `_query_instructions()` in `Model_Bench/l2_pipeline_runtime.py`, live-confirmed present at offset 22147 of the task body):

```text
--- Typed XStudio investigation contract ---
Use the xstudio_l2 tool for ALL XStudio/Helpdesk database, schema, ticket, ...
Operations:
  select              validated table+columns read ...
  ...
Pass database explicitly: XStudio_Helpdesk for ticket/Hermes runtime data,
XStudio_Xbatch for production/heat/billet/quality/delay/SAP data.
```

The rework task bodies (`t_2e3cd3ae`, `t_e339de75`), read live from Kanban, contain only:

```text
run_id / ticket_id / ticket_no / review_cycle / rework_source_id /
prior_investigation_task_id / pipeline_stage
REWORK REASON: <the ACTION_AUTHORITY objection text>
PRIOR FINDINGS (verbatim): <persisted ledger JSON — source, summary, response_type, reply_text>
```

`create_rework_card()` (`Model_Bench/l2_pipeline_runtime.py`, previously ending right after the `PRIOR FINDINGS` block) never called `_query_instructions()`. The database name `XStudio_Xbatch` appears in the `PRIOR FINDINGS` ledger, but only twice, as free-text prose inside a disputed evidentiary claim ("queried `XStudio_Xbatch.dbo.LRF_Per_Heat` and confirmed...") — never as a structured field, and never alongside the operation list or the explicit "pass `database` explicitly" instruction. Confirmed live: the reviewer task bodies (`t_64e658c1`, `t_7cf7b8e1`) also lack `_query_instructions()`, and reviewers issued 0 missing-`database` errors — but reviewer calls are narrow `select`/`get_run_actions` validations against a table already named in the proposal under review, not open-ended `find_objects`/`suggest_tables` schema discovery, so the two situations are not directly comparable.

The active profile SOUL (`deploy/profiles/l2-jev-investigator/SOUL.md`, shared by both investigation and rework because both use `INVESTIGATOR_PROFILE`) does carry a persistent, general "Database Routing" section instructing the model to "always specify the correct `database`". This means the omission was **not** a total absence of guidance — the model had a standing system-level reminder — but it lost the per-task, operation-adjacent reinforcement (the same reinforcement whose addition, per §8 of this document, is what eliminated the 73 pre-fix missing-`database` failures in the investigation stage). The omission occurred specifically on `find_objects` and `suggest_tables` — the two open-ended discovery operations that require deciding a target database from reasoning rather than reusing one already bound to a known table/proposal.

### 10.3 Answering the diagnosis questions

- **Was `XStudio_Xbatch` present in the rework body?** Yes, but only as unstructured prose inside `PRIOR FINDINGS`, not as a directive.
- **Was `dbo.LRF_Per_Heat` present?** Yes, same caveat.
- **Was the prior ledger carried?** Yes, via `_persist_rejected_ledger()` → `PRIOR FINDINGS (verbatim)`.
- **Was database context dropped by `create_rework_card()`?** The *structured, operation-adjacent* routing reminder (`_query_instructions()`) was dropped; the free-text mention in the ledger was not.
- **Did the rework model receive the hardened tool guidance?** Partially: the persistent SOUL-level routing sentence, yes; the per-task typed-tool contract block with the explicit operation list, no.
- **Were the two malformed calls repeated or distinct?** Distinct operations (`find_objects` once, `suggest_tables` once), each failing exactly once — not a repeated-failure-guard pattern.
- **Did they touch SQL?** No. Both raised `ValueError: database is required for operation=...` inside the bridge's own pre-SQL validation (`Model_Bench/xstudio_l2_tool_bridge.py`), before any `pyodbc` call.
- **Why was the 14-call budget reached?** The two rejected calls plus their surrounding retry/discovery churn in `t_2e3cd3ae` (schema probing after the `ACTION_AUTHORITY` objection) accumulated to the 14-call session cap; the budget guard then fired correctly and stopped the session rather than looping further.

### 10.4 Root cause

Reproducible propagation defect, not an isolated model lapse: `create_rework_card()` is the only card-construction path that omits the typed-tool contract block (`_query_instructions()`) that `_investigator_task_spec()` already gives every fresh investigation. This is structural — every rework card is built this way, not just this one instance — and it correlates with the observed failure mode (both omissions on the two discovery-style operations the block exists to guide).

### 10.5 Fix decision

**Code change made.** The gap is a verified, reproducible content-propagation defect (missing reminder text), not a case of the model ignoring context that was actually given to it in the rework card. The smallest sufficient fix is to give `create_rework_card()` parity with `_investigator_task_spec()` by reusing the existing `_query_instructions()` helper — no new tool, service, taxonomy, threshold, or inferred/defaulted database value.

### 10.6 Implementation

- `Model_Bench/l2_pipeline_runtime.py`, `create_rework_card()`: append `_query_instructions(run_id, ticket_id)` to the rework card body, after `PRIOR FINDINGS`, identical to how `_investigator_task_spec()` already appends it to fresh investigation cards.
- `Model_Bench/test_l2_pipeline_runtime.py`: added `test_rework_card_carries_same_typed_tool_contract_as_investigation`, asserting the rework spec body contains the typed-tool contract text and the explicit "Pass database explicitly" line.

No changes to thresholds, WIP, priorities, the review-cycle cap, bridge validation, or architecture.

### 10.7 Test results

```text
python3 -m unittest -v Model_Bench.test_l2_pipeline_runtime      -> 52 tests, OK (new test included)
python3 Model_Bench/test_xstudio_l2_tools_plugin.py               -> 41 tests, OK
python3 Model_Bench/test_jev_fabric.py                             -> 15 tests, OK
python3 Model_Bench/test_kb_retrieval.py                           -> 11 tests, OK
bash Model_Bench/validate_l2_pipeline_local.sh --fast              -> FAST LOCAL GATE PASSED
bash Model_Bench/deploy_l2_pipeline_runtime.sh                      -> deployed, 4 gateways restarted and active
bash Model_Bench/validate_l2_pipeline_local.sh --live-only          -> FULL/LIVE VALIDATION COMPLETE (dry-run reconcile only; no mutation)
```

### 10.8 Success criteria status

The tested rework path now carries the same `database` routing reminder as a fresh investigation. Whether this reduces the omission rate to zero in production can only be confirmed by the next naturally arriving ticket that goes through a rework cycle with an open-ended schema-discovery operation — this was not manufactured or force-triggered, consistent with §15 of `AGENTS.md`.
