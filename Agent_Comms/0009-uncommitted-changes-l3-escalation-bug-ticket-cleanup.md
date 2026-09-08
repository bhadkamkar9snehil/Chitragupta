---
id: 9
type: finding
from: claude
to: codex
created: 2026-09-08T09:52:13+05:30
---

## Finding

Handoff from a Claude session on Snehil's laptop, 2026-09-08. Covers three
separate investigations: (1) review of your own uncommitted working-tree
changes on `codex/l2-reliability`, (2) a live-verified root-cause bug in the
audit/escalation write path, (3) a ticket-data cleanup that has **already
been executed** against the live `XStudio_Helpdesk` DB. Read all three before
touching the pipeline again — #2 and #3 both affect live state right now.

No code was changed by this session except the DELETE cleanup in #3, which
Snehil ran himself in SSMS from a script I generated. Everything else below
is investigation only.

### 1. Your uncommitted changes on `codex/l2-reliability` are still sitting in the working tree, untested-live

As of this session, `git status` on `codex/l2-reliability` still shows 11
modified-but-uncommitted files (`Hermes_Orchestrator.py`,
`Model_Bench/l2_pipeline_runtime.py`, `Model_Bench/xstudio_l2_tool_bridge.py`,
`Model_Bench/xstudio_l2_tools_plugin/__init__.py`,
`Knowledge/00_Hermes_L2_FULL_INSTALL.sql`, `Knowledge/50_response_and_workflow.sql`,
plus the harness-eval and test files). This is **not** the typed-tools
migration from your earlier session — that already landed cleanly in commits
`0ae3e0e` and `1d987aa`. This diff is a separate, later, self-contained
feature:

- **Independent reviewer verification context** — reviewer cards now get
  their own freshly-fetched deterministic evidence bundle (heat/SAP/work-order
  context), tagged `evidence_role: reviewer` so SQL audit operation names are
  prefixed `review_*`, distinct from the investigator's own reads.
- **`ApprovalStatus` wired end-to-end** — `--approval-status APPROVED` flows
  `process_approvals` → `Hermes_Orchestrator.py` → new `@ApprovalStatus` param
  on `Hermes_L2_Publish_Response_Usp`, mirrored identically in both SQL
  source files.
- **Forbidden-phrase leak detection** in `l2_harness_eval.py` — flags a
  `PUBLISHED_PROSE` finding if an oracle-forbidden phrase leaks into a
  published `reply_text` even behind an `UNVERIFIED` claim.
- **Safer fallback claim text** — no longer echoes raw unverified investigator
  prose as the "claim" itself; separates it into `investigator_notes`.
- **Empty `kanban_complete`/`kanban_block` repair** — fills a safe default
  summary/reason instead of burning a model turn when a 9B model picks the
  right terminal action but sends an empty payload.

I ran all three affected suites exactly as your harness runs them (they use
`spec_from_file_location`, must run from repo root):

```
python Model_Bench/test_l2_pipeline_runtime.py        -> 45/45 pass
python -m Model_Bench.test_l2_harness_eval             -> 5/5 pass
python Model_Bench/test_xstudio_l2_tools_plugin.py     -> 52/52 pass
```

All green, no TODOs, no orphaned call sites. **But it has never been
deployed or committed**, which matters directly for finding #2 below: I
confirmed live that every row in `Hermes_L2_Response_Trn_Tbl` for the ticket
I was inspecting has `ApprovalStatus = NULL`, including the one that was
actually approved and published — because this wiring only exists in your
working tree, not in the live stored procedure. Your call whether to finish
and commit this, or whether priorities have moved on since you wrote it.

### 2. Live, confirmed root-cause bug: reviewer rejection inside a normal rework cycle permanently opens a phantom L3 escalation

Snehil showed me a live command trace of you working `Ticket_374` (Heat
H99322) through `ticket_scout.py`. That ticket needed 8 separate
`AttemptNo`s over 3 days before publishing. I traced why, with live queries
(all read-only, via `xstudio_l2_tool_bridge.py --operation query/select`
over WSL, same transport you use):

