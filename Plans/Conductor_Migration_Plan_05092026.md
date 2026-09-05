# Conductor migration plan (2026-09-05)

Explicit phase boundaries so this migration never sits in an ambiguous
half-state — at every point below, exactly one system (Kanban or
Conductor) owns the live ticket pipeline, never both at once.

## Decision made this session

Path A: Conductor's `openai` provider, pointed directly at LM Studio
(`http://100.111.69.102:1235/v1`), driving tool calls with Conductor's
own step/tool model. Conductor's `hermes` provider (NousResearch
`hermes-agent` as a Python library) was evaluated and rejected for this
migration — it is a separate library invocation, not a bridge to the
already-built desktop Hermes profiles/skills/kanban/mem0; using it would
mean re-declaring persona/tools in Conductor YAML anyway, on an
experimental-tier provider, for no benefit over the stable `openai` path.

**Consequence**: the L2 pipeline's use of the Hermes desktop platform
(kanban, the 5 xstudio skills, mem0) is being fully retired as this
migrates, not partially kept. `infra-guardian` and anything else on this
machine keeps using Hermes normally, unaffected — this is scoped to the
L2 ticket pipeline only.

## Phase 0 — done, verified this session

- Installed Conductor v0.1.36 in WSL2 Ubuntu (`uv tool install
  git+https://github.com/microsoft/conductor.git`) — matches where the
  primary Hermes install already lives, and avoids Conductor's own
  documented Windows-`subprocess` gotcha (`.bat`/`.ps1` resolution).
- `conductor doctor` confirmed `openai` provider stable/installed,
  `hermes` provider experimental/not installed.
- Installed `mcp<2` (pinned — 2.x renamed FastMCP to MCPServer) into the
  Windows Python interpreter (`/mnt/c/Python314/python.exe`) that already
  has `pyodbc`, matching this project's established pattern of always
  invoking that interpreter for anything DB-related, even from WSL.

## Phase 1 — done, built and syntactically validated this session; NOT yet run against a live ticket

Scope: prove the investigate step alone works end-to-end against
`qwopus3.5-9b-coder`, with zero risk to the live Kanban pipeline (which
keeps running completely unaffected in parallel).

