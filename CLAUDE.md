# Claude Entry Point — Chitragupta

Read `AGENTS.md` first, then `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` when changing architecture.

## Current system

Hermes owns model/session lifecycle, Kanban dispatch, gateway scheduling and plugin loading.

Chitragupta owns only:

- deterministic Helpdesk claim/review/rework/publication semantics;
- the typed XStudio evidence boundary;
- governed reusable learning and Solution export;
- isolated trust-scoped GBrain retrieval.

`Model_Bench/l2_pipeline_runtime.py` is the lifecycle authority.

The only Chitragupta Hermes plugin is `xstudio-l2-tools`, exposing `xstudio_l2` and read-only `l2_recall`.

## Preserve these invariants

- One lifecycle mutation authority.
- Global SQL WIP is 1.
- Review 30 > rework 20 > new investigation 10.
- Reviewer creation happens only after a reviewable frozen proposal exists.
- Reviewer and publisher operate on the same frozen proposal.
- Current-ticket claims require live `xstudio_l2` evidence.
- Model-built database transport, arbitrary SQL writes/DDL/EXEC and package-install fallbacks remain unavailable.
- Run/ticket identity is harness-bound.
- `trusted` GBrain recall contains only canonical Knowledge, reviewed facts and governed Solutions.
- Historical approved/rejected/reopened cases are analogies/counterexamples, not current proof.
- Workers do not promote their own durable lessons.
- Learning/GBrain convergence is best-effort and cannot own ticket correctness.
- Helpdesk Solution rows enter trusted retrieval only through semantic-hash approval policy.
- Do not add speculative action/execution frameworks without a real supported corrective operation and measured need.

## Repository discipline

Delete obsolete paths instead of documenting them forever. Do not retain benchmark harnesses, generated duplicate indexes, one-time migration/repair scripts, alternate policy registries, duplicate profile variants, or unpinned copies of Knowledge.

Any surviving subsystem should have an active caller and one clear owner.

## Validation

Run:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Update deployment and validation whenever runtime components are added, removed, or consolidated.
