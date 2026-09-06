# Chitragupta L2 Architecture

Status: current branch contract

## Product boundary

Hermes is the agent harness. Chitragupta is an XStudio/Helpdesk domain application running on that harness.

Hermes owns:
- model/session lifecycle;
- Kanban worker dispatch;
- gateway/scheduling;
- plugin/tool loading;
- durable conversation state.

Chitragupta owns only:
- deterministic Helpdesk claim/review/rework/publication semantics;
- the typed XStudio evidence boundary;
- reviewed reusable learning and Solution governance;
- trust-scoped GBrain indexing/retrieval.

Do not add a second agent harness around Hermes.

## Runtime

```text
Helpdesk SQL claim
      |
      v
investigator Kanban card
      |
      v
normalized frozen proposal
      |
      v
reviewer Kanban card
   /       \
approve    reject
  |          |
publish    rework -> review (bounded)
```

`Model_Bench/l2_pipeline_runtime.py` owns those deterministic transitions. The model never chooses lifecycle state directly.

## Model-facing tools

There is one Chitragupta Hermes plugin: `xstudio-l2-tools`.

It registers only:

- `xstudio_l2` — typed XStudio/Helpdesk reads, schema discovery, ticket/run evidence and investigation-ledger writes;
- `l2_recall` — read-only GBrain retrieval.

Identity-sensitive `xstudio_l2` operations are bound to the current Kanban card. Arbitrary SQL is read-only and stored-procedure execution is allowlisted in the Windows bridge.

The Windows bridge exists because pyodbc/SQL access is on Windows while Hermes runs in WSL. It is a real transport boundary, not a second agent layer.

## Evidence and trust

Authority order:

1. **Current incident truth:** live XStudio/Helpdesk evidence through `xstudio_l2`.
2. **Reusable governed reference:** committed `Knowledge/`, explicitly reviewed facts, hash-approved Solution exports.
3. **Historical experience:** approved/rejected/reopened cases. Useful as analogy or counterexample, never current-ticket proof.
4. **Unreviewed candidates:** operator review queue only. Workers cannot retrieve or promote them.

Small L2 workers do not use Mem0, built-in Hermes memory writes, raw session recall or model-authored durable lessons.

## GBrain

GBrain is disposable derivative retrieval state under an isolated `GBRAIN_HOME`.

Model-facing source topology:

| Source | Authority |
|---|---|
| `l2-knowledge` | committed repository `Knowledge/` directly |
| `l2-facts` | explicitly promoted reviewed facts |
| `l2-solutions` | governed Solution exports |
| `l2-approved-cases` | prior reviewed/published successes |
| `l2-rejected-cases` | reviewer counterexamples |
| `l2-reopened-cases` | regression/reopen signals |

All sources are non-federated and every lookup names its source set explicitly. Chitragupta calls `gbrain search`; it does not expose GBrain synthesis/query or a raw GBrain MCP surface to the workers.

`trusted` means only knowledge + facts + governed solutions. Historical cases are deliberately excluded.

Canonical Knowledge is indexed directly from the Git checkout. The learning vault uses local Git only for dynamic facts/solutions/cases because GBrain path sources require committed state.

## Learning

One best-effort sidecar cycle runs after lifecycle work:

```text
reviewed/published/reopened outcomes
        |
        v
historical cases
        |
        v
conservative unverified candidates
        |
        v
GBrain sync
```

Learning failure never owns or blocks ticket lifecycle correctness.

`mine_l2_learning_candidates.py` may create only `unverified_candidate` artifacts from reviewed outcomes. `l2_learning_curator.py` is an operator control-plane tool: explicit human review is required to promote a candidate to the trusted facts lane.

## Governed Solutions

An active Helpdesk Solution row is not automatically trusted reusable knowledge.

`sync_l2_approved_solutions.py` exports a Solution only when its current semantic hash matches `deploy/solution_export_policy.json`. Drift fails closed and requires renewed review.

## Mutation boundary

The current autonomous L2 system diagnoses and recommends. There is no Chitragupta action-capability registry or model-facing execution planner in the current architecture.

When a required production/configuration change is known but not available through the approved interface, the investigator returns `NEEDS_HUMAN_ACTION`. When the cause/safe path is unresolved beyond L2, it returns `L3_ESCALATION`.

Future execution should be designed only when a real corrective operation is ready to implement, with deterministic authorization, idempotency, verification and rollback. Do not prebuild speculative execution frameworks.

## Files that justify their existence

| File | Reason |
|---|---|
| `l2_pipeline_runtime.py` | deterministic Helpdesk/Kanban state machine |
| `ticket_scout.py` | one scheduled entrypoint combining lifecycle scout + best-effort learning |
| `xstudio_l2_tools_plugin/` | single Hermes domain plugin |
| `xstudio_l2_tool_bridge.py` | WSL-to-Windows/pyodbc safety boundary |
| `l2_gbrain.py` | isolated source/scope policy and read-only adapter |
| `sync_l2_gbrain.py` | derivative GBrain source convergence |
| `sync_l2_outcomes.py` | materialize reviewed lifecycle outcomes as historical cases |
| `mine_l2_learning_candidates.py` | conservative candidate generation from reviewed outcomes |
| `l2_learning_curator.py` | explicit operator promotion/rejection boundary |
| `l2_learning_cycle.py` | one best-effort learning convergence call |
| `sync_l2_approved_solutions.py` | fail-closed reusable Solution export |
| `solution_export_policy.json` | reviewed Solution semantic hashes |

Anything added around Hermes should be held to the same test: it must represent a real domain boundary or deterministic business rule that Hermes does not already provide.
