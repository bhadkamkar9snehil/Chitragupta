# Codex handoff prompt — teammate laptop Hermes L2 setup (2026-09-02)

Give this whole prompt to Codex running on the teammate's laptop. It mirrors
the `l2-investigator` bot/Routine/gateway setup already done on Snehil's
machine, adapted to run locally there (Hermes profiles/cron/gateway are
per-machine, not synced by Syncthing — only the project folder itself is).

---

## Prompt

```
The folder you're running in (or a folder named "AIHelpdesk" somewhere on
this machine, synced via Syncthing from a teammate's laptop) contains a
project with AGENTS.md and CLAUDE.md at its root. Read both files in full
first -- they are the source of truth for this task, more current than
anything below if they conflict.

GOAL: this machine has its own local install of Hermes Agent (Nous
Research's desktop agent platform, github.com/NousResearch/hermes-agent) at
~/AppData/Local/hermes, with a ChatGPT/OpenAI subscription already
configured as its model provider. Set up the SAME "l2-investigator" bot/
profile/Routine on THIS machine's Hermes install, so this laptop can also
poll and investigate XStudio Helpdesk L2 tickets -- in parallel with the
identical setup on the other laptop. This is safe: ticket claiming is
atomic (SQL Server sp_getapplock), so two machines polling the same ticket
pool cannot double-claim a ticket. Do not treat "another machine might also
be polling" as a reason to hold back.

STOP AND ASK (do not guess/invent) if any of these are true:
- MSSQL_MCP_SERVER / MSSQL_MCP_USER / MSSQL_MCP_PASSWORD are not set as
  Windows user environment variables on this machine. Check with:
  [Environment]::GetEnvironmentVariable('MSSQL_MCP_SERVER','User')  (PowerShell)
  If missing, ask the human for them -- do not hardcode a guessed password
  anywhere, and do not proceed without real credentials.
- This machine cannot reach 10.2.6.204 (no VPN/network access). Verify with
  a real connection attempt (step 3 below), don't assume it works.
- The synced project folder's absolute path differs from
  C:\Users\Admin\Documents\Office\AIHelpdesk (it likely does -- Syncthing
  syncs content, not the absolute path). Find the real local path first and
  use it everywhere below instead of that one.

STEPS:

1. Find `hermes.exe` on this machine (likely
   ~/AppData/Local/hermes/bin/hermes.exe). Run `hermes --version` to
   confirm it works. Run `hermes profile list` to see what profiles already
   exist here.

2. Find the local Python interpreter that has (or can have) `pyodbc`
   installed. Check with `python -c "import pyodbc; print(pyodbc.__file__)"`.
   If it's missing, `pip install pyodbc` for that interpreter. Note its
   full path -- you'll need it in step 6.

3. Prove DB connectivity from this machine before doing anything else:
   `python "<local AIHelpdesk path>\Hermes_Orchestrator.py" --discover-workflow --server 10.2.6.204`
   This should print live Status/AskStatus combinations from
   dbo.Complaint_Mst_Tbl. If it errors, stop and report the error --
   don't proceed to create a bot that can't actually reach the database.

4. Create the profile (clone from whichever existing local profile already
   has terminal/coding tool access and a working model, if one exists;
   otherwise create fresh and run `l2-investigator setup` to point it at
   the ChatGPT/OpenAI provider):
   `hermes profile create l2-investigator --clone-from <base-profile-name> --description "Investigates XStudio Helpdesk L2 tickets in Complaint_Mst_Tbl (10.2.6.204/XStudio_Helpdesk): claims a ticket, investigates using live SQL against XStudio_Helpdesk and XStudio_Xbatch, writes findings back through the audited Hermes_L2_* stored procedures."`

5. Edit that profile's SOUL.md
   (~/AppData/Local/hermes/profiles/l2-investigator/SOUL.md) -- APPEND this
   section (keep whatever default persona text is already there above it),
   substituting <LOCAL_AIHELPDESK_PATH> for the real local path found above:

   ## Role: L2 Helpdesk ticket investigator

   You investigate one XStudio Helpdesk L2 ticket per Routine run, using
   your terminal tool to run real SQL against a real SQL Server. Full
   project context (schema facts, what's built, what's not, past mistakes
   to avoid) is in `<LOCAL_AIHELPDESK_PATH>\AGENTS.md` -- read it if this is
   your first run or anything here seems stale; that file is the source of
   truth, this is a summary.

   ### Each run

   1. **Poll and claim** (do this first, always):
      ```
      python "<LOCAL_AIHELPDESK_PATH>\Hermes_Orchestrator.py" --poll --eligible-status "Enter" --server 10.2.6.204
      ```
      Prints JSON. "NO_TICKETS" or "NO_CLAIMABLE_TICKET" means nothing to
      do -- say so briefly and stop, don't invent work. "CLAIMED" gives you
      run_id, ticket_id, the full ticket row (including
      ProblemCategory/SourceSystem/ExtractedEntitiesJson/etc. if populated
      -- usually still NULL today), and prior_runs.

   2. **Investigate** using your own judgment and your terminal tool.
      Credentials are in your environment (MSSQL_MCP_SERVER, MSSQL_MCP_USER,
      MSSQL_MCP_PASSWORD). Query directly, e.g.:
      ```
      sqlcmd -S 10.2.6.204 -U sa -P "%MSSQL_MCP_PASSWORD%" -C -d XStudio_Xbatch -Q "SELECT TOP 20 * FROM sys.procedures WHERE name LIKE '%Billet%';"
      ```
      Two databases matter: XStudio_Helpdesk (the ticket itself) and
      XStudio_Xbatch (production data -- SAP posting, heat/billet tracking,
      quality, etc.). Rule: inspect before you trust -- a procedure named
      like a read can still write; check
      `OBJECT_DEFINITION(OBJECT_ID('dbo.<Name>'))` first. Prefer an
      existing official stored procedure over a raw table write when one
      covers the operation. Do not guess table/column names from memory --
      query INFORMATION_SCHEMA/sys.columns/sys.procedures first.

   3. **Publish your finding** (always finish with exactly one of these --
      never leave a run claimed with no response):
      ```
      python "<LOCAL_AIHELPDESK_PATH>\Hermes_Orchestrator.py" --publish-response --run-id <run_id> --response-type UPDATE --reply-text "..." --server 10.2.6.204 [--problem-summary "..."] [--findings "..."] [--root-cause "..."] [--resolution "..."] [--new-ticket-status "..."] [--mirror-to-support-remarks]
      ```
      --response-type is one of:
      - UPDATE -- looked into it, have something useful, not a fix, doesn't
        need the user. Common case for now. Pass
        --new-ticket-status "Solution Work in Progress" so it isn't
        re-claimed next run.
      - QUESTION -- need more info from the requester.
      - RESOLUTION -- confident you found and verified the actual fix.
      - L3_ESCALATION -- genuinely needs a human engineer.
      Never invent a --new-ticket-status value -- re-check with
      --discover-workflow if unsure what's currently live.

   ### What not to do

   - Don't write directly to Complaint_Mst_Tbl.Status/SupportExecutiveRemarks
     yourself -- always go through --publish-response.
   - Don't skip step 3 -- a claimed-but-unpublished run blocks that ticket
     (auto-recovers as stale after ~60 min, but that's a failure mode).
   - Don't fabricate certainty -- say plainly in an UPDATE if you found
     nothing useful.

6. Create ~/AppData/Local/hermes/profiles/l2-investigator/scripts/hermes_l2_poll.py:
   ```python
   #!/usr/bin/env python3
   import subprocess
   import sys

   PYTHON = r"<PYTHON_PATH_FROM_STEP_2>"
   ORCHESTRATOR = r"<LOCAL_AIHELPDESK_PATH>\Hermes_Orchestrator.py"
   ELIGIBLE_STATUS = "Enter"
   SERVER = "10.2.6.204"

   sys.exit(subprocess.call([
       PYTHON, ORCHESTRATOR,
       "--poll", "--eligible-status", ELIGIBLE_STATUS,
       "--server", SERVER,
   ]))
   ```

7. Register the Routine:
   ```
   hermes profile use l2-investigator
   hermes cron create "5m" "A poll script ran before this prompt and injected the result above (or you'll see NO_TICKETS/NO_CLAIMABLE_TICKET). If nothing was claimed, reply with nothing more than 'no tickets' and stop -- do not investigate. If a ticket was claimed, follow SOUL.md exactly: investigate using your terminal tool against XStudio_Helpdesk and XStudio_Xbatch on 10.2.6.204, then finish by running Hermes_Orchestrator.py --publish-response for this run_id. Never leave a claimed run unpublished." --script hermes_l2_poll.py --workdir "<LOCAL_AIHELPDESK_PATH>" --deliver "bot-chat:l2-investigator" --name "Poll Helpdesk L2 tickets"
   hermes profile use default
   ```

8. Install the gateway so it actually fires on a schedule:
   ```
   hermes profile use l2-investigator
   hermes gateway install
   ```
   Accept the interactive prompts (start now: yes; auto-start on login:
   yes). If it asks for UAC elevation and you can't grant it, let it fall
   back to the Startup-folder method -- that's what happened on the other
   laptop and works fine (and runs hidden, no console window).
   `hermes profile use default` afterward to leave the active profile
   unchanged.

9. Verify, don't just assume:
   - `hermes -p l2-investigator cron status` should show the gateway
     running and the job active with a next-run time.
   - Run the poll script standalone ONCE to prove it works:
     `python "~/AppData/Local/hermes/profiles/l2-investigator/scripts/hermes_l2_poll.py"`
     This performs a REAL claim on a REAL ticket in the shared database --
     tell the human before running it. If it claims a ticket, that's
     success; the claim will self-recover as stale in ~60 minutes if
     nothing publishes a response, so it's safe to leave as a pure
     connectivity/plumbing test if you don't want to also do a full manual
     investigation right now.

10. Report back: what was created, what was verified working, what (if
    anything) needed a human decision or failed. Do not report success on
    anything you didn't actually verify with a real command's output.
```
