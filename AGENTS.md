# AI Helpdesk / Hermes L2 — Agent Operating Contract

This file is the stable operating contract for agents working on Chitragupta.
For the exact lifecycle state machine, read `Knowledge/L2_PIPELINE_STATE_MACHINE.md`.
For human-facing architecture and deployment, read `README.md`.
For the adaptive branch north star, experience plane, evaluation plane, and action-autonomy ladder, read `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md`.
For KB design and governance concepts, read `Knowledge/KB_IMPLEMENTATION_PLAN.md`.

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

On `development/autonomous-l2-learning-runtime`, that production-safe lifecycle is the **control plane**, not the final product boundary. The branch adds separate evidence/identity, experience/learning, evaluation, and corrective-action planes while preserving deterministic authority at workflow and side-effect boundaries.

The branch-wide rule is:

```text
recording experience != believing experience
retrieving experience != proving a current-ticket claim
reasoning about an action != permission to execute it
an execution attempt != a verified successful outcome
```

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
INVESTIGATOR [priority 10]
  l2-investigator-primary
        |
        | kanban_complete(metadata)
        v
normalize / validate completion
        |
        | only after the proposal is reviewable
        v
REVIEWER [priority 30]
  l2-reviewer-primary
  frozen proposal_json
       / \
approve   reject
   |         |
   v         v
deterministic  REWORK [priority 20]
publish        l2-investigator-primary
   |             |
   |             | complete + normalize
   |             v
   |          NEW REVIEWER [priority 30]
   |             |
   +-------------+
        |
        v
SQL + Helpdesk terminal/waiting state
```

### Non-negotiable lifecycle rules

- New investigation priority = `10`.
- Rework priority = `20`.
- Review priority = `30`.
- Reviewer creation is **deferred until the investigator/rework completion has been normalized and is reviewable**.
- A reviewer receives a frozen `proposal_json`. The proposal reviewed is the proposal published.
- Investigator never calls `--publish-response`.
- Reviewer never calls `--publish-response` and never retypes the response for publication.
- `review_cycle` counts reviewer/rework loops. SQL `AttemptNo` does not.
- `MAX_REVIEW_CYCLES = 3`; rejection at cycle 2 escalates instead of creating cycle 3.
- A rework is not complete until it gets its own fresh reviewer after rework completion/normalization.
- The old `l2-review` board and `kanban_forward_bridge.py` are retired.
- All investigator/reviewer/rework tasks live on the normal Kanban board.

## 3. Reconciliation is the lifecycle backstop

The central reconciler owns lifecycle sequencing synchronously. Current order:

```text
1. normalize investigator/rework completions
2. convert unreviewable terminal completions into bounded rework
3. create missing reviewers for reviewable completed investigations
4. process reviewer rejections
5. process reviewer approvals and publish
6. recover true SQL/Kanban orphans
```

The old design launched repair/reject/publisher as independent concurrent processes. Do not restore that pattern.

`Model_Bench/xstudio_l2_orchestrator_plugin/` triggers the same reconciler immediately after successful `kanban_complete` / `kanban_block`. Event delivery is an optimization, not a correctness dependency.

The 2-minute `ticket_scout.py` job runs reconciliation before every claim attempt and is the durable mutating backstop. It also invokes one best-effort **learning sidecar cycle** after reconciliation. That sidecar may materialize outcomes and mine candidates, but it must never become claim/review/publish authority or block ticket handling.

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

The deterministic publisher publishes only a reviewer-approved frozen proposal through `Hermes_Orchestrator.py --publish-response --force-run-id`.

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

A resolved ticket is **not automatically a KB article**. KB/Solution promotion is governed separately. `Hermes_Solution_Article_Mst_Tbl.IsActive = 1` also does not by itself make an article trusted retrieval material on the adaptive branch; see §9.

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

Live evidence wins over retrieved knowledge, prior ledgers, historical cases, sessions, or memory.

Evidence hierarchy for a **current-ticket claim**:

1. current ticket state and live SQL evidence through `xstudio_l2`;
2. verified `Knowledge/` reference material and governed reusable Solution articles as guidance;
3. same-ticket run ledger/attempt history;
4. outcome-labelled historical cases as explicit analogies/counterexamples;
5. raw historical sessions as unverified forensic experience;
6. mem0 operational hints.

The ordering does not mean a lower source is useless. It means a relevant historical item cannot override contradictory live evidence.

Never fabricate a table, view, column, SP, ticket status, identifier, capability ID, or action result.

Preferred investigation path, all database work through the typed `xstudio_l2` tool (see §8a):

- use the dispatch-time investigation bundle first;
- `select` when the table/entity is known (identifiers are schema-validated);
- `suggest_tables` for deterministic narrowing;
- `find_objects` / `get_definition` for live metadata when necessary;
- `query` only for read-only SQL, with `database` specified explicitly;
- `read_procedure` only for the explicitly allowlisted diagnostics;
- persist meaningful per-ticket state with `save_ledger`.

Use `l2_recall` deliberately when prior experience can shorten or challenge the investigation:

- `trusted` = governed reference + promoted facts + governed Solution exports;
- `approved_cases` = historical proposals that passed independent review and publisher postconditions;
- `rejected_cases` = reviewer-rejected counterexamples;
- `reopened_cases` = prior published resolutions that later left the recorded terminal state;
- `sessions` = raw unverified historical turns/dead ends.

`trusted` deliberately excludes historical cases. There is no generic automatic zvec prefetch. Relevance is not authority.

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

## 8b. Incident identity is harness-owned

`Model_Bench/xstudio_l2_identity_plugin/` is a cross-cutting guard over identity-sensitive tool calls.

For a Kanban worker, `run_id` and `ticket_id` come from the actual assigned task. They are not free model parameters. Before a sensitive `xstudio_l2` or `l2_action` call, the identity guard:

- resolves the current Kanban task;
- injects the authoritative run/ticket identity where required;
- blocks a conflicting model-supplied identity;
- blocks cross-ticket/cross-run plan access or validation;
- fails closed if an identity-sensitive task cannot be resolved.

Pure schema/object discovery that does not attach evidence to an incident can remain identity-independent.

This is a correctness boundary. A model must never be able to write a ledger, claim evidence, or construct an action plan for incident B while actually working incident A.

## 9. Knowledge, memory, experience, and Solution governance

Do not collapse different authority classes into one "memory" bucket.

```text
live SQL / ticket state
    = current-ticket evidence authority

