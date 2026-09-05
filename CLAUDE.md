# Claude / Agent Entry Point — AI Helpdesk (Hermes L2)

Read `AGENTS.md` first — full folder map, deployment state, SQL write
discipline, and the "Hermes" naming-collision warning.

## Current state (2026-09-05) — read this before touching anything

**This section is a fast-moving daily log, not a stable reference.** If
anything here conflicts with `README.md` or `AGENTS.md`, those two are
more likely to be current — this file has gone stale before (a whole
2026-09-02 architecture description, including a model name and delivery
mode that no longer exist, survived here uncorrected for three days
before being caught). Verify against `deploy/`/live `hermes` commands
before trusting a specific claim below.

**The live pipeline is Kanban-based, not the old poll-into-chat design.**
`ticket_scout.py` (cron, WSL, ~2m tick) creates a Kanban card for
`l2-investigator-primary` (investigator) plus a `--parent`-gated reviewer
card for `l2-reviewer-primary`. Event-driven hook plugins publish an
approval or bridge a rejection into rework, capped at 3 attempts before
escalating to the human L3 queue. Full diagram: `README.md` §1. This
replaced an earlier single-bot-chat design (`hermes_l2_poll.py` injecting
context into one long-lived `bot-chat:l2-investigator` conversation) that
caused a real context-overflow outage — if you see that older flow
described anywhere (old `Plans/` docs), it's history, not the live
mechanism. Profile names were renamed 2026-09-05 from model-based
(`l2-eval-investigator`, `l2-gemma-verifier`, `l2-qwen-verifier`) to
role-based (`l2-investigator-primary`, `l2-reviewer-primary`,
`l2-reviewer-fallback`) — if you see the old names anywhere outside a
historical/dated note, that's stale and worth fixing.

**Ticket claiming is backlog-gated, not blindly interval-based (fixed
2026-09-05).** A real incident: `ticket_scout.py` claimed a new SQL ticket
on every ~2m cron tick regardless of how much unworked investigator
backlog already existed. The single-worker gateway (see below) drains
roughly one card per 10-20 min, so blind polling let intake — plus rework
regenerating even more cards on every rejection — outrun the drain rate
by 10-20x. Confirmed live over the prior 2 days: 572 claimed runs silently
reaped as `"Recovered as stale by Hermes scheduler"`, real ticket
resolution nearly stopped (1 `Complaint_Mst_Tbl` Status write in 6 days),
and 300 tickets sat unclaimed. Fix: `ticket_scout.py` now checks current
investigator backlog (unfinished cards, fresh + REWORK, via
`_investigator_backlog()`) before polling and skips the claim entirely
once it's >= `MAX_INVESTIGATOR_BACKLOG` (3). A board-read failure fails
closed (skips claiming) rather than polling blind. If you're debugging
"why didn't a new ticket get claimed this tick," check the backlog count
first, not the cron schedule.

**Model: live-loaded model as of 2026-09-05 afternoon is `qwen/qwen3.5-9b`
via LM Studio**, serving all active profiles (`l2-investigator`,
`l2-investigator-primary`, `l2-reviewer-primary`, `l2-reviewer-fallback`).
This corrects an earlier entry in this same file claiming
`qwopus3.5-9b-coder` — that claim was stale by the time it was checked
live; do not trust either name without reverifying. LM Studio serves one
model at a time; `l2-gemma` is fully retired (gateway stopped, config kept
as history only). Live-loaded-model check: `curl
http://100.111.69.102:1235/api/v0/models` (look for `"state": "loaded"`),
not `/v1/models` (that lists the whole catalog regardless of load state).

**`deploy/` is the reproducible-topology mirror — keep its `PROFILES` list
in `Model_Bench/mirror_wsl_artifacts.sh` in sync with reality.** A real gap
was found and fixed 2026-09-05: that script's hardcoded profile list was
never updated when `l2-eval-investigator` was created, so `deploy/profiles/`
had no dir for the profile actually running fresh ticket dispatch — a
fresh install from this repo could not have reconstructed the real
topology. Re-run `Model_Bench/mirror_wsl_artifacts.sh` after creating,
renaming, or retiring any profile, not just after editing SOUL.md/skills.