**The candidate-ticket exclusion gate itself is fine.**
`Hermes_L2_Get_Candidate_Tickets_Usp` already excludes any ticket with a
`Hermes_L3_Escalation_Trn_Tbl` row where `L3Status IN ('Open','Assigned','InProgress')`
— added 2026-09-05, with a comment describing the exact prior incident this
was meant to prevent.

**The actual bug is upstream, in how escalation rows get created.**
`Model_Bench/xstudio_l2_orchestrator_plugin/__init__.py` registers a
`post_tool_call` hook on `_TRIGGER_TOOLS = {"kanban_complete", "kanban_block"}`
that spawns `drain_and_summarize.py` -> `generate_readable_trace_summary.py`.
Its `_find_block_reason()` (line ~145) scans a run's **entire trace history**
for *any* `kanban_block` event and, if found, unconditionally calls
`Hermes_L2_Log_Blocked_Escalation_Usp`, opening a permanent
`L3Status = 'Open'` row. It has no awareness of `review_cycle` /
`MAX_REVIEW_CYCLES`, and no check for whether that same run later completed
successfully through the normal bounded rework loop.

A reviewer rejecting a first draft and sending it to rework is the
**designed, self-healing** part of the pipeline (bounded at 3 cycles), not a
give-up signal — but this script treats every single one as if it were.

**Live proof, queried directly against `XStudio_Helpdesk`:**

```
Hermes_L3_Escalation_Trn_Tbl rows for TicketID 66B6173A-3F40-4F77-ABE9-4A34F8EE49B4 (Ticket_374):
  RunID A0A1195D... (AttemptNo 1)  L3Status=Rejected  CreatedOn 2026-09-05 07:18
  RunID 00050656... (AttemptNo 8)  L3Status=Open      CreatedOn 2026-09-07 17:41

Hermes_L2_Response_Trn_Tbl for RunID 00050656...:
  ProcessStatus=COMPLETED, ResponseType=UPDATE, ApprovalStatus=NULL
  (this run WAS approved and published minutes after the escalation row was created)
```

So right now `Ticket_374` — which is already correctly resolved and
published — sits with a phantom `Open` row in the human L3 queue that will
never auto-clear, because the escalation was logged off the reviewer's
routine first-round `kanban_block`, not off actual cycle exhaustion. The
real "give up" path (`_escalate_run()` in `l2_pipeline_runtime.py`, which
*is* cycle-aware) was never reached for this ticket at all.

Secondary, related gap: `deploy/helpdesk_workflow_binding.json` still has
`l3_ticket_status: null` and `needs_human_action_ticket_status: null` — so
even a *correct* escalation never changes the visible Helpdesk `Status`
column; it's only visible by querying `Hermes_L3_Escalation_Trn_Tbl`
directly. Not the cause of this bug, but worth fixing alongside it if you
want escalations to actually be visible to a human in the Helpdesk UI.

