# AI Helpdesk / Hermes L2 — Agent Rules

## No scratch files in this project root

Investigating bots (Windows, WSL, and Codex on the teammate's machine — this
folder syncs both ways via Syncthing) have repeatedly littered this
directory with one-off investigation scripts (`_ticket43_live_read.py`,
`lrf_investigation_queries.sql`, etc.) and even a broken script that
imported a nonexistent `hermes_tools` module. **Do not write files here to
investigate a ticket.** Run SQL/Python directly via your terminal tool
(`sqlcmd -Q "..."` or `python -c "..."`/a python one-liner with `-c`); if you
genuinely need a scratch file, use your own tmp directory, never this
project's folder. `Hermes_Orchestrator.py`'s functions are called by
importing that module directly (`from Hermes_Orchestrator import
HermesL2Client`) — there is no `hermes_tools` package, and `terminal` is a
tool you call directly, not a Python function to import.

## What this project is

A live investigator for the existing XStudio Helpdesk (`XStudio_Helpdesk` on
SQL Server `10.2.6.204`). Not a collection of domain bots, no vector
DB/RAG/embeddings, does not replace the existing Helpdesk ticketing system.
The real ticket table is `dbo.Complaint_Mst_Tbl` — reads/writes go through it
directly via the workflow discovered live, never a parallel queue.

```
End user  <->  L1 chatbot (NOT built yet -- lives outside this project)
                    |
                    |  only when L1 can't resolve it -- writes ONE row
                    v
     dbo.Complaint_Mst_Tbl (Status='Enter' + the ProblemCategory/
     SourceSystem/ConversationSummary/SuspectedCause/ExtractedEntitiesJson/
     ConversationLogJson columns L1 fills in -- this row IS the L2 ticket)
                    v
     Hermes Agent (Nous Research's desktop agent platform, installed at
     C:\Users\Admin\AppData\Local\hermes -- see [[hermes-agent-platform]]
     memory) -- Bot "l2-investigator" -- Routine "Poll Helpdesk L2 tickets"
     (every 5 min, via the bot's own gateway/cron, NOT Windows Task
     Scheduler and NOT Claude Code's CronCreate -- both tried, both rejected)
                    v
     hermes_l2_poll.py (deterministic, no LLM) claims one ticket atomically
     and injects its full context into the bot's prompt
                    v
     the BOT investigates -- real LLM reasoning, using its own terminal
     tool to run sqlcmd/python against XStudio_Helpdesk and XStudio_Xbatch
                    v
     bot finishes by running Hermes_Orchestrator.py --publish-response
     (QUESTION / UPDATE / RESOLUTION / L3_ESCALATION), written back to the
     real ticket through the audited Hermes_L2_* stored procedures
```

**L1 does not exist.** Nothing in this project talks to end users or decides
when to escalate. `Complaint_Mst_Tbl` is also still the plain manual IT
helpdesk table any human can file a ticket into directly — there is no field
that proves a given row came from L1 rather than a person. Working
assumption (confirmed with the user 2026-09-02): `Status='Enter'` is the
eligibility filter regardless; L1 populating the structured columns is what
turns a ticket from a bare complaint into something meaningfully
investigable.

**"Hermes" names two unrelated things — do not conflate them.** (1) The
project's own L2 investigator concept, from the user's original whiteboard
plan. (2) Nous Research's real Hermes Agent desktop platform, installed on
this machine, with its own Bots/Profiles/Cron/Gateway. Early work in this
project built a standalone Python script + tried Claude Code's `CronCreate`
+ tried a raw Windows Scheduled Task — all wrong, because none of them used
the actual Hermes Agent platform the user meant. See the
[[hermes-l2-helpdesk-project]] memory for the full history if this comes up
again. As of 2026-09-02 the real Hermes Agent bot (`l2-investigator` profile)
is what runs this — read `CLAUDE.md` for the current setup.

