# After any `hermes update` (or a fresh install on new infra)

Things in this repo that live partly or entirely inside Hermes's own install
(`~/.hermes/...`) and do NOT survive an update/reinstall on their own.
Run these, in order, after any `hermes update` or when standing this up on
new infra.

## 1. Re-apply the mem0 LM Studio compatibility patch

An update can reinstall/upgrade `mem0ai` inside Hermes's venv, wiping the
patch below.

```bash
source ~/.hermes/hermes-agent/venv/bin/activate
python3 patches/apply_mem0_json_object_patch.py
```

Idempotent -- safe to run even if already patched, and safe to run on a
schedule (see `Model_Bench/` cron jobs) so it self-heals without you having
to remember it.

## 2. Qdrant server + mem0 config

**Check this after EVERY update, not just a fresh install.** mem0 memory
depends on a Qdrant *server*, and both halves can break independently.

```bash
# 2a. Is the vector store up and does it still hold data?
deploy/qdrant/healthcheck_qdrant.sh
```

That script exits non-zero if the service is down or the collection isn't
green, and *warns* if the collection exists but holds zero points. Take the
zero-points warning seriously on an established system: it is exactly what
a silent memory regression looks like, and this project ran with zero
memories for its entire history without noticing.

If the service is missing (fresh install, or the unit was removed):

```bash
deploy/qdrant/install_qdrant.sh     # idempotent; installs binary + systemd user unit
```

**Do not "fix" a Qdrant lock error by switching mem0 back to an embedded
local path.** That was the original configuration and it is the bug:
embedded Qdrant is single-process, kanban workers are separate OS processes
from their gateway, so every worker's memory call failed with `Storage
folder ... already accessed by another instance of Qdrant client`. Giving
each profile its own path does not fix it either — that separates gateways
from each other, never a worker from its own gateway.

Then, if profile directories were rebuilt (fresh install only -- a normal
update leaves `~/.hermes/profiles/*` alone):

```bash
source ~/.hermes/hermes-agent/venv/bin/activate
pip install qdrant-client mem0ai ollama
python3 Model_Bench/setup_mem0.py     # points mem0 at 127.0.0.1:6333
```

Requires: LM Studio reachable (see `deploy/profiles/*/config.yaml` for the
URL this project uses) and Ollama running with `nomic-embed-text` pulled
(`curl http://<desktop>:11434/api/tags` to check; `curl .../api/pull -d
'{"name":"nomic-embed-text"}'` to pull it).

## 3. Re-deploy SOUL.md / skills / plugins

Fresh install only -- copy `deploy/profiles/<profile>/SOUL.md` and
`deploy/skills/xstudio/*/SKILL.md` into the corresponding
`~/.hermes/profiles/<profile>/...` paths, and the plugin code from
`Model_Bench/xstudio_l2_*_plugin/` into
`~/.hermes/profiles/<profile>/plugins/<name>/`. Restart the profile's
gateway (`systemctl --user restart hermes-gateway-<profile>.service`)
after any plugin change.

## 4. Re-deploy the SQL layer

Deploy `Knowledge/00_Hermes_L2_FULL_INSTALL.sql` (regenerate first by
concatenating the six numbered files in order -- see `CLAUDE.md`), then
run `Knowledge/99_postflight.sql` and confirm no errors. Additive-only;
safe to re-run against an existing database.

## 5. Re-create cron jobs

See `deploy/cron_jobs.json` (or `.txt`) for the reference schedule this
project runs. Recreate with `hermes -p l2-investigator cron ...` -- see
`Model_Bench/` for the actual scripts each job runs.

## Ongoing self-healing

Step 1 (the mem0 patch) is the single most update-fragile piece --
consider adding it to a low-frequency cron job (e.g. daily) so a silent
`mem0ai` upgrade never sits broken for long between someone noticing.
