# Claude Entry Point — Chitragupta

Read `AGENTS.md` first. It is the stable operational contract for this repo.

Do **not** duplicate the lifecycle architecture here. The authoritative sources are:

- `AGENTS.md` — current agent operating contract.
- `Knowledge/L2_PIPELINE_STATE_MACHINE.md` — normative ticket lifecycle.
- `Model_Bench/l2_pipeline_runtime.py` — actual lifecycle implementation.
- `deploy/helpdesk_workflow_binding.json` — live Helpdesk status binding.
- `Knowledge/KB_IMPLEMENTATION_PLAN.md` — KB architecture/implementation plan.
- `README.md` — human-facing current architecture/deployment overview.

## Current deployment facts that matter

- Branch: `main` only.
- Live lifecycle: centralized Kanban state machine in `Model_Bench/l2_pipeline_runtime.py`.
- Global SQL WIP: `1` active run.
- Priorities: review `30`, rework `20`, new investigation `10`.
- Reviewer creation is deferred until investigator/rework completion is normalized and reviewable.
- Reviewer receives frozen `proposal_json`; deterministic publisher publishes that same proposal.
- Rework cycles use `review_cycle`, not SQL `AttemptNo`; max cycles = 3.
- `ticket_scout.py` is the 2-minute mutating reconciliation/claim backstop.
- Separate 5-minute publish-safety-net and repair cron jobs were deliberately removed; do not recreate them.
- Reviewer completion audit is read-only.
- Live-verified Helpdesk binding: eligible `Enter`, resolved `Closed`, waiting-user AskStatus `Ask`; L3/human-action ticket statuses remain unbound until proven live.
- A `RESOLUTION` does not automatically create a KB article.
- The generated SQL full-install bundle includes the `25` and `55` hardening sources.
- `.gitattributes` forces LF on `*.sh` and `*.sql` because Windows CRLF conversion broke WSL scripts and install reproducibility.

## Before changing the ticket pipeline

Read:

```text
AGENTS.md
Knowledge/L2_PIPELINE_STATE_MACHINE.md
Model_Bench/l2_pipeline_runtime.py
Model_Bench/test_l2_pipeline_runtime.py
```

Preserve the core invariants unless the user explicitly asks to redesign them.

## Validation

Validate locally against the real environment; do not use GitHub Actions as proof of live correctness.

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
python3 -m unittest -v Model_Bench/test_l2_pipeline_runtime.py
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

## Historical material

`Plans/` and `Agent_Comms/` contain prior architectures, model names, experiments, and incident notes. They are not current instructions. In particular, do not revive:

- poll-into-long-lived-chat architecture;
- separate `l2-review` board;
- `kanban_forward_bridge.py`;
- old model-based role names;
- backlog-cap-3 claiming;
- SQL `AttemptNo` as the review/rework counter;
- separate publisher/reject/repair lifecycle authorities.

If a historical file conflicts with `AGENTS.md` or the state-machine contract, treat the historical file as provenance only.