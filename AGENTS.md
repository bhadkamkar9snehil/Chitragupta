# AI Helpdesk / Hermes L2 — Agent Operating Contract

This file is the stable operating contract and engineering discipline for agents working on Chitragupta.

### Authority Hierarchy

```text
AGENTS.md
    stable engineering/runtime invariants & Scope Guard
              │
              ▼
Knowledge/L2_PIPELINE_STATE_MACHINE.md
    sole normative architecture and lifecycle specification
              │
              ▼
runtime code (Model_Bench/l2_pipeline_runtime.py) / SQL implementation
```

`README.md` is only a human-facing overview; it must not become an independent specification.
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

### The Five Architectural Responsibilities

Chitragupta has exactly five architectural responsibilities:
1. **XStudio Helpdesk** (`dbo.Complaint_Mst_Tbl`) — User-visible incident store and operational state.
2. **Chitragupta Control** (`Model_Bench/l2_pipeline_runtime.py`) — Deterministic lifecycle, claim/WIP/queue management, retry/recovery, review routing, and audited publication.
3. **Jev — System One** (`Model_Bench/jev/`, `jev_workflow_bridge.py`) — Fast semantic layer: triage, evidence planning, candidate rating, execution-depth choice, and primary semantic review.
4. **Hermes / Qwen — System Two** — Local model reasoning for composition, focused investigation, bounded rework, and exceptional deep review.
5. **Evidence / Knowledge** (`xstudio_l2` tool, `Knowledge/`, SQL KB) — Typed read-only SQL, canonical Git documents, governed Solution articles, ticket/run ledgers.

The surrounding implementation mechanisms are not additional architecture:
- SQL locks / leases / runtime tables = persistence and coordination
- Kanban = execution transport for Hermes workers
- Trace pipeline = observability
- Cron / event hook = lifecycle triggering and liveness
- Tests / postflight = verification
- Deployment scripts = deployment
- Qdrant = retrieval index, never authority
- mem0 = bounded operational heuristics, never ticket truth

No sixth architectural box exists.

## 1a. Scope Guard — Permanent Project Engineering Rule

All agents and developers must adhere to the Scope Guard:

1. **Smallest Sufficient Change:** Solve the specific task with the minimal code and documentation change necessary.
2. **Inspect Existing Implementation First:** Read current code and invariants before designing or proposing changes.
3. **Reuse Existing Patterns & Dependencies:** Do not introduce new libraries, frameworks, or execution modes when existing mechanisms suffice.
4. **No Speculative Abstractions:** Do not create wrapper classes, generalized architectures, or speculative hooks for future requirements.
5. **Delete Replaced Implementations:** When replacing an obsolete script, configuration, or model, cleanly delete the old path rather than keeping parallel dead code.
6. **Do Not Widen Scope:** Do not touch nearby files, refactor unrelated modules, or add unsolicited features.
7. **Test Requested Behavior:** Verify the exact behavior requested. Do not perform repeated unnecessary test cycles.
8. **Re-anchor on Growing Scope:** If an implementation or investigation begins ballooning in complexity, stop immediately and return to the minimal requested requirement.
9. **Architectural Guard:** Any proposed new runtime component must map to one of the five existing architectural responsibilities. If it does not, the change is an architecture change and requires explicit approval before implementation.

## 2. Current live L2 lifecycle

`Model_Bench/l2_pipeline_runtime.py` is the single lifecycle authority.

The current LM Studio deployment still has **one** safe local inference slot, but Jev/deterministic work is no longer serialized behind it. The default SQL pipeline capacity is **8 active runs** (`L2_MAX_PIPELINE_WIP`), while the shared local-model capacity is hard-limited to **one RUNNING Qwen task** with a default priority-aware waiting threshold of **4** (`L2_MAX_QWEN_WAITING`). New investigations pause claiming when total queued $\ge$ 4, while rework (priority 20) and reviews (priority 30) are admitted unless equal/higher-priority backlog fills the threshold; total queued work in SQL may therefore legitimately exceed 4 to prevent starving ongoing runs. SQL owns both admission invariants.

