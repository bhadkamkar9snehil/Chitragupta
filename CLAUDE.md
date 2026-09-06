# Claude Entry Point — Chitragupta Adaptive L2 Branch

You are on the deliberate experimental branch:

```text
development/autonomous-l2-learning-runtime
```

The product north star for this branch is the highest-level contract:

> Build an autonomous, AI-driven, deterministic L2 Helpdesk that gets measurably better from experience and progressively earns the ability to solve XBatch issues itself.

Read `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` first, then `AGENTS.md`. `AGENTS.md` remains the current production-safety/lifecycle baseline, but any old instruction that says “main only”, fixes Qdrant/mem0 as the only possible learning architecture, or treats permanent read-only diagnosis as the end state is **not** a design constraint on this branch. Preserve deterministic safety properties unless a better implementation replaces them explicitly.

## Current authoritative sources

- `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` — branch north star, experience/retrieval plane, learning lifecycle, evaluation plane, and action-autonomy ladder.
- `AGENTS.md` — current production lifecycle/safety baseline.
- `Knowledge/L2_PIPELINE_STATE_MACHINE.md` — current deterministic ticket lifecycle.
- `Model_Bench/l2_pipeline_runtime.py` — actual lifecycle implementation.
- `deploy/helpdesk_workflow_binding.json` — observed Helpdesk workflow binding.
- `deploy/xstudio_action_capabilities.json` — machine-readable future corrective-action registry; initially observe-only/empty.
- `Knowledge/manifest.json` / `Knowledge/task-router.md` — current routing.
- `Knowledge/KB_IMPLEMENTATION_PLAN.md` — still authoritative for knowledge governance concepts (provenance, lifecycle, applicability, abstention), but its choice of retrieval substrate is no longer sacred; zvec/Qdrant/other indexing should be decided empirically.

## What this branch adds

The existing deterministic lifecycle remains the control plane:

```text
claim -> investigate -> normalize -> frozen independent review -> publish/rework
```

The branch adds a separate **Experience & Retrieval Plane**:

```text
~/.hermes/l2-learning/
  sessions/              redacted, unverified episodic turns
  facts/                 reviewed operational lessons
  candidates/            unverified model-proposed lessons
  knowledge/             mirrored Git/skill reference
  solutions/approved/    future governed Solution export
```

`zvec-grep` provides local BM25 + vector hybrid search over that corpus.

Important distinction:

```text
recording experience != believing it
retrieving experience != proving the current ticket
reasoning about a fix != permission to execute it
```

### Sessions are deliberately recorded

Every completed L2 turn is useful experience for replay, failure mining, reviewer-correction analysis, token/tool optimization, and learning. `xstudio-l2-learning` records completed turns through `post_llm_call` as redacted `unverified_episodic` Markdown.

### Generic automatic prefetch is deliberately disabled

Do not add a zvec `pre_llm_call`/turn-start top-k injection just because it is convenient. Old sessions include incorrect investigator hypotheses, reviewer-rejected claims, stale workflow state, and model hallucinations. Generic relevance-based injection gives that text epistemic privilege before the worker classifies provenance.

Use explicit `l2_recall` scopes instead. `scope=trusted` is the normal prior-knowledge path; `scope=sessions` is explicitly forensic/unverified and still requires live verification.

`l2_lesson` may write only unverified candidates. Promotion is separate and deterministic via `Model_Bench/l2_learning_curator.py`.

mem0 remains available for compact durable operational memory; the zvec learning plane does not replace it merely to reduce component count.

## Future XBatch solving

Current investigator/reviewer SQL remains read-only. That is the present capability state, not the final product boundary.

Do **not** solve future autonomy by giving a model arbitrary UPDATE/EXEC access. Build typed corrective capabilities with:

```text
parameter schema
preconditions
supported execution path
idempotency
required evidence
postcondition verification
rollback/compensation
risk class
approval policy
```

Progress capability-by-capability through:

```text
A0 observe
A1 recommend
A2 shadow-plan
A3 supervised execute
A4 autonomous low-risk execute
A5 broader autonomous remediation
```

The registry is `deploy/xstudio_action_capabilities.json`. A capability earns autonomy from replay/live evidence and observed outcomes, not from prompt confidence.

## Existing production facts still important

- Global SQL WIP currently `1` because of local inference constraints.
- Priorities: review `30`, rework `20`, new investigation `10`.
- Reviewer creation is deferred until normalized/reviewable completion.
- Reviewer receives frozen `proposal_json`; publisher publishes that exact proposal.
- `review_cycle` controls bounded rework, not SQL `AttemptNo`.
- `ticket_scout.py` remains the reconcile-first claim backstop.
- Database evidence uses typed `xstudio_l2`; model-driven Python/pyodbc/sqlcmd/package-install transport stays blocked.
- Helpdesk workflow states are harness-bound from observed values, not invented by the model.
- A resolution does not automatically become a trusted KB article.
- GitHub Actions are not the live validation authority.

These are implementation facts, not immutable product dogma. Change them when a better design demonstrably improves the north star without losing correctness.

## Validation

Run locally on the real Windows/WSL/Hermes/SQL/LM Studio machine:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
bash Model_Bench/validate_l2_pipeline_local.sh
python3 Model_Bench/test_xstudio_l2_learning_plugin.py
python3 Model_Bench/validate_action_capabilities.py
```

For the first natural live ticket on this branch, verify all three planes independently:

1. control plane still progresses correctly;
2. evidence still goes through `xstudio_l2`;
3. the learning plane records a redacted session, exposes `l2_recall`/`l2_lesson`, and injects no automatic zvec-memory block.

Do not manufacture a production ticket or raw-poll around the lifecycle gate merely to test it.

## Historical material

`Plans/` and `Agent_Comms/` remain provenance. Do not revive dead duplicate orchestration merely because it appears in history. Conversely, do not reject a better future architecture just because it differs from an old rule: the branch north star is the governing design criterion.
