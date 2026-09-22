# Agent_Comms — Claude <-> Codex <-> Antigravity async channel

This folder is a file-based message queue between AI agents working on the
AIHelpdesk / Hermes L2 project, with no shared API or live bridge between
them -- this folder is the only transport, full stop. **All three agents
here run on Snehil's own laptop.** None of them poll this folder
automatically; Snehil is the transport for every leg.

- **Claude** (Claude Code) — no persistent background process. Reads/writes
  this folder only when invoked in a session.
- **Codex** — a local terminal/IDE coding agent on this same laptop, with
  real file read/write and terminal access to this repo once a session is
  running. No scheduler, no autonomous polling -- Snehil starts each
  session and gives it a task.
- **Antigravity** — same laptop, in the XS_Builder workspace. Also has real
  file read/write and terminal access to this repo once invoked (confirmed
  live: it created `0011-context-envelope-wiring-research.md` itself, ran
  real `git`/`python -m unittest` commands, read real files). No scheduler
  either -- Snehil starts each session and gives it a task.

**The only actual gap for both is the wake-up, not the work.** Neither agent
checks this folder on its own; Snehil is the one who starts a session and
tells it "you have a pending request in Agent_Comms, go handle it" (or
pastes the request's content directly). Once running, either agent should
read and write these files itself -- create its own response in the
request file, set `status: answered`, open its own `finding` thread if it
finds something unprompted -- exactly as Claude does. Don't have Snehil
relay text back and forth by hand when the agent can just edit the file.
The one thing Claude still does on their behalf: if an agent's own output
somehow doesn't make it into this folder (saved to Downloads/, pasted into
chat, whatever), Claude reads that and writes it in for them.

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

## Getting Codex or Antigravity to work

1. Write a normal `type: request` file here, `to: codex` or
   `to: antigravity` as appropriate (same format as any other thread) --
   self-contained, assumes no other context beyond this file and
   `AGENTS.md`/`CLAUDE.md`.
2. Tell Snehil the file exists and ask him to start a session with that
   agent and point it at the file (or paste the `## Request` content
   directly -- either works).
3. The agent does the work in a real session against the real repo, and
   writes its own `## Response`, `status: answered`, `answered:` directly
   into the file. Claude picks it up next time it checks this folder.
4. Only if the agent's output didn't land in the file for some reason
   (saved elsewhere, pasted into chat, a `.docx`, etc.) does Claude read it
   from wherever it landed and write it into `## Response` itself.

If an agent produces a finding unprompted, it should write its own
`type: finding` thread directly (`from: codex` or `from: antigravity`,
`to: claude`). If Snehil relays one by hand instead, Claude creates the
file itself once it has read and understood the content -- don't
paraphrase away specifics; quote real output.

## Division of labor: default pattern

The default split, unless a task clearly calls for something else:

- **Claude does design, research it can do itself, implementation, and
  writes the tests.** Claude is the one who understands this codebase's
  architecture (`AGENTS.md`, the frozen five-box design) and should not
  hand over decisions that require holding that context.
- **Antigravity/Codex run those tests and report** -- pass/fail, exact
  output, anything that broke. This is genuine load-splitting: they have
  their own terminal/session against the same repo, so a verification pass
  doesn't have to compete with Claude's own context budget.
- **Claude reviews what comes back and corrects** -- fixes real failures,
  pushes back on a report that doesn't hold up, iterates.
- This is the default, not a rule: research delegation (like `0011`,
  `0012`), independent code review, or a from-scratch build are all fair
  asks too when they fit the situation better. Use judgment.

### Keep Antigravity's tasks bounded

Antigravity runs on Gemini, which is meaningfully less reliable at
open-ended judgment calls than Claude or Codex. Every `to: antigravity`
request should be concrete and mechanical:

- Exact commands to run, exact files to read, exact assertions to check --
  not "figure out if X is a problem."
- A defined stopping point and a defined output shape ("paste the real
  command output for each of these five checks"), not an open-ended
  investigation with its own judgment calls about scope.
- If real judgment is required (does this defect matter, what's the
  right fix), Claude makes that call after reading Antigravity's bounded,
  factual report -- not Antigravity itself.
- `0012` is the template: numbered, concrete sub-questions, exact commands,
  explicit "do not fix this yourself, report and propose only."

Codex does not need this constraint by default -- give it real design or
implementation latitude when the task warrants it, same as Claude would use
for itself. Adjust either way if actual results say otherwise.

## Known gotchas for live DB checks (read this before writing a query)

Antigravity has repeatedly hit two avoidable errors when running its own
live-DB diagnostic checks. Both are process mistakes, not environment
limitations -- follow this and they stop recurring:

1. **Never guess a column name.** If a check needs a column you haven't
   already seen used elsewhere in this repo, look it up first:
   - Grep for the table name in `Knowledge/00_tables_and_indexes.sql` (the
     canonical schema source) to see its real columns, OR
   - Run `SELECT TOP 0 * FROM dbo.<Table>` / query
     `INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '<Table>'` live first,
     THEN write the real check against confirmed column names.
   `ExecutionDepth` is not a real column on any Hermes_L2 table -- that
   error was a guess, not a schema surprise.

2. **Never write a multi-quote SQL/Python one-liner as an inline
   `wsl ... -- bash -lc "python3 -c '...'"` command.** Nesting
   Windows-shell -> `wsl` -> `bash -lc` -> `python3 -c` -> an embedded SQL
   string, each layer with its own quoting rules, is exactly how you get
   "unexpected EOF while looking for matching backtick/quote". Instead:
   - Write the check as a real `.py` file (same pattern as
     `check_local_model_state.py` -- that part is right), and
   - Invoke it as `wsl python3 /mnt/c/path/to/script.py` with NO inline
     Python or SQL source on the command line at all -- just the file
     path. If you need different parameters per run, take them as
     `sys.argv`, don't inline different source each time.

Both agents should follow this, not just Antigravity -- it's just that
Antigravity has been the one hitting it in practice so far.
