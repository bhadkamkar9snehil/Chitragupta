# Autonomous L2 Learning Architecture

Status: **experimental branch contract**  
Branch: `development/autonomous-l2-learning-runtime`  
North star: **an autonomous, AI-driven, deterministic L2 Helpdesk that gets measurably better from experience and progressively earns the ability to solve XBatch issues itself.**

## 1. The one rule

Everything in this branch is subordinate to one product rule:

> Chitragupta must become an autonomous L2 Helpdesk system whose reasoning improves continuously while workflow, evidence attribution, side effects and outcome verification remain deterministic enough to trust in production.

Existing production rules are useful implementation constraints, not sacred architecture. Keep a rule when it protects the north star; replace it when a better mechanism preserves correctness with more capability.

## 2. Four planes, not one monolithic agent

```text
                         CHITRAGUPTA

 ┌──────────────────── CONTROL PLANE ────────────────────┐
 │ claim -> investigate -> normalize -> independent      │
 │ frozen review -> deterministic publish/rework         │
 │                                                       │
 │ owns WIP, idempotency, review cycles, workflow state  │
 └──────────────────────────┬────────────────────────────┘
                            │
 ┌──────────────────── EVIDENCE PLANE ───────────────────┐
 │ xstudio_l2 typed reads                                │
 │ schema/object discovery                               │
 │ run ledger + SQL action history                       │
 │ xstudio-l2-identity binds current run/ticket          │
 └──────────────────────────┬────────────────────────────┘
                            │
 ┌──────────────── EXPERIENCE / LEARNING PLANE ──────────┐
 │ sessions -> outcome cases -> candidate lessons        │
 │ Git/facts/governed solutions -> zvec hybrid retrieval │
 │ historical replay + retrieval measurement             │
 │ repeated human actions -> capability-design backlog   │
 └──────────────────────────┬────────────────────────────┘
                            │
 ┌───────────────────── ACTION PLANE ────────────────────┐
 │ typed capability registry                             │
 │ governed candidate -> shadow registry workflow        │
 │ validated recommendation/shadow plans                 │
 │ future supervised/autonomous deterministic executor   │
 │ append-only action receipts + verified postconditions │
 └───────────────────────────────────────────────────────┘
```

The model reasons. Deterministic code owns identity, lifecycle transitions, trust promotion, action contracts and irreversible side-effect boundaries.

## 3. Storage is not authority

The core epistemic rule is:

```text
recording experience != believing experience
retrieving experience != proving a current ticket
review approval != universal truth
reasoning about an action != permission to execute it
execution returned != corrective action verified
```

### Session recording is ON

Every completed investigator/reviewer turn is valuable experience:

- successful diagnostic paths;
- dead ends and repeated failures;
- reviewer corrections;
- hallucinated hypotheses;
- tool-call ergonomics problems;
- token/context waste patterns;
- model-specific behavior;
- operator corrections;
- evidence-selection strategies.

The learning plugin records completed turns as redacted Markdown with:

```text
trust: unverified_episodic
profile / model / session
Kanban task when resolvable
run_id / ticket_id / stage / review_cycle when resolvable
user text
assistant text
```

One file per turn avoids multi-process append contention.

### Generic automatic prefetch is OFF

A relevance engine answers "what text is similar?" It does not answer "what is true?"

If an investigator once says:

```text
"database access is unavailable"
```

and the reviewer later proves that statement false, the session should absolutely be preserved. It is excellent failure data. It should **not** be injected into a future ticket merely because the new prompt sounds similar.

Therefore the normal path is:

```text
choose retrieval scope
-> retrieve candidates
-> expose trust/provenance
-> reason about applicability
-> verify ticket-specific claims live
```

A future automatic context builder may become stage-aware and source-aware, but it must never degrade into generic top-k injection from mixed memory.

## 4. Shared learning vault

Default:

```text
~/.hermes/l2-learning/
```

Current structure:

```text
sessions/                    raw redacted L2 turns
cases/
  approved/                  review approved + publisher postconditions observed
  rejected/                  reviewer-rejected frozen proposals
  reopened/                  published RESOLUTION later leaves terminal state
facts/                       explicitly promoted operational lessons
candidates/                  unverified lesson candidates
knowledge/                   disposable mirror of Git + deployable skills
solutions/
  approved/                  governed hash-pinned reusable SQL Solution exports
  solution_export_manifest.json
actions/
  plans/                     durable non-executing action plans
  candidates/                repeated human-action capability design backlog
  receipts/                  future append-only action execution outcomes
eval/                        runtime-generated historical retrieval replay sets
archive/
  candidates/                promoted/rejected lesson provenance
  solutions/                 de-approved or content-drifted managed exports
.zvec-grep/                  disposable hybrid index
```

The zvec index is not a source of truth. The vault contains multiple authority classes; directory and metadata semantics matter.

## 5. Explicit retrieval and trust scopes

`l2_recall` exposes deliberate source classes:

| Scope | Meaning | Authority |
|---|---|---|
| `trusted` | Git reference + promoted facts + approved reusable solutions | Governed prior guidance; still not ticket proof |
| `knowledge` | Git/skill mirror | Canonical documented behavior |
| `facts` | promoted operational lessons | Reviewed heuristic |
| `solutions` | governed reusable solutions | Approved reusable guidance |
| `approved_cases` | historical proposal passed review + publisher postconditions | Strong historical analogy |
| `rejected_cases` | reviewer-rejected proposal | Negative/counterexample signal |
| `reopened_cases` | prior resolution later regressed/reopened | Regression signal |
| `cases` | all outcome-labelled historical cases | Mixed historical evidence |
| `sessions` | raw model/user history | Unverified episodic |
| `candidates` | proposed lessons | Unverified candidate |
| `all` | mixed corpus | Explicitly mixed/untrusted |

`trusted` deliberately excludes historical cases. Even a successful old incident is not automatically a reusable rule.

## 6. Outcome-conditioned learning

Raw sessions preserve experience; lifecycle outcomes add stronger labels.

`sync_l2_outcomes.py` materializes:

```text
reviewer blocked
    -> cases/rejected

reviewer done + deterministic publisher postconditions succeed
    -> cases/approved

published RESOLUTION later leaves recorded terminal ticket status
    -> cases/reopened
```

This turns the deterministic Helpdesk itself into a source of labels.

The outcome sidecar is independent of lifecycle correctness. Learning failure must never stop a ticket from reconciling, reviewing or publishing.

### Conservative automatic lesson mining

`mine_l2_learning_candidates.py` converts high-value outcomes into **unverified** candidates:

- reviewer rejection -> failure-pattern candidate;
- reopened resolution -> regression-pattern candidate;
- same lexically normalized approved root cause on at least two distinct tickets -> repeated-root-cause candidate.

The miner is intentionally conservative. It does not use an LLM to decide semantic equivalence in the background and it never promotes its own output.

### Central learning cycle

`l2_learning_cycle.py` is the one sidecar coordinator:

```text
sync outcomes
-> mine lesson candidates
-> mine action-capability candidates
```

`ticket_scout.py` calls this single boundary best-effort after deterministic reconciliation. This prevents learning features from becoming a ponytail of independent lifecycle-like schedulers.

## 7. From repeated human work to an action-capability backlog

A system that eventually solves XBatch issues should notice when humans repeatedly perform the same reviewed corrective action.

`mine_l2_action_capability_candidates.py` looks only at **approved** historical `NEEDS_HUMAN_ACTION` cases. When the same normalized corrective action occurs on at least two distinct tickets it creates/updates:

```text
actions/candidates/<id>.json
```

with:

```text
trust: unverified_capability_candidate
status: needs_executor_design
source historical cases
source ticket/run count
representative human action
unclassified risk
unknown parameter schema
unknown execution binding
empty precondition/verification/rollback design fields
```

This is a development/control-plane backlog, not an executable capability. It answers:

> Which human actions are repeated enough that automating them would materially improve L2?

It deliberately does **not** invent a stored procedure signature, API endpoint, risk level or parameter contract.

