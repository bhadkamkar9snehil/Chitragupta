# Claude Entry Point — Chitragupta

Read `AGENTS.md` first. It is the stable operational contract for this repo.

This file is a thin entry point by design: durable rules live in `AGENTS.md` first, and this file only digests them. Do **not** duplicate the lifecycle architecture here. The authoritative sources are:

- `AGENTS.md` — current agent operating contract.
- `Knowledge/L2_PIPELINE_STATE_MACHINE.md` — normative ticket lifecycle.
- `Model_Bench/l2_pipeline_runtime.py` — actual lifecycle implementation.
- `deploy/helpdesk_workflow_binding.json` — live Helpdesk status binding.
- `Knowledge/KB_IMPLEMENTATION_PLAN.md` — KB architecture/implementation plan.
- `README.md` — human-facing current architecture/deployment overview.

## Current deployment facts that matter

- Branch: `main` only.
- Live lifecycle: centralized Kanban state machine in `Model_Bench/l2_pipeline_runtime.py`.
- Pipeline WIP: up to `8` active runs (`L2_MAX_PIPELINE_WIP`); exactly one RUNNING local-model (Qwen) slot, waiting threshold `4`.
- Priorities: review `30`, rework `20`, new investigation `10`.
- No-Qwen first: audited probes -> harness fact table -> Jev `direct_answer` picks the outcome -> fixed reply published. Jev never writes text; the local model runs only on NEEDS_REASONING.
- XBatch investigation has one generated world: `Knowledge/process_world.json` -> `Knowledge/world/**` -> GBrain/world_walk. The retired semantic atlas/recipe registry is not a live dependency.
- The model never writes SQL or names columns: `xstudio_read_table(table)` lets the harness pick filter and columns.
- Worker profiles: `l2-jev-investigator`, `l2-reviewer-primary`; `l2-investigator` hosts the cron jobs. Gemma/primary/fallback profiles are retired.
- Reviewer creation is deferred until investigator/rework completion is normalized and reviewable.
- Reviewer receives frozen `proposal_json`; deterministic publisher publishes that same proposal.
- Rework cycles use `review_cycle`, not SQL `AttemptNo`; max cycles = 3.
- UPDATE continuations are capped at 3 per ticket version (no new requester input); the next UPDATE escalates to L3.
- Stale/orphan recovery has one owner: `recover_orphan_runs` in the runtime. `--poll` no longer runs the blind `Hermes_L2_Recover_Stale_Runs_Usp` sweep.
- `ticket_scout.py` is the 2-minute mutating reconciliation/claim backstop.
- Separate 5-minute publish-safety-net and repair cron jobs were deliberately removed; do not recreate them.
- L2 agents reach the database ONLY through the typed `xstudio_l2` tool (`xstudio-l2-tools` plugin + `Model_Bench/xstudio_l2_tool_bridge.py`). Model-driven terminal use of an interpreter, database driver, `sqlcmd`, or package install is blocked by the plugin guard and `approvals.deny`; benign terminal/file inspection still works. Raw agent SQL is read-only, arbitrary `EXEC` is unavailable, and `read_procedure` is an explicit allowlist. See `AGENTS.md` §8a.
- Qdrant and mem0 were removed on 2026-09-30 (`docs/decisions/2026-09-30-drop-qdrant-mem0.md`); do not reinstall them. Agent knowledge is the dispatch bundle, GBrain world, KB articles and ledgers only.
- Reviewer completion audit is read-only.
- Live-verified Helpdesk binding: eligible `Enter`, resolved `Closed`, waiting-user AskStatus `Ask`; L3/human-action ticket statuses remain unbound until proven live.
- A `RESOLUTION` does not automatically create an approved KB article: curation writes a `Candidate`, promoted to `Approved` only when a verified resolution on a different ticket reuses it.
- The generated SQL full-install bundle includes the `25` and `55` hardening sources.
- `.gitattributes` forces LF on `*.sh` and `*.sql` because Windows CRLF conversion broke WSL scripts and install reproducibility.

## Working agreements (full text: `AGENTS.md` §1b)

- End goal: a self-sustaining L2 helpdesk. Jev decides and selects, the harness does the heavy lifting, Qwen only writes when reasoning is needed. Never tailor anything to synthetic test tickets.
- Research and reuse before building; never guess settings. Dev SQL `10.2.6.204` is the owner's own: act without asking, never hand the owner commands you can run, never store a pasted credential.
- Do not restart gateways, toggle cron, or load/unload LM Studio models unless asked. Reuse `benchmark_l2_performance.py`, `seed_real_xbatch_tickets.py`, `reset_l2_test_tickets.py`; no throwaway scripts.
- `main` only; commit and push every finished change; audit other agents' branches and claims locally before merging. Research goes to Antigravity/Codex via `Agent_Comms/`, not to your own subagents.
- Report in IST, plain English, short bullets.

## L1 console facts (full text: `AGENTS.md` §19)

- `l1-ui/` (Next.js, :3417) plus `L1/api/` (.NET, :5116); run both as standalone processes and restart the API after editing `L1/api/*.cs`.
- One `QueueRow`, one `Outcome` chip, charts from `components/ui/charts.tsx`; mono only for ids and numbers; amber only where a person must act.
- `L3Status` allows `Open/Assigned/InProgress/Resolved/Rejected` only; ticket `StateLabel` is requester-facing.

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
python Model_Bench/benchmark_l2_performance.py --hours 2   # live health; extend it, do not write ad hoc scripts
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

Console changes: `npx tsc --noEmit` and `npx eslint components lib` in `l1-ui/`, then check the screens at 1600, 768 and 375 px against real tickets (`AGENTS.md` §19).

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