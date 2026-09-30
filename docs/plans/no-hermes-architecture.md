# Chitragupta without Hermes: architecture and plan

Date: 2026-09-30. Branch: `no-hermes` (long-lived; `main` stays the Hermes version until parity).
Status: plan accepted; nothing below is built yet except where marked done.

## 1. Goal and constraints

- **Goal:** one packaged product that installs on any Windows server, launches with nothing connected, and is configured afterwards (SQL, LM Studio, Jev). Packaging and control are the point.
- **Constraints (from the owner):** Windows native; SQL Server stays external (out of scope); **never Docker**; a real UI installer, not setup scripts; **no change to the UI's look and feel** (wording may change where it names Hermes); GBrain stays; Kanban and its card tools stay as a feature; ponytail principles (delete first, reuse before build, fewest files, libraries welcome where they replace wheel reinvention).

## 2. What Hermes actually contributed (evidence)

Measured on the live system, last 168 h: 42 runs, 42 published, 0 failed, 20 answered without the local model.

| Hermes piece | Use here | Replacement |
|---|---|---|
| Kanban store + dispatcher | Runtime shells out to `hermes kanban create/list/runs/archive/edit` (`Model_Bench/l2_pipeline_runtime.py`); Hermes spawns the worker per card | SQL card table + `cards.py` (same signatures) + a small dispatcher |
| Agent loop | LM Studio tool-calling loop, SOUL.md prompt, toolset gating, `max_turns 20`, 65k context | Python engine, `openai` SDK (`base_url` = LM Studio) |
| Plugin hooks | 4 plugins, ~1.8k lines, incl. compensation for the model misusing Hermes tools | Ordinary code in our loop; most guards disappear |
| Cron | 3 no-model jobs (scout 2 min, audit 10 min, session maintenance 6 h) | In-process loop |
| Gateway, profiles, approvals deny-list | Host for cron/dispatch; per-role config; terminal guard | Config file; no terminal tool exists, so no guard needed |

Kanban was duplicate state: SQL already holds the run, admission slot and lease. The orphan-recovery and completion-audit machinery exists to reconcile the two stores.

Tools the workers actually call (week): `xstudio_*` ~400, `kanban_*` 191, `l2_recall` 41, file/skill tools 27 (dropped; `write_file` failed 3 of 5).

What Hermes cost: WSL + systemd, the CRLF `.env` bug, the native-Windows cron-fence bug (Errno 36), `hermes update` wiping patches, a redeploy checklist.

## 3. Target architecture

```
 Windows server
 ├─ Service "Chitragupta API"     .NET, self-contained, Windows Service
 │    serves the console UI (static files) + /api/*, talks to SQL, LM Studio, Jev
 ├─ Service "Chitragupta Engine"  Python, hosted by WinSW
 │    scheduler loop + dispatcher + agent loop + card store (pyodbc)
 ├─ GBrain                        Bun + pinned checkout, PGLite state in ProgramData
 └─ config: ProgramData\Chitragupta\chitragupta.json (SQL secret protected with DPAPI)
 External, connected after launch: SQL Server, LM Studio (chat + embedding model, same host), Jev (TypeSafe key)
```

## 4. Decisions and reasons

**D1. Engine language: Python.** The runtime (4k lines), SQL bridge, typed tools and `world_walk` are already Python. Rewriting them is the opposite of reuse.

**D2. Agent loop: the official `openai` SDK, no agent framework.** LM Studio is OpenAI-compatible; our tool surface is about 10 typed tools; the loop is roughly 50 lines. A framework adds its own runtime and abstractions for a job we can state in a page. Ceiling: Qwen 9B tool-call quirks and the 65k context are ours to handle now (Hermes handled them). Upgrade path: none needed unless failures show.

**D3. Cards: one SQL table beside the run tables, via `pyodbc`.** No ORM. `cards.py` keeps the signatures the runtime already calls (`list_tasks`, `get_runs`, create, archive, edit) so about ten call sites change. Card tool names (`kanban_show/complete/block/comment/attachments`) stay so prompts barely change; `complete`/`block` become harness actions driven by a validated `submit_proposal`. Old Hermes card history is not migrated; runs and outcomes are already in SQL.

**D4. Scheduler: a plain stdlib loop in the engine.** Two intervals do not justify APScheduler.

**D5. UI: static export served by the API.** The only server-side code in `l1-ui` is one pass-through proxy (`app/api/l1/[...path]/route.ts`); there are two pages (`/`, `/admin`). `output: 'export'` plus `UseStaticFiles` on the API deletes Node, a port and a service. Look and feel is unchanged by construction; verified by before/after screenshots of both pages (gate G1). Needed: the API answers `/api/l1/*` as it does `/api/*` today (one route alias), and the iframe embed URL moves to the API's port. `next dev` stays for development.

