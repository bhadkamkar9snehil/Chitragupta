---
id: 42
type: request
from: claude
to: codex
status: answered
created: 2026-10-02T14:00:00+05:30
answered: 2026-10-02T15:30:00+05:30
---

## Request

Take over Chitragupta from Claude. Primary job: **finish, verify and ship the Windows installer and packaging**. Then the open product items in section 7. This file is self-contained; read it with `AGENTS.md`, `CLAUDE.md`, `README.md`, `Knowledge/L2_PIPELINE_STATE_MACHINE.md` and `docs/plans/no-hermes-architecture.md` (the design record: decisions D1-D10, gates, implementation log). All times IST. Last commit at handoff: `120aa18` on `main` (pushed).

### 1. State of the repo

- **One long-lived branch: `main`.** On 2026-10-02 the `no-hermes` branch was fast-forward merged into `main` (nothing was lost; `main` had no commits `no-hermes` lacked). `origin/no-hermes` still exists on GitHub and equals the old tip plus one docs commit; delete it when the owner agrees. Other old local/remote branches are not ours; leave them.
- The product is a **native Windows system with no WSL and no agent framework**: a .NET API that serves the static console, and a Python engine (scheduler, dispatcher, agent loop, SQL card board) with GBrain supervised as a child process. The Hermes/WSL era is gone from the live docs; `Plans/` and `Agent_Comms/` hold history only.
- Docs were brought up to date on 2026-10-02 (README, AGENTS.md, CLAUDE.md, state-machine contract, deploy and validation guides). Do not describe the project as "migrated from Hermes"; the owner asked that the docs not mention it.

### 2. Standing rules from the owner (non-negotiable)

