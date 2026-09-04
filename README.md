# Chitragupta — XStudio Hermes L2 Helpdesk

An autonomous L2 support pipeline for the XStudio/XMES platform, built on
[Hermes Agent](https://hermes-agent.nousresearch.com). It polls the live
Helpdesk queue, investigates tickets against the real XStudio_Xbatch/
XStudio_Helpdesk schema, has a second bot verify every proposed response
before it's published, escalates genuinely stuck cases to a human work
queue, and keeps a full, human-readable audit trail (and compute-cost
accounting) of every investigation attempt — resolved or not.

Named after the Hindu deity of meticulous record-keeping and judgment:
this system's job is exactly that — investigate, keep a complete account,
and decide what needs to go to a human.

## Layout

- **`Hermes_Orchestrator.py`** — the two primitives everything else is
  built on: atomic ticket claim (`--poll`) and audited response write-back
  (`--publish-response`). Investigation itself is the bot's own job, using
  its own tools.
- **`Model_Bench/`** — deterministic bridge/orchestration scripts (kanban
  dispatch, reject/approval publishing, trace summarization) plus the two
  Hermes plugins (`xstudio_l2_trace_plugin`, `xstudio_l2_orchestrator_plugin`)
  that make the pipeline event-driven instead of cron-polled.
- **`Knowledge/`** — the deployable SQL layer (six numbered files,
  concatenated into `00_Hermes_L2_FULL_INSTALL.sql`), plus schema/SP
  reference dumps and routing knowledge.
- **`deploy/`** — everything that otherwise lives *only* inside Hermes's
  own install (`~/.hermes/...`) and wouldn't survive a fresh install or an
  update on its own: each profile's `SOUL.md` + `config.yaml`, the
  `xstudio-*` skills, plugin manifests, and the live cron schedule. See
  `Model_Bench/mirror_wsl_artifacts.sh` to refresh this from a running
  instance.
- **`patches/`** — fixes to third-party packages inside Hermes's own venv
  that get silently wiped by an update. **Read `patches/POST_UPDATE.md`
  after every `hermes update`.**
- **`AGENTS.md` / `CLAUDE.md`** — the actual agent-facing operating
  instructions: folder map, deployment state, SQL write discipline, naming
  gotchas. Read these first if you're an agent picking this project back
  up.

## Setting this up on new infra

1. Deploy the SQL layer (`Knowledge/00_Hermes_L2_FULL_INSTALL.sql`, then
   `Knowledge/99_postflight.sql`).
2. Install Hermes Agent, create the profiles listed in `deploy/profiles/`.
3. Copy each profile's `SOUL.md`/`config.yaml` and the `xstudio-*` skills
   from `deploy/` into the matching `~/.hermes/profiles/<name>/...` paths.
4. Deploy the plugins from `Model_Bench/xstudio_l2_*_plugin/` and enable
   them per profile.
5. Set `MSSQL_MCP_SERVER`/`MSSQL_MCP_USER`/`MSSQL_MCP_PASSWORD` in the
   environment — every script reads credentials from there, nothing is
   hardcoded.
6. Recreate the cron schedule from `deploy/cron_jobs.json`.
7. Set up mem0 (`Model_Bench/setup_mem0.py`) if you want cross-run memory —
   needs an OpenAI-compatible LLM endpoint and an Ollama instance for
   embeddings; see the script for exact config.
8. Run `patches/apply_mem0_json_object_patch.py` if using mem0 with
   LM Studio as the LLM provider (LM Studio rejects mem0's default
   `response_format`).

## Credentials

Nothing in this repo is a secret. Every script reads `MSSQL_MCP_SERVER`/
`MSSQL_MCP_USER`/`MSSQL_MCP_PASSWORD` from the environment. `.env` files,
`.hermes_infra_creds/`, and anything password-shaped are gitignored.