### Capability-candidate governance workflow

`l2_action_capability_curator.py` turns a real backlog item into a reviewed design without collapsing discovery into permission:

```text
needs_executor_design
      |
      v
researching_executor
      |
      v
contract_drafted
      |
      v
shadow_ready
      |
      v
registry_entry
```

A candidate may also be explicitly rejected. Every governance transition requires reviewer/operator identity plus evidence.

Before `shadow_ready`, the curator requires a concrete supported future execution target and non-empty:

- preconditions;
- idempotency contract;
- verification/postconditions;
- required evidence;
- rollback/compensation contract;
- approval policy.

The draft is structurally validated against `deploy/xstudio_action_capabilities.json`. Promotion writes the capability at `mode=shadow` only and **never raises the registry's `global_mode`**. With the current `global_mode=observe`, a newly registered shadow capability is still inactive for planning/execution until policy is deliberately promoted.

This separation prevents "we discovered a repeated fix" from silently becoming "the model may now execute it."

## 8. Harness-owned run/ticket identity

Transport ownership was not enough. Evidence must also be attached to the correct incident.

`xstudio-l2-identity` is a cross-cutting `pre_tool_call` guard. Hermes supports modifying tool arguments before dispatch, so the guard resolves the actual Kanban card and shallow-merges authoritative identifiers into sensitive calls.

It binds:

```text
xstudio_l2:
  select/query/read_procedure/get_run_actions/save_ledger -> current run_id
  get_ticket_context                                      -> current ticket_id

l2_action:
  plan/plans                                               -> current run_id + ticket_id
  validate_plan                                            -> rejects cross-run/cross-ticket plan
```

Conflicting model-supplied identifiers are blocked. Pure schema discovery remains independent because discovering an object does not attach evidence to a different ticket.

The long-term rule is:

```text
model chooses investigation/action semantics
harness chooses identity and side-effect authority
```

## 9. Historical replay and measurable improvement

A system that "keeps getting better" needs regression tests built from its own history.

There are two retrieval gates:

1. `l2_learning_eval_cases.jsonl` — static policy/architecture smoke cases.
2. `build_l2_historical_retrieval_eval.py` — runtime-derived real-history replay cases.

The historical builder correlates:

```text
earliest recorded user/task text for a run
        -> expected outcome-labelled historical case for that run
```

and emits JSONL consumed by the deterministic retrieval benchmark.

Metrics already available include:

```text
hit rate
p50/p95 latency
retrieved context characters
explicit forbidden-result checks
```

The evaluation plane should grow toward:

```text
resolution correctness
review reject rate
reopen rate
false-resolution rate
L3/human-action precision
tool calls per ticket
input/output tokens per ticket
wall time
context-overflow rate
retrieval hit@k / MRR
false-positive retrieval@1
abstention correctness
live-evidence coverage
shadow-action agreement with human action
supervised-action success/rollback rate
```

Adversarial cases matter more than easy recall: same symptom, different cause; same historic fix, now invalid; same identifier shape, different entity.

## 10. mem0 remains narrow

This branch does not collapse all memory into zvec.

```text
mem0
  = compact high-value operational behavior

zvec learning vault
  = high-recall experience, cases, replay and hybrid retrieval

Git / governed SQL Solution export
  = reusable knowledge with explicit provenance/trust gates

live SQL
  = current-ticket truth

run ledger / trace
  = incident execution evidence
```

These stores have different trust/lifetime semantics. Component count is less important than preserving epistemic meaning.

## 11. Governed SQL Solution export

The SQL KB already has `dbo.Hermes_Solution_Article_Mst_Tbl`, but an active row is not automatically trusted retrieval material.

`sync_l2_approved_solutions.py` and `deploy/solution_export_policy.json` add an explicit governance bridge:

```text
live active SQL Solution
       |
       | operator reviews semantics
       v
solution_export_policy.json
  solution_id
  semantic content_sha256
  approved_by / approved_at
  review_evidence
       |
       | exporter re-reads live SQL
       | hash must match exactly
       v
solutions/approved/<id>.md
  trust: governed_reusable_solution
       |
       v
trusted zvec scope
```