Built:
- **`Hermes_Orchestrator.py` additions** (all live-tested against the
  real DB, independent of Conductor):
  - `suggest_tables_mechanically()` / `--suggest-tables` — narrows ~1200
    real tables down to the handful relevant to a ticket's own text via
    keyword overlap (table/column name tokens + an optional curated
    domain-keyword index), no LLM, no embeddings. Verified against real
    ticket text; a real scoring bug (a table whose columns share one
    repeated prefix word drowning out genuinely relevant tables) was
    found and fixed during testing.
  - `Knowledge/table_keyword_index.json`, built by the new
    `Model_Bench/build_table_keyword_index.py` from the existing curated
    domain docs (`xbatch-investigation-surfaces.md`,
    `sohar-sms-event-workflows.md`, `task-router.md`) — 63 keywords to
    129 real tables, mechanically extracted, not hand-typed. Re-run this
    script whenever those docs change.
  - **Investigation ledger**: reused the already-existing but never-
    populated `InvestigationJson` column on
    `Hermes_L2_Response_Trn_Tbl` (no schema change needed) as the
    structured findings record. `--publish-response --ledger '<json>'`
    stores it on a terminal response; new `--save-ledger --run-id ID
    --ledger '<json>'` stores it independent of outcome (so a rejected
    investigation's findings survive); new `--get-ledger --ticket-id ID`
    reads back the most recent one for a ticket. This is the concrete
    fix for "context dropping" from the earlier research — carried
    forward verbatim, never re-summarized by the model.
  - Real, previously-undetected bug found and fixed while building this:
    `build_query_mechanically()`'s generated SQL was never database-
    qualified (`dbo.Table`, not `[Database].dbo.Table`), so `--build-query
    --execute` against a table that only exists in `XStudio_Xbatch`
    would silently run against whichever database the connection
    happened to already be open on. Fixed to always emit a three-part
    qualified name; verified live against `XStudio_Xbatch.dbo.SAP_Posting_Tbl`
    from a connection opened against the default `XStudio_Helpdesk`.
  - `run_readonly_query()` — the guarded read path `--query` already
    used, factored out so new callers (the MCP server) share it instead
    of a second, divergent implementation.
- **`Model_Bench/l2_investigation_mcp_server.py`** — a local stdio MCP
  server exposing `suggest_tables`, `build_query`, `find_sql_objects`,
  `get_sql_object_definition`, `search_solutions`, `execute_sql` as
  tools, each a thin wrapper around the already-audited orchestrator
  functions above. This replaces the raw `terminal` tool the old
  Hermes-Kanban investigator used to run `sqlcmd`/python one-liners
  directly. Verified standalone via a real stdio `ClientSession`
  handshake — all six tools list correctly.
- **`Model_Bench/conductor/l2_investigate_phase1.yaml`** — the actual
  workflow: `poll_ticket` (script, real atomic claim) → `investigate`
  (agent, `qwopus3.5-9b-coder`, the six MCP tools, `context.mode:
  explicit` so it sees only what its own `input:` declares) →
  `release_claim` (script, `--fail-run` — cleanly releases the claim
  instead of publishing, since nothing downstream is wired yet).
  `conductor validate` passes clean. Several real, version-specific
  schema corrections were needed along the way (this installed v0.1.36's
  actual field names differ from the public docs on `main`, confirmed by
  reading the installed source directly rather than re-guessing):
  `agents:`/`tools:`/`output:` are top-level keys, not nested under
  `workflow:`; context mode is `workflow.context.mode`
  (`accumulate`/`last_only`/`explicit`), not a per-step `context_mode`;
  an agent's `input:` is a flat list of `"agent_name.output"` strings,
  not a dict; and a workflow-level `tools:` allowlist (distinct from
  `runtime.mcp_servers.*.tools`) is what actually makes an
  `mcp_server__tool` name referenceable by an agent at all.

**Not yet done**: an actual `conductor run` against a real ticket. This
performs a genuine atomic claim on a real, shared ticket queue row (the
same kind of side effect any `--poll` test always has) — confirm before
running, same as every prior live-claim test in this project.

## Phase 2 — not started

Add `review` (agent, judgment only) and `publish`/`reject`/`escalate`
steps to the SAME workflow, replacing
`kanban_approval_publisher.py`/`kanban_reject_bridge.py`'s logic with
Conductor `script` steps calling the exact same
`Hermes_Orchestrator.py --publish-response`/`--fail-run`/
`--escalate-blocked` primitives — nothing new invented there, just a
different caller. The `AttemptNo`-based reject-rework cap and the
`EscalationCategory` split carry over unchanged; they're properties of
the SQL layer, not the orchestration layer.

## Phase 3 — not started (the actual cutover point)

Retire `ticket_scout.py`'s kanban-card-creation role. Either replace its
cron trigger with one that calls `conductor run` directly, or keep a
thin cron wrapper that does the same `--poll` claim and then invokes
Conductor for everything after. Only after Phase 1+2 are proven reliable
across real ticket volume (not just one test run) should live dispatch
actually move — this is the line past which Kanban stops receiving new
tickets.

## Phase 4 — not started (decommission)

Retire the 4 xstudio-* skills for this pipeline
(`xstudio-l2-ticket-workflow`, `xstudio-sap-api-investigation`,
`xstudio-sohar-heat-execution`, `xstudio-quality-delay-workorder`;
`xstudio-sql-write-discipline`'s official-SP-first rule gets folded into
the `investigate` step's own system_prompt instead), the
`l2-eval-investigator`/`l2-gemma-verifier`/`l2-qwen-verifier` Hermes
profiles, and this pipeline's mem0 setup. `l2-investigator` itself likely
stays (it may still host anything genuinely still needed from the
desktop platform), but audit that explicitly rather than assuming.

## What stays exactly as-is throughout

The SQL layer (`Knowledge/*.sql`, all `Hermes_L2_*`/`Hermes_L3_*`
tables/procs) is orchestration-agnostic — nothing above touches it.
Whichever orchestrator is calling `Hermes_Orchestrator.py`, the audited
write path, the reject-rework cap, and the escalation categories are
unchanged.
