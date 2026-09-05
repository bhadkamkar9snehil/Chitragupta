# Work plan: event-driven orchestration, observability, memory & knowledge (2026-09-05)

Written after the first-ever full end-to-end ticket resolution succeeded
(Ticket_343, see "Baseline" below). Documents what is actually broken or
missing, grounded in live checks — not aspirations. Work starts after
this is committed.

## Baseline as of writing (all verified live, not assumed)

- **Pipeline is flowing for the first time.** `l2-investigator-primary`
  went 0 → 2 done, 1 running after two fixes today: clearing the zombie
  FIFO queue that starved it, and setting
  `max_in_progress: 2` + `max_in_progress_per_profile: 1` so investigator
  and reviewer each hold a dedicated slot.
- **Ticket_343 completed end to end**: investigate (160s, real finding
  from live data) → metadata repair → independent review (136s) →
  published to `Complaint_Mst_Tbl.SupportExecutiveRemarks`.
- Lifetime totals remain poor and are the thing to move: 630 FAILED,
  164 L3_ESCALATION, 13 UPDATE, **1 RESOLUTION**, out of ~864 attempts.

## 1. Event-driven orchestration (replace cron backstops)

**Finding: an event layer already exists and appears not to fire.**
`xstudio_l2_orchestrator_plugin` declares `provides_hooks: [post_tool_call]`
and is enabled in `config.yaml` (`plugins.enabled`). Its stated job is to
run `kanban_reject_bridge.py` / `kanban_approval_publisher.py` /
`drain_and_summarize.py` the instant `kanban_complete`/`kanban_block`
succeeds, instead of waiting for a cron tick.

Evidence it is not firing:
- After the reviewer approved Ticket_343, nothing published. The
  publisher only ran when invoked by hand, and then published fine.
- The only `xstudio-l2-orchestrator` lines in `logs/agent.log` are
  `capability_check ... decision=deny` for `tools.override`. No
  execution/fired/spawned lines at all.
- (`tools.override` denial itself is benign — these are pure observer
  hooks, they never override a tool. Not the cause.)

**Work:**
1. Determine whether `post_tool_call` hooks fire at all in **kanban worker
   subprocesses** (workers are separate `hermes chat` processes; the hook
   may only be wired into gateway-hosted turns).
2. If hooks don't fire in workers, move the trigger to where the event
   genuinely lands — candidates: Hermes's own `worker_spawned` /
   dispatch-tick observer hooks (`_fire_worker_spawned_hook`,
   `_fire_dispatch_tick_hook` exist in `kanban_db_dispatch.py`), or a
   kanban task-event subscription rather than a wall clock.
3. Keep cron strictly as a failure backstop, not the primary path — and
   say so explicitly in each script's header so the next person doesn't
   assume cron is the design.

## 2. Observability — is what we built still being fed?

Already built and confirmed real: `Hermes_Agent_Trace_Trn_Tbl` (9,983
events), `Hermes_L2_Compute_Per_Ticket_Vw` (171 tickets: avg 441,939
tokens, 16 tool calls, 33 API requests, 75 min wall-clock, worst 8.2h),
GPU samples (avg 78.9% util, 7,330/8,188 MB VRAM).

**Work:**
1. Confirm the trace drain is still running now that profiles were
   renamed and the pipeline restarted — the view is only as good as its
   feed (`drain_l2_trace_log.py`).
2. Re-measure compute per ticket on the *new* config (thinking off,
   q4_0 KV cache, qwen) — the 442K/75-min numbers are from the old,
   broken regime and are almost certainly stale.
3. Surface it: nothing reads these numbers today except ad-hoc SQL.
   See GitHub issue #3 (MI dashboard).

## 3. Memory — currently zero, and separate from ticket resolution

mem0 is fully wired (per-profile embedded Qdrant, correct dims, patched
for LM Studio) and holds **0 points on every profile**. Nothing has ever
been written. This is independent of the resolution pipeline and must not
be conflated with it.

**Work:**
1. Establish *why* nothing writes — SOUL.md tells the bot to record
   durable facts, but no completion path calls a memory write. Determine
   whether it should be the model's judgment at all, or a deterministic
   write at publish time (the latter matches everything else that
   actually works here).
2. Decide what is worth remembering: schema gaps, dead ends, corrections
   — not per-ticket detail, which belongs on the ticket.

## 4. Cross-ticket knowledge generation, preservation, retrieval

**Finding: `Hermes_Solution_Article_Mst_Tbl` has 0 rows.** The mechanism
exists (`Hermes_Create_Solution_Article_Usp`, called from
`kanban_approval_publisher.py` for `RESOLUTION` responses only) but with
exactly 1 RESOLUTION ever, it has effectively never run.

**Work:**
1. Persist an **investigation ledger** per run — the structured
   findings record (tables queried, values found, ruled out, conclusion)
   already designed and built into `Hermes_Orchestrator.py`
   (`--save-ledger` / `--get-ledger`, reusing the unused
   `InvestigationJson` column). Wire it into the publish path so every
   completion, not just RESOLUTIONs, leaves reusable structure behind.
2. Carry a prior attempt's ledger **verbatim** into rework cards, rather
   than letting a 9B model re-summarize it (the mechanical-carry-forward
   pattern; re-summarization is exactly what small models do badly).
3. Broaden solution-article creation beyond `RESOLUTION` — an UPDATE
   that correctly diagnoses a data-entry gap is reusable knowledge too.

## 5. Existing KB retrieval and enhancement

What exists: `Knowledge/*.md` (domain notes), `task-router.md` +
`manifest.json` (pattern → skill/doc routing), `schema_allowlist.json`
(1.16MB, ground truth for identifiers), `validate_identifiers.py`,
`--build-query` (mechanically-validated SELECT), `--suggest-tables`
(keyword-scored schema narrowing, built on the conductor branch).

Gaps: routing is static keyword matching; there is no semantic retrieval
over the KB; nothing measures whether a KB doc actually helped resolve a
ticket; the RFP requirement to **cite the knowledge source used per
resolution** (GitHub issue #1) is unimplemented.

**Work:**
1. Wire `--suggest-tables` into the investigator's card body at dispatch
   so it starts with a narrowed, real table list instead of guessing.
2. Record which KB docs/tables an investigation actually used, in the
   ledger — this is both the RFP citation requirement and the raw data
   for measuring KB value.
3. Only then consider a filesystem/markdown MCP server for semantic KB
   access; the mechanical wins above come first and are cheaper.

## Order of work

1. Event-driven trigger (§1) — largest architectural payoff, and the
   pipeline currently depends on wall clocks for its final publish step.
2. Investigation ledger wired into publish (§4.1/§4.2) — turns every
   completed run into reusable structure.
3. Observability re-measure + trace-drain confirmation (§2).
4. Memory write path (§3).
5. KB narrowing at dispatch + citation capture (§5).
