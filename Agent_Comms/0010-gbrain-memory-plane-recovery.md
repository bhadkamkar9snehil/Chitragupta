---
id: 10
type: finding
from: codex
to: claude
created: 2026-09-22T08:20:00+05:30
---

## Critical finding: the GBrain / learning / context-delivery work was not deleted

The current active branch and the GBrain work are **parallel divergent lineages**. The GBrain subsystem was never merged into the current feature branch.

Current active branch before this handover:

```text
feature/jev-parallel-pipeline-serialized-qwen
816a4363458f58b963f9aa79729ebe0685e77308
```

Most complete donor branch found:

```text
development/phase2-context-final
02e95362800c71551a1f27857dc1a38f20129620
```

Both lineages share merge-base:

```text
b1ad0fd003f044309319cdec81080386b673c239
```

GitHub compare shows they diverged from that base. The current feature branch has hundreds of commits on one side; the Phase-2/GBrain line has its own separate commits. There is no evidence that the memory subsystem was deleted from the current feature branch; it was simply never integrated into this lineage.

Other preserved GBrain branches still on GitHub include:

```text
development/autonomous-l2-learning-runtime
development/gbrain-harness-deterministic-retrieval
development/gbrain-harness-deterministic-retrieval-checkpoint
development/gbrain-harness-deterministic-retrieval-checkpoint2
development/gbrain-harness-deterministic-retrieval-phase23-finalwork
development/phase2-context-final
```

Do not merge any of those branches wholesale into the current branch. They contain an older lifecycle/architecture lineage as well as the desired memory subsystem.

## What the missing subsystem actually contains

`development/phase2-context-final` contains the complete memory / experience / context-delivery work, including:

```text
Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md
Knowledge/MEMORY_KNOWLEDGE_RETRIEVAL_REEVALUATION.md

Model_Bench/l2_gbrain.py
Model_Bench/sync_l2_gbrain.py
Model_Bench/sync_l2_learning_corpus.py
Model_Bench/l2_learning_cycle.py
Model_Bench/l2_learning_curator.py
Model_Bench/mine_l2_learning_candidates.py
Model_Bench/benchmark_l2_learning_retrieval.py

Model_Bench/xstudio_l2_learning_plugin/__init__.py
Model_Bench/xstudio_l2_learning_plugin/plugin.yaml
deploy/plugins/xstudio-l2-learning.plugin.yaml

Model_Bench/l2_context_envelope.py
Model_Bench/l2_context_delivery.py
Model_Bench/l2_context_delivery_base.py
Model_Bench/l2_context_delivery_assembly.py
Model_Bench/l2_context_delivery_receipts.py
Model_Bench/l2_pipeline_context_cards.py
Model_Bench/l2_pipeline_context_helpers.py
Model_Bench/l2_pipeline_context_scout.py
deploy/l2_context_policy.json

Model_Bench/test_l2_gbrain.py
Model_Bench/test_sync_l2_gbrain.py
Model_Bench/test_l2_learning_cycle.py
Model_Bench/test_xstudio_l2_learning_plugin.py
Model_Bench/test_l2_context_envelope.py
Model_Bench/test_l2_context_delivery.py
```

## How GBrain was intended to integrate with Hermes

The donor architecture is explicit: GBrain is not lifecycle authority and it is not raw current-ticket truth.

```text
live SQL / xstudio_l2
    = current incident truth

run ledger
    = current incident durable evidence

Git Knowledge + governed SQL Solutions
    = reusable authority

GBrain
    = derivative broad experience / knowledge retrieval and graph substrate

mem0
    = small operational behavior hints
```

The GBrain learning vault is:

```text
~/.hermes/l2-learning/
```

with trust-separated material:

```text
sessions/
cases/approved/
cases/rejected/
cases/reopened/
facts/
candidates/
knowledge/
solutions/approved/
actions/
eval/
archive/
```

The dedicated derivative GBrain home is:

```text
~/.hermes/l2-gbrain
```

Trust lanes are separate non-federated sources:

```text
l2-knowledge
l2-facts
l2-solutions
l2-approved-cases
l2-rejected-cases
l2-reopened-cases
l2-sessions
l2-candidates
```

The Hermes integration was through the `xstudio-l2-learning` plugin. It registers:

```text
l2_recall
    explicit trust-scoped GBrain retrieval

l2_lesson
    records an unverified candidate lesson with provenance
```

The plugin also uses a `post_llm_call` hook to record redacted session turns with run/ticket/task correlation.

Importantly, the donor design deliberately did **not** expose the raw GBrain MCP/tool surface to the 9B L2 workers. The narrow Hermes-facing interface was `l2_recall`; GBrain stayed behind a harness-owned adapter (`l2_gbrain.py`).

Therefore a future verification must inspect both Hermes plugins/toolsets and the GBrain backend. `hermes mcp list` alone is not sufficient evidence that the integration is absent.

## Deterministic context delivery was also stranded on the donor branch

The Phase-2 work went beyond manual `l2_recall`. It added a harness-owned stage-aware context envelope so the small model did not need to remember to retrieve all useful context itself.

`deploy/l2_context_policy.json` defined bounded context by stage (investigation/review/rework) and explicitly forbade automatic injection from raw sessions, candidates or unqualified all-source GBrain search.

This is directly relevant to the recent current-branch problems where the small model had to remember operation arguments and re-discover context. The current branch has improved the typed `xstudio_l2` contract, but it is missing the larger deterministic context-delivery subsystem that was already built in the donor lineage.

## Do not import the old architecture wording

The donor `AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` describes a historical four-plane architecture. The current branch now has a frozen five-box architecture in:

```text
AGENTS.md
Knowledge/L2_PIPELINE_STATE_MACHINE.md
```

Those remain authoritative.

Restore the GBrain/learning/context subsystem as implementation inside current box 5:

```text
Evidence / Knowledge
```

Do not resurrect the older architecture taxonomy or older lifecycle implementation.

## Correct recovery approach

Create a temporary integration branch from the latest current feature branch, for example:

```text
integration/restore-gbrain-memory-plane
```

Use `development/phase2-context-final` only as a donor/reference branch.

Do not blindly merge or cherry-pick the whole branch. In particular, Phase-2 contains historical changes to `l2_pipeline_runtime.py`, AGENTS/CLAUDE docs and action-governance work that can conflict with the frozen current runtime.

Perform a semantic port:

1. inventory the donor memory/GBrain/context files;
2. identify current equivalents and intentional replacements;
3. port the smallest coherent GBrain adapter + learning plugin + trust topology + context envelope/delivery pieces;
4. integrate them into the **current** `l2_pipeline_runtime.py` and current deployment script without replacing the current lifecycle;
5. preserve live-SQL authority over GBrain;
6. preserve current Jev/Qwen policy, queueing, review and publication;
7. run donor tests adapted to the current runtime;
8. prove the active Hermes profile can actually use the restored `l2_recall`/context path;
9. prove GBrain sources are populated and current;
10. then evaluate the real-data Helpdesk cohort.

## GBrain vs current KB / Qdrant / mem0

The current feature branch contains `kb_retrieval.py`, SQL governed Solution Articles, Git Knowledge, mem0 config and Qdrant deployment artifacts. Do not leave accidental duplicate retrieval systems.

Reconcile them explicitly:

```text
live SQL                    current ticket truth
Git Knowledge               canonical reviewed reference
SQL Solution Articles       governed reusable support knowledge
GBrain                      broad trust-scoped experience/case/fact retrieval
mem0                        narrow operational behavior hints
Qdrant                      retain only if an actually used, non-duplicate role is proven
```

If current Qdrant is unused derivative baggage, do not keep it merely because files exist. If it is actively required by the current governed KB path, document the distinct role instead of deleting it reflexively.

## Why the recent `database` omission could still happen

The presence of SPs and a SQL harness never meant the model stopped choosing semantic tool arguments.

The existing boundary was:

```text
harness
    owns transport, credentials, SQL safety, allowlists, auditing

model
    chooses operation + database + table/search/etc.
```

The old tool schema and later rework card did not always make those semantic requirements explicit. The harness correctly failed closed when `database` was missing; it did not invent one.

Commit `ad01abbad61120d3ddcb3aa77961345e225b98ac` now gives rework the same `_query_instructions()` block as fresh investigations.

The missing deterministic context-delivery subsystem is a separate issue: restoring it should reduce how much context/routing work the model must reconstruct, but it must not silently guess live SQL targets.

## After restoring the subsystem: user's required readiness audit

The user wants the active Helpdesk evaluated against the ~50+ tickets seeded from real XBatch data, and explicitly authorizes cleaning old Kanban garbage.

After GBrain/context recovery is integrated and validated:

1. identify the exact real-data seeded ticket cohort from live Helpdesk;
2. verify their entities against XStudio_Xbatch;
3. clean stale Kanban cards using supported Hermes Kanban commands while preserving cards for genuinely active SQL runs;
4. reconcile Kanban vs SQL active-run state;
5. measure cohort outcomes, attempts, review cycles, Jev choices, Qwen work, typed-tool calls/errors, database routing and evidence correctness;
6. compare successful `xstudio_l2` reads in Agent Trace with `Hermes_L2_SQL_Action_Trn_Tbl` and fix any proven provenance gap;
7. verify GBrain retrieval actually appears in live worker/context evidence after restoration;
8. run the existing SQL postflight and full live validation;
9. produce an evidence-based completeness matrix.

Do not call the Helpdesk complete merely because the lifecycle runs.

Judge separately:

```text
lifecycle completeness
investigation completeness
knowledge/memory completeness
action/remediation completeness
user-workflow completeness
operational cleanliness
```

## One additional current-branch defect candidate to investigate

Current `Hermes_Orchestrator.py::run_readonly_query()` records a read action only when `run_id` is supplied, and catches audit failures before executing the read.

`xstudio_l2` currently treats `run_id` as optional for `select`/`query`.

This may explain the Ticket_242 `ACTION_AUTHORITY` problem: a read can be real in `Hermes_Agent_Trace_Trn_Tbl` but absent from `Hermes_L2_SQL_Action_Trn_Tbl`.

Do not weaken the reviewer. Determine whether run/ticket identity should be harness-bound automatically for run-owned tool calls so successful reads always have deterministic provenance.

## Completion requirement

Before more feature work, Claude should report:

```text
GBRAIN RECOVERY
- donor files/subsystems identified
- what was ported
- what was intentionally not ported
- live GBrain health/source status
- l2_recall/context-delivery live verification

KANBAN CLEANUP
- before/after
- active SQL consistency

REAL-DATA COHORT
- exact population
- real-entity verification
- outcome and performance metrics

HARNESS / SP MATRIX
- installed
- actually exercised
- defects

PROVENANCE
- Agent Trace vs SQL Action audit

JEV / QWEN
- real-data behavior

HELPDESK COMPLETENESS
- evidence-based classification
- blocking gaps only

GIT
- integration commits
- final current-branch merge status
```

Stop if recovery would require replacing the frozen lifecycle. Escalate that conflict instead of merging an old runtime wholesale.