- `main` only; commit and push every finished change. Co-author line: `Co-Authored-By: <your model> <noreply@...>`.
- Times in IST, never UTC. Commands handed to the owner: full absolute paths, **PowerShell 5.1** syntax (no `&&`), one command per block.
- Plain English, short bullets.
- **Act, do not ask** on the owner's dev SQL (`10.2.6.204` LAN, `100.94.169.57` over Tailscale). Never store or print a pasted credential. Never put credentials in prompts, cards, tickets, traces or commits.
- **Do not restart the engine/API or touch LM Studio models unless asked.** Do not toggle scheduled tasks. When the owner says stop, stay stopped.
- **Ponytail**: reuse the existing owner, delete superseded code and its tests in the same change, fewest files. No throwaway scripts: live health is `python Model_Bench/benchmark_l2_performance.py --hours 2` (extend it).
- **E2E-first testing**; never write unit tests after the code. Validate locally against the real environment; GitHub Actions is not proof.
- Never tailor knowledge or code to synthetic test tickets. Use `seed_real_xbatch_tickets.py` / `reset_l2_test_tickets.py`.
- **One engine per database.** Never run two engines claiming from the same Helpdesk DB (for example this laptop's engine and an installed one).
- Do not reinstall Qdrant or mem0 (`docs/decisions/2026-09-30-drop-qdrant-mem0.md`).
- `.gitattributes` forces LF on `*.sh` and `*.sql`; keep it.
- Console UI: keep the graphite + mint design system, shared `QueueRow`/`Outcome`, check 1600/768/375 px (`AGENTS.md` section 19).

### 3. This laptop right now

- **Not installed.** No Chitragupta service, nothing in Program Files. It runs as a staged copy from `build\stage` through `build\dev-start.ps1`, which starts the API and the engine each in a hidden restart loop.
- The **`Chitragupta` scheduled task (logon trigger) was disabled on 2026-10-02** at the owner's request, so nothing starts at boot. To start by hand: `powershell -ExecutionPolicy Bypass -File C:\Users\Admin\Documents\Office\AIHelpdesk\build\dev-start.ps1 -Open`. As of this handoff the API (:3417) and the engine are still running from the earlier session; the owner has not asked to stop them.
- The `AIHelpdesk_GitSync` scheduled task (periodic `git_sync.sh`, writes `.git_sync.log`) is still on and auto-commits "auto: periodic sync ..." on whatever branch is checked out (now `main`). Leave it unless the owner asks.
- Dev data folder: `C:\ProgramData\Chitragupta` (`chitragupta.json`, `logs\engine.log`, `gbrain\`, `trace\`, `calltrace\`, `lifecycle.lock`, worker logs).
- The engine runs the **staged copy** of `Model_Bench`. An edit to the working tree is not live until `build\build.ps1` restages it and the engine restarts.
- Four dead startup files from the old Hermes setup were deleted from the user Startup folder on 2026-10-02 (they had caused "Select an app to open this .disabled file" popups).
- Topology: SQL Server external (use the **Tailscale address**, not the office LAN address, off-network); LM Studio on the owner's desktop (`100.111.69.102:1235`, one Qwen inference slot plus the nomic embedding model); the laptop is the source setup.

### 4. Architecture in one screen

```
Chitragupta Console service (L1Api.exe, .NET, :3417 = CHITRAGUPTA_PORT)   serves l1-ui static export + /api/*
Chitragupta Engine service (WinSW -> embedded python engine.py)
   scheduler: scout 120 s, audit 600 s, trace drain
   dispatcher: cards.claim() every 2 s -> agent_loop.py <card> (one process per card, bounded by max runtime) -> reconcile at once
   gbrain_service: gbrain.exe serve --http (PGLite is single-process; this is the single owner)
   config: ProgramData\Chitragupta\chitragupta.json -> environment (chitragupta_config.py); a change makes the engine exit 75 so the service host restarts it
SQL: XStudio_Helpdesk / XStudio_Xbatch (external). Cards: L2_Card_Tbl, L2_Card_Run_Tbl (created on first use).
```

Key files: `Model_Bench/engine.py`, `agent_loop.py`, `cards.py`, `chitragupta_config.py`, `l2_pipeline_runtime.py` (the single lifecycle authority), `deploy/engine.json` (LM Studio URL, model, context 65,792, 20 turns), `deploy/profiles/*/SOUL.md`, `deploy/plugins/*`, `Model_Bench/xstudio_l2_tools_plugin/` + `xstudio_l2_trace_plugin/` (loaded by the worker). Lifecycle invariants (WIP 8, one RUNNING Qwen slot, waiting threshold 4, priorities 30/20/10, review cycles 3, UPDATE continuations 3) are in `AGENTS.md` and the state-machine contract; do not change them without the owner.

### 5. Build and packaging: what exists

Everything is in `build/` and `installer/`.

| Step | Command (from the repo root) | Needs |
|---|---|---|
| Knowledge index, once or when `Knowledge/world` changes | `build\build-brain.ps1 -LmStudio http://100.111.69.102:1235/v1` | `build\cache\gbrain.exe` (made by build.ps1), LM Studio serving `text-embedding-nomic-embed-text-v1.5` (768 d), about 30 min; outputs `build\cache\brain.zip`, `brain.token`, `brain.client` |
| Stage the payload into `build\stage` | `build\build.ps1 [-Version 0.1.0]` | Node 20.19+, .NET 10 SDK, Python 3.14 (+pip), Bun, git, network on first run (downloads go to `build\cache`: Python embeddable 3.14.4, WinSW 2.12.0, GBrain v0.50.5.0 source); `build\cache\brain.zip` and `brain.client` must exist |
| MSI | `dotnet build installer\Package\Chitragupta.wixproj -c Release -p:Version=0.1.0` | WiX SDK 5.0.2 + UI/Firewall/Util extensions (NuGet), the staged payload |
| Setup.exe (Burn bundle) | `dotnet build installer\Bundle\Setup.wixproj -c Release -p:Version=0.1.0` | MSI above; `build\cache\msodbcsql.msi` (Microsoft ODBC Driver 18, already cached) |

What `build.ps1` stages (about 363 MB): `api\` (self-contained .NET publish with the console in `wwwroot`), `engine\` (embedded Python + `pyodbc==5.3.0` + `tzdata`, `app\Model_Bench`, `app\deploy`, `app\Knowledge` minus the large generated folders, `Hermes_Orchestrator.py`, WinSW renamed `ChitraguptaEngine.exe` + `ChitraguptaEngine.xml`), `gbrain\` (`gbrain.exe`, `brain.zip`), `chitragupta.json` (first-run template), `version.txt`.

What the MSI does (`installer/Package/Package.wxs`): installs to `Program Files\Chitragupta` (wizard: install folder, then console port, default 3417); registers services **`ChitraguptaConsole`** (the API, `L1Api.exe`, auto start, restart on failure) and **`ChitraguptaEngine`** (WinSW, auto start); firewall exception for the port; sets machine env `CHITRAGUPTA_PORT`; creates `ProgramData\Chitragupta\logs` and a never-overwritten, permanent `chitragupta.json` so settings survive upgrade and uninstall; MajorUpgrade enabled. The Burn bundle installs ODBC Driver 18 first, then the MSI with its own wizard shown.

Existing artifacts: `installer\Bundle\bin\Release\Chitragupta-Setup.exe` (147 MB) and `installer\Package\bin\Release\Chitragupta.msi` (143 MB), built **2026-10-01 00:16-00:17 IST**. They are **stale**: later commits changed the build (`fc436ba` embedded-Python path-file fix, `a7e469f` GBrain OAuth client, world-links work). Rebuild before testing anything.

### 6. Installer and packaging: your task list, in order

Nothing below the "verified" line in `docs/plans/no-hermes-architecture.md` section 9 has been done. Gate **G3**: a clean Windows machine, nothing connected, installs, both services run, the console opens, and Settings -> Connections brings it live.

1. **Get a clean target.** Windows Sandbox or a spare VM. Not this laptop (it would start a second engine and must stay on dev-start). Installing elevated on this laptop also risks two engines on one DB; if you must test here, stop the dev loops first and ask the owner.
2. **Rebuild from current `main`**: run `build-brain.ps1` only if `Knowledge/world` changed or the links step needs verifying (see item 5), then `build.ps1`, then both `dotnet build` commands. Confirm `build\stage\chitragupta.json`, `version.txt` and the services list in the MSI (`wix msi` or Orca) look right.
3. **Elevated install test on the clean target.** Verify: both services register and start; restart-on-failure (kill each process, watch it return); the firewall rule exists for the chosen port; the wizard shows folder then port and a non-default port works end to end (`CHITRAGUPTA_PORT` flows to the API); the console loads at `/admin` and `/` with nothing connected; Connections test buttons work and saving makes the engine restart itself (exit 75 -> WinSW restarts); upgrade (install 0.1.1 over 0.1.0 keeps `chitragupta.json` and logs); uninstall removes services and keeps ProgramData. Capture every failure as an Agent_Comms finding or fix it.
4. **Known gaps to close** (all unverified or unbuilt):
   - **Secret in the template.** `build.ps1` writes the GBrain OAuth `client_id` and `client_secret` (from `build\cache\brain.client`) into the staged `chitragupta.json`, which the MSI installs into `ProgramData\Chitragupta`. That file also receives SQL and Jev secrets later. The plan says it must be restricted to SYSTEM and Administrators; today the API only applies that ACL **when it saves**, and the installed template inherits ProgramData's default (users can read). Fix: set the ACL in the MSI (or on first service start) and consider a per-install GBrain secret instead of one baked into the payload. Also consider DPAPI for the SQL password (the plan, D9, said DPAPI).
   - **Burn bundle licence page** is `hyperlinkLicense` with an empty `LicenseUrl`; give it a real URL or switch theme.
   - **Code signing**: unsigned MSI/EXE triggers SmartScreen on other servers. Owner decision needed (certificate, or accept and document).
   - **Naming consistency**: services are `ChitraguptaConsole` / `ChitraguptaEngine`; README diagram says "Chitragupta API". Pick one and align docs.
   - **`build.ps1` still copies `Hermes_Orchestrator.py`** into the payload because `xstudio_l2_tool_bridge.py` and the publisher import its guarded SQL primitives. Rename it to a neutral module and update imports/tests when convenient; do not break publication.
   - **Offline target**: the target needs outbound internet only for Jev (TypeSafe); network path to SQL and LM Studio. Put target-server requirements into an install guide (`docs/`), including the ODBC driver, port, firewall and the Connections order (SQL, LM Studio, Jev key, GBrain).
   - **GBrain on the target**: `gbrain.exe serve --http` is supervised by the engine, index extracted from `brain.zip` on first start (`seed_index`). Confirm first-start extraction, the bearer/OAuth client works from the installed API, and that `pglite_busy` never appears (single owner).
   - **Version stamping**: `-Version` is passed to staging and WiX but nothing bakes it into the console footer or `status`; add if wanted.
   - **Release process**: a single script (`build\release.ps1`) that runs brain check, stage, MSI, bundle and prints hashes would replace the four manual steps. Only build it after the manual path is proven (ponytail).
   - **`apply-helpdesk-update.ps1`** is the old dev apply for the Node/.NET split and the `RepoPad` macropad. Decide with the owner whether it is retired in favour of the installer or kept for UI/API dev only. `build\dev-start.ps1` is labelled TEMPORARY until the installer is used on this machine; remove it (and the `Chitragupta` scheduled task definition) once an installed copy replaces it.
5. **Verify GBrain links are in the shipped index.** `Model_Bench/world_links.py` loads `Knowledge/world/links.jsonl` so `get_links`/graph walks return results. History: the first prune run deleted 2,325 world files through gbrain and was committed by mistake (restored in `a034e02`); the posix-path fix is `711590a`; `build-brain.ps1` now runs the links step. Whether the current `brain.zip` (built 2026-10-01 00:11 IST) contains the links is **not verified**. Rebuild if in doubt, then run `python Model_Bench/e2e/run_world.py` (the 10 retrieval cases) and `run_walk.py`. Gate S1 requires 10/10. Never run a prune/delete step against the committed world without a dry run; `sync` reads committed files only.

### 7. Open product items after the installer

From `docs/plans/no-hermes-architecture.md` sections 7, 9, 10, 11:

1. **Gate G2 at scale.** Pipeline parity was shown on 6 seeded tickets (Ticket_1/5/33/38 -> NEEDS_HUMAN_ACTION without Qwen; Ticket_3/35 -> L3_ESCALATION via the full loop). About 15 others (`Model_Bench/seeded_ticket_expectations.jsonl`) were not re-run. Use `reset_l2_test_tickets.py`, then `benchmark_l2_performance.py --hours 2`. Archive garbage tickets first; a low resolve rate is a finding, not a failure to hide.
2. **Logs and history continuity.** Confirm each stream still lands where the console reads it (call trace, observer events, worker logs, trace drain to SQL, readable ticket notes). Old WSL logs and Hermes card history are not migrated by owner decision.
3. **Stronger L1 gate** (plan section 11): Jev scores each turn (how-to, fault, identifiers present, duplicate, urgency, confidence); code applies thresholds; Qwen only phrases. Start in shadow mode, build the labelled evaluation set from real conversations and tickets first, enforce class by class. Open owner questions: acceptable missed-escalation rate, who reviews the question bank and checklists, whether L1 may run the read-only fact probes.
4. **Replace `infra-guardian`** (it was a Hermes watchdog agent): proposal is WinSW restart-on-failure plus a health view in the console. Owner to confirm.
5. **Delete retired code and its tests in one change** (documented as retired; verify nothing imports them first):
   - WSL deploy path: `Model_Bench/deploy_l2_pipeline_runtime.sh`, `validate_l2_pipeline_local.sh`, `patch_profile_config.py`, `patch_tool_search_off.py`, `patch_l2_worker_budget.py`, `hermes_cli_bench.py`, `sync_gbrain_knowledge.sh` (check each is unreferenced first). `git_sync.sh` is not retired: the sync task uses it.
   - `Model_Bench/xstudio_l2_orchestrator_plugin/`, `xstudio_l2_learning_plugin/`, `sync_l2_gbrain.py`, their tests, and `deploy/plugins/xstudio-l2-orchestrator.plugin.yaml`, `xstudio-l2-learning.plugin.yaml`.
   - `deploy/cron_jobs.txt` (historical snapshot), `deploy/profiles/l2-investigator`, `l2-investigator-primary`, `l2-reviewer-fallback`, `patches/`, root-level clutter (`AgentCode.zip`, `tmp_select_ccm_heat.sql`, `_publish.sql`, `_publish_sql.sql`, `L2_JEV_Validation_Output.txt`, `__pycache__`) after the owner agrees.
   - `Agent_Comms/00xx-pipeline-stall-detected.md` (0028-0041) are noise from the old stall monitor; archive.
6. **Test suite hygiene.** Last known green: 126 tests across runtime, trace and tools plugins plus the 30 knowledge tests run on 2026-10-02 (`test_validate_gbrain_knowledge`, `test_kb_retrieval`). Run `python -m unittest -v Model_Bench/test_l2_pipeline_runtime.py` before and after any lifecycle change; fix tests that still assume WSL or Hermes when you find them (delete them if the thing they test is gone).

### 8. Gotchas that cost real hours (still true)

- **Use the Tailscale SQL address off-network.** On the LAN address every scout tick fails with `HYT00 Login timeout` and the board looks idle.
- **SQL timestamps (`CreatedOn`, `EventOn`) are already IST.** Do not add 5:30.
- **pyodbc hides procedure errors behind result sets** until `nextset()`; drain before commit.
- **GBrain `sync` reads committed git files.** Commit regenerated world pages before syncing. **GBrain PGLite is single-process**: all access goes through the engine's `serve --http` (MCP over HTTP, bearer/OAuth client).
- **Embedded Python ignores `PYTHONPATH` and the script dir**: the app folders are listed in its `._pth` by `build.ps1`. A `._pth` mistake looks like "module not found" only in the staged copy.
- **LM Studio quirk**: `reasoning_effort` must be sent as `none` (`off` is rejected with HTTP 400). The 160-character summary floor is told to the model in the prompt.
- **`XMES_Log_Trn_Tbl` is huge** (3.5 GB, PK only). Never `LIKE`-scan it live.
- **Launching servers**: the owner wants the API and UI as standalone processes (`Start-Process`), never through an IDE/agent preview pane that kills them when idle.
- **CRLF**: this repo is edited on Windows; `.sh` and `.sql` are forced LF. A CRLF `.sql` bundle breaks reproducibility.
- **Resolution binding fails closed.** `deploy/helpdesk_workflow_binding.json`: eligible `Enter`, resolved `Closed`, waiting-user AskStatus `Ask`. L3/human-action statuses are unbound until proven live.
- **Do not hardcode the loaded LM Studio model** in docs; verify it live.

### 9. How to verify your work

- Console: `npx tsc --noEmit` and `npx eslint components lib` in `l1-ui/`, `npm --prefix l1-ui run check` and `run build`, then look at 1600/768/375 px against real tickets.
- Pipeline: `python Model_Bench/benchmark_l2_performance.py --hours 2` (exit 1 if a lifecycle invariant breaks) and the staged runtime `status`:
  `C:\Users\Admin\Documents\Office\AIHelpdesk\build\stage\engine\python\python.exe C:\Users\Admin\Documents\Office\AIHelpdesk\build\stage\engine\app\Model_Bench\l2_pipeline_runtime.py status`
- Knowledge: `python Model_Bench/validate_knowledge_manifest.py`, `python Model_Bench/e2e/run_world.py`.
- Installer: the checklist in section 6.3 on a clean machine. "Built" is not "verified"; report what you actually ran.

### 10. Reporting back

Write your response into this file (set `status: answered`, `answered:` timestamp IST) or open a new numbered thread for findings. Report in short bullets: what you built, what you ran, what failed, what needs the owner (code-signing decision, `infra-guardian` decision, branch deletion, L1 gate thresholds).

## Response

- Owner prioritized packaging and explicitly authorized installation on this laptop, followed by server `10.2.6.204`. Historical advice to keep this laptop on dev-start was superseded by that request.
- Built release **0.1.1**, self-contained API/console, embedded Python, GBrain and cached knowledge index. Setup and MSI are in `build/out/0.1.1/`, with `SHA256SUMS.txt`. Build succeeded; WiX emitted WIX1149 for native service failure configuration, which was checked live (`qfailureflag = TRUE`).
- Fixed first-run settings ACLs, generated GBrain OAuth credentials per installation, started knowledge before SQL setup, and made settings exits clean up the GBrain child. Added engine recovery actions in MSI, explicit API port arguments, saved-port lookup, version file, staging-directory guard and native build exit checks. The old launcher now refuses to start development loops when the engine service is installed.
- **Laptop:** stopped both dev loops; installed 0.1.0 and upgraded to 0.1.1. Both automatic services run from Program Files. Existing settings hash survived upgrade. Settings save restarted the engine; the old GBrain child exited; authenticated knowledge search and `/` and `/admin` returned successfully. SQL connection to the LAN address passed; the handoff's Tailscale preference did not match current connectivity. The disabled logon task was left unchanged.
- **Knowledge:** 19/19 world checks passed against the installed laptop service and a separate fresh extraction of the shipped index (2,406 pages, all required workflow links, no foreign pages). No embeddings rebuild was necessary.
- **Server:** clean install on Windows Server 2025 Standard passed; both automatic services, HTTP pages and authenticated knowledge search worked. Forced service-tree termination recovered both services. Saving settings with SQL unconfigured restarted the engine. Uninstall removed services/firewall and retained settings/logs. Reinstall using `PORT=3418` passed, with the matching service arguments and TCP firewall rule. Settings file ACL is protected, SYSTEM/Administrators only. Server is deliberately disconnected from SQL to avoid a second claimant.
- Final Setup restored/verified 64-bit ODBC Driver 18 after uninstall testing, retained port 3418 and settings, and again passed both HTTP pages and authenticated search. Both automatic services are running. Server console: `http://10.2.6.204:3418/admin`.
- Local health helpers initially timed out using `localhost`; repeating with IPv4 `127.0.0.1` passed. Those were verification-address failures, not failed installations.
- **Regression/build checks:** 118 lifecycle tests passed; console production build and .NET publish passed; installed engine/API hashes match the release payload. `git diff --check` passed.
- **Limits:** LM Studio connection timed out; no model was loaded/unloaded and no new ticket-processing validation is claimed. Jev check confirmed a key is set, not a live reasoning response. Wizard interactions were not visually tested; installs used quiet mode, with custom port tested through MSI. No reboot/automatic-start-after-reboot test. Artifacts are unsigned; no signing certificate is available. Secrets are ACL-protected JSON, not DPAPI-encrypted.
- Empty Burn `LicenseUrl` is a documented supported way to hide the hyperlink. The guarded publisher filename remains unchanged. Retired-code cleanup, seeded-ticket reruns and L1/product changes were outside this priority and were not undertaken. Installation guide: `docs/install-windows.md`.

### Follow-up: Start menu and connections, 2026-10-02 IST

- The owner found the missing Start menu entry. Added Helpdesk (`/`) and Console (`/admin`) shortcuts to the MSI, using the configured port and the existing WiX Util extension. Added matching shortcuts immediately to the laptop user's Start menu and the server's common Start menu; read back all four targets and verified both Helpdesk pages return HTTP 200.
- Laptop SQL connection test passed again (`10.2.6.204`, SQL Server 2022). After the owner connected LM Studio, its connection test passed and returned the models listing. This establishes endpoint connectivity, not a completed ticket/inference run or exactly one loaded model.
- Server SQL/LM Studio/Jev settings are still empty. It remains an isolated installation until the owner chooses the active engine host. RDP connectivity does not populate application connection settings.

### Superseding deployment: 0.1.3, 2026-10-02 16:10 IST

- Owner explicitly chose the server as the active engine host and required independent startup/configuration: Tailscale and external services are not prerequisites for launch or saving.
- Release 0.1.3 fixes the missing Start menu shortcuts and encrypts SQL passwords, Jev keys and GBrain secrets with Windows machine-bound DPAPI. Both .NET and Python read the same protected format; existing plaintext files migrate on API startup. Writes replace configuration atomically. Explicitly clearing an address clears the process setting; blank secret inputs keep existing credentials. Settings data remains in ProgramData through upgrade/uninstall.
- Removed the packaged Tailscale model-server default and the API's hard-coded SQL host/user defaults. SQL migration waits for configuration. Connections UI loads independently of SQL-backed assistant settings.
- Offline test: empty installation returned its Connections configuration; saved fixture secrets and an unreachable model URL without testing connectivity; `/` and `/admin` returned 200; no SQL migration was attempted. .NET-to-Python and Python-to-.NET encrypted credential checks passed. Frontend check/build and .NET publish passed; 123 Python configuration/lifecycle tests passed. The rebuilt MSI has both port-aware shortcut records; Setup/MSI build passed (existing WIX1149 warning).
- Server upgrade exit 0; it served both HTTP pages before SQL/LM Studio/Jev configuration. After saving actual settings, all populated connection secrets had the DPAPI prefix, the engine restarted, SQL and LM Studio tests passed, and GBrain authenticated search passed. Jev check confirms the stored key, not a live Jev reasoning response. Embedded Python recovered zero orphaned running cards using its decrypted SQL connection.
- Laptop upgrade exit 0. Its engine was stopped and SQL address cleared before server activation, so there was no overlapping SQL claimant. Final laptop engine is Stopped/Manual; its credentials and original installation backup are encrypted. Laptop common/user Start menu and desktop shortcuts open the server at `http://10.2.6.204:3418/admin` (Helpdesk `/`). Disabled development logon task unchanged.
- Current release artifacts: `build/out/0.1.3/Chitragupta-Setup.exe`, `Chitragupta.msi`, hashes and verification records. Older 0.1.1 facts above describe the earlier install test; 0.1.3 supersedes its plaintext-secret limitation and previously unavailable LM Studio connection. Signing remains unavailable; the installer is unsigned. No claim of a new end-to-end ticket or reboot test.