**D6. Engine as a service: WinSW.** Off-the-shelf service host (an exe plus one XML) with restart-on-failure and log rotation; not a hand-written supervisor. API and engine stay separate services so an API redeploy does not kill a run.

**D7. GBrain: keep, run natively.** Evidence from github.com/garrytan/gbrain:
- **Correction (2026-09-30, from the live `config.json`):** the live world brain runs on **PostgreSQL 16 + pgvector in WSL** (`engine: postgres`, GBrain 0.50.5.0), not PGLite; embeddings are `lmstudio:text-embedding-nomic-embed-text-v1.5`, 768 dimensions, served by the LM Studio host (port 1235 lists it). The world is 2,407 files, far below PGLite's documented ~50k-page range. A second home, `~/.hermes/l2-gbrain`, is provisioned by `sync_l2_gbrain.py` with `init --pglite` (empty today). Packaging Postgres+pgvector on Windows is heavy, so S1 must test **PGLite for the world**. The risk is PGLite being single-process (the same lock failure that broke embedded Qdrant): the API and the engine must reach GBrain through one owner process (`gbrain serve`), not concurrent CLI calls.
- Requires Bun 1.3.11+, PGLite default store, `GBRAIN_HOME` for state. Commands we use exist: `search`, `sync`, `embed`, `serve`, `sources`, `schema`, `doctor`.
- The README states no Windows support either way. Open Windows issues exist (#5595 managed-persistence EPERM, #5475 shared-skill publication, #5414 backup restore fsync); all three are in features we do not use, but they show Windows is not yet clean. **Spike S1 is therefore a gate.**
- Install via git checkout + `bun install && bun link`, not `bun install -g` (postinstall migrations are blocked on global installs).
- Embeddings come from the same LM Studio host: provider `lmstudio:<model-id>`, `LMSTUDIO_BASE_URL`, and `--embedding-dimensions <N>` is required and locked into the schema at `gbrain init`; changing model later needs `gbrain migrate embeddings`. The installer/Connections panel must therefore record model id and dimension at first init.
- Fallback if S1 fails: `world_walk` plus lexical retrieval; decided with the owner, not silently.

**D8. Installer: WiX (MSI) inside a Burn bundle.** Reasons: it is the standard for servers that IT deploys (silent, GPO/SCCM, rollback, major upgrade); services are declared natively (`ServiceInstall`/`ServiceControl`) instead of `sc create` scripts; the Burn chain installs the ODBC Driver 18 MSI as a prerequisite before ours; `WixStandardBootstrapperApplication` / WixUI give a real wizard (install directory, port), with data under ProgramData kept across upgrade. Rejected: **Inno Setup**, faster to author but produces an EXE and registers services through `sc`/batch calls, which is the script-style setup the owner ruled out; **MSIX** needs signing and fits desktop apps, not multi-service servers; **Velopack** is a desktop-app updater. Cost accepted: WiX authoring is steeper than Inno.
The installer asks only for install directory and port. Everything else is the Connections panel.

**D9. Configuration: one web panel, `/admin` Connections.** Tests and saves SQL, LM Studio (chat and embedding model), Jev key and GBrain, and can be re-run on a new server. Same visual language as the existing Settings page (no new look). The API and engine start with nothing connected; the dispatcher waits.

**D10. Bundling.** .NET `publish` self-contained; Python embeddable distribution plus a `site-packages` folder built from a pinned `requirements.txt` (`pyodbc`, `openai`); Bun executable plus GBrain checkout; ODBC 18 MSI. No installs on the target beyond the bundle.

## 5. Deleted with Hermes

Gateways, profiles, the approvals deny-list, the `hermes`/`wsl` wrapper code (`run_hermes`), the `wsl.exe` shell-outs in `L1/api` (`Health.cs`, `Ops.cs`, `Knowledge.cs`), plugin compensation guards, cron jobs, `patches/POST_UPDATE.md`, `deploy_l2_pipeline_runtime.sh` and the validate `.sh` scripts (ported to Python), Node runtime and the UI proxy route. Already removed on `main` (2026-09-30): Qdrant and mem0 (`docs/decisions/2026-09-30-drop-qdrant-mem0.md`).

## 6. Order of work and gates

1. **S1 spike: GBrain native on Windows.** Sync the world, run the existing 10 retrieval cases, compare with WSL. Gate: 10/10.
2. **S2 spike: static UI.** Gate G1: screenshots of `/` and `/admin` match the current UI.
3. Card table + `cards.py`; point the runtime at them.
4. Agent loop + tool extraction. **Gate G2:** seeded tickets (`seeded_ticket_expectations.jsonl`) give the same outcomes on both branches.
5. Engine service, scheduler, dispatcher; cron off.
6. De-WSL the console; Connections panel.
7. Bundle, WinSW config, WiX installer. **Gate G3:** clean-VM install with nothing connected launches; Connections panel brings it live.

## 7. Risks and unverified items

- GBrain on native Windows is unverified (S1). Its Windows issues are in unused features but open.
- Qwen 9B tool-call robustness and the 65k context now belong to our loop.
- `hermes-gateway-infra-guardian` runs live but is not in this repo; identify before removal.
- Which process dispatches Kanban cards today is unverified (`dispatch_in_gateway: false` on `l2-jev-investigator`); moot once we own the dispatcher, but it decides the slot-rule wiring.
- Branch drift: shared code (SQL, console, Knowledge) diverges; fixes land on `main` and merge into `no-hermes`.

## 8a. Prerequisites (checked 2026-09-30)

Have: .NET SDK 10.0.203, Python 3.14.4 (wheels for `pyodbc` 5.3.0 cp314 and `openai` 3.22.1 download cleanly), Node, Bun 1.4.2 (Windows, WinGet), WiX 5.0.2 (dotnet tool), ODBC Drivers 17 and 18, git; LM Studio on :1235 serving chat models (incl. `qwen/qwen3.5-9b`) and the nomic embedding model; SQL reachable over Tailscale with working credentials.

Needed before building:
1. **Baseline on `main`:** one live E2E run after the mem0/Qdrant removal, and record outcomes for the seeded tickets. Without it gate G2 has nothing to compare against.
2. **One engine per database.** `main` (Hermes) and `no-hermes` must never both claim from the same Helpdesk DB. Parity runs need either main's gateways stopped or a restored copy of the DB.
3. **GBrain S1 inputs:** PGLite vs PostgreSQL for the world (see D7), and single-owner access design.
4. **A clean Windows target for gate G3** (Windows Sandbox or a spare VM); not this laptop.
5. **Code signing decision:** unsigned MSI/EXE triggers SmartScreen on other servers.
6. **`infra-guardian` decision:** it is a Hermes agent acting as an operations watchdog. Proposed replacement: WinSW restart-on-failure plus a health view in the console. Owner to confirm.
7. **Target-server requirements to state in the install guide:** outbound internet for Jev (TypeSafe), network path to SQL and LM Studio.
8. **POSIX audit (measured):** only 7 non-test Python files carry `fcntl`/`/home`/`~/.hermes`/`wsl`/`systemctl` coupling (`l2_pipeline_runtime.py` has 20 matching lines); the port is small.

## 8. Branch policy

`main` = with Hermes (deployed). `no-hermes` = this plan. This overrides the "Branch: `main` only" line in AGENTS.md/CLAUDE.md for this work; both files are updated together.

## 9. Implementation log (no-hermes branch)

2026-09-30. Hermes gateways were stopped and disabled (no double claiming). Built, in this order:

- **`Model_Bench/cards.py`**: SQL board (`L2_Card_Tbl`, `L2_Card_Run_Tbl`, created on first use). Same card/run dict shape the runtime already read. One connection per thread, because a login over the Tailscale relay costs seconds. `claim()` is atomic (`UPDLOCK, READPAST`, priority then age).
- **Runtime port (`l2_pipeline_runtime.py`)**: the `hermes kanban` calls (list, runs, create, edit, archive) became `cards` calls; `run_hermes` and every WSL/Windows path constant are gone (`REPO_ROOT` is derived from `__file__`); the lifecycle lock is portable (`msvcrt`/`fcntl`); the worker dependency probe reads `deploy/engine.json` instead of a Hermes profile.
- **`Model_Bench/agent_loop.py`** (D2 amended: stdlib HTTP, no `openai` SDK; one `urllib` POST replaces the SDK, so the bundle needs one Python dependency fewer): one process per card. The xstudio tools plugin and the trace plugin **run unchanged** through a 15-line Hermes-compatible context (`register_tool`, `register_hook`), so every existing guard, repair and budget rule is kept; the four `kanban_*` tools are built in. LM Studio quirk found live: `reasoning_effort` must be sent as `none` (`off` is rejected with HTTP 400).
- **`Model_Bench/engine.py`**: dispatcher (claim, run worker under the card's max runtime, reconcile at once, drain traces) plus scheduler (scout 2 min, audit 10 min). Starts with SQL down and waits.
- **`deploy/engine.json`**: LM Studio URL, model and limits per role, replacing the Hermes profile `config.yaml`.
- **Console (`L1/api`)**: `Board()` reads the card tables; runtime status, GBrain search and log tails run natively (no `wsl.exe`).
- **GBrain S1 (native Windows)**: v0.50.5.0 cloned, `bun install` + `bun link` work; `gbrain init --pglite --embedding-model lmstudio:text-embedding-nomic-embed-text-v1.5 --embedding-dimensions 768` works; the `xbatch-world` schema pack validates; source registered. Sync/embed/search result recorded below when complete.

Live findings: a ticket that hit the 400 crashed its first card and the runtime's own failure recovery created the rework card on the new board, i.e. the recovery path works end to end on SQL cards. Scout ticks take minutes over the relay; that latency, not the engine, dominates.

