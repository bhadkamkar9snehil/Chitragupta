# AI Helpdesk / Hermes L2 — Agent Operating Contract

This file is the stable operating contract for agents working on Chitragupta.
For the exact lifecycle state machine, read `Knowledge/L2_PIPELINE_STATE_MACHINE.md`.
For human-facing architecture and deployment, read `README.md`.
For KB design, read `Knowledge/KB_IMPLEMENTATION_PLAN.md`.

Do not treat `Plans/`, `Agent_Comms/`, old commit messages, or dated incident notes as current runtime instructions. They are historical evidence only.

## 1. What this project is

Chitragupta is the autonomous L2 support pipeline for the existing XStudio Helpdesk.

Authoritative ticket store:

```text
SQL Server: 10.2.6.204
Database:   XStudio_Helpdesk
Ticket:     dbo.Complaint_Mst_Tbl
```

Production/plant evidence primarily lives in `XStudio_Xbatch`.

Chitragupta does not replace the Helpdesk workflow. It claims an existing ticket, investigates it, gets an independent review, and publishes through the audited Hermes SQL path.

## 2. Current live L2 lifecycle

`Model_Bench/l2_pipeline_runtime.py` is the single lifecycle authority.

The current LM Studio deployment has one safe inference slot, so global SQL pipeline WIP is **1**. Finish existing work before claiming more.

```text
Complaint_Mst_Tbl Status='Enter'
        |
        v
Ticket Scout (2-minute cron)
        |
        | first runs synchronous reconcile()
        |
        +-- active SQL run exists --> WIP_LIMIT; claim nothing
        |
        v
Hermes_Orchestrator.py --poll
        |
        v
JEV TRIAGE + EVIDENCE PLAN
        |
        v
deterministic bounded probes
        |
        v
JEV INVESTIGATION ASSESSMENT
 + META-ATTENTION CONTEXT COMPILE
        |
        v
INVESTIGATOR [priority 10]
  l2-jev-investigator
  COMPOSE_ONLY or FOCUSED_REASONING
        |
        | kanban_complete(metadata)
        v
normalize / freeze proposal
        |
        v
JEV PRIMARY REVIEW
   /       |          |             \
APPROVE  REWORK  L3_ESCALATION  LOCAL_REVIEW
   |       |          |              |
   v       v          v              v
publish  rework    L3 path       qwen reviewer
                                      |
                                approve/reject
                                  |       |
                                  v       v
                               publish  rework
```

### Non-negotiable lifecycle rules

- New investigation priority = `10`.
- Rework priority = `20`.
- Review priority = `30`.
- Every normalized proposal gets one Jev primary semantic review. A local reviewer card is created only for `LOCAL_REVIEW`, Jev unavailability/uncertainty, or genuine deep reasoning.
- Any local reviewer receives a frozen `proposal_json`. The proposal reviewed is the proposal published.
- Investigator never calls `--publish-response`.
- Jev/local reviewers never publish; deterministic lifecycle code owns publication.
- `review_cycle` counts reviewer/rework loops. SQL `AttemptNo` does not.
- `MAX_REVIEW_CYCLES = 3`; rejection at cycle 2 escalates instead of creating cycle 3.
- A rework is not complete until its fresh proposal receives a fresh Jev primary review; a local reviewer is added only if that review falls back.
- The old `l2-review` board and `kanban_forward_bridge.py` are retired.
- All investigator/reviewer/rework tasks live on the normal Kanban board.

## 3. Reconciliation is the lifecycle backstop

The central reconciler owns lifecycle sequencing synchronously. Current order:

```text
1. normalize investigator/rework completions
2. convert unreviewable terminal completions into bounded rework
3. run Jev primary reviews and apply direct approve/rework/escalation or create local-review fallback
4. process local-review rejections
5. process local-review approvals through the same deterministic publisher
6. recover true SQL/Kanban orphans
```

The old design launched repair/reject/publisher as independent concurrent processes. Do not restore that pattern.