The semantic hash covers reusable guidance fields and deliberately excludes mutable operational counters such as `UsageCount`. A usage counter change therefore does not demand re-approval, while title/problem/root-cause/resolution/route/tags/view content drift does.

If governed semantic content changes after approval, export fails closed and a previously managed trusted mirror is archived until the new version is reviewed. Removing policy approval also archives only the managed vault copy; it does not mutate the SQL article.

`--preview-live` exposes active Solution IDs and semantic hashes for review without trusting or exporting them.

## 12. Action plane and autonomy ladder

Read-only diagnosis is A0, not the destination.

```text
A0 OBSERVE
   read-only diagnosis
        ↓
A1 RECOMMEND
   known action; human performs it
        ↓
A2 SHADOW
   registered capability + parameters + evidence validated;
   durable plan generated; no execution
        ↓
A3 SUPERVISED EXECUTE
   deterministic executor revalidates plan;
   explicit human approval; execute + verify
        ↓
A4 AUTONOMOUS LOW-RISK
   proven allowlisted capability executes automatically
        ↓
A5 BROADER AUTONOMY
   progressively larger domain/risk after measured promotion
```

Autonomy is granted per capability, never as global raw SQL permission.

## 13. Current action registry and planner

`deploy/xstudio_action_capabilities.json` is the machine-readable capability registry.

A capability contract requires:

```text
id
description
risk
mode
parameter_schema
preconditions
execution
idempotency
verification
rollback
required_evidence
approval_policy
```

`validate_action_capabilities.py` enforces increasingly strict requirements as a capability moves toward supervised/autonomous execution. Critical-risk capabilities cannot be autonomous under the current policy.

`xstudio-l2-actions` currently exposes:

```text
list
describe
plan
plans
validate_plan
```

There is deliberately no `execute` operation.

A plan contains capability/registry hashes, validated parameters, declared evidence, current run/ticket identity, required preconditions, verification/rollback contract and:

```text
execution_authorized: false
execution_tool_available: false
```

This lets Chitragupta begin measuring whether it would choose the correct corrective action before we allow it to execute anything.

## 14. Action receipts are defined before the first executor

`deploy/xstudio_action_receipt.schema.json` and `xstudio_action_receipts.py` define the audit/result contract now, before any model-visible executor exists.

```text
planned -> approved -> executed -> verified
    \         \          \
     +-> failed <---------+
           |
           v
      compensated
```

Important semantics:

- the receipt is append-only history;
- one deterministic receipt exists per plan/action attempt;
- a `planned` receipt records intent, not authority;
- an action is not successful merely because an executor returned without error;
- `verified` requires deterministic postconditions to have been checked;
- `compensated` requires rollback/compensation state to have been verified;
- a verified terminal receipt cannot later be rewritten into failure;
- receipt hashes pin the plan, capability and registry versions used for that attempt.

This prevents a future executor from being added first and audit/outcome learning bolted on later.

Action receipts will eventually become high-value learning/evaluation data: which plans were approved, which actions executed, which postconditions passed, which failed, which required compensation, and whether autonomy should be promoted or demoted.

## 15. What must be true before the first real executor

Do not promote an action because its name sounds safe.

For the first real XBatch capability we need to verify:

1. the actual supported SP/API/service operation;
2. exact current parameter signature;
3. real business preconditions;
4. an idempotency strategy;
5. required live evidence;
6. deterministic postcondition reads;
7. rollback or compensation behavior;
8. risk classification;
9. approval policy;
10. replay/shadow evidence showing that the planner selects it correctly.

The capability backlog tells us *what is worth automating*. Live discovery and source inspection tell us *how to automate it safely*.

A synthetic test capability name is never evidence that the corresponding XBatch operation exists. The first real capability must come from a real runtime `actions/candidates/**` item plus verified live/source implementation evidence.

## 16. Knowledge promotion is outcome-gated

`l2_lesson` writes only to `candidates/**`. Automatic miners also write only untrusted candidates.

