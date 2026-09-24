---
id: 39
type: request
from: claude
to: codex
status: pending
created: 2026-09-24T17:10:00+05:30
answered: null
---

## Request

Take over the Chitragupta L2 work from Claude. This file is self-contained; read it with
`AGENTS.md`, `CLAUDE.md`, `Knowledge/L2_PIPELINE_STATE_MACHINE.md` and
`Knowledge/L2_ENGINEER_DESIGN.md`. All times are IST. Last commit at handoff: `c428cce` on `main`.

### 1. Standing rules from the user (non-negotiable)

- **`main` only; commit and push every change.** 8 old local branches exist (not ours); leave them unless asked.
- **Times in IST**, never UTC. Commands handed to the user: full absolute paths, PowerShell 5.1 syntax (no `&&`).
- **Ponytail** (installed plugin `DietrichGebert/ponytail` + AGENTS.md §16a): don't build it -> reuse the
  existing owner -> stdlib -> installed dependency -> shortest correct code. Delete superseded code and its
  tests in the same change. One owner per state/rule/transport.
- **Testing: E2E only.** Never write unit tests after code. For isolated logic, write the failure modes
  first (`Model_Bench/e2e/*_FAILURE_MODES.md`), then the code. Fast iterations against live data.
- **Jev never writes text, SQL or arithmetic.** Code finds candidates, reads data, compares numbers and
  dates; Jev chooses among prepared options (TypeSafe docs: Jev 1.13 is weak at math, dates, indirection).
  Qwen only writes replies from evidence, with no data tools.
- **One diagnostic:** live health via `python Model_Bench/benchmark_l2_performance.py --hours 2`; extend it,
  never write ad hoc monitoring scripts.
- **No hand-written facts in the world.** Everything in `Knowledge/world` is generated from XBatch.
- **Edit Python with an editor, not shell heredocs.** Heredoc escaping corrupted files several times
  (`\n` turned into real newlines).
- Every `CLAUDE.md` edit needs the matching `AGENTS.md` edit in the same commit.

### 2. What was built this session (2026-09-24), in commit order

| Commit | What |
|---|---|
| `e29c576`..`86f2664` | Evidence walk -> world walk; E2E suites; realistic tickets from real faults |
| `d14ff1d` | Generated XBatch world in GBrain (pages + typed links), step walker; stall check fixed (`--candidates`) |
| `3086730`, `86f2664` | Single-table identifiers, log index, survey + batched judging, type-safe lookups |
| `9e1988c` | `Knowledge/L2_ENGINEER_DESIGN.md` (researched design) + general-ticket cases |
| `efd8d80` | Ponytail: deleted `Knowledge/xbatch_tables` (592 docs), `Knowledge/atlas`, playbook, builder |
| `91f4b46`, `8ee9a77` | Screens (579 list views, 270 filters), value/activity indexes, no-ID investigations, code checks |
| `52649bb` | `connect()` retries prelogin resets; E2E runners share one connection |
| `79ad7b2` | **The world walk is the live L2 investigation** (replaces the Jev evidence-plan loop) |
| `d723114` | Walk hands only Jev-relevant reads to the runtime; seeder `--style walk|general` |
| `85ad9aa` | Walk trail saved to the run (`InvestigationJson`); walk Jev calls audited |
| `c428cce` | Call trace installed in the walk and Jev bridge subprocesses |

### 3. How Chitragupta works now

1. Ticket in `XStudio_Helpdesk.dbo.Complaint_Mst_Tbl`, Status `Enter`.
2. `ticket_scout` (2-min cron on the `l2-investigator` gateway, WSL) claims via
   `Hermes_L2_Claim_Ticket_Usp`; WIP 1.
3. `l2_pipeline_runtime.py::_jev_first_investigation` runs `Model_Bench/world_walk.py` as a repo-resident
   subprocess (`_run_world_walk`, stdin JSON `{ticket_text, run_id, ticket_id}`, timeout 240 s).