Git Knowledge/ + deployable skills
    = canonical reference

Hermes_Solution_Article_Mst_Tbl
    = SQL knowledge source requiring separate governance before trusted export

solutions/approved/** in the learning vault
    = hash-pinned governed reusable guidance

facts/**
    = explicitly promoted operational heuristics

cases/approved|rejected|reopened/**
    = outcome-labelled historical experience, analogy/counterexample only

sessions/**
    = redacted unverified episodic experience

candidates/**
    = unverified lessons awaiting control-plane review

mem0
    = compact durable operational behavior intended to influence routine work

zvec-grep index
    = disposable retrieval substrate over the local learning vault, never source of truth
```

The current deterministic KB retriever remains a conservative layer and must obey:

- route alone cannot retrieve a solution;
- weak generic overlap must abstain;
- every hit carries provenance;
- live verification remains mandatory;
- pre-investigation retrieval must not use `SuspectedCause` as a primary signal, avoiding self-confirmation.

`Knowledge/KB_IMPLEMENTATION_PLAN.md` remains authoritative for provenance/lifecycle/applicability/abstention concepts. Its historical choice of retrieval substrate is not an immutable branch constraint.

### Governed SQL Solution export

`Model_Bench/sync_l2_approved_solutions.py` exports SQL Solution articles only when `deploy/solution_export_policy.json` explicitly names the `solution_id`, exact semantic `content_sha256`, reviewer identity/time, and review evidence.

Rules:

- `IsActive = 1` is not trust approval.
- Semantic content drift fails closed and removes/archives the stale managed file from trusted recall until re-reviewed.
- Mutable operational counters such as `UsageCount` do not invalidate the semantic approval hash.
- Removing an approval archives only the generated vault mirror; it does not mutate the SQL article.
- `--preview-live` may be used to enumerate active Solution IDs and semantic review hashes before an operator updates policy.

### Outcome-conditioned learning

The learning sidecar records stronger historical signals after workflow outcomes:

- reviewer rejection -> negative historical case;
- reviewer approval + publisher postconditions -> approved historical case;
- a later terminal-status change after a published resolution -> reopened/regression case.

`mine_l2_learning_candidates.py` may turn repeated/corrective outcome patterns into **unverified** lesson candidates. `l2_learning_curator.py` performs explicit promotion/rejection. A model cannot promote its own lesson merely by writing confident prose.

Historical retrieval replay is built from real recorded incident context and corresponding outcome cases. Improvement claims should come from replay/live metrics, not intuition.

## 10. SQL write discipline and corrective-action autonomy

Never write directly to `Complaint_Mst_Tbl` from an investigation.

Ticket publication goes through the audited Hermes stored-procedure path exposed by `Hermes_Orchestrator.py` after independent reviewer approval.

The **current investigator/reviewer worker surface remains read-only** for arbitrary SQL. Do not interpret older "official SP first/direct write exception" guidance as permission for a model to execute a production mutation directly.

For future XStudio corrective action, use the typed capability architecture:

```text
verified diagnosis
  -> repeated NEEDS_HUMAN_ACTION evidence
  -> actions/candidates backlog
  -> researching_executor
  -> contract_drafted
  -> shadow_ready
  -> registry_entry (mode=shadow)
  -> separately promoted policy/global mode
  -> future deterministic executor
  -> deterministic postcondition verification
  -> append-only action receipt
```

`Model_Bench/mine_l2_action_capability_candidates.py` detects repeated reviewed human-action patterns but deliberately does not invent risk, parameters, executor, preconditions, verification, rollback, or approval policy.

`Model_Bench/l2_action_capability_curator.py` is the operator/control-plane workflow for filling and reviewing that contract. Its promotion path:

- requires reviewer/evidence provenance;
- validates the contract against `deploy/xstudio_action_capabilities.json`;
- requires a concrete supported execution target plus preconditions, idempotency, verification, evidence, rollback/compensation, and approval policy before `shadow_ready`;
- writes only `mode=shadow` registry entries;
- **never raises `global_mode`**.

The model-facing `l2_actions` plugin remains non-executing and exposes only `list`, `describe`, `plan`, `plans`, and `validate_plan`. `execution_authorized=false` is not a suggestion; it is the current authority boundary.

The old `xstudio-sql-write-discipline` principle remains useful for designing a future capability: prefer a real supported XStudio stored procedure/API/service action over direct table mutation. But execution belongs behind a reviewed deterministic capability, not a model-built write path.

## 10a. Future action-result receipts are defined before execution exists

`deploy/xstudio_action_receipt.schema.json` and `Model_Bench/xstudio_action_receipts.py` define the audit lifecycle a future executor must use:

```text
planned -> approved -> executed -> verified
    \         \          \
     +-> failed <---------+
           |
           v
      compensated
```

Rules:

- receipt history is append-only;
- one deterministic receipt identity exists per plan/action attempt;
- creating a `planned` receipt grants no execution permission;
- `verified` requires deterministic postconditions to have been checked;
- `compensated` requires compensation/rollback state to have been verified;
- a terminal verified receipt cannot later be rewritten into failure;
- receipts record outcomes; capability registry + approval policy still decide authority.

This contract exists now so eventual execution cannot be introduced without audit/outcome semantics.

## 11. No scratch files in the project root

Do not litter the synced project directory with one-off investigation scripts or SQL files.

Use terminal one-liners or a real temporary directory. If a utility is reusable, place it intentionally under `Model_Bench/` and document/test it.

## 12. Current profiles and model handling

Active role names:

```text
l2-investigator-primary
l2-reviewer-primary
l2-reviewer-fallback
```

`l2-investigator` remains the dispatcher/host profile and compatibility location for scripts.

Old model-based role names such as `l2-eval-investigator`, `l2-gemma-verifier`, and `l2-qwen-verifier` are historical only.

The four active/compatibility profiles are expected to expose these adaptive branch plugins:

```text
xstudio-l2-tools
xstudio-l2-identity
xstudio-l2-learning
xstudio-l2-actions
```

with direct toolsets:

```text
xstudio_l2
l2_learning
l2_actions
```

`xstudio-l2-orchestrator` remains the event-driven lifecycle reconciler trigger. `xstudio-l2-trace` may remain separately enabled for trace/observability purposes.

Do not hardcode the current LM Studio model into architecture documentation. The loaded model can change. Verify it live at the configured LM Studio endpoint before diagnosing model mismatch.

## 13. Repository sources of truth

Use this hierarchy when documents disagree:

1. live SQL/Hermes state for runtime facts;
2. `Model_Bench/l2_pipeline_runtime.py` for lifecycle behavior;
3. `Knowledge/L2_PIPELINE_STATE_MACHINE.md` for the documented lifecycle contract;
4. `deploy/helpdesk_workflow_binding.json` for workflow status binding;
5. `deploy/xstudio_action_capabilities.json` for registered corrective-action policy;
6. `deploy/solution_export_policy.json` for trusted SQL Solution export approvals;
7. deployable skills under `deploy/skills/xstudio/` for worker behavior;
8. `Knowledge/manifest.json` for machine-readable KB routing/catalog;
9. `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` for adaptive-branch product architecture;
10. `README.md` for human-facing architecture;
11. `Plans/` and `Agent_Comms/` only for history/research.

The runtime learning vault contains experience and derived retrieval mirrors, not canonical project policy. Its zvec index is disposable.

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

Primary command:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

That script is the aggregate local contract and currently covers lifecycle, typed evidence, identity, adaptive learning, outcome sync/mining, governed Solution export, historical retrieval replay, action planning, action-capability curation, future action receipts, profile patching, deploy drift, KB validation, live workflow discovery/status, and reconcile dry-run.

Useful narrower commands include:

```bash
python3 Model_Bench/test_xstudio_l2_tools_plugin.py
python3 Model_Bench/test_xstudio_l2_identity_plugin.py
python3 Model_Bench/test_xstudio_l2_learning_plugin.py
python3 Model_Bench/test_sync_l2_approved_solutions.py
python3 Model_Bench/test_l2_action_capability_curator.py
python3 Model_Bench/test_xstudio_action_receipts.py
python3 Model_Bench/test_adaptive_deploy_contract.py
python3 -m unittest -v Model_Bench/test_l2_pipeline_runtime.py
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py reconcile --dry-run
```

The typed-tool half of the harness is only fully exercised by a naturally arriving ticket. For the next one, check the trace shows `xstudio_l2` calls and no terminal attempt at an interpreter, database driver, `sqlcmd`, or package install. Do not manufacture a production claim to test this, and do not raw-poll a ticket — that bypasses the scout's WIP/lifecycle gate.

## 16. Deployment mirror

`deploy/` is the reproducible mirror of artifacts that otherwise live under `~/.hermes/profiles/...`, plus Git-tracked adaptive policy/contract artifacts.

After changing profile SOUL/config/skills/plugins or the cron schedule, refresh the mirror with `Model_Bench/mirror_wsl_artifacts.sh` and inspect the diff before committing.

The adaptive profile/plugin contract includes:

```text
xstudio-l2-orchestrator
xstudio-l2-tools
xstudio-l2-identity
xstudio-l2-learning
xstudio-l2-actions
```

`Model_Bench/deploy_l2_pipeline_runtime.sh` installs lifecycle scripts, plugins, SOULs, skills, workflow/action policy fallbacks, and profile-config entries. It synchronizes the canonical learning corpus, materializes only hash-approved SQL Solution articles, indexes the resulting vault, runs the learning outcome/candidate sidecar, and restarts the four active gateways unless `--no-restart` is passed.

Config edits are applied by `Model_Bench/patch_profile_config.py`, which is deliberately a targeted text editor rather than a YAML round-trip: the live configs carry explanatory comments (Security/Tirith, fallback-model providers) that a load-and-dump silently destroys.

`deploy/xstudio_action_receipt.schema.json` is installed as a future-executor contract. No action executor is currently installed or exposed by the model-facing plugin.

## 17. Security / credentials

Do not commit or print credentials.

Scripts use environment-provided SQL credentials. WSL may not see the same environment as Windows Python, so subprocess construction must omit `--password` when no value is present; never pass Python `None` as an argv element.

Experience/session recording must redact common secret shapes before persistence. Trusted Solution exports must never copy credentials from ticket/session prose. Action plans/receipts should reference evidence, not embed connection secrets.

## 18. When changing lifecycle, learning, or action authority

Any lifecycle change must preserve or deliberately revise these invariants:

- WIP ownership is explicit.
- Exactly one lifecycle authority performs ticket workflow mutations.
- Every publishable investigator/rework result gets exactly one reviewer.
- Reviewers see an immutable proposal.
- Publication is deterministic and idempotent.
- Review cycles are bounded.
- Event loss is recoverable by reconciliation.
- SQL/Helpdesk postconditions define publication success.
- Knowledge retrieval cannot substitute for live evidence.

Any adaptive-learning/action change must also preserve or deliberately revise:

- current run/ticket identity is harness-owned for identity-sensitive calls;
- session recording does not make session text trusted;
- historical cases remain labelled by outcome and are not current-ticket proof;
- generic automatic zvec prefetch stays off unless a future deterministic stage-aware design explicitly replaces it;
- model-proposed lessons remain unverified until separately promoted;
- SQL Solution trust requires explicit governance and semantic content pinning;
- action planning does not grant execution permission;
- capability registry promotion is per-capability and cannot silently raise `global_mode`;
- arbitrary raw SQL mutation is not introduced as a shortcut around typed capability policy;
- a future action is not successful merely because execution returned; deterministic postconditions must reach a `verified` receipt state;
- compensation/rollback, when required, is itself verified and recorded.

If a proposed change violates one of these, update the relevant state-machine/architecture contract and tests in the same commit.