`l2_learning_curator.py` is the separate lesson-promotion boundary. `sync_l2_approved_solutions.py` is the separate SQL Solution trust boundary. `l2_action_capability_curator.py` is the separate action-capability design/promotion boundary.

These are deliberately different because they promote different things:

```text
lesson candidate -> reviewed heuristic
SQL Solution      -> governed reusable retrieval article
action candidate  -> reviewed typed shadow capability contract
```

The rule is:

```text
model says it learned something
        !=
system learned something

repeated human action observed
        !=
action is safe to automate
```

## 17. Implemented branch components

```text
Model_Bench/xstudio_l2_identity_plugin/
    harness-owned run/ticket binding for sensitive tools

Model_Bench/xstudio_l2_learning_plugin/
    session recording + explicit trust-scoped zvec recall + candidate proposal

Model_Bench/sync_l2_outcomes.py
    approved/rejected/reopened historical case labels

Model_Bench/sync_l2_approved_solutions.py
    explicit semantic-hash-governed SQL Solution -> trusted vault export

deploy/solution_export_policy.json
    reviewed Solution IDs/content hashes and provenance

Model_Bench/mine_l2_learning_candidates.py
    conservative outcome -> lesson candidate mining

Model_Bench/mine_l2_action_capability_candidates.py
    repeated approved human actions -> capability design backlog

Model_Bench/l2_action_capability_curator.py
    governed candidate research -> contract -> shadow-ready -> registry workflow

Model_Bench/l2_learning_cycle.py
    one lifecycle-independent learning sidecar coordinator

Model_Bench/build_l2_historical_retrieval_eval.py
    real session/outcome replay-set generation

Model_Bench/benchmark_l2_learning_retrieval.py
    deterministic retrieval measurement

Model_Bench/xstudio_l2_actions_plugin/
    non-executing registered action planner

Model_Bench/validate_action_capabilities.py
    structural autonomy/promotion policy gate

deploy/xstudio_action_receipt.schema.json
Model_Bench/xstudio_action_receipts.py
    append-only future execution-outcome contract
```

## 18. Next major increments

The earlier structural continuation points are now implemented: adaptive deploy drift validation, expanded vault layout checks, branch operating-contract alignment, capability-candidate governance, governed Solution export, and action receipt semantics.

The branch should now move in this order:

1. **Populate governed Solution approvals deliberately.** Use `sync_l2_approved_solutions.py --preview-live`, review high-value active SQL articles, and pin only those that deserve trusted retrieval.
2. **Triage the real capability backlog.** Run the learning cycle against real history, rank `actions/candidates/**` by repeated independent tickets, and choose a real repeated action for executor research. Do not assign low risk before inspecting the actual side effect.
3. **Research the first real candidate.** Verify the supported SP/API/service path, parameter signature, preconditions, idempotency, postconditions, rollback/compensation and approval needs from live/schema/source evidence.
4. **Create the first real shadow registry entry.** Use the capability curator to move that candidate through `researching_executor -> contract_drafted -> shadow_ready -> registry_entry`. Keep registry `global_mode=observe` until deliberate shadow activation is justified.
5. **Shadow agreement metrics.** Compare generated capability/parameters with what the human actually performs and whether the incident resolves.
6. **Candidate promotion evidence.** Require repeated independent support, no contradictory/reopen signal, and replay performance before promoting operational lessons.
7. **Supervised executor.** Separate from the planner; revalidate identity, capability hash, current evidence, preconditions, approval, idempotency and postconditions immediately before mutation, and write action receipts throughout.
8. **Action-outcome evaluation.** Use verified/failed/compensated receipts to promote or demote capability autonomy.
9. **Stage-aware context assembly.** If automatic retrieval is introduced, make it deterministic by stage/source/trust budget rather than generic memory prefetch.

The direction is no longer "better memory." It is a closed improvement loop:

```text
observe
-> reason
-> independently review
-> act only through typed deterministic capability
-> verify outcome
-> record experience
-> label outcome
-> mine lessons and repeated human work
-> replay/evaluate
-> promote what earns trust
-> expand safe autonomous capability
```
