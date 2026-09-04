# Codex handoff prompt — Agent_Comms channel setup (2026-09-02)

Give this to Codex on the teammate's laptop.

---

## Prompt

```
There is a folder named "Agent_Comms" in the synced AIHelpdesk project
(same root as AGENTS.md/CLAUDE.md/Hermes_Orchestrator.py). Read
Agent_Comms/PROTOCOL.md in full first -- it defines a file-based message
channel between Claude (Snehil's laptop) and you (Codex, running via a
Hermes Agent Routine on this laptop). Follow it exactly, including the
numbering/status rules.

TWO THINGS TO DO:

1. RIGHT NOW: there is already one pending request waiting for you --
   Agent_Comms/0001-l2-bot-status-check.md (status: pending, to: codex).
   Read it, actually do what it asks (real commands, real output -- no
   guessing or reporting something you didn't verify), write your findings
   into its "## Response" section, set status: answered and answered: to
   the current timestamp. Save the file.

2. THEN: set up a recurring Hermes Routine so you keep checking this folder
   automatically going forward, using the same profile/gateway already set
   up for l2-investigator (reuse it -- don't create a second bot for this):

   hermes profile use l2-investigator
   hermes cron create "10m" "Check the Agent_Comms folder in this project for files with status: pending and to: codex. Follow Agent_Comms/PROTOCOL.md exactly -- do the real work each request asks for, write real verified output into its Response section, set status: answered. If there is nothing pending, do nothing and reply with nothing more than 'no pending requests'." --workdir "<LOCAL_AIHELPDESK_PATH>" --deliver "bot-chat:l2-investigator" --name "Check Agent_Comms for Claude requests"
   hermes profile use default

   (Use whatever the actual local synced project path is -- same one you
   used when setting up the l2-investigator ticket-polling Routine earlier.
   10-minute interval, not 5, so this doesn't compete for attention with
   the ticket-polling Routine on the same bot.)

   Verify it's registered: `hermes -p l2-investigator cron list` should
   show both "Poll Helpdesk L2 tickets" and "Check Agent_Comms for Claude
   requests" as active jobs.

Report back: what you found for request 0001 (paste the actual command
output you used), and confirmation the new Routine is registered and
active.
```
