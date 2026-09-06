# Claude Entry Point — Chitragupta Adaptive L2 Branch

You are on the deliberate experimental branch:

```text
development/autonomous-l2-learning-runtime
```

The product north star is the highest-level contract:

> Build an autonomous, AI-driven, deterministic L2 Helpdesk that gets measurably better from experience and progressively earns the ability to solve XBatch issues itself.

Read `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` first, then `AGENTS.md`. `AGENTS.md` now includes the adaptive branch's identity, experience, governed-Solution and action-authority rules while preserving the production lifecycle baseline. Permanent read-only diagnosis, a fixed retrieval substrate, or old topology rules are not product constraints on this branch. Preserve deterministic safety properties unless a better implementation replaces them explicitly.

## Current architecture

### Control plane

```text
claim -> investigator -> normalize -> frozen independent reviewer
      -> approve/publish OR reject/rework -> fresh reviewer
```

`Model_Bench/l2_pipeline_runtime.py` owns lifecycle transitions, WIP, review cycles, publication and recovery.

### Evidence plane

`xstudio_l2` is the typed SQL/schema/ticket/run evidence surface.

`xstudio-l2-identity` is a cross-cutting pre-tool guard. It resolves the real Kanban card and binds identity-sensitive evidence/ledger calls and `l2_action` plan provenance to the current `run_id`/`ticket_id`. Conflicting model-supplied identifiers are blocked. Do not reintroduce model-controlled incident identity.

### Experience & learning plane

Shared vault:

```text
~/.hermes/l2-learning/
  sessions/              redacted unverified episodic turns
  cases/approved/        review + publisher-postcondition historical cases
  cases/rejected/        reviewer counterexamples
  cases/reopened/        prior resolutions later regressing/reopening
  facts/                 promoted operational lessons
  candidates/            unverified lesson candidates
  knowledge/             disposable Git/skill mirror
  solutions/approved/    governed hash-pinned SQL Solution exports
  actions/plans/         non-executing action plans
  actions/candidates/    repeated human-action capability design backlog
  actions/receipts/      future append-only action outcome history
  eval/                  runtime historical retrieval replay cases
```

`zvec-grep` provides BM25 + vector hybrid retrieval. mem0 remains separate for compact durable operational behavior.

### Action plane

`deploy/xstudio_action_capabilities.json` is the typed corrective-action registry. `l2_actions` currently supports only:

```text
list
describe
plan
plans
validate_plan
```

There is no execute operation. A plan is an identity-bound, capability-hashed, evidence-carrying recommendation/shadow artifact with `execution_authorized=false`.

Repeated reviewed human actions are mined into `actions/candidates/**`. `Model_Bench/l2_action_capability_curator.py` is the separate operator/control-plane path:

```text
needs_executor_design
-> researching_executor
-> contract_drafted
-> shadow_ready
-> registry_entry
```

The curator requires provenance, validates the registry contract, requires a concrete supported execution target plus preconditions/idempotency/verification/evidence/rollback/approval policy before `shadow_ready`, promotes only at `mode=shadow`, and never raises registry `global_mode`.

## Storage is not authority

The central rule is:

```text
recording experience != believing experience
retrieving experience != proving a current ticket
historical success != universal fix
reasoning about an action != permission to execute it
execution returned != corrective action verified
```

### Sessions are deliberately recorded

Every completed L2 turn is valuable for replay, failure mining, reviewer-correction analysis, token/tool optimization and future training/evaluation. Keep session recording ON.

### Generic automatic prefetch stays OFF

Do not add a generic zvec `pre_llm_call`/turn-start top-k injection. Sessions contain incorrect investigator hypotheses, reviewer-rejected claims, stale state and hallucinations. Similarity is not trust.

Use explicit `l2_recall` scopes. `trusted` excludes historical cases. `approved_cases`, `rejected_cases`, `reopened_cases`, and `sessions` all expose different trust semantics and still require live verification for current-ticket claims.