**Two new response-handling mechanisms (2026-09-05), both live**:
`EscalationCategory` on `Hermes_L3_Escalation_Trn_Tbl`
(`UNRESOLVED` vs `NEEDS_HUMAN_ACTION`) and an `AttemptNo`-capped
reject-rework loop (`--fail-run`/`--escalate-blocked`) so a ticket stuck
on the same mistake stops looping forever instead of generating an
endless string of rework cards. See `README.md` §3.

**A second bot, `infra-guardian`, maintains this bot's infrastructure**
(WSL only) — separate profile/gateway, 30-min Routine, one skill
(`hermes-infra-guardian-checks`) covering gateway/VM/LM-Studio/session
health with an explicit guardrail: it reports LM Studio being down, never
tries to fix it (the user controls that machine directly). See `AGENTS.md`
for the full incident chain this was built in response to.

**Conductor migration — Phase 0+1 built, not yet cut over.** Evaluating
replacing this Kanban pipeline with Microsoft Conductor
(`github.com/microsoft/conductor`, real, MIT, installed in WSL2) for
deterministic step orchestration + schema-narrowed/audited tool access
via a new local MCP server (`Model_Bench/l2_investigation_mcp_server.py`).
**Kanban is completely unaffected and still runs the live pipeline** —
this is a parallel, isolated proof-of-concept, not yet wired to publish
anything real. Full phase plan, what's built vs. still open, and the
explicit decision to retire Kanban/mem0/the 4 xstudio-* skills for this
pipeline only if/when the cutover actually happens:
`Plans/Conductor_Migration_Plan_05092026.md`. Read that before assuming
either the Kanban or the Conductor path is "the" current pipeline.

**Why `Hermes_Orchestrator.py` is a thin-wrapper CLI, not a full
pipeline**: the user directly asked why a hand-written script should be
doing investigation at all when a real reasoning bot exists. Correct
question — the keyword-search "brain" (`investigate()`, `run_one_cycle()`)
was deleted long ago. What's grown back since is a set of genuinely
mechanical, schema-validated primitives worth not re-deriving from
scratch each run: atomic claim (`--poll`), audited write-back
(`--publish-response`), a schema-validated query builder
(`--build-query`), schema-narrowing (`--suggest-tables`), and a
structured investigation ledger (`--save-ledger`/`--get-ledger`, reusing
the previously-unused `InvestigationJson` column). Investigation
judgment itself is still the bot's/agent's job.

**`dbo.Complaint_Mst_Tbl` now carries the L1 handoff fields directly**
(`ProblemCategory`, `SourceSystem`, `ConversationSummary`, `SuspectedCause`,
`ExtractedEntitiesJson`, `ConversationLogJson`) — added straight to the
platform table per the user's explicit instruction, not a companion table.
Verified live: a ticket with `ExtractedEntitiesJson = {"HeatNo": "H12345"}`
and `SourceSystem = 'Xbatch'` correctly steered a keyword search toward the
right database in the old `investigate()` — the bot should do the analogous
thing now: read these fields from `--poll`'s output and use them as
investigation hints when populated (usually NULL today, since L1 doesn't
exist yet).

**Deterministic KB retrieval landed and was independently validated
2026-09-05** (`Model_Bench/kb_retrieval.py`, commits `602f0a1`..`4f26ef1`).
Replaces the old broad `Route=? TOP 5` solution lookup in the investigation
bundle: routes are inferred from `Knowledge/manifest.json`
(`identifier_routing` is the sole canonical identifier->route source, no
second hardcoded mapping), articles are ranked against the ticket's actual
text with a hard rule that **route alone can never retrieve an article**
(route only adds a bonus once textual relevance already exists), and every
hit carries provenance (`kb_id`, `source_ref`, `matched_terms`,
`verification_required: true`) plus explicit abstention when nothing
clears the relevance threshold. `ticket_scout.py` wires this in by
stripping the bundle's old `known_solutions` and replacing it with
`kb_retrieval`'s ranked result; a KB failure degrades to an abstention
dict, never blocks dispatch. `Model_Bench/validate_knowledge_manifest.py`
is a fail-fast consistency check (manifest<->task-router route drift,
missing knowledge files, stale-workflow-skill regression) wired into
`.github/workflows/knowledge-validation.yml`, though that workflow has not
yet run successfully on a real runner — validate locally
(`python3 Model_Bench/validate_knowledge_manifest.py`,
`python3 -m unittest Model_Bench.test_kb_retrieval`) rather than trusting
CI status.