`Model_Bench/xstudio_l2_orchestrator_plugin/` triggers the same reconciler immediately after successful `kanban_complete` / `kanban_block`. Event delivery is an optimization, not a correctness dependency.

The 2-minute `ticket_scout.py` job runs reconciliation before every claim attempt and is the durable mutating backstop.

Current L2 cron policy:

- `L2 Ticket Scout` — mutating lifecycle backstop, every 2 minutes.
- `L2 Kanban Completion Audit` — read-only reviewer/SQL divergence audit, every 10 minutes.
- Do **not** independently schedule `enforce_publish_safety_net.py` or `repair_incomplete_completions.py`; they are compatibility entrypoints into the central runtime and separate schedules reintroduce mutation races.

See `deploy/cron_jobs.txt`.

## 4. Helpdesk workflow status is deterministic

Models do not invent or choose Helpdesk status names.

Canonical binding:

`deploy/helpdesk_workflow_binding.json`

Current live-verified values:

```text
eligible_ticket_status        Enter
resolved_ticket_status        Closed
waiting_user_ask_status       Ask
l3_ticket_status              null / unbound
needs_human_action_status     null / unbound
```

`Closed` was bound from live Helpdesk evidence, not guessed. `Ask` was observed live. L3/human-action ticket statuses remain unbound because no distinct live status was demonstrated.

`strict_resolution_status_binding = true` means a `RESOLUTION` must fail closed if the resolved status binding is unavailable. Never permit:

```text
Hermes = COMPLETED / RESOLUTION
Helpdesk = still visibly unresolved
```

## 5. Publication contract

The deterministic publisher publishes only a semantically approved frozen proposal—either a Jev-primary direct approval that passes deterministic safety gates or a local-review fallback approval—through `Hermes_Orchestrator.py --publish-response --force-run-id`.

After publication, verify persisted SQL state; Kanban narration is not the final truth.

For a `RESOLUTION`, the expected postcondition includes:

```text
Hermes_L2_Response_Trn_Tbl.ProcessStatus = COMPLETED
Hermes_L2_Response_Trn_Tbl.ResponseType  = RESOLUTION
Hermes_L2_Response_Trn_Tbl.IsResolved    = 1
Hermes_L2_Response_Trn_Tbl.IsActive      = 0
Complaint_Mst_Tbl.Status                 = Closed
```

For a `QUESTION`, use the existing waiting-user workflow semantics and `Ask` binding where applicable.

For an `UPDATE`, `NextEligibleOn` must give the ticket a bounded continuation window rather than making it permanently unclaimable.

A resolved ticket is **not automatically a KB article**. KB promotion is governed separately.

## 6. Stale/orphan recovery

Age alone does not make a run stale.

Any Kanban task referencing a run protects that run, including `todo`, `ready`, `running`, `blocked`, `review`, scheduled work, and a done reviewer awaiting deterministic publication.

A SQL run is recoverable as a true orphan only when:

1. it is still active in SQL;
2. no Kanban task at any stage references that exact `run_id`; and
3. the orphan grace period has elapsed.

Do not reintroduce the retired `l2-review` board lookup.

## 7. Candidate selection / claiming

`Knowledge/25_ticket_dispatch_hardening.sql` moves non-L2 customization exclusion inside `Hermes_L2_Get_Candidate_Tickets_Usp` before `TOP (@BatchSize)`.

The production scout must never implement:

```text
SQL TOP N -> Python removes unsupported rows -> falsely report no work
```

Global WIP=1 is stricter than the old temporary `MAX_INVESTIGATOR_BACKLOG=3` design. References to that old backlog cap are stale.

Do not manually use raw `Hermes_Orchestrator.py --poll` for production testing because it bypasses the scout's lifecycle/WIP gate.

## 8. Investigator evidence rules

Live evidence wins over retrieved knowledge, prior ledgers, or memory.

Evidence hierarchy:

1. current ticket state and live SQL evidence;
2. verified `Knowledge/` reference material;
3. approved/retrieved solution articles as hypotheses;
4. same-ticket prior ledger/attempt history;
5. mem0 operational hints.

Never fabricate a table, view, column, SP, ticket status, or identifier.

Preferred investigation path, all through the typed `xstudio_l2` tool (see §8a):

- use the dispatch-time investigation bundle first;
- `select` when the table/entity is known (identifiers are schema-validated);
- `suggest_tables` for deterministic narrowing;
- `find_objects` / `get_definition` for live metadata when necessary;
- `query` only for read-only SQL, with `database` specified explicitly;
- `read_procedure` only for the explicitly allowlisted diagnostics;
- persist meaningful per-ticket state with `save_ledger`.

Do not put per-ticket facts into shared mem0.

## 8a. Agent execution surface is typed and harness-owned

L2 agents do not build database transport. They call one typed tool,
`xstudio_l2`, registered by the `xstudio-l2-tools` plugin
(`Model_Bench/xstudio_l2_tools_plugin/`), which invokes the Windows-side
bridge (`Model_Bench/xstudio_l2_tool_bridge.py`) internally. The bridge reuses
the guarded primitives already in `Hermes_Orchestrator.py` rather than being a
parallel SQL implementation.

Why this exists: on 2026-09-05, Ticket_424 and Ticket_441 showed the lifecycle
working correctly while the investigator burned 1,026,911 tokens / 27 tool
calls / 2 sessions building the transport itself — it malformed the interpreter
call as `python3 <windows-python> <orchestrator>`, retried the same broken shape
under `timeout` wrappers, fell back to installing a database driver, hit
Tirith's fail-closed dependency scan, and overflowed context. That is an
agent-computer-interface defect, not a lifecycle defect.

Rules:

- The model never composes Windows/WSL paths, interpreters, driver imports, SQL
  credentials, `sqlcmd`, or package installation. Those terminal forms are
  blocked by the plugin's `pre_tool_call` guard, with `approvals.deny` entries
  in each active profile config as defense in depth.
- Benign terminal and file inspection (`ls`, `cat`, `grep`, `git`, reading
  documentation) stays available. The guard targets transport, not the shell.
- Deterministic harness subprocesses executed by trusted runtime/plugin code are
  unaffected; the restriction is on model-driven terminal fallback.
- Raw SQL exposed to the model is read-only. Write/DDL/`EXEC` keywords are
  rejected after string literals are blanked, so a keyword inside quoted text is
  not a false positive.
- Arbitrary `EXEC` is not available. `read_procedure` accepts only procedures in
  an explicit allowlist with a validated parameter contract (currently
  `XMES_Get_API_Transaction_Summary` with `APIType`).
- Ticket/Helpdesk mutation stays outside the agent interface entirely;
  publication remains the deterministic publisher's job (§5).
- Usage is bounded so one bad idea cannot consume the context window: about 14
  `xstudio_l2` calls per session, a third identical failing call is blocked, and
  results are capped (~8 KB, ~25 list rows) with an instruction to narrow rather
  than repeat.
- Fresh cards rendered by the runtime contain only this typed contract. They no
  longer carry a raw interpreter/query recipe, and the plugin re-asserts the
  contract before each LLM turn so a pre-migration card's stale command text
  cannot steer a worker back to the retired path.
- Interpreter paths, driver setup, and dependency mechanics are deterministic
  harness concerns. They belong in code and config, never in mem0.

## 9. KB and memory boundaries

The current deterministic KB retriever is an interim conservative layer. It must obey:

- route alone cannot retrieve a solution;
- weak generic overlap must abstain;
- every hit carries provenance;
- live verification remains mandatory;
- pre-investigation retrieval must not use `SuspectedCause` as a primary signal, avoiding self-confirmation.

`Knowledge/KB_IMPLEMENTATION_PLAN.md` is the implementation contract for the larger KB redesign.

Do not collapse these concepts:

```text
live SQL evidence        != KB
schema discovery         != KB
same-ticket history      != KB
mem0                     != KB
Qdrant                   != source of truth
solution history         != automatically trusted knowledge
```

## 9a. TypeSafe Jev System-One fabric

Jev is the default bounded semantic layer for L2. The deterministic runtime remains the lifecycle authority, but the old rule "always run a second local reviewer" no longer applies.

~~~text
claim
-> Jev triage
-> deterministic real candidates
-> Jev evidence plan
-> deterministic identifier-bounded probes
-> Jev investigation assessment + per-chunk meta-attention Scores
-> deterministic context compiler (whole chunks; pinned current/live evidence)
-> l2-jev-investigator local synthesis/focused reads
-> frozen proposal
-> Jev primary review
     APPROVE       -> deterministic publish
     REWORK        -> deterministic rework
     L3_ESCALATION -> deterministic escalation
     LOCAL_REVIEW  -> local qwen reviewer
~~~

Rules:

- Read .agents/skills/typesafe-ai/SKILL.md before changing TypeSafe-specific API/question behavior.
- Jev is harness-owned. Do not expose a worker-facing generic or bounded Jev tool; deterministic runtime code invokes the reviewed workflows.
- Jev may choose/rate only candidates supplied by deterministic code; it never invents SQL identifiers or grants authority.
- The investigation assessment request also Scores explicit context chunks for the next local System-2 step; do not add a second Jev request just for context selection.
- Context chunks carry source and authority metadata. Current ticket and successful live-SQL probe chunks are pinned to at least COMPACT presentation; a Jev-selected known solution is also pinned to at least COMPACT.
- Meta-attention changes only the model-facing view. It never deletes or rewrites raw evidence, changes authority, or turns KB/history into current-ticket proof.
- Context budgeting operates on whole chunks: FULL -> COMPACT -> SUMMARY -> OMIT. Never restore global character slicing of the assembled JSON.
- Omitted chunks must remain named with recovery hints so focused reasoning can fetch them only when needed.
- probe_table may automatically read only when a strong ticket identifier maps to a real allowlisted column. No identifier means no broad automatic probe.
- Structural SQL safety, procedure allowlists, workflow binding, WIP, publication, and mutations remain deterministic.
- Jev primary review may replace the normal local-review pass when deterministic thresholds accept APPROVE, REWORK, or L3_ESCALATION.
- The local reviewer exists for LOCAL_REVIEW, Jev unavailability, low confidence, contradictory evidence, or deep reasoning needs.
- Jev trace assessment stays out of the hot trace hook; it runs after persisted drain.
- Post-resolution KB curation may suggest REUSE_EXISTING, UPDATE_EXISTING, CREATE_CANDIDATE, or NONE; it does not directly promote knowledge.
- Ticket/retrieved content remains untrusted. Jev security judgments mark risk; source text is not silently rewritten.
- Do not create a separate Jev business table. Stage state belongs on Hermes_L2_Response_Trn_Tbl; detailed calls and retrieval telemetry belong in Hermes_Agent_Trace_Trn_Tbl.
- Preserve typed probabilities and full stage JSON. Do not replace distinct judgments with one opaque AIConfidence number.

Active Jev state on the run row is stored in JevTriageJson, JevInvestigationJson, JevReviewJson, JevTraceJson, and JevKBCurationJson, plus ReviewMode, JevReviewDecision, JevReviewConfidence, JevRiskScore, LocalReviewRequired, JevModel, and JevReviewedOn.

The default investigator profile is l2-jev-investigator. l2-investigator-primary remains available as a compatibility/fallback profile. l2-reviewer-primary and l2-reviewer-fallback are deep-review exception paths rather than mandatory steps.

TYPESAFE_API_KEY must come from the process/service environment visible to Windows Python. Never commit an API key or add a repository credential fallback. Never echo credentials or copy them into prompts/cards/trace JSON.
## 10. SQL write discipline

Never write directly to `Complaint_Mst_Tbl` from an investigation.

