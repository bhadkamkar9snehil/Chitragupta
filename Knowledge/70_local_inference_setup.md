---
type: "Reference"
title: "Local Inference Setup -- Desktop GPU (RTX 4060, 8GB VRAM)"
description: "Real, tested settings for LM Studio and Ollama on the desktop that serves l2-investigator/infra-guardian: what settings fixed a real 3.2 tok/s -> 19.6 tok/s regression, per-model benchmark results (Qwen3.5-9B, Qwen2.5-Coder-7B, Gemma-4-12B), and why Ollama isn't yet production-deployable (a persistence problem, not a speed problem)."
status: draft
verified: "2026-09-03"
---

# Local Inference Setup (RTX 4060, 8GB VRAM, 15.9GB system RAM)

Desktop: Tailscale `B19CL3PC` / `100.111.69.102`. Hosts LM Studio (primary,
proven, currently in production) and Ollama (tested, real numbers below,
**not currently deployable** -- see "Why Ollama isn't the backend yet").

## LM Studio presets -- real files, real location

Presets are JSON files bundling sampling/system-prompt overrides, applied
via LM Studio's GUI preset selector. Official docs say the default location
is `%USERPROFILE%\.lmstudio\config-presets` -- **wrong for this machine**,
which has a custom install at `D:\LMStudioHome\.lmstudio\config-presets\`.
Always verify the real install root (`lms.exe`'s own path, currently
`D:\LMStudioHome\.lmstudio\bin\lms.exe`) before assuming the default path.

Schema: `{identifier, name, changed, operation: {fields: [{key, value}]},
load: {fields: []}}`. Keys are dotted (`llm.prediction.<setting>`); sampling
fields wrap their value as `{checked: bool, value: N}` (checked = override
enabled), plain fields (like `topKSampling`) are just the raw value.

**`OptimisedPreset 1.preset.json`** -- the real preset applied 2026-09-02
that fixed a genuine repetition-loop outage on `qwen3.5-9b`:
```json
repeatPenalty: {checked: true, value: 1.5}
minPSampling:  {checked: false, value: 0}
topKSampling:  20
```
No temperature/top_p override -- LM Studio's own defaults for those. The
elevated `repeatPenalty=1.5` is notably higher than Qwen's own official
recommendation of `repetition_penalty=1` (effectively off) -- makes sense:
breaking an active degenerate loop needs a stronger penalty than
steady-state generation would. If a similar loop recurs, this is the
proven-working value to reapply, not the vendor's "normal operation"
recommendation.

**`Hermes SQL LMEL XMES.preset.json`** -- real prior art for a related
SQL/XMES project (not this one, but same domain), worth adapting:
```json
repeatPenalty: {checked: true, value: 1.05}
minPSampling:  {checked: false, value: 0.05}
topPSampling:  {checked: true, value: 0.9}
cpuThreads: 8
systemPrompt: "...generate T-SQL for Microsoft SQL Server only. Follow
  XStudio/XMES conventions: SQLCMD variables for database names, no ORM,
  no physical foreign keys, TRY/CATCH error handling, SET NOCOUNT ON,
  SET XACT_ABORT ON, and rerunnable/idempotent scripts..."
