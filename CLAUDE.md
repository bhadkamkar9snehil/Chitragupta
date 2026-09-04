# Claude / Agent Entry Point — AI Helpdesk (Hermes L2)

Read `AGENTS.md` first — full folder map, deployment state, SQL write
discipline, and the "Hermes" naming-collision warning.

## Current state (2026-09-02, end of day) — read this before touching anything

**Primary working install is now WSL2 Ubuntu**, not native Windows — the
native install hit a real, unfixable-here `[Errno 36]` POSIX-locking bug in
Hermes's own cron fire fence. Both installs still exist and both have the
`l2-investigator` profile, but WSL is the one whose gateway actually runs
Routines. WSL2 itself needed a persistence fix: the VM silently shuts down
when idle, taking its systemd services (and the gateway) down with it —
fixed via `vmIdleTimeout=-1` in `%UserProfile%\.wslconfig` plus a hidden
Startup-folder `WSL_KeepAlive.vbs` holding one background
`wsl -d Ubuntu -- sleep infinity` session.

- Bot/profile: `l2-investigator`, WSL path
  `~/.hermes/profiles/l2-investigator/` (`/home/snehil/...`), Windows path
  `C:\Users\Admin\AppData\Local\hermes\profiles\l2-investigator\` (parallel,
  secondary)
- Persona/instructions: that profile's `SOUL.md` — routes to
  `Knowledge/task-router.md` and five `xstudio-*` Skills for what to check;
  see "Durable Skills" below
- Routine: "Poll Helpdesk L2 tickets", every 5 min, script
  `hermes_l2_poll.py`, **delivers to `local`, NOT `bot-chat:l2-investigator`**
  — the bot-chat delivery mode was the original setup and caused a real
  context-overflow outage (one ever-growing thread instead of isolated
  per-run sessions); fixed via `hermes cron edit <job-id> --deliver local`.
- Gateway installed as a systemd user service
  (`hermes-gateway-l2-investigator.service`), started automatically by the
  WSL keep-alive session above.
- Check it: `hermes -p l2-investigator cron status` /
  `cron runs` (run from WSL: `wsl -d Ubuntu -- ...`), or tail
  `~/.hermes/profiles/l2-investigator/logs/gateway.log`.

**Durable Skills (2026-09-02)**: domain/procedure knowledge that used to be
hardcoded prose in `SOUL.md` is now five local Hermes Skills under
`skills/xstudio/` on this profile — `xstudio-l2-ticket-workflow`,
`xstudio-sap-api-investigation`, `xstudio-sohar-heat-execution`,
`xstudio-quality-delay-workorder`, `xstudio-sql-write-discipline`. Verify
with `hermes -p l2-investigator skills list`. `Knowledge/task-router.md`
maps ticket patterns to both the matching skill and the matching
`Knowledge/*.md` file.

**A second bot, `infra-guardian`, now maintains this bot's infrastructure**
(WSL only) — separate profile/gateway, 30-min Routine, one skill
(`hermes-infra-guardian-checks`) covering gateway/VM/LM-Studio/session
health with an explicit guardrail: it reports LM Studio being down, never
tries to fix it (the user controls that machine directly). See `AGENTS.md`
for the full incident chain this was built in response to.

**Known unresolved issue as of setup**: manual test calls to this profile's
model provider (`gpt-5.6-terra`) failed twice with "Hermes can't reach the
model provider" — and the *same* error hit the pre-existing `local-coder`
profile too, so it's not something wrong with the new profile's config. Looks
like a transient provider/network issue on this machine, not something to
"fix" in this project. If Routine runs keep failing with this same error,
that's the first thing to check (`hermes -p l2-investigator -z "test"`).

**Why `Hermes_Orchestrator.py` is now only ~600 lines of thin wrappers, not
a full pipeline**: the user directly asked why a hand-written script should
be doing investigation at all when a real reasoning bot exists. Correct
question — the keyword-search "brain" (`investigate()`, `run_one_cycle()`)
was deleted. What's left is exactly the two primitives worth not
re-deriving from scratch each run: atomic claim (`--poll`) and audited
write-back (`--publish-response`). Investigation itself is the bot's job,
using its own terminal tool.

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
   … `50_response_and_workflow.sql`), never `00_Hermes_L2_FULL_INSTALL.sql`
   directly.
2. Regenerate `00_Hermes_L2_FULL_INSTALL.sql` by concatenating the six files
   in numeric order.
3. Deploy with `sqlcmd` (handles `GO` batch separators; `pyodbc` does not) —
   prepend `SET QUOTED_IDENTIFIER ON; GO` or the filtered index on
   `Hermes_L2_Response_Trn_Tbl` fails to create.
4. Run `Knowledge/99_postflight.sql` and confirm no errors.
5. Schema changes to a live, shared database are confirm-first with the
   user, even though the install script is additive-only.