**The ticket lifecycle was centralized into `Model_Bench/l2_pipeline_runtime.py`
(2026-09-05), validated and deployed live the same day.** This is now the
single owner of investigator/reviewer/rework/publish sequencing — read
`Knowledge/L2_PIPELINE_STATE_MACHINE.md` before touching any of it.
Everything the compat-named scripts (`kanban_approval_publisher.py`,
`kanban_reject_bridge.py`, `repair_incomplete_completions.py`,
`audit_kanban_completions.py`, `enforce_publish_safety_net.py`) do is now
just `cli(["<mode>", ...])` into that one module — they are thin
compatibility entrypoints, not independent orchestration authorities. Key
facts:
- **Global WIP = 1.** `ticket_scout.py` (still the 2-minute cron) now runs
  the full synchronous `reconcile()` (normalize → repair missing
  reviewers → process rejections → process approvals/publish → recover
  true orphans) before ever checking whether to claim, and refuses a new
  claim (`WIP_LIMIT`) while any SQL run is active. `MAX_INVESTIGATOR_BACKLOG`
  from the prior day's fix is gone — superseded by this stricter global gate.
- **Priorities**: review=30, rework=20, new investigation=10 — finish
  existing work before starting more.
- **Reviewer cards are created only after the investigator's completion
  metadata is normalized**, and carry a **frozen `proposal_json`** the
  reviewer judges and the publisher later publishes verbatim — no
  reconstruction from prose at either step.
- **Review cycles are a separate `review_cycle` counter**, not SQL
  `AttemptNo`. `MAX_REVIEW_CYCLES = 3`; a rejection at cycle 2 escalates
  instead of looping forever.
- **`deploy/helpdesk_workflow_binding.json` is the sole source of workflow
  status names** — `resolved_ticket_status` bound to the live-verified
  `"Closed"` (confirmed by cross-referencing the one real RESOLUTION this
  project had published, `Ticket_233`), `waiting_user_ask_status` bound to
  `"Ask"`. `l3_ticket_status`/`needs_human_action_ticket_status` are
  deliberately left `null` — no distinct live value for either was ever
  observed, and the runtime fails closed rather than inventing one.
  `RESOLUTION` publication fails closed if this binding is incomplete.
- **No automatic KB article creation on RESOLUTION anymore** — that's a
  separate governed process now (`Knowledge/KB_IMPLEMENTATION_PLAN.md`).
- **Cron cleanup (2026-09-05)**: removed "L2 Publish Safety Net"
  (`enforce_publish_safety_net.py`, 5m) and "L2 Repair Incomplete
  Completions" (`repair_incomplete_completions.py`, 5m) — both were pure
  subsets of what `ticket_scout.py`'s `reconcile()` already does every
  2 minutes, and running them as separate independently-scheduled OS
  processes reintroduced the exact concurrent-mutation race this
  migration's synchronous-reconciler design exists to eliminate. Only
  "L2 Ticket Scout" (mutating, 2m) and "L2 Kanban Completion Audit"
  (read-only, 10m) remain. See `deploy/cron_jobs.txt`.
- **Real defect found and fixed during validation**: `Knowledge/
  00_Hermes_L2_FULL_INSTALL.sql` had gone stale — never regenerated after
  `25_ticket_dispatch_hardening.sql`/`55_update_retry_hardening.sql` were
  added, so a fresh install from it alone would have silently missed both.
  Regenerated; `.gitattributes` now forces LF on `*.sh`/`*.sql` so a
  Windows checkout's `core.autocrlf` can't corrupt either the install
  bundle or WSL-executed shell scripts again (the latter broke
  `Model_Bench/validate_l2_pipeline_local.sh` outright — `pipefail\r:
  invalid option name` — until this was added).