A future automatic context builder must be deterministic and stage/source/trust aware; it must not be mixed-memory top-k injection.

## Outcome-conditioned learning is implemented

`Model_Bench/sync_l2_outcomes.py` materializes:

```text
review reject                              -> cases/rejected
review approve + publisher postconditions  -> cases/approved
published RESOLUTION later leaves terminal -> cases/reopened
```

`Model_Bench/mine_l2_learning_candidates.py` conservatively mines these labels into unverified lesson candidates.

`Model_Bench/mine_l2_action_capability_candidates.py` detects repeated independently reviewed `NEEDS_HUMAN_ACTION` actions across distinct tickets and creates/updates `actions/candidates/*.json`. These are **design backlog items**, not executable registry entries. Never invent missing procedure/API signatures, risk or parameter schemas to promote them.

`Model_Bench/l2_learning_cycle.py` is the one best-effort sidecar coordinator. Keep learning mechanics behind this boundary instead of growing independent cron/scout choreography.

## Governed SQL Solution retrieval is implemented

`dbo.Hermes_Solution_Article_Mst_Tbl` is a source of reusable knowledge, but `IsActive=1` is not trust approval.

`Model_Bench/sync_l2_approved_solutions.py` + `deploy/solution_export_policy.json` require an explicit:

```text
solution_id
semantic content_sha256
approved_by
approved_at
review_evidence
```

before an article enters `solutions/approved/**` and therefore the `trusted` zvec scope.

The semantic hash deliberately excludes mutable telemetry such as `UsageCount`. Governed semantic drift fails closed and archives the stale managed trusted export until the new content is reviewed. `--preview-live` lists active Solution IDs and semantic hashes without trusting them.

Do not weaken this to "all active Solutions are trusted."

## Historical replay is implemented

`Model_Bench/build_l2_historical_retrieval_eval.py` correlates the earliest recorded user/task text for a run with that run's outcome-labelled historical case and writes runtime JSONL replay cases.

`Model_Bench/benchmark_l2_learning_retrieval.py` measures deterministic retrieval hit rate, latency, context size and forbidden hits without an LLM judge.

Expand replay with adversarial same-symptom/different-root-cause cases rather than only easy recall.

## Learning promotion boundaries

Different artifacts have different governance paths:

```text
unverified lesson candidate
  -> l2_learning_curator.py
  -> reviewed operational fact

active SQL Solution
  -> solution_export_policy.json + semantic hash check
  -> governed trusted retrieval export

repeated human-action candidate
  -> l2_action_capability_curator.py
  -> reviewed shadow registry contract
```

The model cannot promote any of these merely by asserting confidence.

## Future XBatch solving

Current arbitrary SQL remains read-only, but that is A0—not the destination.

```text
A0 observe
A1 recommend
A2 shadow plan
A3 supervised execute
A4 autonomous low-risk execute
A5 broader autonomous remediation
```

Autonomy is earned per capability.

Before adding a real capability, verify the actual supported SP/API/service path and exact current signature. The registry contract requires parameter schema, preconditions, idempotency, evidence, verification, rollback/compensation, risk and approval policy.

Synthetic test capability names are never evidence that such an XBatch operation exists.

## Action receipts are already defined

Before any real executor exists, `deploy/xstudio_action_receipt.schema.json` and `Model_Bench/xstudio_action_receipts.py` define:

```text
planned -> approved -> executed -> verified
    \         \          \
     +-> failed <---------+
           |
           v
      compensated
```

The history is append-only. `verified` requires deterministic postcondition proof; `compensated` requires verified rollback/compensation. Creating a planned receipt is not permission to execute.

A future deterministic executor must re-check:

```text
current run/ticket identity
capability + registry hashes
current live evidence
preconditions
approval policy
idempotency
execution result
postconditions
rollback/compensation path
```

