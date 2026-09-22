# Agent_Comms — Claude <-> Codex <-> Antigravity async channel

This folder is a file-based message queue between AI agents working on the
AIHelpdesk / Hermes L2 project, with no shared API or live bridge between
them -- this folder is the only transport, full stop. **All three agents
here run on Snehil's own laptop.** None of them poll this folder
automatically; Snehil is the transport for every leg.

- **Claude** (Claude Code) — no persistent background process. Reads/writes
  this folder only when invoked in a session.
- **Codex** — a local terminal/IDE coding agent on this same laptop,
  invoked manually by Snehil per task (no Hermes Agent Routine, no
  scheduler, no direct autonomous access to this repo outside a session
  Snehil starts). Snehil relays: he gives Codex a request's content, and
  brings its output back for Claude to read.
- **Antigravity** — same laptop, in the XS_Builder workspace, invoked
  manually by Snehil per task, same relay pattern as Codex (no scheduler,
  no direct filesystem/API access to this repo from inside its own
  session). Snehil copies a request's content into Antigravity, and copies
  its finished output back out as a file Claude then reads from this
  folder (or from wherever Antigravity saved it -- Claude checks
  Downloads/ and the working tree if it isn't in Agent_Comms/ yet).

No agent has any other way to reach another directly. Treat Snehil's manual
copy-paste as the transport for all three legs -- the file format and
numbering below is what makes that relay auditable, not a live channel.

## Scope: not just tickets

This channel is general-purpose, not limited to Hermes L2 ticket status.
Any agent can ask another about anything relevant to the shared project(s)
on this laptop — XS_Builder work, XStudio/XKB findings, build/deploy state,
errors hit, whatever comes up. Don't assume a request is ticket-related
just because earlier threads were.

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
  trail across sessions that don't otherwise share state.
- **Be concrete, not aspirational.** A response/finding claiming something
  works or is true must be backed by an actual command's output, quoted —
  not a claim you didn't verify.
- **New topics get their own new numbered file.** Don't append unrelated
  asks/findings into an existing thread.
- **Don't manufacture findings.** A `finding` should be something you'd
  actually stop and mention if you were pairing with someone — not routine
  "everything's fine" noise. If nothing's noteworthy, don't write one.

## What Claude should do

Claude has no automatic schedule -- it checks this folder for `to: claude`
files (both answered requests and findings) whenever asked to, in a normal
session, and should proactively mention any unread `finding` threads to the
user even if they weren't specifically asked about.

## Working with Codex or Antigravity (both relay-only, identical mechanics)

Neither Codex nor Antigravity can poll this folder or edit its files
themselves -- Snehil is the transport for both. When Claude wants either of
them to do something:

1. Write a normal `type: request` file here, `to: codex` or
   `to: antigravity` as appropriate (same format as any other thread) --
   self-contained, assumes no other context beyond this file and
   `AGENTS.md`/`CLAUDE.md`.
2. Tell Snehil the file exists and ask him to hand its `## Request` content
   to the relevant agent.
3. When Snehil brings back that agent's output (pasted text, a file path,
   a saved `.md`/`.docx`, whatever form it takes), Claude reads it and is
   the one who writes it into `## Response` in the original request file --
   filling in `status: answered` and `answered:` the same as any other
   reply. Claude checks Downloads/ and the working tree for a saved output
   file if Snehil doesn't hand over the content directly.

If either agent produces a finding unprompted (Snehil relays it without a
matching request file), Claude creates the `type: finding` file itself,
`from: codex` or `from: antigravity`, `to: claude`, once it has read and
understood the content -- don't paraphrase away specifics; quote real
output the same way any other agent's finding must be backed by real
evidence, not a claim.
