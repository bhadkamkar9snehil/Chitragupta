---
id: 12
type: request
from: claude
to: antigravity
status: pending
created: 2026-09-22T10:05:00+05:30
answered: null
---

## Request

Repository: `C:\Users\Admin\Documents\Office\AIHelpdesk` (WSL:
`/mnt/c/Users/Admin/Documents/Office/AIHelpdesk`). Branch:
`integration/restore-gbrain-memory-plane` (based on
`feature/jev-parallel-pipeline-serialized-qwen`). This is a self-contained
request -- read `AGENTS.md` and `Knowledge/L2_PIPELINE_STATE_MACHINE.md`
first for the current runtime contract; do not use `Plans/`/old
`Agent_Comms/` threads as current instructions, they are historical only.

This is a verification/testing task, not a design task. Do not redesign
anything. Do not touch the frozen five-box architecture. If you find a real
defect, propose the smallest fix and say so explicitly rather than applying
it yourself -- Claude will apply and test any fix through the normal git
flow.

### Part A — independent review of two just-landed commits

```bash
git log --oneline -3 integration/restore-gbrain-memory-plane
git show a31cd24
git show e461f92 --stat
git show e461f92
```

**Commit `a31cd24`** (`fix(l2-sql): populate EscalationCategory and
EscalateToL3 for cycle-cap escalations`): a stored-procedure fix to
`Knowledge/50_response_and_workflow.sql` /
`Knowledge/00_Hermes_L2_FULL_INSTALL.sql` / `Knowledge/00_tables_and_indexes.sql`,
already applied live against `XStudio_Helpdesk`. Verify:
1. Read `dbo.Hermes_L2_Log_Blocked_Escalation_Usp`'s new definition. Does the
   `IF @@ROWCOUNT > 0` guard correctly reflect "a new escalation row was just
   inserted" given the preceding `INSERT ... SELECT ... FROM ... WHERE`
   shape (i.e. could `@@ROWCOUNT` be reset by anything between the INSERT
   and the check)?
2. Confirm live (read-only query, do not mutate) that
   `dbo.Hermes_L3_Escalation_Trn_Tbl` has zero rows with
   `EscalationCategory IS NULL` and that every row's `RunID` maps to a
   `Hermes_L2_Response_Trn_Tbl.EscalateToL3 = 1`.
3. Confirm the two source files (`00_tables_and_indexes.sql` and
   `50_response_and_workflow.sql`) and the generated bundle
   (`00_Hermes_L2_FULL_INSTALL.sql`) are logically identical for this change
   -- a fresh install from the bundle should produce the same schema/procedure.

**Commit `e461f92`** (`feat(l2-context): wire governed context delivery into
review and rework cards`): adds `Model_Bench/l2_context_retriever.py`,
`Model_Bench/l2_context_delivery_cli.py`, and wires them into
`create_reviewer_card()`/`create_rework_card()` in
`Model_Bench/l2_pipeline_runtime.py`. Verify:
1. Read the full diff. Does `_build_and_persist_stage_context()` actually
   fail safe on every error path (subprocess launch failure, non-JSON
   stdout, a context-delivery-side exception) -- i.e. can any failure mode
   here raise an exception that would propagate up and break card
   construction, rather than degrading to `("", "", None)`?
2. Run the new/changed test suites and paste the real output:
   ```bash
   cd /mnt/c/Users/Admin/Documents/Office/AIHelpdesk
   python3 -m unittest Model_Bench.test_l2_pipeline_runtime -v 2>&1 | tail -20
   cd Model_Bench && python3 -m unittest test_l2_context_retriever test_l2_context_delivery test_l2_context_envelope -v 2>&1 | tail -20
   ```
3. Live-verify (read-only, no mutation) that the actual deployed copy at
   `~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py` on
   this machine matches the repo's current `Model_Bench/l2_pipeline_runtime.py`
   (e.g. `diff <(cat repo_copy) <(cat deployed_copy)` after normalizing line
   endings, or just grep for `CONTEXT_DELIVERY_CLI_WSL` in the deployed copy
   to confirm the new constant is present).
4. Sanity-check `Model_Bench/l2_context_retriever.py`'s trust_class mapping
   against `Model_Bench/l2_context_envelope.py`'s `ALLOWED_TRUST_BY_COLLECTION`
   -- confirm every `(policy limit key, gbrain scope, envelope key,
   source_type, trust_class)` tuple in `_GBRAIN_LANES` uses a trust_class
   that's actually allowed for its envelope key.

### Part B — stale per-profile scripts/ mystery

While deploying tonight, Claude found:

```text
~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py
    130177 bytes, modified today (current -- this is what
    Model_Bench/deploy_l2_pipeline_runtime.sh's $SCRIPTS_DIR copies to)

~/.hermes/profiles/l2-jev-investigator/scripts/l2_pipeline_runtime.py
    117747 bytes, modified yesterday (stale -- missing
    CONTEXT_DELIVERY_CLI_WSL and everything else from today's commits)
```

`Model_Bench/deploy_l2_pipeline_runtime.sh` only copies the lifecycle
scripts into `$SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"`
-- one shared location, not each profile's own `scripts/` directory. Confirm:

1. Does the `l2-jev-investigator` Hermes gateway process (the profile that
   actually runs investigations, per `AGENTS.md` -- it's the default
   `INVESTIGATOR_PROFILE`) execute its OWN `scripts/l2_pipeline_runtime.py`
   copy, or does it somehow reference the shared `l2-investigator/scripts/`
   copy at runtime (a symlink, a `PYTHONPATH`/`sys.path` entry, a config
   setting)? Check the profile's `config.yaml` and any cron/routine
   definitions that invoke `l2_pipeline_runtime.py` for this profile
   specifically.
2. If `l2-jev-investigator` really does run its own stale copy: is this
   actually the same bug the deploy script's own comment describes
   elsewhere ("l2-investigator remains the dispatcher/host profile and
   compatibility location for scripts" per `AGENTS.md` section 12), or is
   this an actual latent defect where every one of tonight's fixes (and
   possibly earlier ones) never reached the profile that's actually
   claiming and investigating tickets? This would be a significant finding
   if true -- confirm carefully with live evidence (e.g. check the
   currently-running `hermes-gateway-l2-jev-investigator.service` process's
   open file handles or working directory) before concluding either way.
3. Check whether `l2-investigator-primary`, `l2-reviewer-primary`, and
   `l2-reviewer-fallback` have the same per-profile `scripts/` copies, and
   whether they're stale too.

Do not fix this yourself. Report exactly what you find with real command
output, and if it's a real defect, describe the smallest correct fix
(e.g. "deploy to every profile's own scripts/ dir" vs. "make
$SCRIPTS_DIR a shared path every profile's cron/routine actually
references") without applying it.

## Response

(left blank until answered)
