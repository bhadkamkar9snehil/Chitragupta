# Handover: Chitragupta L2 pipeline — quality & reliability findings requiring resolution

**Written:** 2026-09-23, ~09:35 IST, by Claude (Sonnet 5), end of a marathon debugging/audit session.
**For:** a fresh Claude Opus 5.5 session, no prior context beyond this file + the repo's own `AGENTS.md`/`CLAUDE.md`.
**Read `AGENTS.md` first.** It is the stable operating contract (five architectural boxes, Scope Guard, Ponytail audit standard, lifecycle rules). This document does not repeat it — it only adds what AGENTS.md doesn't yet know: findings from tonight's live data audit, and exact next steps.

---

## <mission>

Chitragupta is an autonomous L2 support pipeline for the XStudio Helpdesk (`AGENTS.md` §1). Tonight's session did two things: (1) fixed a live production incident (pipeline-wide crash loop) and did a real complexity/Ponytail refactor pass on the hottest files, and (2) ran a full data-quality audit against the *real* live `Hermes_L2_Response_Trn_Tbl`/`Complaint_Mst_Tbl` tables — not assumptions, actual SQL. That audit surfaced several serious, evidence-backed defects that are still open. **Your job is to resolve the open items in `<open_issues>` below**, in priority order, using the same evidence-before-action standard this session used throughout (verify against real SQL/trace data before concluding something is broken, and before claiming something is fixed).

</mission>

## <what_is_already_fixed_do_not_redo>

These are done, tested, deployed, and confirmed against real live traffic. Don't re-investigate them.

1. **Pipeline-wide crash loop (the original incident).** `recover_failed_workers()` in `Model_Bench/l2_pipeline_runtime.py` now releases a terminated worker's stale SQL local-model lease (via `_finish_local_model_work`, wrapped in `try/except RuntimeError`) before queuing rework, and the fault got isolated per-item across all reconcile-stage loops (`normalize_investigator_completions`, `process_unreviewable_completions`, `process_jev_primary_reviews`, `process_approvals`, `recover_failed_workers`) so one bad run can no longer crash the whole scout tick. Confirmed live: multiple recoveries succeeded automatically in production traffic after deploy.
2. **Cyclomatic-complexity / Ponytail pass**, real overhaul not cosmetic:
   - `Hermes_Orchestrator.py:main()` — CC 129 (807 lines, ~28 unrelated CLI handlers glued into one function) → CC 33 dispatcher + 28 named `_cli_*` handlers, each 6–26. Added 15 new regression tests (`Model_Bench/test_hermes_orchestrator_cli_handlers.py`) — this file had **zero** test coverage before tonight.
   - `xstudio_l2_tools_plugin/__init__.py`: `_pre_tool_call` CC ~40→12, `_submit_proposal_handler` CC 40→10 (split into `_validate_submit_proposal_inputs`/`_derive_proposal_metadata`), `deterministic_ticket_route` in `l2_pipeline_runtime.py` CC 41→10-12 (split into `_route_sap_api`/`_route_work_order`/`_route_heat`).
   - Every split verified: exactly one def + one call site each (no duplication), all existing tests still pass (127 pipeline-runtime + 88 plugin + 17 jev-fabric + 15 new orchestrator tests, all green), deployed via `Model_Bench/deploy_l2_pipeline_runtime.sh`.
3. **Security: hardcoded SQL password removed from `Model_Bench/benchmark_l2_performance.py`** (was `DEFAULT_PASSWORD = "$$Mit@1234"`, a live `sa` credential, committed in `47f084d`, with a GitHub remote configured — **this password is very likely on GitHub right now**). Code fixed to require `--password`/`MSSQL_MCP_PASSWORD` like every other script in the repo. **The user still needs to (a) rotate this SQL password and (b) decide whether to scrub git history** (`git filter-repo`/BFG — deleting the current file version does not remove it from history). This is a standing action item for the user, not something to redo, but confirm it's actually been done before treating this as closed.

</what_is_already_fixed_do_not_redo>

## <open_issues priority="ordered">

Each issue below has: what was found, the exact evidence (query results, examples), where the likely code lives, and what "done" looks like. Verify each against fresh live data before and after any fix — this session's whole methodology was "real command output, not a claim."

### 1. Response-type misclassification — the majority of "UPDATE" outcomes should be RESOLUTION (highest priority, most evidence)

**Finding:** Of 132 published `ResponseType='UPDATE'` rows, **68 (51.5%) explicitly contain the word "RESOLUTION" in their own reply text or investigation summary.** This is not noise — it's the dominant pattern in the UPDATE population. Two distinct causes, confirmed with real row data:

**Cause A (~55 rows) — a harness safety default absorbs real findings.** These rows all carry the exact canned text `"Evidence status: INCOMPLETE. The investigation produced findings that require independent review..."`. Trace this to `_kanban_completion_metadata_guard()` in `Model_Bench/xstudio_l2_tools_plugin/__init__.py` (around line 718 as of tonight's refactor — grep for the function, it moved during the Ponytail pass). It hardcodes `response_type: "UPDATE"` whenever a small model completes with a flat summary instead of the full structured claims contract — a deliberate conservative choice (an unstructured completion can't be auto-trusted), but it means real, correct verification work gets downgraded because the *submission format* failed, not because the *investigation* was incomplete. **Open question you need to answer with real data:** why is `xstudio_submit_proposal` (the structured, harness-assembled submission path, see `_submit_proposal_handler` in the same file) not being used more often instead of the flat-summary fallback firing on ~40%+ of all UPDATE outcomes? Check real trace rows (`ToolName='xstudio_submit_proposal'` in `Hermes_Agent_Trace_Trn_Tbl`, 202 pre/post pairs exist) vs. `kanban_complete` calls that hit the fallback, and find out what's steering Qwen toward the wrong path.

**Cause B (~10-15 rows, more concerning) — Qwen explicitly states a correction and it doesn't take.** Concrete real examples pulled from `InvestigationJson`/`ReplyText`:
- Ticket_269: *"Reworked L2 Ticket_269 to **correct response_type from UPDATE to RESOLUTION**. The investigation only performed READ/VERIFY operations..."* → published as UPDATE anyway.
- Ticket_240 (run `4B806431-2DE1-4926-A6A3-3DCA91C6C372`): *"Addressed rework objection: **corrected response_type from 'UPDATE' to 'RESOLUTION'** since only read verification occurred (no mutation)."* → published as UPDATE anyway. Full row: the live `ReplyText` column is literally `NULL`; the real content only survives in `InvestigationJson` from a prior rejected attempt.
- Ticket_241 (run `60126C1A...`): *"Rework complete: Addressed worker-authority mismatch by correcting response_type from 'UPDATE'... to 'RESOLUTION'"* → published as UPDATE anyway.

This means whatever field the rework/resubmission path actually freezes and publishes is not reading the corrected value Qwen states in its own prose. Find the exact code path: likely in `create_rework_card()` or wherever a rework's prior-context / frozen proposal gets carried forward and re-submitted — check whether `response_type` is being defaulted/copied from a stale template rather than re-read from the current submission. This is the single most fixable, most valuable finding from tonight.

**Also found in the same scan:** Ticket_241 (a different row, run `F2DB9885...`) has raw tool-call scaffolding leaked into the customer-facing reply text: `"RESOLUTION: LRF arc time verified for Heat 1604013\n</result>\n<parameter=summary>\nVerified LRF database records..."`. That `</result>`/`<parameter=summary>` is tool-call XML that should never reach `ReplyText`. Separate, smaller bug, same investigation area.