```text
Complaint_Mst_Tbl Status='Enter'
        |
        v
Ticket Scout / reconcile
        |
        +-- SQL pipeline slots available (default 8)
        |
        +---- claim A -> Jev + bounded probes -> QWEN_FREE -> review/publish
        |
        +---- claim B -> Jev + bounded probes -> queue COMPOSE_ONLY
        |
        +---- claim C -> Jev + bounded probes -> queue FOCUSED_REASONING
        |
        +---- ... until pipeline cap or priority-aware Qwen backlog
                                      |
                                      v
                         SQL LOCAL-MODEL ADMISSION
                          exactly one RUNNING task
                         priority: review > rework > new
                                      |
                                      v
                         l2-jev-investigator / rework /
                           local-review fallback
                                      |
                                      v
                         normalize / freeze proposal
                                      |
                                      v
                            JEV PRIMARY REVIEW
                      /          |          |          \
                 APPROVE      REWORK   L3_ESCALATION  LOCAL_REVIEW
                    |            |           |             |
                    v            v           v             v
                 publish      queued       L3 path    queued reviewer
                              rework
```

### Non-negotiable lifecycle rules

- New investigation priority = `10`.
- Rework priority = `20`.
- Review priority = `30`.
- Pipeline capacity and local-model capacity are separate. SQL claim admission defaults to 8 active runs; all local Qwen purposes share one SQL-serialized RUNNING slot.
- `COMPOSE_ONLY`, `FOCUSED_REASONING`, investigator rework, and local-review fallback all consume that same one local-model slot. `QWEN_FREE` consumes none.
- Local-model work is frozen into `PendingLocalModelJson` before admission. Never create investigator/rework/reviewer Kanban cards outside the shared admission path.
- Queued local-model work is valid active-run state even when no Kanban card exists yet. Do not classify it as an orphan.
- Review priority `30` > rework `20` > new investigation `10` determines the single-Qwen queue order.
- Jev recommends one execution depth in the same investigation-assessment call: `QWEN_FREE`, `COMPOSE_ONLY`, or `FOCUSED_REASONING`. Deterministic code owns the final gate.
- `QWEN_FREE` (no-Qwen) is the target path: after the audited probes, the harness builds a fact table (fields the ticket names, recorded vs reported values, action IDs), Jev's `direct_answer` workflow picks CONFIRMED/CORRECTED/ANSWERED/NOT_FOUND/NEEDS_REASONING, and the harness renders a fixed reply with VERIFIED claims and publishes it. Jev never writes text; outcomes the facts contradict are refused. Only NEEDS_REASONING (or no audited facts) goes to the local model.
- `COMPOSE_ONLY` uses a smaller context budget and normally no additional live read; `FOCUSED_REASONING` receives the larger bounded context/recovery budget.
- The route-specific domain skill is loaded only when the same Jev assessment says it materially helps the next System-2 step.
- Every normalized local-model proposal gets one Jev primary semantic review. A no-Qwen direct answer is not reviewed a second time: Jev already chose its outcome on the same audited facts. A local reviewer card is created only for `LOCAL_REVIEW`, Jev unavailability/uncertainty, or genuine deep reasoning.
- Any local reviewer receives a frozen `proposal_json`. The proposal reviewed is the proposal published.
- Investigator never calls `--publish-response`.
- Jev/local reviewers never publish; deterministic lifecycle code owns publication.
- `review_cycle` counts reviewer/rework loops. SQL `AttemptNo` does not.
- `MAX_REVIEW_CYCLES = 3`; rejection at cycle 2 escalates instead of creating cycle 3.
- `MAX_UPDATE_CONTINUATIONS = 3` published `UPDATE`s per ticket version (no new requester input); the next `UPDATE` escalates through the same L3 handoff.
- A rework is not complete until its fresh proposal receives a fresh Jev primary review; a local reviewer is added only if that review falls back.
- The old `l2-review` board and `kanban_forward_bridge.py` are retired.
- All investigator/reviewer/rework tasks live on the normal Kanban board.

## 3. Reconciliation is the lifecycle backstop

The central reconciler owns lifecycle sequencing synchronously. Current order:

```text
1. release terminal local-model leases; recover stale leases only when no live local card owns the run
2. normalize investigator/rework completions
3. convert unreviewable terminal completions into queued bounded rework
4. run Jev primary reviews and apply direct approve/rework/escalation or queue local-review fallback
5. process local-review rejections
6. process local-review approvals through the same deterministic publisher
7. recover true SQL/Kanban orphans
8. admit at most one next local-Qwen task
```

The old design launched repair/reject/publisher as independent concurrent processes. Do not restore that pattern.

`Model_Bench/xstudio_l2_orchestrator_plugin/` triggers the same reconciler immediately after successful `kanban_complete` / `kanban_block`. Event delivery is an optimization, not a correctness dependency.