**A second bot, `infra-guardian`, maintains the first bot's infrastructure**
(2026-09-02, WSL only) — separate profile, separate gateway
(`hermes-gateway-infra-guardian.service`), 30-min Routine, does NOT touch
ticket content. Built after a real multi-hour outage chain that day: a
stalled cron ticker → traced to the whole WSL2 VM silently shutting down
when idle (fixed: `vmIdleTimeout=-1` in `.wslconfig` + a Startup-folder
`WSL_KeepAlive.vbs` holding one background `wsl sleep infinity` session,
same hidden-launch pattern as the existing Hermes gateway `.vbs`s) → a
context-compression exhaustion → a hung single LLM turn against a
deliberately-stopped LM Studio. `infra-guardian` exists so the next
occurrence of any of these gets caught by a dedicated bot instead of
another manual debugging session. Its whole runbook (health-check
commands, known-good baseline, and — critically — the guardrail that it
must only report LM Studio being down, never try to fix it) lives in its
`hermes-infra-guardian-checks` skill, not duplicated here.

**Working remote PowerShell to the desktop running LM Studio** (Tailscale
`B19CL3PC` / `100.111.69.102`), set up 2026-09-02 — confirmed working
end-to-end, both from this laptop's native PowerShell and from WSL via
interop:
```powershell
$cred = Import-Clixml "$env:USERPROFILE\.hermes_infra_creds\desktop_pc.xml"
Invoke-Command -ComputerName 100.111.69.102 -Credential $cred -ScriptBlock { ... }
```
From WSL: `/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -File "C:/..."` —
write the script to a `.ps1` file first (inline `-Command` mangles
`$variables` through the bash→wsl→powershell.exe chain) and use forward
slashes in the path (backslashes get stripped crossing the WSL→Win32
boundary). Full setup story, gotchas, and the "wrong machine" debugging
saga are in `infra-guardian`'s `hermes-infra-guardian-checks` skill and
the `desktop-pc-remote-access` Claude memory — don't re-diagnose from
scratch, read those first. **Never type a password into chat, even with
explicit user authorization** — that's a hard rule; use `Get-Credential`
interactively instead.

**Circular-dependency fix (2026-09-02)**: `infra-guardian`'s core health
checks (gateway ticker, LM Studio server, LM Studio actual generation) now
also run as a separate deterministic `--no-agent` cron job
(`infra_watchdog.py`, every 10 min, zero LLM calls) — the whole point
being that an LLM-driven health-check bot is useless when the LLM it needs
is the exact thing that's broken. The LLM-driven `hermes-infra-guardian-checks`
skill is for deeper analysis when the model IS available; the watchdog is
the check that survives when it isn't.

**Both bots now carry durable Hermes Skills, not just SOUL.md prose**
(2026-09-02, following Anthropic's/OpenAI's published agent-skill
guidance — narrow scope per skill, description written as a trigger
condition not a summary, high-signal gotchas over restating the obvious):
`l2-investigator` has five (`xstudio-l2-ticket-workflow`,
`xstudio-sap-api-investigation`, `xstudio-sohar-heat-execution`,
`xstudio-quality-delay-workorder`, `xstudio-sql-write-discipline`, all
under `skills/xstudio/`), `infra-guardian` has one
(`hermes-infra-guardian-checks`, under `skills/ops/`). Verify with `hermes
-p <profile> skills list`. `Knowledge/task-router.md` maps ticket patterns
to both the matching skill and the matching `Knowledge/*.md` file — add a
row there for anything new rather than only adding a skill.

## Folder map