4. **World walk** (`Model_Bench/world_walk.py`, the "L2 engineer"; design in `Knowledge/L2_ENGINEER_DESIGN.md`):
   - `understand`: Jev routes data / how_to / access / infrastructure / hardware / change_request.
   - identifier path: `spans` -> value index lookup (`resolve`) -> `subject` (Jev picks among several)
     -> `survey` of every holding table (audited reads) + procedures from the log index.
   - no-identifier path: `scope` = GBrain hybrid search over world pages + Jev Noul per candidate
     (0.30 gate) -> `health` (activity vs history, screen filters) + `code_presence` (e.g. grade B500SX
     in master tables). Dates parsed in code (`window`).
   - `judge_all`: one batched Jev call assigns sees / stuck / cause / unrelated per finding.
   - step loop (max 8): Jev picks the next world link (writes/reads/calls/holds->connector/shows/
     records_to) or stops; `look` reads; `judge`.
   - `trace_numbers`: code finds where quoted numbers are stored; Jev matches the requester's wording.
   - With a `run_id`: every SQL read goes through the bridge's `_audited_probe_read`
     (`Hermes_L2_Execute_SQL_Usp`, action IDs); every Jev call through `jev.audit` (stages
     `WORLD_WALK_*`); the trail (`ledger()`) is saved to `Hermes_L2_Response_Trn_Tbl.InvestigationJson`.
5. Runtime outcome: not-data -> `direct_answer.routed_proposal` (NEEDS_HUMAN_ACTION, no Qwen);
   identifier absent -> `direct_answer.not_found_proposal` (QUESTION); probes -> existing
   `_jev_direct_answer` (QWEN_FREE fact table); else Qwen (`l2-jev-investigator`, writer-only) composes
   from the compiled context (walk findings are the `evidence_plan` chunk, relevant reads the probe chunks).
6. Jev primary review of the frozen proposal -> approve / rework (<=3) / L3 / local review.
7. Deterministic publisher writes Helpdesk state.

### 4. The world and its indexes (all generated)

| Artifact | Built by | Notes |
|---|---|---|
| `Knowledge/process_world.json` | `python Model_Bench/build_process_world.py` (~25 min, Windows) | procedures, writers/readers, events, schema, keys, identifiers, screens |
| partial rebuilds | `... build_process_world.py --only keys|screens|indexes|activity` | |
| `Knowledge/world/**` (2,406 pages) + `links.jsonl` (4,805) | `python Model_Bench/build_world_pages.py` | must be **committed** before syncing: GBrain sync reads git |
| GBrain | `bash Model_Bench/sync_gbrain_knowledge.sh` (WSL; also run by the deploy) | installs `deploy/gbrain/xbatch-world/pack.yaml`, syncs, embeds, `world_links.py`, `e2e/run_world.py` gate |
| `.cache/world_index.sqlite` (gitignored) | `--only indexes` / `--only activity` | `value_columns` (1.23M values), `runs` (procedure runs per value), `table_daily`, `proc_daily` |

GBrain: `~/.hermes/xstudio-gbrain`, Postgres, embeddings via LM Studio nomic on the desktop over
Tailscale; source `xstudio-knowledge` = `Knowledge/world` only; one client owner `Model_Bench/l2_gbrain.py`
(`Brain` = one `gbrain serve` MCP session). `XMES_Log_Trn_Tbl` is 3.5 GB with only a PK: never scan it
per ticket; use the indexes. `XStudio_DataSource_Mst_Tbl` stores the plant `sa` password in plain
text: never read it into the world or logs (flagged to the user for the vendor).

### 5. Tests (E2E, live data + real Jev)