The 2-minute `ticket_scout.py` job runs reconciliation before every claim attempt and is the durable mutating backstop.

Current L2 cron policy:

- `L2 Ticket Scout` — mutating lifecycle backstop, every 2 minutes.
- `L2 Kanban Completion Audit` — read-only reviewer/SQL divergence audit, every 10 minutes.
- Legacy compatibility scripts (`repair_incomplete_completions.py`, `kanban_approval_publisher.py`, `kanban_reject_bridge.py`, `enforce_publish_safety_net.py`) have been retired and deleted. All lifecycle triggering runs strictly through `ticket_scout.py` or event-driven `reconcile_l2_pipeline.py`.

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
2. no Kanban task at any stage references that exact `run_id`;
3. it is not in `LocalModelState = 'QUEUED'`; and
4. the orphan grace period has elapsed.

Do not reintroduce the retired `l2-review` board lookup.

## 7. Candidate selection / claiming

`Knowledge/25_ticket_dispatch_hardening.sql` moves non-L2 customization exclusion inside `Hermes_L2_Get_Candidate_Tickets_Usp` before `TOP (@BatchSize)`.

The production scout must never implement:

```text
SQL TOP N -> Python removes unsupported rows -> falsely report no work
```

Global WIP=1 is retired. The claim procedure enforces the configured multi-WIP cap atomically with `sp_getapplock('HermesL2:PipelineCapacity')`. Within the same Helpdesk priority, genuinely fresh/user-changed work precedes failed retries and old `UPDATE` continuations so continuation loops cannot starve new incidents.

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

Preferred investigation path, all through the named `xstudio_*` tools in the `xstudio_l2` toolset (see §8a):

- use the dispatch-time investigation bundle first;
- `xstudio_read_table(table)` for one more table: the harness filters by the ticket's own
  identifier (billet, material document, work order, heat) and chooses the columns;
- `xstudio_heat_context` / `xstudio_work_order_context` / `xstudio_sap_api_context` for fixed
  cross-table evidence of one identifier;
- persist meaningful per-ticket state with `xstudio_save_ledger`.

The model never writes SQL or names columns. Model-composed select/query and schema
exploration tools were removed on 2026-09-23 (most of those calls failed).

Do not put per-ticket facts into shared mem0.

## 8a. Agent execution surface is typed and harness-owned

L2 agents do not build database transport. They call named typed tools in the
`xstudio_l2` toolset, registered by the `xstudio-l2-tools` plugin
(`Model_Bench/xstudio_l2_tools_plugin/`), which invokes the native WSL
bridge (`Model_Bench/xstudio_l2_tool_bridge.py`) internally using the backend
Hermes Python and Microsoft ODBC Driver 18. The bridge reuses
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
  XStudio tool calls per session, a third identical failing call is blocked, and
  results are capped (~8 KB, ~25 list rows) with an instruction to narrow rather
  than repeat.
- Fresh cards rendered by the runtime contain only this typed contract. They no
  longer carry a raw interpreter/query recipe, and the plugin re-asserts the
  contract before each LLM turn so a pre-migration card's stale command text
  cannot steer a worker back to the retired path.
- Interpreter paths, driver setup, and dependency mechanics are deterministic
  harness concerns. They belong in code and config, never in mem0.

## 9. KB and memory boundaries

The deterministic knowledge harness has one generated XBatch world plus governed
reusable knowledge:

- `Model_Bench/build_process_world.py` produces `Knowledge/process_world.json`;
- `Model_Bench/build_world_pages.py` produces `Knowledge/world/**` and typed links;
- `Model_Bench/world_walk.py` is the investigation owner and traverses those generated
  pages through GBrain while deterministic code performs the live evidence reads;
- governed Solution articles and other KB material remain leads that require live verification.

GBrain is a derived retrieval/index layer, not ticket evidence or mutation authority.