- **`Hermes_Orchestrator.py`** — thin Python client around the 20
  `Hermes_L2_*` stored procedures. Deliberately does NOT contain any
  investigation logic (that used to be here as a keyword-search heuristic;
  removed 2026-09-02 — the calling bot reasons, this script doesn't). Two
  CLI entry points only:
  - `--poll --eligible-status "Enter"` — atomically claim one ticket, print
    its full context as JSON, stop. Wraps `Hermes_L2_Claim_Ticket_Usp`'s
    `sp_getapplock`/`UPDLOCK`/`OUTPUT`-param handling, which is genuinely
    easy to get wrong from scratch (this project got it wrong once already).
  - `--publish-response --run-id ID --response-type {QUESTION,UPDATE,
    RESOLUTION,L3_ESCALATION} --reply-text "..."` — write a response
    through `Hermes_L2_Publish_Response_Usp` so it lands in
    `Hermes_L2_Response_Trn_Tbl` with a proper audit trail instead of a raw
    `UPDATE Complaint_Mst_Tbl`.
  - `--discover-workflow` — print live `Status`/`AskStatus` combinations.
  See the module docstring for full changelog (v1 hallucinated schema, v2
  added a keyword-search brain, v3 removed the brain in favor of the bot).
- **`Knowledge/`** — the deployable SQL runtime and its design docs.
  - `00_Hermes_L2_FULL_INSTALL.sql` — deploy artifact, a straight
    concatenation of `00_tables_and_indexes.sql`, `10_helpdesk_discovery.sql`,
    `20_ticket_dispatch.sql`, `30_context_and_live_discovery.sql`,
    `40_investigation_runtime.sql`, `50_response_and_workflow.sql` in that
    order. **Edit the numbered per-concern file, then regenerate this one by
    re-concatenating** — do not hand-edit `00_Hermes_L2_FULL_INSTALL.sql`
    directly, it will drift out of sync (happened once already).
  - `99_postflight.sql` — verification script; run after any redeploy.
  - `*.md` — design docs (mental model, execution model, SQL write model,
    task router, SP catalog, runtime DB design, deploy playbook, validation
    notes). Short (< 160 lines each), safe to read in full.
- **`dbo.Complaint_Mst_Tbl` schema extension (2026-09-02)** — 6 nullable
  columns added directly to the live platform table, at the user's explicit
  instruction (they rejected a companion table): `ProblemCategory
  varchar(100)`, `SourceSystem varchar(100)`, `ConversationSummary
  nvarchar(max)`, `SuspectedCause nvarchar(max)`, `ExtractedEntitiesJson
  nvarchar(max)`, `ConversationLogJson nvarchar(max)`. Additive only —
  verified existing views/rows/procs unaffected. `Hermes_L2_Get_Ticket_Context_Usp`
  uses `c.*` so these flow through automatically. Meant for the (not yet
  built) L1 chatbot to fill in; today they're NULL on real tickets, and the
  investigating bot should query/reason over them when present rather than
  assume they're always empty.
- **`Reference Documents/`** — the **one** copy of the live-exported
  `XStudio_Helpdesk` / `XStudio_Xbatch` schema and stored-procedure dumps.
  Large (schema: ~12K/33K lines, SPs: ~1K/54K lines). **Do not duplicate
  these into `Knowledge/`** — that happened once (~100K redundant lines,
  removed 2026-09-02). Grep the specific table/procedure needed instead of
  loading these files whole.
- **`Plans/`** — planning docs, one per planning session, dated in the
  filename.
- **`Knowledge/task-router.md`** (+ its machine-readable mirror
  `Knowledge/manifest.json`) — the entry point for domain knowledge. Routes
  a ticket's category/area/identifiers to the specific `Knowledge/*.md`
  file(s) worth loading, instead of either cold-searching with
  `find_sql_objects` or hand-listing files in `SOUL.md` (both bot profiles
  read this router now, 2026-09-02 — adding a new knowledge file means
  adding a row here, not editing `SOUL.md`).
  - **`Knowledge/xbatch-investigation-surfaces.md`** — curated map of the
    real SAP integration / historian / production-tracking / work order /
    quality / delay-OEE / billet-yard / API-transaction table and SP
    families in `XStudio_Xbatch`, grounded in live-exported schema/SP text
    (not name-guessing).
  - **`Knowledge/sohar-sms-event-workflows.md`** — one level deeper: the
    real event state-machine and workflow-SP SQL behind the EAF/LRF/CCM/
    Billets/SMS-Plant-Process-Time per-heat flows, sourced from the
    vendor's own project handover docs (confirms `XStudio_Xbatch` on
    10.2.6.204 **is** the Sohar Steel Oman plant). Explains *why* a value
    is wrong/missing, not just where it lives — e.g. it documents a real,
    live-confirmed `@ActualHeatID = @HeatID - 1` decrement in the SMS
    Plant Process Time workflow that looks like a bug but isn't.
  Still verify the specific object live before trusting either file — the
  map can go stale, schema drifts.

## Mechanism verification (2026-09-02)

