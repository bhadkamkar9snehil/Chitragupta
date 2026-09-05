# Chitragupta — XStudio Hermes L2 Helpdesk

An autonomous L2 support pipeline for the XStudio/XMES manufacturing
platform, built on [Hermes Agent](https://hermes-agent.nousresearch.com).
It polls the live Helpdesk ticket queue, investigates tickets against the
real XStudio_Xbatch/XStudio_Helpdesk database, has a second bot verify
every proposed response before it's published, escalates genuinely stuck
cases to a human work queue, and keeps a full, human-readable audit trail
(with compute-cost accounting) of every investigation attempt — resolved
or not.

Named after the Hindu deity of meticulous record-keeping and judgment:
this system's job is exactly that — investigate, keep a complete account,
and decide what needs to go to a human.

This README documents the whole system end to end: architecture, every
script, every SQL object, every skill, how to deploy it on new
infrastructure, and what to do after a Hermes update.

---

## 1. Architecture

```
                    ┌─────────────────────┐
  Complaint_Mst_Tbl │  XStudio Helpdesk    │  (live production ticket queue)
  (Status='Enter')  │  SQL Server          │
                    └──────────┬──────────┘
                               │ polled every 2m (ticket_scout.py cron)
                               ▼
                    ┌─────────────────────┐
                    │  Hermes_Orchestrator │  --poll: atomic claim,
                    │  .py                 │  full ticket context
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
              ┌────►│ kanban card:        │  assignee l2-investigator-primary
              │     │ investigator        │  skill: xstudio-l2-ticket-workflow
              │     └──────────┬──────────┘
              │                │ kanban_complete(summary, metadata)
              │                ▼ auto-promotes via native --parent gating
              │     ┌─────────────────────┐
              │     │ kanban card:         │  assignee l2-reviewer-primary
              │     │ reviewer             │  skill: xstudio-l2-draft-verifier
              │     └──────────┬──────────┘
              │        approve │  reject → kanban_block(reason)
              │                ▼                    │
              │     ┌─────────────────────┐          │  AttemptNo < 3?
              │     │ kanban_approval_     │          ▼  yes: rework card
   rework     │     │ publisher.py (hook-  │   kanban_reject_bridge.py
   card       │     │ triggered, no-LLM)   │          │  no: --fail-run +
   created◄───┘     └──────────┬──────────┘          │  --escalate-blocked
   (attempt < 3)                ▼                      │  (EscalationCategory
                     │--publish-response                │   = UNRESOLVED)
                     ▼ --force-run-id                    ▼
          Hermes_L2_Response_Trn_Tbl          Hermes_L2_Log_Blocked_
          + Complaint_Mst_Tbl (Status)        Escalation_Usp (visibility-
          (ResponseType incl.                 only -- doesn't touch the run)
           NEEDS_HUMAN_ACTION, which also                │
           writes EscalationCategory =                    ▼
           'NEEDS_HUMAN_ACTION' -- diagnosed   Hermes_L3_Escalation_Trn_Tbl
           but needs a human to act, distinct  (human work queue, excluded
           from an UNRESOLVED "couldn't        from re-polling while its own
           figure it out" escalation)          EscalationCategory stays open)
```

All active LLM-driven profiles (`l2-investigator`, `l2-investigator-primary`,
`l2-reviewer-primary`, `l2-reviewer-fallback`) currently point at the same LM
Studio model, `qwopus3.5-9b-coder` — see `deploy/profiles/*/config.yaml`.
LM Studio serves one model at a time; profile-to-model assignment is a
single line (`model.default`) per profile, changed via `hermes profile
use <name>` triggering a JIT load/evict, never by loading two models
side by side. `l2-gemma` (the original gemma-4-e4b-it investigator this
project started with) is fully retired — profile still exists with its
old config as historical record, gateway stopped, zero live kanban tasks.

Every hop after `kanban_complete`/`kanban_block` is **event-driven**, not
cron-polled: a Hermes observer-hook plugin
(`Model_Bench/xstudio_l2_orchestrator_plugin/`) fires the relevant
deterministic script the instant the triggering tool call succeeds. Cron
jobs still exist, but only as backstops for cases an event genuinely can't
see (a crashed process, a gateway restart mid-flight) — not as the primary
mechanism.

### Why two separate bots investigate and verify

LM Studio (the local model backend used here) cannot force a specific
named tool call — only "call something." Trusting a model to reliably
remember a second, separate `--publish-response` call after finishing its
reasoning turned out to fail regularly (confirmed live: 0 of 6 real
completions in a row). So the verifier's only job is judgment
(`kanban_complete`/`kanban_block`); a deterministic, no-LLM script performs
the actual database write using the *investigator's own* recorded
metadata — never anything the verifier retyped.

### Why native `--parent` gating, not `hermes kanban swarm`

`hermes kanban swarm` looks like the obvious fit (parallel workers →
verifier → synthesizer) but was evaluated and rejected: its verifier/
synthesizer skills are **hardcoded in Hermes's own source**
(`requesting-code-review` / `humanizer`) with no CLI or config override,
which would silently replace the real SQL/schema-verification skill with
a generic one. Plain `kanban create --parent <task-id>` — the primitive
swarm itself is built on — gives the same auto-promotion behavior with
full control over assignee/skill/body. Both investigator and reviewer
cards live on a single board; the old two-board split (see
`Model_Bench/kanban_forward_bridge.py`, now retired) existed to avoid a
same-task reassignment bug that doesn't apply to separate parent-gated
cards.

---

## 2. Repository layout

```
Hermes_Orchestrator.py     Core CLI: --poll (atomic claim) and
                            --publish-response (audited write-back), plus
                            read-only investigation helpers (--query,
                            --find-sql-objects, --get-sql-object-definition,
                            --get-run-actions, --search-solutions,
                            --log-activity, --create-solution,
                            --link-solution), plus (2026-09-05) --fail-run
                            (mark a run FAILED with a reason, without
                            publishing a response), --escalate-blocked
                            (visibility-only L3 insert for a genuinely
                            stuck investigation), and --build-query
                            (mechanically-built, schema-validated SELECT —
                            see §3). This is the ONLY code path that
                            writes to the ticket/response tables.

AGENTS.md / CLAUDE.md      Agent-facing operating instructions: folder map,
                            deployment state, SQL write discipline, the
                            Hermes-naming-collision gotcha. Read these
                            first if you're an agent picking this project
                            back up cold.

Knowledge/                 The deployable SQL layer + reference docs.
  00_tables_and_indexes.sql       All Hermes_* tables, indexes.
  10_helpdesk_discovery.sql       Live-workflow discovery procs.
  20_ticket_dispatch.sql          Hermes_L2_Get_Candidate_Tickets_Usp,
                                   Hermes_L2_Recover_Stale_Runs_Usp.
  30_context_and_live_discovery.sql   Ticket context, SQL object search.
  40_investigation_runtime.sql    Claim/execute-SQL audit procs.
  50_response_and_workflow.sql    Publish/escalate/activity/trace procs.
  60_metrics_and_reporting.sql    Hermes_L2_Compute_Per_Ticket_Vw and
                                   other reporting views.
  99_postflight.sql               Verifies every expected object exists
                                   after a deploy.
  00_Hermes_L2_FULL_INSTALL.sql   Generated by concatenating the six
                                   numbered files above, in order. Never
                                   edit this file directly.
  view_catalog.json/.md           Indexed XStudio_Xbatch views (what each
                                   one returns, real column names).
  schema_allowlist.json           Identifier allowlist the verifier checks
                                   claimed table/column names against.
  validate_identifiers.py         The script the verifier actually runs
                                   to catch hallucinated identifiers.
  task-router.md                  Maps ticket problem patterns to the
                                   matching xstudio-* skill.
  vendor_docs_extracted/,
  view_docs/                      Per-view/per-domain investigation notes.

Model_Bench/                Orchestration scripts + Hermes plugins.
  ticket_scout.py            Cron (2m): --poll a new ticket, create the
                              investigator card + a --parent-gated
                              reviewer card, archive stale duplicate cards
                              for the same ticket.
  kanban_reject_bridge.py    Hook-triggered: verifier kanban_block → fresh
                              rework card back to the investigator with
                              the objection attached.
  kanban_approval_publisher.py  Hook-triggered, no-LLM: verifier
                              kanban_complete → real --publish-response
                              call using the investigator's own recorded
                              metadata, then logs a Ticket Activity entry
                              (and a Solution article for real
                              resolutions).
  drain_l2_trace_log.py      Reads the trace plugin's local JSONL event
                              log, inserts each event into
                              Hermes_Agent_Trace_Trn_Tbl via
                              Hermes_Log_Agent_Trace_Usp.
  generate_readable_trace_summary.py  Turns raw trace events into one
                              plain-English activity note per
                              investigation attempt — runs whether or not
                              the ticket got resolved. Also detects a real
                              kanban_block and calls
                              Hermes_L2_Log_Blocked_Escalation_Usp so a
                              genuinely stuck ticket surfaces to a human
                              instead of sitting silently blocked.
                              (2026-09-05) Second pass,
                              find_trace_free_terminal_runs(): catches
                              terminal runs (COMPLETED/FAILED/
                              WAITING_USER) that somehow got zero trace
                              events at all -- the original trace-based
                              loop could never find these -- and writes a
                              minimal honest note anyway, so "something is
                              always written to Helpdesk" holds even when
                              the trace pipeline itself missed a run.
                              Recovered 206 previously-silent runs on
                              first live pass, alongside 162 normal
                              trace-based summaries.
  drain_and_summarize.py     Runs the two scripts above sequentially in
                              one process (avoids a race where the summary
                              could run before the drain committed).
  enforce_publish_safety_net.py  Cron (5m) backstop: force-escalates a
                              claimed-but-unpublished run only if Kanban
                              has genuinely lost track of it (no live task
                              at all) — never touches a run still tracked
                              by a live, non-terminal kanban card.
  audit_kanban_completions.py  Cron (10m) backstop: reconciles kanban
                              'done' state against the actual SQL response
                              row.
  session_maintenance.py     Cron (6h): routine housekeeping.
  seed_test_tickets.py       Generates realistic test tickets across
                              multiple XStudio domains, deduped on
                              BriefDetails.
  model_scorecard.py,
  verify_l2_run.py,
  nudge_unpublished_runs.py,
  audit_kanban_completions.py,
  fix_malformed_ticket_ids.py,
  build_schema_allowlist.py,
  add_views_to_allowlist.py,
  bulk_index_views.py,
  export_view_samples.py,
  extract_vendor_docs.py,
  hermes_cli_bench.py         One-off / recurring maintenance and
                              investigation-support utilities — see each
                              file's own docstring.
  setup_mem0.py               Configures the mem0 memory provider (OSS
                              mode: LM Studio LLM + Ollama embedder +
                              Qdrant SERVER on 127.0.0.1:6333) across all
                              profiles. Embedded/local-path Qdrant was
                              replaced 2026-09-05 -- it is single-process,
                              so every kanban worker's memory call failed
                              on a file lock. See §7.
  mirror_wsl_artifacts.sh     Refreshes deploy/ from a live WSL install
                              (SOUL.md, config.yaml, skills, plugin
                              manifests, cron schedule).
  git_sync.sh                 Periodic commit+push, safely no-ops if no
                              remote is configured.
  xstudio_l2_trace_plugin/    Hermes observer-hook plugin: records every
                              tool call / API request / GPU+LM-Studio
                              hardware sample to a local JSONL log,
                              correlated to the real kanban task ID
                              (extracted from sys.argv, NOT the task_id
                              kwarg Hermes passes — that's actually the
                              session_id).
  xstudio_l2_orchestrator_plugin/  Hermes observer-hook plugin: the
                              instant kanban_complete/kanban_block
                              succeeds, immediately (debounced) fires
                              kanban_reject_bridge.py,
                              kanban_approval_publisher.py, and
                              drain_and_summarize.py instead of waiting
                              for a cron tick.

deploy/                     Everything that otherwise lives ONLY inside a
                             live Hermes install and would not survive a
                             fresh install or update on its own.
  profiles/<name>/SOUL.md    Each bot's persona/instructions.
  profiles/<name>/config.yaml  Each profile's Hermes config (toolsets,
                              memory provider, gateway settings — no
                              secrets; those live in .env, gitignored).
  skills/xstudio/*/SKILL.md  The six xstudio-* skills (see §4).
  plugins/*.plugin.yaml      Plugin manifests.
  cron_jobs.json / .txt      The live cron schedule at last mirror time.

patches/                    Fixes to third-party packages inside Hermes's
                             own venv that a `pip install --upgrade` or
                             `hermes update` can silently wipe.
  apply_mem0_json_object_patch.py  mem0's memory/main.py hardcodes
                              response_format={"type":"json_object"} for
                              its LLM fact-extraction calls; LM Studio
                              only accepts "json_schema" or "text" and
                              400s on json_object. This patch changes it
                              to "text". Idempotent, safe to re-run.
                              Self-healing: a daily cron job
                              (reapply_mem0_patch.py on l2-investigator)
                              re-runs this automatically.
  POST_UPDATE.md              The runbook — read this after every
                              `hermes update` or when standing this up on
                              new infrastructure.

Plans/, Agent_Comms/        Historical design docs and inter-agent
                             coordination logs from earlier phases of the
                             project. Kept for provenance, not
                             load-bearing.

Reference Documents/        Exported schema + stored-procedure catalogs
                             for XStudio_Helpdesk and XStudio_Xbatch
                             (generated by XMES/scripts/SP.py and
                             SchemaExporter.py — see the xstudio-db-export
                             skill if regenerating).
```

---

## 3. The SQL layer

All Hermes-side tables/procs/views live in `XStudio_Helpdesk`, prefixed
`Hermes_`. Key objects:

| Object | Purpose |
|---|---|
| `Hermes_L2_Response_Trn_Tbl` | One row per investigation attempt (run). `ProcessStatus` (CLAIMED→INVESTIGATING→COMPLETED/FAILED/WAITING_USER), `ResponseType` (UPDATE/QUESTION/RESOLUTION/L3_ESCALATION), the full proposed response text and metadata. |
| `Hermes_L2_SQL_Action_Trn_Tbl` | Audit trail of every SQL action an investigation took (read or write), keyed by RunID. |
| `Hermes_Agent_Trace_Trn_Tbl` | Raw event-level trace (tool calls, API requests, GPU/LM-Studio hardware samples) drained from the observer-hook plugin's local log. |
| `Hermes_L2_Compute_Per_Ticket_Vw` | Aggregated token/tool-call/wall-clock cost per RunID, computed from the trace table. |
| `Hermes_Ticket_Activity_Trn_Tbl` | Human-readable activity notes (existing platform table) — both real publishes and the deterministic trace-summary narrative land here. |
| `Hermes_L3_Escalation_Trn_Tbl` | The human work queue. Populated two ways: (1) a real `L3_ESCALATION`/`NEEDS_HUMAN_ACTION` response via `Hermes_L2_Publish_Response_Usp`, (2) a genuine stuck `kanban_block` via `Hermes_L2_Log_Blocked_Escalation_Usp` (visibility-only — does NOT complete/fail the run, Kanban is still free to retry). Carries an `EscalationCategory` column (`UNRESOLVED` vs `NEEDS_HUMAN_ACTION`) added 2026-09-05 via the official `XStudio_AddAttribute_Usp` route — a real diagnosis that needs a human to *execute* a change is now distinguishable from a genuine "couldn't figure it out." |
| `Hermes_L2_Get_Candidate_Tickets_Usp` | The polling eligibility query. Excludes tickets with an active run, and excludes tickets with an open L3 escalation — a ticket already in the human queue is never silently re-investigated by a later staleness event. |
| `Hermes_L2_Recover_Stale_Runs_Usp` | Marks a run FAILED after `@StaleMinutes` (default 60) with no heartbeat — but only for runs with `@ExcludeRunIDs` NOT protected by a still-live, non-terminal kanban task (checked client-side before this SP runs; see `Hermes_Orchestrator.py`'s `recover_stale_runs()`). |

**Reject-rework loop cap (2026-09-05)**: `kanban_reject_bridge.py` counts
`AttemptNo` (already tracked per-ticket by the claim logic) for the
ticket behind a rejected card. Under 3 attempts → a fresh rework card
back to the investigator with the reviewer's exact objection attached.
At 3 → `--fail-run` (stops the run looking active) then
`--escalate-blocked` (visibility-only L3 insert, `EscalationCategory=
'UNRESOLVED'`) instead of another doomed rework cycle. This closed a real
unbounded-loop bug: a ticket hitting the same underlying mistake forever
got a brand-new kanban task ID each time, so the native
block-recurrence-breaker (which keys off a single re-blocked task) never
applied.

**Mechanical, schema-validated query building (2026-09-05)**:
`Hermes_Orchestrator.py --build-query <table> --columns c1,c2 [--where
...] [--top N] [--order-by ...] [--execute] [--database ...]` builds a
SELECT deterministically against `Knowledge/schema_allowlist.json` (the
same allowlist the verifier already checks claims against), rejecting
any hallucinated table/column with `difflib`-based fuzzy suggestions
toward the real name, and warning when a table name is ambiguous across
`XStudio_Helpdesk`/`XStudio_Xbatch` (e.g. `Area_Mst_Tbl` exists in both).
Exists because a 9B local model, unassisted, occasionally invents a
plausible-sounding column name — this gives it (and the human) a way to
get a guaranteed-valid query without round-tripping through
`INFORMATION_SCHEMA` by hand first.

Deploy order: edit the relevant numbered file in `Knowledge/`, regenerate
`00_Hermes_L2_FULL_INSTALL.sql` by concatenation, deploy with `sqlcmd`
(handles `GO` batch separators — `pyodbc` does not; prepend
`SET QUOTED_IDENTIFIER ON; GO` or filtered indexes fail to create), then
run `Knowledge/99_postflight.sql` and confirm no errors. The install is
additive-only, but schema changes to a live shared database should still
be confirmed with a human first.

---

## 4. The `xstudio-*` skills

Live under `deploy/skills/xstudio/` (source of truth is whichever profile
last had it edited — see `Model_Bench/mirror_wsl_artifacts.sh`).

| Skill | Used by | Purpose |
|---|---|---|
| `xstudio-l2-ticket-workflow` | investigator | The poll → investigate → publish procedure, response-type semantics, when to check the knowledge base first. |
| `xstudio-sap-api-investigation` | investigator | SAP integration error investigation patterns. |
| `xstudio-sohar-heat-execution` | investigator | Steel-heat production/EAF/LRF/CCM domain investigation patterns. |
| `xstudio-quality-delay-workorder` | investigator | Quality deviation / work-order delay investigation patterns. |
| `xstudio-sql-write-discipline` | investigator + reviewer | The official-SP-first rule: prefer a real stored procedure over a direct write; documented no-SP exceptions only for genuinely new-entity system-column provisioning. |
| `xstudio-l2-draft-verifier` | reviewer | Independent verification procedure: check every claimed identifier against `schema_allowlist.json`, verify a "doesn't exist" claim with `--find-sql-objects` before accepting it, spot-check the core factual claim with a real `--query`, judge response-type proportionality, then exactly one terminal call (`kanban_complete` to approve, `kanban_block` to reject with an actionable reason). Never calls `--publish-response` itself. |

---

## 5. Deploying on new infrastructure

1. **SQL layer**: deploy `Knowledge/00_Hermes_L2_FULL_INSTALL.sql`, then
   run `Knowledge/99_postflight.sql` and confirm no errors.
2. **Hermes profiles**: install Hermes Agent, create the profiles under
   `deploy/profiles/` (`l2-investigator` — hosts the kanban dispatcher
   gateway and doubles as rework fallback; `l2-investigator-primary` — the
   live fresh-ticket investigator; `l2-reviewer-primary` — the live
   reviewer; `l2-reviewer-fallback` — second reviewer pairing, kept
   for rework fallback only, not used by fresh dispatch; `l2-gemma` —
   fully retired, gateway stopped, kept as historical record only). Copy
   each profile's `SOUL.md`/`config.yaml` into the matching
   `~/.hermes/profiles/<name>/...` path. All active profiles currently
   point `model.default` at the same LM Studio model
   (`qwopus3.5-9b-coder`) — LM Studio only serves one model at a time,
   so do not point different active profiles at different models unless
   you're deliberately accepting the load/evict thrash that causes.
3. **Skills**: copy `deploy/skills/xstudio/*/SKILL.md` into each profile's
   `~/.hermes/profiles/<name>/skills/xstudio/<skill>/SKILL.md` (per §4 for
   which profile needs which skill).
4. **Plugins**: copy `Model_Bench/xstudio_l2_trace_plugin/` and
   `xstudio_l2_orchestrator_plugin/` into
   `~/.hermes/profiles/<name>/plugins/<plugin-name>/` for all 4 profiles,
   enable in each profile's `config.yaml`. Restart each profile's gateway
   after any plugin change:
   `systemctl --user restart hermes-gateway-<profile>.service`.
5. **Credentials**: set `MSSQL_MCP_SERVER` / `MSSQL_MCP_USER` /
   `MSSQL_MCP_PASSWORD` in the environment. Every script reads these —
   nothing is hardcoded anywhere in this repo.
6. **Cron schedule**: recreate from `deploy/cron_jobs.json` (or `.txt`) —
   see `Model_Bench/` for what script each job runs.
7. **Memory**: first run `deploy/qdrant/install_qdrant.sh` (installs the
   Qdrant binary and enables the systemd user service; idempotent), then
   `Model_Bench/setup_mem0.py` after installing `qdrant-client`, `mem0ai`,
   `ollama` into Hermes's own venv. Verify with
   `deploy/qdrant/healthcheck_qdrant.sh` -- it fails loudly if the service
   is down and warns if the collection exists but holds zero points, which
   is what a silent memory regression actually looks like. Needs an
   OpenAI-compatible LLM endpoint (this project points it at LM Studio,
   reusing the already-loaded investigation model — do NOT load a second
   model into LM Studio, it only serves one model at a time) and a
   reachable Ollama instance with `nomic-embed-text` pulled for
   embeddings (CPU-only, no GPU needed — verify with
   `curl http://<host>:11434/api/tags`). Then run
   `patches/apply_mem0_json_object_patch.py` — required for mem0 to work
   with LM Studio at all (see §7).
8. **Verify**: `hermes -p l2-investigator kanban list`, confirm the
   dispatcher is running, trigger `ticket_scout.py`'s cron job once
   manually and confirm both an investigator and a gated reviewer card
   appear.

---

## 6. After a `hermes update`

**Read `patches/POST_UPDATE.md`.** Short version: the mem0 patch (§7) is
the single most update-fragile piece — a `mem0ai` package upgrade wipes it
silently. A daily cron job already reapplies it automatically
(idempotent), but if mem0 stops working right after an update, run
`patches/apply_mem0_json_object_patch.py` by hand first. SOUL.md/skills/
plugins/cron live in profile directories that a normal update does not
touch; only a *fresh install* needs those redeployed from `deploy/`.

---

## 7. Memory (mem0)

Built-in Hermes memory (`MEMORY.md`/`USER.md`) is enabled by default but
was found completely unused in practice — the tool was available in every
profile's toolset, but nothing prompted the small local models used here
to actually reach for it, so 2+ days and hundreds of investigations
produced zero memory entries. Two things fixed this:

1. **A `## Memory` section in every profile's `SOUL.md`** telling the bot
   explicitly when to write an entry (durable, reusable facts — a schema
   gap, a dead end, a correction) and when not to (per-ticket details,
   which belong in the ticket's own trail via `--publish-response`, not
   memory).
2. **Switched to the `mem0` provider** (OSS mode) for real semantic
   retrieval instead of a flat markdown file, so a fact learned by one bot
   benefits all four (shared vector store + shared `user_id`):
   - **LLM** (fact extraction): LM Studio, reusing the already-loaded
     investigation model — adds zero new VRAM.
   - **Embedder**: Ollama, running `nomic-embed-text` (274MB, CPU-only —
     embedding models don't need a GPU, and loading one into LM Studio
     would have evicted the live investigation model since it only serves
     one model at a time).
   - **Vector store**: Qdrant **server** on `127.0.0.1:6333`, run as a
     systemd user service from the plain static binary — still no Docker.
     Install/enable with `deploy/qdrant/install_qdrant.sh` (idempotent);
     verify with `deploy/qdrant/healthcheck_qdrant.sh`. One shared
     collection (`hermes_l2`) across all profiles.

     **This replaced embedded/local-path Qdrant on 2026-09-05, and the
     reason matters**: embedded mode is single-process (a file lock).
     Kanban workers are separate OS processes from their gateway, so every
     worker's mem0 call failed with `Storage folder ... already accessed by
     another instance of Qdrant client`. Confirmed from a live worker log —
     the model *did* call `mem0_search` and got that error. Memory sat at
     zero entries for the project's entire history not because nothing
     wrote to it, but because every read and write failed on that lock. An
     earlier "fix" that gave each profile its own path addressed the wrong
     level: it separated gateways from each other, never a worker from its
     own gateway. A server is multi-process safe by construction and
     restores the cross-profile shared learning the per-profile split had
     given up.

Set up via `Model_Bench/setup_mem0.py` (writes `mem0.json`/`.env`/
`config.yaml`'s `memory.provider` per profile directly — the `hermes
memory setup mem0 --mode oss ...` CLI flags are NOT actually wired through
to the plugin by Hermes's own argument parser; confirmed by reading the
source, this is a real gap in the framework, not a misuse).

**Known gotcha #1**: mem0's Qdrant vector-store config defaults
`embedding_model_dims` to 1536 (OpenAI's dimension) regardless of what
embedder you actually configure — must be set explicitly to match your
real embedder's output size (768 for `nomic-embed-text`), or every search
fails with a shape-mismatch error the moment the collection already has
data at the wrong dimension.

**Known gotcha #2**: mem0's own `memory/main.py` hardcodes
`response_format={"type": "json_object"}` for its LLM extraction calls.
LM Studio's structured-output implementation only accepts `"json_schema"`
or `"text"` and returns a 400 on `"json_object"`. See §6/`patches/`.

---

## 8. Credentials

Nothing in this repo is a secret. Every script reads
`MSSQL_MCP_SERVER`/`MSSQL_MCP_USER`/`MSSQL_MCP_PASSWORD` from the
environment — 15 scripts that used to hardcode a literal password were
redacted to this pattern before this repo's first commit. `.env` files,
`.hermes_infra_creds/`, and anything password-shaped are gitignored.

---

## 9. Known limitations / open items

- The `EscalationCategory` split (`UNRESOLVED` vs `NEEDS_HUMAN_ACTION`)
  and the `AttemptNo`-capped reject-rework loop are new as of 2026-09-05
  — verified live (11 rows correctly tagged, 6 pre-existing stale tickets
  up to 10 attempts deep escalated and confirmed excluded from
  re-polling), but haven't yet run through a full multi-day cycle under
  the current `qwopus3.5-9b-coder` model.
- `l2-ministral`/`l2-nemo` (earlier architecture iteration, unused) have
  been deleted (2026-09-05), not just left installed.
- The investigator model was switched from `gemma-4-e4b-it` to
  `qwopus3.5-9b-coder` (2026-09-05) after evaluating LM Studio's full
  local model catalog; not yet run through the same multi-day volume the
  gemma configuration saw, so its real reject/rework/escalation rates
  under load are still unproven, only spot-checked.
- **Cross-run context loss**: each investigation attempt starts cold —
  a rejected attempt's reviewer objection is passed forward via the
  rework card body, but a genuinely NEW ticket gets no benefit from a
  similar ticket solved days earlier beyond whatever mem0 happens to
  surface unprompted. Evaluating Microsoft Conductor and
  knowledge-base-retrieval tooling for this gap is an open, in-progress
  task — see `Plans/` for the latest research findings once written up.