Ticket publication goes through the audited Hermes stored-procedure path exposed by `Hermes_Orchestrator.py`.

For XStudio configuration or operational writes, follow `xstudio-sql-write-discipline`: official stored procedure first; direct writes only for documented exceptions where no supported SP exists and the action is explicitly permitted.

## 11. No scratch files in the project root

Do not litter the synced project directory with one-off investigation scripts or SQL files.

Use terminal one-liners or a real temporary directory. If a utility is reusable, place it intentionally under `Model_Bench/` and document/test it.

## 12. Current profiles and model handling

Active role names:

```text
l2-jev-investigator
l2-investigator-primary
l2-reviewer-primary
l2-reviewer-fallback
```

`l2-investigator` remains the dispatcher/host profile and compatibility location for scripts.

Old model-based role names such as `l2-eval-investigator`, `l2-gemma-verifier`, and `l2-qwen-verifier` are historical only.

Do not hardcode the current LM Studio model into architecture documentation. The loaded model can change. Verify it live at the configured LM Studio endpoint before diagnosing model mismatch.

## 13. Repository sources of truth

Use this hierarchy when documents disagree:

1. live SQL/Hermes state for runtime facts;
2. `Model_Bench/l2_pipeline_runtime.py` for lifecycle behavior;
3. `Knowledge/L2_PIPELINE_STATE_MACHINE.md` for the documented lifecycle contract;
4. `deploy/helpdesk_workflow_binding.json` for workflow status binding;
5. deployable skills under `deploy/skills/xstudio/` for worker behavior;
6. `Knowledge/manifest.json` for machine-readable KB routing/catalog;
7. `README.md` for human-facing architecture;
8. `Plans/` and `Agent_Comms/` only for history/research.

Conductor is a parallel experiment only. It is **not** the live L2 pipeline until an explicit cutover is performed and documented.

## 14. SQL deployment

Edit numbered SQL sources, not the generated bundle directly.

The generated install currently concatenates these nine source files in numeric order:

```text
00_tables_and_indexes.sql
10_helpdesk_discovery.sql
20_ticket_dispatch.sql
25_ticket_dispatch_hardening.sql
30_context_and_live_discovery.sql
40_investigation_runtime.sql
50_response_and_workflow.sql
55_update_retry_hardening.sql
60_metrics_and_reporting.sql
```

`98_pipeline_postflight.sql` and `99_postflight.sql` are validation, not install-bundle input.

`Knowledge/00_Hermes_L2_FULL_INSTALL.sql` has been regenerated to include the 25/55 hardening sources. Keep it byte/logically aligned with the numbered sources.

`.gitattributes` forces LF for `*.sh` and `*.sql`; do not remove that protection on the Windows checkout.

## 15. Local validation, not GitHub Actions

This pipeline depends on the real Windows/WSL/Hermes/Kanban/SQL/LM Studio environment. Validate locally.

