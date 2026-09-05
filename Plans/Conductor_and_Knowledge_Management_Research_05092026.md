# Conductor and knowledge-management research (2026-09-05)

Research pass answering: is Microsoft Conductor real and worth adopting,
and what fixes "context dropping" (a rejected/reworked investigation, or
a brand-new ticket similar to one solved days ago, gets no benefit from
prior findings)? This is research only — nothing below has been wired up
yet.

## 1. Microsoft Conductor — real, confirmed

`github.com/microsoft/conductor` — "a CLI tool for defining and running
multi-agent workflows with the GitHub Copilot SDK and Anthropic Agents
SDK." MIT licensed, YAML-defined, no Docker. Announced May 2026:
[Conductor: Deterministic orchestration for multi-agent AI workflows](https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows/).
Docs: `docs/workflow-syntax.md`, `docs/providers/hermes.md`.

**Not** the Netflix/AWS-style `conductor-oss/conductor` durable-execution
engine — same name, unrelated project. Design philosophy matches this
project's own stated direction (mechanical steps, LLM only for
judgment): "no LLM in the orchestration loop," aimed at "workflows with
known structure where deterministic orchestration provides clear
advantages over dynamic LLM-based routing." It even ships an
experimental **Hermes provider** that talks to `hermes-agent` directly —
unusually convenient given this project's own stack.

**Confirmed mechanics relevant here:**
- **Local endpoint routing**: `runtime.provider` routes the Copilot SDK
  to any OpenAI-compatible endpoint — `base_url: http://localhost:1234/v1`
  style config for LM Studio (example: `examples/copilot-local-llm.yaml`).
- **Non-LLM steps**: `type: script` steps run a shell command, capturing
  stdout/stderr/exit code, routing on either — a real fit for wrapping
  `Hermes_Orchestrator.py --build-query` as a deterministic step with no
  model call at all.
- **Explicit context flow**: opt-in per step via `context_mode`:
  `accumulate` (full history, the default), `snapshot` (start-time
  context only), `minimal` (named prior outputs only, e.g.
  `{{ classifier.output.category }}`). `minimal` is the one that matches
  "each step sees only what it needs," directly addressing the
  context-dropping/context-overflow failure mode already hit once this
  project (the original bot-chat outage).
- **Output validation**: per-step JSON-Schema-like `output:` declarations
  (`type`, `enum`, `pattern`, min/max), with automatic retry via
  correction prompts up to `max_parse_recovery_attempts` — directly
  targets the "drops structured tool-call arguments" failure class
  already root-caused in this project (investigator completions missing
  `response_type`/`reply_text`).
- **Windows/WSL2 gotcha**: documented issue — Windows `subprocess` can't
  resolve `.bat`/`.ps1` wrappers by bare name (`[WinError 2]`); needs the
  full CLI path. Given this project's existing WSL2 fragility (the
  `[Errno 36]` POSIX-lock bug that already forced the primary install off
  native Windows), **Conductor should run inside the same WSL2 Ubuntu
  environment**, not native Windows, if adopted.

**Recommendation**: worth a real prototype spike, specifically using the
built-in Hermes provider — install in WSL2, model one investigation
sub-step (e.g. the SQL-gathering phase) as a `script` step calling
`--build-query` plus one `minimal`-context LLM step for evaluation, and
compare its reliability against the current raw Kanban-card approach
before deciding whether to migrate the whole pipeline.

## 2. Cross-run context preservation — no silver bullet beyond mem0/RAG; the real fix is a mechanical findings ledger

Coding-agent harnesses converge on the same low-tech pattern:
**externalize findings to a plain file the next turn re-reads**, rather
than trusting model-internal memory. Documented as the "Scratchpad
Pattern" for Claude-Code-style agents (offload to markdown, update as
items complete, re-read to resume); Claude Code's own layered memory
(static instructions file + a separate self-curated evolving-facts file)
is the same idea formalized.

For a 9B model specifically: **don't let the LLM write or maintain the
ledger's structure** — summarization is exactly the kind of judgment
call a small model does unreliably. Have the deterministic side
(`Hermes_Orchestrator.py`, same spirit as `build_query_mechanically`)
write a structured findings record (queries run, tables touched,
entities resolved, conclusion) mechanically at `kanban_complete`/publish
time, and inject the prior attempt's record **verbatim** into a rework
card — never re-summarized by the small model. This matches published
Case-Based-Reasoning-for-LLM-agents work
([arXiv:2504.06943](https://arxiv.org/abs/2504.06943)): "explicit memory
banks containing successful problem-solving exemplars (input,
intermediate reasoning, output)" — a structured case record, not replayed
free-text history. Help-desk-specific prior art (CBR-TM: case-based
reasoning for ticket resolution, retrieving and adapting similar prior
tickets) is directly on-point for the rework-attempt-2/3 flow already
built here.

**Concrete, buildable-today next step** (no new framework required):
extend the investigator's `kanban_complete` metadata contract to include
a small structured `investigation_ledger` (tables queried, key values
found, ruled-out hypotheses), have the deterministic publish/reject-bridge
scripts carry that ledger forward verbatim into any rework card body
instead of only the reviewer's rejection reason, and (separately)
`--search-solutions`/mem0 surface similar past tickets' ledgers when a
new ticket looks related.

## 3. Obsidian / filesystem markdown MCP servers — real, no Obsidian app needed

Confirmed maintained servers that work directly against markdown files
on disk:
- `StevenStavrakis/obsidian-mcp`
- `cyanheads/obsidian-mcp-server` — read/write/search/surgical edit,
  tags, frontmatter; STDIO or Streamable HTTP.
- `bitbonsai/mcpvault` — lightweight, path-validated safe vault access.
- `marcelmarais/obsidian-mcp-server` — direct filesystem access.

Since `Reference Documents/` and `Knowledge/*.md` are plain markdown, not
an actual Obsidian vault (no `.obsidian/` metadata, no backlinks needed),
a generic filesystem-markdown server (`cyanheads/obsidian-mcp-server`, or
even a bare filesystem-search MCP server) is a better fit than anything
Obsidian-vault-specific.

## 4. More constrained SQL-generation tooling — real prior art, incrementally more sophisticated, not fundamentally beyond the allowlist approach

- **Vanna.ai** (MIT) — RAG index over DDL/docs/historical queries,
  retrieves only relevant schema fragments at query time instead of
  dumping the full schema; explicitly anti-hallucination via grounding
  in retrieved real DDL.
- Community-documented pattern: "two-step prompting" — filter candidate
  tables first, then generate SQL only against that filtered set;
  separate query planning (name tables/columns, validate) from SQL
  generation (fill a validated template).

**Verdict**: `build_query_mechanically`'s allowlist + fuzzy-match
approach is already stricter than Vanna's RAG-retrieval (generative-then-
checked vs. allowlist-constrained). The one idea worth borrowing:
Vanna's dynamic retrieval narrows what the LLM even *sees* to ~5-10
relevant tables instead of a full schema dump — worth adopting if any
current investigation prompt is passing a large schema chunk wholesale,
independent of whether Conductor itself is adopted.

## Bottom line

Nothing here replaces the Kanban pipeline outright. Conductor is real
and a legitimate prototype candidate specifically for turning the
investigation phase into mechanical steps + one narrow-context judgment
step, using its native Hermes provider. The context-dropping problem's
real fix doesn't require adopting any new framework — it's a structured,
mechanically-written findings ledger carried forward verbatim, which can
be built directly into the existing `Hermes_Orchestrator.py` metadata
contract today.
