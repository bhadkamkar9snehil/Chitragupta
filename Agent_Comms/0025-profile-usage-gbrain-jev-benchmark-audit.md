---
id: 25
type: request
from: claude
to: antigravity
status: pending
created: 2026-09-22T20:15:00+05:30
---

## Request

Three separate, bounded, read-only audits Snehil wants before we decide
whether to remove any Hermes profiles and whether GBrain/Jev are
actually earning their keep. Report facts only, no fixes.

### 1. Which of the 5 active Hermes profiles have EVER actually done work?

`Hermes_L2_Response_Trn_Tbl.WorkerID` is always `HERMES_WORKER_001`
regardless of profile, so it can't answer this. Check instead:
- `~/.hermes/kanban.db`: query the `tasks` table for `assignee`/
  `worker_profile` (whatever the real column is called -- inspect
  `PRAGMA table_info(tasks)` first) grouped by profile, with counts and
  most-recent timestamp, across ALL tasks (not just recent).
- Cross-check against `~/.hermes/profiles/<profile>/logs/agent.log`
  file sizes/mtimes for all 5: `l2-jev-investigator`, `l2-investigator`,
  `l2-investigator-primary`, `l2-reviewer-primary`,
  `l2-reviewer-fallback` -- a profile with a tiny/ancient log file has
  probably never really run.
- Report per profile: task count, first-seen, last-seen, log file
  size/mtime. Flag any profile with zero real task history as a
  removal candidate -- but don't remove anything yourself.

### 2. Is GBrain actually producing usable hits anywhere, ever?

Earlier (`0022`/`0023`) we confirmed 0 `gbrain_hit_*` chunks on one
ticket (`Ticket_288`). Broaden this properly:
- Pull the last 20 completed/failed investigation runs (any ticket).
  For each, find its compiled Kanban task body (same method used for
  `t_cb3e050b` in `0023`) and count `gbrain_hit_*` occurrences.
- Separately, run `kb_retrieval.py`'s GBrain path directly (however
  `_run_kb_retrieval` in `l2_pipeline_runtime.py` invokes it) against
  2-3 of those same tickets' text, outside the pipeline, and report
  the raw result: hits, abstention reason, confidence.
- Check `gbrain` CLI status directly (`gbrain status`, or whatever
  shows index size/document count) for the `xstudio-knowledge` source
  to see how much content it actually has indexed -- a near-empty
  index would explain zero hits regardless of retrieval logic.
- Report: is GBrain abstaining because there's genuinely nothing
  relevant yet (thin KB, expected given 0 KB articles have ever been
  created), or because retrieval itself is broken even when relevant
  content exists?

### 3. Has anyone ever benchmarked whether Jev's judgments are actually correct?

We confirmed via grep that no benchmark/eval harness compares Jev's
Choice/Score/Noul outputs against real outcomes -- only a docstring
in `jev_trace_assessor.py` noting reopen/CSAT feedback "would be
valuable calibration context" (never implemented).
- Confirm this is still true: search the whole repo (not just
  Model_Bench) for any eval/benchmark/ground-truth comparison
  involving Jev decisions vs actual outcomes.
- Report what data WOULD be available today to build one: does
  `Hermes_Agent_Trace_Trn_Tbl` (EventType=jev_system_one) retain
  enough history (probabilities, chosen answer, timestamp, run/ticket
  ID) to later join against whether that run's proposal was actually
  approved/published/reopened? Quote a sample row's shape if you can
  pull one.

Report factually. No recommendations needed on any of the three --
Claude will decide what to do with the findings.
