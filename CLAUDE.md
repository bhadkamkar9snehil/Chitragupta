# Claude Entry Point — Chitragupta Adaptive L2 Branch

You are on the deliberate experimental branch:

```text
development/autonomous-l2-learning-runtime
```

The product north star is the highest-level contract:

> Build an autonomous, AI-driven, deterministic L2 Helpdesk that gets measurably better from experience and progressively earns the ability to solve XBatch issues itself.

Read `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` first, then `AGENTS.md`. `AGENTS.md` remains the production lifecycle/safety baseline, but permanent read-only diagnosis, a fixed retrieval substrate, or old topology rules are not product constraints on this branch. Preserve deterministic safety properties unless a better implementation replaces them explicitly.

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
  solutions/approved/    governed reusable Solution export target
  actions/plans/         non-executing action plans
  actions/candidates/    repeated human-action capability design backlog
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

## Storage is not authority

The central rule is:

```text
recording experience != believing experience
retrieving experience != proving a current ticket
historical success != universal fix
reasoning about an action != permission to execute it
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

## Historical replay is implemented

`Model_Bench/build_l2_historical_retrieval_eval.py` correlates the earliest recorded user/task text for a run with that run's outcome-labelled historical case and writes runtime JSONL replay cases.

`Model_Bench/benchmark_l2_learning_retrieval.py` measures deterministic retrieval hit rate, latency, context size and forbidden hits without an LLM judge.

Expand replay with adversarial same-symptom/different-root-cause cases rather than only easy recall.

## Learning promotion boundary

`l2_lesson` and automatic miners may create only `unverified_candidate` artifacts. Promotion is separate through the learning curator/governance layer.

The rule is:

```text
model says it learned something != system learned something
```

Use reviewer outcomes, repeated independent evidence, reopen/regression signals and replay results to decide promotion.

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

Before any future execution, a separate deterministic executor must re-check:

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

Do not add raw UPDATE/EXEC access as an autonomy shortcut.

## Current authoritative sources

- `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` — branch north star and implemented multi-plane architecture.
- `AGENTS.md` — production lifecycle/safety baseline.
- `Knowledge/L2_PIPELINE_STATE_MACHINE.md` — deterministic lifecycle.
- `Model_Bench/l2_pipeline_runtime.py` — lifecycle implementation.
- `Model_Bench/l2_learning_cycle.py` — learning sidecar coordinator.
- `Model_Bench/xstudio_l2_identity_plugin/` — run/ticket identity guard.
- `Model_Bench/xstudio_l2_learning_plugin/` — session recording + explicit recall + lesson candidates.
- `Model_Bench/xstudio_l2_actions_plugin/` — non-executing action planner.
- `deploy/xstudio_action_capabilities.json` — executable-capability registry contract, currently independent of the candidate backlog.
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
- a resolution does not automatically become trusted KB.
- no GitHub Actions workflow is the project validation mechanism.

## Next design priorities

1. Export governed approved Solution knowledge into `solutions/approved/**` with provenance.
2. Strengthen lesson promotion with repeated evidence, contradiction/reopen checks and replay metrics.
3. Treat `actions/candidates/**` as a capability-engineering backlog: inspect the real XBatch implementation and fill exact registry contracts.
4. Introduce the first **verified** low-risk action in `shadow`, not supervised/autonomous.
5. Measure shadow-plan agreement against what humans actually do and whether the issue resolves.
6. Build the separate supervised executor only after shadow evidence is strong.
7. Record action execution/postcondition/rollback receipts into the learning plane and use them to promote or demote autonomy.
8. Build deterministic stage-aware context assembly if automatic retrieval becomes worthwhile; do not regress to generic prefetch.

Historical `Plans/` and `Agent_Comms/` remain provenance. Do not revive dead duplicate orchestration merely because it appears there, and do not reject a better architecture merely because it differs from an old rule.