**How to re-run this evidence yourself:** live SQL access works reliably from the Windows-side Bash shell (not WSL) in this environment — `MSSQL_MCP_SERVER`/`MSSQL_MCP_USER`/`MSSQL_MCP_PASSWORD` are already set in that shell's env, `pyodbc` is installed. Query pattern:
```python
cs = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE=XStudio_Helpdesk;UID={user};PWD={password};TrustServerCertificate=yes;Connection Timeout=15;"
```
Do NOT run ad hoc queries from inside WSL bash — that path hit repeated Kerberos/login-timeout failures tonight; the direct Windows-side path was reliable. Write real `.py` script files to a scratch dir and run them — never inline multi-quoted SQL in a shell one-liner (this repo's own `Agent_Comms/PROTOCOL.md` documents this exact gotcha).

**Done looks like:** re-run the 68-row contradiction query after your fix; the count should drop close to 0 for *new* runs (historical rows won't retroactively fix themselves, that's fine).

### 2. Investigation-stage Qwen reliability is the real bottleneck, not review

**Finding (from `Hermes_L2_Response_Trn_Tbl`, real query):**
| LocalModelPurpose | Completed | Avg queue wait | Avg run time |
|---|---|---|---|
| REVIEW | 87 | 3s | 331s |
| REWORK | 3 | 0s | 286s |
| **INVESTIGATION** | **3** | **3,060s (~51 min)** | 764s |

And: **all 17 of the 37 total FAILED runs** (`ErrorMessage = 'Recovered as stale by Hermes scheduler.'`) were stuck on `LocalModelPurpose = 'INVESTIGATION'` — zero were REVIEW or REWORK. Investigation-purpose local-model work either completes rarely (3 times across 127 tickets) or hangs and gets stale-recovered (17 times) — a >85% "doesn't finish cleanly" rate, while review-purpose work is fast and reliable (87 clean completions, near-zero queue wait). The 51-minute average queue wait before investigation work even starts is consistent with the documented priority order (review 30 > rework 20 > new-investigation 10 — see AGENTS.md §2) starving it under load, but that doesn't explain the high stuck/timeout rate once it *does* start.

**What to check:** why does investigation-purpose Qwen work hang so much more than review-purpose work? Candidates worth checking with real data: context size difference (investigation gets the larger `FOCUSED_REASONING` budget per AGENTS.md §2 — is it too large, causing timeouts?), tool-call loop behavior (does investigation retry/loop more than review?), or a genuine LM Studio/Qwen-side issue specific to longer generation. `Model_Bench/benchmark_l2_performance.py` and `Model_Bench/model_scorecard.py` already exist for this kind of analysis — reuse them (Ponytail: reuse existing ownership) rather than writing new ad hoc tooling.

### 3. Retry loops against phantom/archived tickets waste real compute

**Finding:** top `AttemptNo` values are 15, 12, 9, 8 attempts — and 4 of the top 5 have **no matching row in `Complaint_Mst_Tbl` at all** (orphaned — the parent ticket was archived as synthetic test data while a run was still in-flight, a known cleanup event referenced in several `ErrorMessage` values as `"Retired: parent ticket ... was archived..."`). The retirement handling exists (it does eventually stop these), but it's stopping them only after many wasted attempts. Check whether the retirement detection could run earlier (e.g., at claim/reclaim time rather than only at publish time) to cut the waste.

### 4. Knowledge base: the SQL-backed curated KB has zero content; live git-corpus retrieval fires infrequently

**Finding, confirmed by direct query:** `dbo.Hermes_Solution_Article_Mst_Tbl` — **zero rows**. No solution article has ever been created. Consistent with a second finding: `JevKBCurationJson` is `NULL` on **100% of 159 completed runs** — the post-resolution KB-write step (`Model_Bench/jev_post_resolution_curation.py`, built earlier this same session, wired into `main()`) has never actually fired/written in production. Given only 5 real RESOLUTIONs exist total, low trigger volume is expected, but *zero* writes across even those 5 needs a direct check: either verify it's correctly never triggering (and why), or find the wiring gap.

Separately, the git-committed `Knowledge/` corpus (GBrain-indexed, ~738 pages) IS being retrieved sometimes: real trace rows exist (`ToolName='GBRAIN_APPLICABILITY'`, `EventType='jev_system_one'` in `Hermes_Agent_Trace_Trn_Tbl`) with plausible Jev-judged relevance scores (e.g. one real row: `applicable_k1: 0.88`, `relevant_k1: 0.84` — a genuinely strong candidate). But this only fired **19 times against 120 `JEV_INVESTIGATION` events (~16%)** — meaning ~84% of investigations get zero qualifying KB candidate at all. Check whether that 16% coverage rate is a real reflection of "most tickets have no relevant prior knowledge yet" (plausible, KB is young) or a retrieval-threshold/indexing gap worth tuning. `min_retrieval_score` was recalibrated from 0.70→0.50 earlier this session (`Knowledge/manifest.json`) — check if it needs further tuning, backed by real hit-quality data, not another blind threshold guess.

### 5. `Knowledge/schema_allowlist.json` is stale — missing real live columns/tables

**Finding:** live `Hermes_L2_Response_Trn_Tbl` has 25 real columns not in the allowlist — literally every `Jev*` column (`JevTriageJson`, `JevReviewDecision`, `JevRiskScore`, etc.) and every `LocalModel*` column. The allowlist is also missing entire tables that are referenced directly in code (`Hermes_Solution_Article_Mst_Tbl`, `Hermes_Agent_Trace_Trn_Tbl`). This file backs `Hermes_Orchestrator.py --query`'s "did you mean...?" column-typo-correction feature — it currently cannot suggest any of these real columns. Find the allowlist's generator (search for what produces `Knowledge/schema_allowlist.json` — don't hand-edit a generated file) and regenerate it, or confirm these columns/tables are *deliberately* excluded (e.g., internal-only, not meant for model-facing typo suggestions) before touching anything.

</open_issues>

## <ways_of_working>

- **Read `AGENTS.md` §16a (Ponytail audit standard) and §1a (Scope Guard) before changing anything.** This session's whole value came from small, surgical, evidence-backed changes with full test coverage before deploy — not speculative rewrites. Keep that discipline.
- **Verify before claiming fixed.** Every finding above was confirmed with a real SQL query or real trace row, not inference from code reading alone. Do the same before reporting anything resolved.
- **Test, then deploy, then verify against live traffic.** The pattern that worked all session: make the change → run the relevant test suite (`Model_Bench/test_l2_pipeline_runtime.py`, `Model_Bench/test_xstudio_l2_tools_plugin.py` — note this one uses a **custom runner**, invoke as `python3 test_xstudio_l2_tools_plugin.py` directly, `python3 -m unittest` silently finds 0 tests) → `bash Model_Bench/deploy_l2_pipeline_runtime.sh` → check the next real `ticket_scout` cron tick at `~/.hermes/profiles/l2-investigator/cron/output/25e16b1941aa/` for `"ok": true` and no new errors.
- **Live SQL from the Windows-side shell, not WSL bash**, per the note in issue #1. This was re-confirmed multiple times tonight.
- **Route open-ended research to Antigravity/Codex via `Agent_Comms/`**, per this project's standing protocol (`Agent_Comms/PROTOCOL.md`) — not your own subagents. Design, implementation, and tests are yours to own directly.
- **Report times in IST to the user.** Hard rule, emphasized strongly in this project.
- The user is deeply engaged and technical, has been driving this for a long single session, and reacts badly to hedging or unverified claims presented as fact. Be direct, be concrete, cite real numbers.

</ways_of_working>