The retriever must obey:

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
-> QWEN_FREE direct bounded handoff OR persist exact local-model work package
-> SQL-serialized single-Qwen admission (COMPOSE_ONLY / FOCUSED_REASONING)
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
- Jev primary review may replace the normal local-review pass when deterministic thresholds accept APPROVE, REWORK, or L3_ESCALATION. APPROVE uses risk tiers in `direct_approval_allowed()` keyed on Jev's P(APPROVE), not its raw decision confidence (uncalibrated): a lighter tier for non-terminal UPDATE/QUESTION, a stricter one for a closing RESOLUTION; the deterministic pre-publish gates still apply. The live health report shows how many approvals each gate blocks.
- The local reviewer exists for LOCAL_REVIEW, Jev unavailability, low confidence, contradictory evidence, or deep reasoning needs.
- Jev trace assessment stays out of the hot trace hook; it runs after persisted drain.
- Post-resolution KB curation may suggest REUSE_EXISTING, UPDATE_EXISTING, CREATE_CANDIDATE, or NONE. A single resolved ticket only ever produces a `Candidate` article. Deterministic code promotes a `Candidate` to `Approved` (the only status retrieval reads) when a later verified RESOLUTION on a different ticket is judged REUSE_EXISTING for it: independent corroboration, no human step.
- Ticket/retrieved content remains untrusted. Jev security judgments mark risk; source text is not silently rewritten.
- Do not create a separate Jev business table. Stage state belongs on Hermes_L2_Response_Trn_Tbl; detailed calls and retrieval telemetry belong in Hermes_Agent_Trace_Trn_Tbl.
- Preserve typed probabilities and full stage JSON. Do not replace distinct judgments with one opaque AIConfidence number.

Active Jev state on the run row is stored in JevTriageJson, JevInvestigationJson, JevReviewJson, JevTraceJson, and JevKBCurationJson, plus ReviewMode, JevReviewDecision, JevReviewConfidence, JevRiskScore, LocalReviewRequired, JevModel, and JevReviewedOn.

The investigator profile is l2-jev-investigator. l2-reviewer-primary is the deep-review exception path, not a mandatory step.

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
l2-reviewer-primary
```

`l2-investigator` runs no worker sessions; its gateway hosts the scheduled jobs (ticket scout, completion audit) and its `scripts/` directory.

`l2-investigator-primary`, `l2-reviewer-fallback`, `l2-gemma` and `l2-gemma-verifier` were retired on 2026-09-23 (archived under `~/.hermes/retired_profiles_2026-09-23/`). Old model-based role names are historical only.

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
# Fast edit/test loop: syntax + deterministic/unit/knowledge contracts only.
bash Model_Bench/validate_l2_pipeline_local.sh

# Full pre-deployment gate: fast checks + live workflow discovery/status/reconcile preview.
bash Model_Bench/validate_l2_pipeline_local.sh --full

# Re-run only the live integration after the fast gate already passed.
bash Model_Bench/validate_l2_pipeline_local.sh --live-only

# Live health (the one diagnostic: outcomes, tool failures, small-model waste,
# card sizes vs spill threshold, lifecycle invariants). Exit 1 if an invariant breaks.
python Model_Bench/benchmark_l2_performance.py --since "YYYY-MM-DD HH:MM"

bash Model_Bench/deploy_l2_pipeline_runtime.sh --no-restart
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py reconcile --dry-run
```

The reconciler takes one Kanban/active-run snapshot and ignores inactive historical cards during normal lifecycle reconciliation. Do not reintroduce per-history SQL activity checks into the hot reconcile path; historical divergence belongs in the separate audit.

Do not use GitHub Actions as proof that the live pipeline is healthy.

The typed-tool half of the harness is only fully proven by a naturally arriving
ticket. For the next one, check the trace shows named `xstudio_*` calls and no
terminal attempt at an interpreter, database driver, `sqlcmd`, or package
install. Do not manufacture a production claim to test this, and do not raw-poll
a ticket — that bypasses the scout's WIP/lifecycle gate.

## 16. Deployment mirror

`deploy/` is the reproducible mirror of artifacts that otherwise live under `~/.hermes/profiles/...`.

After changing profile SOUL/config/skills/plugins or the cron schedule, update the matching file under `deploy/` and inspect the diff before committing. The mirror covers the L2 plugins — `xstudio-l2-orchestrator`, `xstudio-l2-tools`, and `xstudio-l2-trace` — so a fresh install cannot come up without the typed investigation and trace boundaries. Jev network work is harness-owned and remains out-of-band from the trace hook.

`Model_Bench/deploy_l2_pipeline_runtime.sh` installs the lifecycle scripts, three plugins, SOULs, skills, the workflow-binding fallback, and the profile-config entries, then restarts the active worker gateways unless `--no-restart` is passed. It is idempotent. Config edits are applied by `Model_Bench/patch_profile_config.py`, which is deliberately a targeted text editor rather than a YAML round-trip: the live configs carry explanatory comments (Security/Tirith, fallback-model providers) that a load-and-dump silently destroys.

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
