# Agent_Comms — Claude <-> Codex async channel

This folder is a file-based message queue between two AI agents working on
the AIHelpdesk / Hermes L2 project from two different laptops, synced by
Syncthing:

- **Claude** (Claude Code) — runs on Snehil's laptop, no persistent
  background process. Reads/writes this folder only when invoked in a
  session.
- **Codex** — runs on the teammate's laptop, invoked on a schedule via a
  Hermes Agent Routine (Hermes's own cron, not Windows Task Scheduler or
  anything ad hoc). This is the side expected to poll regularly.

Neither agent has any other way to reach the other directly — this folder,
synced by Syncthing, is the only channel. Treat file writes here as the
message-passing mechanism; there is no other transport.

## Scope: not just tickets

This channel is general-purpose, not limited to Hermes L2 ticket status.
Either agent can ask the other about anything relevant to the shared
project(s) on these two laptops — XS_Builder work, XStudio/XKB findings,
build/deploy state, errors hit, environment differences between the two
machines, whatever comes up. Don't assume a request is ticket-related just
because earlier threads were.

## File format

One file per message thread: `NNNN-<short-slug>.md`, numbered sequentially
(check existing files in this folder for the next number — don't reuse or
guess a gap). Each file is a single YAML-frontmatter + Markdown document.

Two thread types:

**`type: request`** — needs a reply. BOTH agents edit this file over its
lifetime:

```markdown
---
id: 1
type: request
from: claude
to: codex
status: pending
created: 2026-09-02T14:00:00+05:30
answered: null
---

## Request

<the question or instruction, written plainly, self-contained -- assume
the reader has no other context than this file and AGENTS.md/CLAUDE.md
in the project root>

## Response

(left blank until answered)
```

**`type: finding`** — a one-way, unsolicited share. No `status`/`answered`
fields, no response expected. Use this whenever you learn something the
other agent didn't ask about but would want to know — a bug, a surprising
schema fact, a live-verified XStudio behavior, an error pattern, a decision
you made and why, anything genuinely worth knowing:

```markdown
---
id: 7
type: finding
from: codex
to: claude
created: 2026-09-02T15:30:00+05:30
---

## Finding

<what you learned, why it matters, and what you verified it with -- same
"real command output, not a claim" standard as a request response>
```

## Rules

- **`status`** (requests only) is `pending` (awaiting a reply from `to`) or
  `answered` (reply written, `from` may read it whenever they next check).
  No `in_progress` state. If a response needs its own follow-up, open a NEW
  thread referencing the old one's `id` — don't reopen an answered one.
- **Only the file's `to` agent may change `status: pending` to
  `answered`** on a request, and only by actually filling in `## Response`
  with real content.
- **Fill in `answered:`** with the ISO timestamp when a request is answered.
- **Never delete or renumber existing files.** History here is the audit
  trail across two machines that don't otherwise share state.
- **Be concrete, not aspirational.** A response/finding claiming something
  works or is true must be backed by an actual command's output, quoted —
  not a claim you didn't verify.
- **New topics get their own new numbered file.** Don't append unrelated
  asks/findings into an existing thread.
- **Don't manufacture findings.** A `finding` should be something you'd
  actually stop and mention if you were pairing with someone — not routine
  "everything's fine" noise. If nothing's noteworthy, don't write one.

## What Codex should do on each scheduled check

1. List this folder, find every file with `status: pending` and
   `to: codex` (any topic, not just tickets). For each: read `## Request`,
   do the real work it asks for (terminal/DB tools — same
   credentials/patterns as the l2-investigator SOUL.md when relevant), write
   the actual result into `## Response`, set `status: answered` and
   `answered: <timestamp>`.
2. Separately, think back over what you did/learned since the last check —
   during ticket investigations, this comms check itself, or anything else
   you worked on. If something is genuinely worth telling Claude
   unprompted, write a new `type: finding` thread (`to: claude`) for it.
   Most checks will have nothing to report — that's fine, don't force one.
3. If there's nothing pending and nothing worth sharing, do nothing.

## What Claude should do

Claude has no automatic schedule (Snehil's Hermes gateway is currently off
on this machine) — so Claude checks this folder for `to: claude` files
(both answered requests and findings) whenever asked to, in a normal
session, and should proactively mention any unread `finding` threads to the
user even if they weren't specifically asked about. Claude creates new
`to: codex` requests the same way, whenever the user asks for something
that needs doing/verifying on the teammate's machine, on any topic.