```
A more moderate, steady-state-tuned repeat penalty (1.05, close to Qwen's
own official 1.0) plus a real domain-appropriate system prompt. Better
starting point than `OptimisedPreset 1` for normal operation once a loop
is broken -- `OptimisedPreset 1`'s 1.5 is a "stop the bleeding" value, not
necessarily the best long-run setting.

**`Coder.preset.json`** -- generic coding-assistant preset (`temperature
0.4`, `topK 25`, `repeatPenalty 1.05`, `topP 0.9`), not specific to any
one model. Reasonable default if configuring a coder-family model, though
see the Qwen2.5-Coder benchmark below -- this project's copy of that model
is slow regardless of sampling settings, so a preset alone won't fix it.

**`Qwen2.5-Coder-Optimised.preset.json`** -- built and tested 2026-09-03
(temperature 0.7, top_p 0.8, top_k 20, repeat_penalty 1.05, min_p off,
SQL/XStudio-tuned system prompt -- Qwen's own official params plus a
slightly-above-1.0 repeat penalty for safety). **Result: 3.4 tok/s warm,
statistically the same as the untuned 3.6 tok/s baseline.** This is the
conclusive proof that Qwen2.5-Coder-7B's slowness on this hardware is not
a sampling-parameter problem at all -- the preset is real, saved, and
correctly applied, and it made no meaningful difference. Don't spend more
time tuning sampling settings for this specific model; the bottleneck is
elsewhere (architecture/checkpoint, see the benchmark table).

## LM Studio -- current production config

- Model: `qwen/qwen3.5-9b`, GGUF at
  `D:\LocalModels\lmstudio-community\Qwen3.5-9B-GGUF\Qwen3.5-9B-Q4_K_M.gguf`
  (5.24GB on disk).
- Served via LM Studio's own `llama.cpp` backend
  (`D:\LMStudioHome\.lmstudio\extensions\backends\llama.cpp-win-x86_64-nvidia-cuda12-avx2-2.31.2\llama-server.exe`).
- **The real fix for the 2026-09-02 repetition-loop outage was a sampling
  preset change** (proper temperature/repetition-penalty), not an engine
  change -- confirmed by testing the same model+quant under Ollama with
  default settings and seeing no inherent improvement until Ollama's own
  settings were separately tuned. Don't re-diagnose future loops as an
  LM-Studio-specific bug; check sampling settings first.
- Native diagnostic tool: `D:\LMStudioHome\.lmstudio\bin\lms.exe` --
  `lms ps` shows live model state (`GENERATING`/idle), far more reliable
  than HTTP-timing guesses. `lms server status`/`lms server stop` have
  their own state-tracking bugs (report "not running" even while serving
  real traffic) -- don't trust those two specifically; `lms ps` and
  `nvidia-smi` are the reliable ground truth.

## Ollama -- tested settings and results

**Environment variables that mattered** (from Ollama's own
`envconfig/config.go`, confirmed live):

```
OLLAMA_HOST=0.0.0.0:11434
OLLAMA_FLASH_ATTENTION=1      # was NOT auto-enabled by default in this build
OLLAMA_KV_CACHE_TYPE=q8_0     # default is FP16; this halves KV-cache VRAM
```

**Modelfile used to import the existing GGUF (zero download)**:
```
FROM D:\LocalModels\lmstudio-community\Qwen3.5-9B-GGUF\Qwen3.5-9B-Q4_K_M.gguf
PARAMETER num_ctx 8192
PARAMETER num_gpu -1
PARAMETER num_thread 6
```
Created via `ollama create qwen3.5-9b -f <modelfile>`.

**Measured impact**: default settings (no Flash Attention, FP16 KV cache,
`num_gpu` left to Ollama's own heuristic) produced **3.2-3.6 tokens/sec**
-- unusably slow. Adding `OLLAMA_FLASH_ATTENTION=1` +
`OLLAMA_KV_CACHE_TYPE=q8_0` alone (before `num_gpu -1` was even applied)
produced **19.6 tokens/sec** -- a ~5-6x improvement. This was a genuine
config problem, not a WinRM-measurement artifact as first suspected --
confirmed because the fix reproduced across multiple separate test runs.

## Per-model results (same desktop, same settings unless noted)

| Model | Size on disk | VRAM fit | Result |
|---|---|---|---|
| `qwen3.5-9b` (Q4_K_M) | 5.24GB | Fits comfortably | **19.6 tok/s** with Flash Attention + q8_0 KV cache. Current best choice -- native tool-calling, newest Qwen generation, proven in real ticket investigations (aside from the sampling-preset issue, already fixed). |
| `qwen2.5-coder-7b-instruct` (Q4_K_M) | 4.36-4.7GB (two copies on disk, `bartowski` and `lmstudio-community`) | Fits | **Slow on BOTH engines, confirmed 2026-09-03**: Ollama 5 tok/s, LM Studio 2.7 tok/s cold / 3.6 tok/s warm (tested with official Qwen sampling params: temp 0.7, top_p 0.8, top_k 20, repeat_penalty 1). Since it's consistently slow across two independent serving engines, this is **not a serving-config problem** -- likely the `Qwen2` architecture (vs. `qwen35` for the working model, per `lms ls`) not benefiting from the same llama.cpp/CUDA optimizations, or an inefficient GGUF conversion of this specific checkpoint. Not recommended for this deployment regardless of tuning.
| `gemma4-12b-qat` (Q4_0, already in Ollama) | 7.0GB | **Does not fit** | Hard failure: `"model requires more system memory (8.1 GiB) than is available (5.6 GiB)"` -- 6.5GB CUDA weights + 787MB CPU-spillover weights + 833MB KV cache + compute graph = 8.3GB total, exceeding both the 8GB VRAM card and available system RAM. This is a genuine capacity limit, not a settings problem -- **no Gemma-4-12B variant (Q4_K_M 6.87GB, QAT-Q4_0 6.5GB) will fit this hardware.** The smaller `gemma-4-E4B-it-UD-Q4_K_XL.gguf` (4.75GB, on disk but not yet imported into Ollama) is the only Gemma variant realistically worth testing on this machine, if a Gemma-family model is ever needed. |

| `qwen/qwen3-8b` (Q4_K_M) | 5.03GB | Fits | **Real, separate problem from speed: won't stop "thinking."** Tested 2026-09-03 with Qwen3's own official non-thinking params (temp 0.7, top_p 0.8, top_k 20, min_p 0, presence_penalty 1.5) plus the documented API mechanism to disable reasoning (`chat_template_kwargs: {enable_thinking: false}`) -- **198 of 200 completion tokens still went to hidden reasoning, zero visible content produced**, both with and without the disable flag. Raw throughput on those reasoning tokens: **2.4 tok/s** -- slower than the working model even setting the content problem aside. This LM-Studio/GGUF combination doesn't respect the standard non-thinking API contract. Same failure class as the DeepSeek-R1 forced-`<think>`-block issue documented earlier in this project (see AGENTS.md) -- not recommended without a much larger `max_tokens` budget and no guarantee that's even sufficient. |

| `gemma-4-e4b-it` (7.01GB per `lms ls`) | 7.01GB | Fits | **Genuinely promising, worth further evaluation.** Tested 2026-09-03 with Gemma's own official settings (temp 1.0, top_p 0.95, top_k 64, min_p 0, repetition_penalty 1.0). Also defaults to heavy hidden reasoning (529 of 700 tokens on a first test) -- **but raw throughput is fast enough (46.4 tok/s) that it doesn't matter in practice**: produced a real, correct, complete SQL query in 15 seconds total including all the reasoning overhead. Compare Qwen3-8B, which was both slow (2.4 tok/s) AND reasoning-heavy -- a combination that made it unusable; Gemma-4-E4B is reasoning-heavy but fast enough to route around the problem. **If evaluating a replacement for qwen3.5-9b, test this one properly with real ticket-style multi-turn tool-calling work**, not just a single-shot generation -- that hasn't been done yet, and tool-calling capability specifically (needed for the agentic SQL-investigation loop) wasn't verified in this pass.

**Not yet tested**: `Qwopus3.5-9B-Coder` variants (~5GB, custom Qwen/Opus
merge), `DeepSeek-R1-0528-Qwen3-8B` (deliberately skipped -- documented
repetition-loop history with this exact family earlier in this project).

**Methodology note for future single-shot speed tests**: use a generous
`max_tokens` (500+) before concluding a model is "broken" or unusably
slow -- both Qwen3-8B and Gemma-4-E4B defaulted to heavy hidden reasoning
that a 200-token budget doesn't leave room to get past. A model that looks
broken at 200 tokens (empty content, `finish_reason: length`) may just
need more room; check `completion_tokens_details.reasoning_tokens` before
concluding anything.

## Why Ollama isn't the backend yet -- a persistence problem, not a speed one

19.6 tok/s is genuinely competitive. The blocker is keeping it *running*:

- Ollama's Windows GUI app (`ollama.exe` launched bare) fails to
  initialize when launched over a WinRM remote session
  (`"Unable to init instance: Unspecified error"`) -- it needs an
  interactive desktop session it doesn't have over WinRM. Confirmed
  reproducible every time.
- The headless alternative, `ollama serve`, works fine -- but only for
  the lifetime of the PowerShell session that launched it. Backgrounding
  it via `Start-Job` does not survive the remote session closing; the
  process dies with the session (confirmed twice: once during initial
  testing, once during a real production test where `l2-investigator` was
  pointed at Ollama and every request failed with `Request timed out`
  because the server had already died).
- `hermes gateway install` (Windows Scheduled Task) failed outright with
  `schtasks /Create failed (code 1): ERROR: The system cannot find the
  path specified` when attempted over this same WinRM session -- a
  known WinRM "double-hop" limitation (the session's security token can't
  create tasks that outlive it), not a config mistake.

**The real fix, not yet applied**: wrap `ollama serve` (with the env vars
above) as a genuine Windows Service, which runs independent of any
interactive or remote session. Options, in order of preference:
1. **Native `sc.exe create` / PowerShell `New-Service`** -- built into
   Windows, zero install. Standard tool for exactly this problem. Caveat:
   worth verifying GPU/CUDA access works correctly from a Session-0
   service context (services are more isolated from the interactive
   desktop than a normal user process); this hasn't been confirmed yet
   for Ollama specifically on this machine.
2. **Servy** (actively maintained, has a PowerShell module, real-time GUI,
   automated health recovery) if the native approach hits GPU-access
   issues -- modern replacement for the unmaintained NSSM/WinSW.
3. Fixing the Scheduled Task path-resolution error directly (root cause
   not yet diagnosed) would also unblock `hermes gateway install` for the
   same underlying reason.

Until one of these is done and verified, Ollama stays a proven-but-parked
option. Do not point `l2-investigator` or any production cron job at it
again without first confirming the server survives independent of any
interactive/remote session that configured it.