and append receipt events throughout. Do not add raw UPDATE/EXEC access as an autonomy shortcut.

## Current authoritative sources

- `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` — branch north star and implemented multi-plane architecture.
- `AGENTS.md` — detailed operating contract for lifecycle, evidence, learning and action authority.
- `Knowledge/L2_PIPELINE_STATE_MACHINE.md` — deterministic lifecycle.
- `Model_Bench/l2_pipeline_runtime.py` — lifecycle implementation.
- `Model_Bench/l2_learning_cycle.py` — learning sidecar coordinator.
- `Model_Bench/xstudio_l2_identity_plugin/` — run/ticket identity guard.
- `Model_Bench/xstudio_l2_learning_plugin/` — session recording + explicit recall + lesson candidates.
- `Model_Bench/sync_l2_approved_solutions.py` + `deploy/solution_export_policy.json` — governed SQL Solution trust bridge.
- `Model_Bench/xstudio_l2_actions_plugin/` — non-executing action planner.
- `Model_Bench/l2_action_capability_curator.py` — reviewed action candidate -> shadow registry workflow.
- `deploy/xstudio_action_capabilities.json` — corrective-action registry contract.
- `deploy/xstudio_action_receipt.schema.json` + `Model_Bench/xstudio_action_receipts.py` — future execution outcome contract.
- `deploy/helpdesk_workflow_binding.json` — observed Helpdesk workflow binding.
- `Knowledge/manifest.json` / `Knowledge/task-router.md` — domain routing.
- `Knowledge/KB_IMPLEMENTATION_PLAN.md` — useful governance/provenance concepts; its retrieval technology choice is not sacred.

## Current implementation facts worth preserving until deliberately replaced

- Global SQL WIP currently `1` because of local inference constraints.
- Priorities: review `30`, rework `20`, new investigation `10`.
- Reviewer creation is deferred until completion is normalized/reviewable.
- Reviewer receives frozen `proposal_json`; publisher publishes that exact proposal.
- `review_cycle` controls bounded rework, not SQL `AttemptNo`.
- `ticket_scout.py` remains the reconcile-first claim backstop.
- model-driven Python/pyodbc/sqlcmd/package-install SQL transport stays blocked.
- Helpdesk workflow states are harness-bound from observed values.
- run/ticket identity for evidence/action planning is harness-bound.
- sessions/cases are not automatically trusted knowledge.
- a resolution does not automatically become a trusted Solution export.
- action candidate/plan creation does not grant execution authority.
- capability curation cannot implicitly raise global autonomy mode.
- no GitHub Actions workflow is the project validation mechanism.

## Next design priorities

1. Use `sync_l2_approved_solutions.py --preview-live` to review and pin genuinely reusable active SQL Solutions rather than bulk-trusting them.
2. Run the learning cycle against real history and inspect the real `actions/candidates/**` backlog; choose the strongest repeated candidate by evidence, not by a synthetic test name.
3. Research that candidate's actual XBatch SP/API/service implementation, signature, preconditions, idempotency, postconditions and compensation path.
4. Move it through `l2_action_capability_curator.py` into the first **real** `shadow` registry entry while leaving `global_mode=observe` until shadow activation is deliberately justified.
5. Measure shadow-plan agreement against what humans actually do and whether the issue resolves.
6. Strengthen lesson promotion with repeated evidence, contradiction/reopen checks and replay metrics.
7. Build the separate supervised executor only after shadow evidence is strong, using the existing action receipt contract from the first execution attempt.
8. Use verified/failed/compensated receipts to promote or demote per-capability autonomy.
9. Build deterministic stage-aware context assembly if automatic retrieval becomes worthwhile; do not regress to generic prefetch.

Historical `Plans/` and `Agent_Comms/` remain provenance. Do not revive dead duplicate orchestration merely because it appears there, and do not reject a better architecture merely because it differs from an old rule.