All 20 `Hermes_L2_*` procedures were individually exercised against real
claimed tickets with real DB-state assertions (not just "no exception") —
every terminal outcome (`RESOLUTION`, `QUESTION`, `L3_ESCALATION`, `FAILED`
via each of `Resolve_Ticket`/`Ask_Question`/`Escalate_L3`/`Fail_Run`), the
full mid-investigation lifecycle (`Start_Investigation` → `Heartbeat` →
`Save_Investigation_State` → `Execute_SQL` → `Update_SQL_Action_Evidence` →
`Get_Run`/`Get_Run_Actions`), and the discovery surface
(`Find_SQL_Objects`, `Get_SQL_Object_Definition`, `Get_Reference_Documents`).
32/33 assertions passed on first run; the one apparent failure
(`Get_Candidate_Tickets` not immediately re-surfacing a just-failed ticket)
turned out to be correct retry-window behavior (`NextEligibleOn` filtering,
confirmed by re-checking after the window elapsed) — 0 real defects found.
`Recover_Stale_Runs` was separately proven working multiple times earlier in
the session (visible `"stale_runs_recovered"` counts in live cycle output).
Conclusion: the SQL runtime mechanism is sound. What's still shallow is
investigation *content* (see `xbatch-investigation-surfaces.md` above), not
the plumbing.

## Deployment state (verified 2026-09-02)

The Hermes SQL runtime **is deployed** to `10.2.6.204` / `XStudio_Helpdesk`:
2 tables (`Hermes_L2_Response_Trn_Tbl`, `Hermes_L2_SQL_Action_Trn_Tbl`) + 20
`Hermes_L2_*` stored procedures. `99_postflight.sql` ran clean. The full
poll→claim→publish cycle was proven end-to-end multiple times against real
tickets. Before assuming this is still deployed and current, re-run
`99_postflight.sql` — this paragraph is a snapshot, not live proof.

The install is idempotent (`IF OBJECT_ID(...) IS NULL` / `CREATE OR ALTER`)
— safe to re-run after edits. It does **not** touch `Complaint_Mst_Tbl`
directly (the 6 handoff columns were a separate, explicit `ALTER TABLE`).

**Bugs found and fixed during the original deploy**: `sp_getapplock`'s
`@Resource` parameter was passed as a string-concatenation expression
directly in the `EXEC` call — T-SQL doesn't accept expressions there, only
constants/variables (fixed via a `@LockResource` variable in
`20_ticket_dispatch.sql`/`40_investigation_runtime.sql`). Also needed `SET
QUOTED_IDENTIFIER ON` before running the install, or the filtered index on
`Hermes_L2_Response_Trn_Tbl` fails to create.

## SQL write discipline

Investigation and writes are not read-only — direct `UPDATE`/`INSERT`/DDL is
fine when no official path exists. Follow the precedence in
`Knowledge/sql-write-model.md`: resolve the real database/object → search
for the official SP/API that owns the operation → inspect its live
definition → use it if it covers the operation → only then a direct write,
deliberately → verify the full affected chain afterward. Prefer
`Hermes_L2_Execute_SQL_Usp` (records every action to
`Hermes_L2_SQL_Action_Trn_Tbl`) over an unaudited raw connection when
practical.

## Credentials

Never hardcode a password into a command that gets logged, written to a
file, or pasted into this repo. Everything here defaults to
`$MSSQL_MCP_SERVER` / `$MSSQL_MCP_USER` / `$MSSQL_MCP_PASSWORD` (persistent
Windows user env vars) when not passed explicitly. Note: the `SSLDATABASE`
hostname (`$MSSQL_MCP_SERVER`'s value) has intermittently failed to resolve
during testing even though the server is fine — the IP `10.2.6.204` has been
reliable every time; the cron poll script pins the IP explicitly for this
reason.

## Verify claims against the live server, not memory

This project has repeatedly had code written against guessed schema that
turned out not to exist (v1 of `Hermes_Orchestrator.py` invented tables and
columns wholesale). Query `sys.parameters` / `INFORMATION_SCHEMA` /
`sys.columns` before writing SQL against a table or procedure you haven't
just checked.