WSL helpers used this session (scratch copies are in Claude's scratchpad; recreate as needed):
`set -a; source <(tr -d '\r' < ~/.hermes/profiles/l2-investigator/.env); set +a` then:

| Suite | Command | Last result |
|---|---|---|
| World | `python3 Model_Bench/e2e/run_world.py` (WSL) | 19/19 |
| Identifier walk | `python3 Model_Bench/e2e/run_walk.py` (WSL) | 8/8 (`ud_locked` flipped once: Jev borderline) |
| General (no identifier, key fact required) | `python3 Model_Bench/e2e/run_general.py` (WSL) | 8/8 |
| Identifier resolution | `python Model_Bench/e2e/run_entity.py` (Windows ok) | 12/12, 1-28 ms |
| Runtime units (existing) | `python -m unittest Model_Bench.test_l2_pipeline_runtime` | 128/128 |

### 6. Logs

| What | Where |
|---|---|
| Call trace, every process incl. walk (2 days kept) | WSL `~/.hermes/logs/l2_calltrace/<date>.jsonl` |
| SQL reads + action IDs | `Hermes_L2_SQL_Action_Trn_Tbl` |
| Jev decisions (incl. `WORLD_WALK_*`) | `Hermes_Agent_Trace_Trn_Tbl` |
| Walk trail per run | `Hermes_L2_Response_Trn_Tbl.InvestigationJson` (`source: world_walk`) |
| Cron output | WSL `~/.hermes/profiles/l2-investigator/cron/output/` |

### 7. Live state at handoff (17:10 IST) — first thing to check

**Update:** SQL answered again at 16:48 IST and the preflight passed (`{"preflight": "ok"}`), so the scout
resumes claiming on its own. Step 8.1 below is done; start at 8.2 (verify the first processed ticket).

- **The SQL server `10.2.6.204` stopped answering logins ~16:30 IST** (TCP 1433 open; every client,
  ODBC 18 and unencrypted SqlClient, Windows and WSL, times out in prelogin). Nothing of ours was
  running. Earlier in the day it intermittently reset TLS prelogin handshakes. Needs whoever runs that
  host if it persists.
- Deploy of `85ad9aa` copied files but the **post-deploy preflight failed** (bridge timeout = SQL down),
  so the scout will not claim until SQL is back. `c428cce` (call trace) needs no deploy (repo-resident).
- **16 test tickets queued**: `Ticket_377`-`384` (identifier cases, reset at 16:21 via
  `reset_l2_test_tickets.py`, backup `Model_Bench/results/ticket_resets/reset_20260924_162124.json`) and
  `Ticket_385`-`392` (general cases, new). Expectations in `Model_Bench/seeded_ticket_expectations.jsonl`.
- `Agent_Comms/0036`-`0038` stall alerts are false positives from the old detector (before the
  `--candidates` fix was deployed ~14:45 IST); they can be closed.

### 8. Next steps, in order

1. When SQL answers: rerun the preflight
   (`python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py preflight`, WSL, env loaded);
   if it passes, the scout resumes on its own.
2. On the first processed ticket, verify live: `InvestigationJson` has `"source": "world_walk"`;
   `Hermes_Agent_Trace_Trn_Tbl` has `WORLD_WALK_*` rows for the run; the call trace has `world_walk`
   calls; SQL actions carry `operation_name = world_walk`.
3. Score the 16 tickets against their expectations with `benchmark_l2_performance.py` (it already has
   expectation scoring). Compare with the old path: 381 had been L3-escalated, 377 asked a question.
4. Known behaviour to decide on: a no-Qwen QUESTION cannot publish (`waiting_user_ticket_status` is null
   in `deploy/helpdesk_workflow_binding.json`), so "identifier not found" falls back to Qwen.
5. Ponytail cleanup still owed: the old atlas family is now only used by validation/tests/orchestrator
   helpers: `xbatch_world.py`, `Knowledge/xstudio_semantic_atlas.json` (already stale vs its builder),
   `xbatch_investigation_recipes.json`, `build_xstudio_semantic_atlas.py`, the world check in
   `validate_gbrain_knowledge.py`, `table_keyword_index.json` (read by `Hermes_Orchestrator.py`),
   `view_catalog`/`view_docs` (read by `kb_retrieval.py`). Remove with their deploy copies and tests.
6. Update `CLAUDE.md` + `AGENTS.md` "current deployment facts" to the world-walk flow (still describe
   `xstudio_read_table` probing).
7. Tighten judging: Jev over-flags "stuck" (e.g. a batch merely `Created`); add a penalty for extra
   flags in `run_walk.py`/`run_general.py`, then fix.
8. Lessons: after verified resolutions, write GBrain takes/timeline entries on the pages involved and
   resolve them later (design section 7).
9. Held-out tickets written by Qwen from real faults, scored only at the end.
10. Open items for the user: Windows-side Hermes gateway `l2-investigator` running since 2026-09-23
    alongside WSL (possible double cron); plain-text `sa` password in the vendor config;
    `Plans/2026-09-24-antigravity-local-model-harness.md` to revisit later.

## Response

(left blank until answered)