- A genuine **pre-migration backlog of ~32 stale active SQL runs** existed
  at cutover (average age 13+ hours, from the old ticket_scout.py's
  since-fixed backlog-runaway bug). The reconciler correctly recognizes
  all of them via their still-live Kanban tasks (0 anomalies) and refuses
  new claims until they drain — this is expected transitional state, not
  a pipeline defect. Check `python3 ~/.hermes/profiles/l2-investigator/
  scripts/l2_pipeline_runtime.py status` for current backlog depth before
  assuming the pipe is idle vs. draining.

## Quick reference

```
python Hermes_Orchestrator.py --discover-workflow
python Hermes_Orchestrator.py --poll --eligible-status "Enter" --server 10.2.6.204
python Hermes_Orchestrator.py --publish-response --run-id <ID> --response-type UPDATE --reply-text "..." --server 10.2.6.204
```

Pin `--server 10.2.6.204` explicitly — `$MSSQL_MCP_SERVER` (`SSLDATABASE`
hostname) intermittently failed to resolve during testing even though the
server itself was fine.

`hermes` CLI lives at `C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe`
(not necessarily on PATH — add it or use the full path). Useful commands:

```
hermes profile list
hermes profile use l2-investigator   # then: hermes profile use default  to switch back
hermes cron list / status / runs / doctor
hermes gateway status / list
```

## Don't re-duplicate the schema/SP dumps

`Reference Documents/` holds the one copy of the exported
`XStudio_Helpdesk`/`XStudio_Xbatch` schema and SP catalogs. `Knowledge/` had
a second copy of all four plus two zip archives (~100K redundant lines)
that was removed 2026-09-02 specifically because it made the folder too
large to read productively. Grep `Reference Documents/` for the specific
table/procedure needed instead.

## Before deploying any SQL change

1. Edit the relevant numbered file in `Knowledge/` (`00_tables_and_indexes.sql`
   … `60_metrics_and_reporting.sql`, now nine files including the
   `25_ticket_dispatch_hardening.sql`/`55_update_retry_hardening.sql`
   overlays added 2026-09-05), never `00_Hermes_L2_FULL_INSTALL.sql`
   directly.
2. Regenerate `00_Hermes_L2_FULL_INSTALL.sql` by concatenating all numbered
   files in numeric order (`00`, `10`, `20`, `25`, `30`, `40`, `50`, `55`,
   `60` — `98_pipeline_postflight.sql`/`99_postflight.sql` are verification,
   not part of the install bundle). A real drift was caught and fixed
   2026-09-05: the bundle went stale for a day after `25`/`55` were added,
   so a fresh install from it alone would have missed both hardening fixes
   silently. Diff-check after regenerating:
   `diff <(cat Knowledge/00_tables_and_indexes.sql Knowledge/10_helpdesk_discovery.sql Knowledge/20_ticket_dispatch.sql Knowledge/25_ticket_dispatch_hardening.sql Knowledge/30_context_and_live_discovery.sql Knowledge/40_investigation_runtime.sql Knowledge/50_response_and_workflow.sql Knowledge/55_update_retry_hardening.sql Knowledge/60_metrics_and_reporting.sql) Knowledge/00_Hermes_L2_FULL_INSTALL.sql`
   should print nothing.
3. Deploy with `sqlcmd` (handles `GO` batch separators; `pyodbc` does not) —
   prepend `SET QUOTED_IDENTIFIER ON; GO` or the filtered index on
   `Hermes_L2_Response_Trn_Tbl` fails to create. On a Windows checkout,
   `MSSQL_MCP_PASSWORD` may not be visible inside WSL even when it works
   fine for Windows Python — use the Windows `sqlcmd.exe` (via PowerShell)
   in that case, not WSL's.
4. Run `Knowledge/99_postflight.sql` and confirm no errors.
5. Schema changes to a live, shared database are confirm-first with the
   user, even though the install script is additive-only.