Useful commands:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
bash Model_Bench/validate_l2_pipeline_local.sh
python3 Model_Bench/test_xstudio_l2_tools_plugin.py
python3 -m unittest -v Model_Bench/test_l2_pipeline_runtime.py
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py reconcile --dry-run
```

Do not use GitHub Actions as proof that the live pipeline is healthy.

The typed-tool half of the harness is only fully proven by a naturally arriving
ticket. For the next one, check the trace shows `xstudio_l2` calls and no
terminal attempt at an interpreter, database driver, `sqlcmd`, or package
install. Do not manufacture a production claim to test this, and do not raw-poll
a ticket — that bypasses the scout's WIP/lifecycle gate.

## 16. Deployment mirror

`deploy/` is the reproducible mirror of artifacts that otherwise live under `~/.hermes/profiles/...`.

After changing profile SOUL/config/skills/plugins or the cron schedule, refresh the mirror with `Model_Bench/mirror_wsl_artifacts.sh` and inspect the diff before committing. The mirror covers the L2 plugins — `xstudio-l2-orchestrator`, `xstudio-l2-tools`, and `xstudio-l2-trace` — so a fresh install cannot come up without the typed investigation and trace boundaries. Jev network work is harness-owned and remains out-of-band from the trace hook.

`Model_Bench/deploy_l2_pipeline_runtime.sh` installs the lifecycle scripts, three plugins, SOULs, skills, the workflow-binding fallback, and the profile-config entries, then restarts the four active gateways unless `--no-restart` is passed. It is idempotent. Config edits are applied by `Model_Bench/patch_profile_config.py`, which is deliberately a targeted text editor rather than a YAML round-trip: the live configs carry explanatory comments (Security/Tirith, fallback-model providers) that a load-and-dump silently destroys.

## 16a. Ponytail audit standard

Run a Ponytail audit before merging any substantial runtime/tooling/architecture branch.

The order is strict:

1. **Do not build it.** Ask whether the code/concept is needed now. Delete speculative future surfaces, compatibility facades with no live caller, duplicate abstractions, dead flags, and pre-built extension points.
2. **Reuse existing ownership.** Prefer the existing lifecycle/tool/SQL/trace/KB owner over creating a parallel path or side table.
3. **Prefer stdlib/native behavior.** Use the platform/runtime primitive before adding a dependency.
4. **Prefer an already-installed dependency.** Reuse what the project already carries before adding another package.
5. **Choose the shortest correct implementation.** Fewer state transitions, fewer files, fewer branches, fewer config switches.
6. **Only then write new machinery.**

Deletion/consolidation comes before extraction. Do not split a bad abstraction into five neat files; first ask whether the abstraction should exist.

Audit every change for:

- one authoritative owner per state/rule/transport;
- duplicate business logic or duplicate semantic judgments;
- compatibility code whose original caller is gone;
- model-facing tools that duplicate harness-owned work;
- hidden network calls inside deterministic evidence/safety surfaces;
- generated/derived state replacing the raw evidence it came from;
- speculative feature flags or future-only modules;
- broad exception swallowing that hides correctness failures;
- hard-coded machine paths/config where an existing canonical source exists;
- credentials, tokens, passwords, or secret fallback files in Git;
- deployment scripts that add new artifacts but fail to remove retired live copies;
- tests/docs that preserve deleted concepts after the code is gone.

Complexity is a hotspot detector, not a score to game:

- investigate functions around **>45 lines** or approximate cyclomatic complexity **>12**;
- **>20** is a strong refactor signal;
- split by real responsibility/owner, not arbitrary line count;
- prefer dispatch tables, early returns, and small pure helpers when they make ownership clearer;
- do not increase indirection merely to lower a metric.

For every Ponytail cleanup, update tests, deploy mirrors, documentation, and AGENTS.md contracts in the same branch. A Git deletion is incomplete if deployment can leave the retired artifact live.

### Secret hygiene

.env files, API keys, tokens, passwords, and credential fallbacks must never be tracked. Credentials come from process/service environment or an external secret store. If a secret ever enters Git history, remove the tracked file immediately and rotate the credential; deleting the latest file does not erase history.
## 17. Security / credentials

Do not commit or print credentials.

Scripts use environment-provided SQL credentials. WSL may not see the same environment as Windows Python, so subprocess construction must omit `--password` when no value is present; never pass Python `None` as an argv element.

## 18. When changing the lifecycle

Any lifecycle change must preserve or deliberately revise these invariants:

- WIP ownership is explicit.
- Exactly one lifecycle authority performs mutations.
- Every publishable investigator/rework result gets exactly one Jev primary semantic review; a local reviewer exists only on the fallback path.
- All semantic review operates on the same immutable frozen proposal; a local reviewer never reconstructs it.
- Publication is deterministic and idempotent.
- Review cycles are bounded.
- Event loss is recoverable by reconciliation.
- SQL/Helpdesk postconditions define success.
- Knowledge retrieval cannot substitute for live evidence.

If a proposed change violates one of these, update the state-machine contract and tests in the same commit.