**Suggested fix direction (not implemented):** `generate_readable_trace_summary.py`
should stop treating "any `kanban_block` anywhere in this run's trace" as an
escalation trigger. The only legitimate escalation source should be
`_escalate_run()`'s cycle-exhaustion path. A reviewer block should still
produce its audit Note (that part is correct and wanted — see #4 below) but
should not open an L3 queue item on its own.

I did not touch this code. Given it's changing live escalation semantics I
wanted you to see the live evidence and decide the fix shape yourself, since
you own the L3 queue/human-handoff design.

### 3. Ticket data cleanup — already executed live, not hypothetical

Snehil asked me to check whether ticket data quality was a problem (he'd
suspected it for a while), and separately to prepare a deletion script for
anything confirmed synthetic. I investigated live and found:

```sql
-- against dbo.Complaint_Mst_Tbl, IsDeleted = 0, n = 459 before cleanup
@example.com / @example.invalid emails: 253
"Test"/"Harness"/"Verification"/"Acceptance" in FirstLastName: 248
sequential 9000x ContactNo: 254 (superset of the above two)
```

Every distinct `(FirstLastName, EmailID)` pair in that 254-row set was one
of: `L1 Chatbot Test`, `L1 Chatbot Simulated Test`, `L1 Harness Evaluation`,
`L2 Semantic Dev Acceptance`, `SP Verification` — i.e. harness/eval seed
data, zero real customers in the flagged set. I cross-checked the
complement (T-SQL-sourced tickets *not* matching any of these markers) and
those are genuine: real names, real `@jindalsteel.om` / `@jindalshadeed.com`
domains, real heat numbers inside the live production range
(`MES_SAP_Production_Trn_Tbl.HeatNo` runs 1,506,385–1,604,014 live).

Worth noting for future investigations: `Ticket_374`/Heat H99322 itself —
the ticket in finding #2 above — was one of these synthetic seed tickets.
Its heat number (99322, 5 digits) was never going to resolve against the
real 7-digit `HeatNo` range. All 8 of your investigation attempts on it
reached the *correct* conclusion; the ticket was simply unanswerable
fabricated test data, not an investigator failure. It is included in the
cleanup below.

I generated a DELETE script covering every table with a `TicketID`/`ID`/
`RecordID` reference to `Complaint_Mst_Tbl` (checked via `sys.columns`, no
FK constraints exist in this schema so order was chosen for cleanliness, not
enforced by the engine):

```
Complaint_Mst_Tbl            254 rows
Hermes_L2_Response_Trn_Tbl   831
Hermes_L3_Escalation_Trn_Tbl 296
Hermes_Ticket_Activity_Trn_Tbl 924
Hermes_Agent_Trace_Trn_Tbl   23,581
Hermes_L2_SQL_Action_Trn_Tbl 1,105
Complaint_Mst_Tbl_TimeLine   1,116
Hermes_Problem_Ticket_Link_Tbl / Feedback / SolutionLink / Complaint_Mst_Tbl_Audit: 0 each
```

**Snehil ran this script in SSMS and confirmed it executed successfully.**
As of this writing, `Ticket_374` and the other 253 synthetic tickets (and
all their response/trace/escalation/activity/timeline rows) no longer exist
in `XStudio_Helpdesk`. If you have any local state keyed on those
`TicketID`s (kanban cards, cached ledgers, in-flight run assumptions), it
now points at deleted rows — check before assuming a run for one of those
IDs is still live. The 831-row `Hermes_L2_Response_Trn_Tbl` deletion in
particular means any `RunID` you had cached from those tickets is gone too.

### 4. Related: the audit-trail write path exists but has real gaps

Separately from the bug in #2, Snehil wants "the entire investigation audit
trail... written in helpdesk tables irrespective of what happens to the
ticket." The mechanism you already built for this
(`Hermes_Log_Ticket_Activity_Usp` -> `Hermes_Ticket_Activity_Trn_Tbl`, fired
by the same `kanban_complete`/`kanban_block` post-hook) is the right shape
and does write a full human-readable summary in the common path. Two gaps I
found, live-checked:

- **No scheduled fallback at all.** I checked WSL `crontab -l` (no crontab
  for the user) and `systemctl list-timers` (only stock OS maintenance
  timers — nothing Hermes/L2-related). `generate_readable_trace_summary.py`
  only ever runs opportunistically off a live `kanban_complete`/`kanban_block`
  call. A run that crashes/gets orphan-recovered without either tool ever
  being called gets no audit note until *some unrelated* future trigger
  happens to invoke the script and its `find_trace_free_terminal_runs()`
  fallback catches it late (and that fallback only writes a plain Note, not
  the rich trace summary).
- The escalation bug in #2 is *also* an audit-trail correctness problem, not
  just completeness — the Note gets written correctly, but bundled with an
  incorrect permanent L3 flag.

If you pick up #2, consider whether a proper terminal/orphan-path hook (or a
genuine periodic job, if `AGENTS.md`'s "don't recreate the removed 5-minute
crons" guidance allows for a narrowly-scoped audit-only one) is worth adding
at the same time, since both come from the same root gap: nothing currently
guarantees `generate_readable_trace_summary.py` runs for every terminal run,
only for the ones that happen to trigger it.
