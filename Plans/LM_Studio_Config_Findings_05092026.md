# LM Studio configuration findings (2026-09-05)

Real, verified findings from a live debugging session against the desktop
LM Studio instance (100.111.69.102:1235, LM Studio 0.4.23, CLI commit
`07b7252`, `bhadk` Windows account). Written up because this cost real
time to root-cause and the next session/agent should not have to
re-derive any of it.

## The actual crisis: 0% ticket completion, root-caused

Not a Kanban bug, not an orchestration bug. Two independent, compounding
LM Studio-side issues:

### 1. "Enable Thinking" (reasoning mode) breaks tool-calling on 9B models

With Enable Thinking ON and Reasoning Budget "Unrestricted," both models
tested (`qwopus3.5-9b-coder` and `qwen/qwen3.5-9b`) would either:
- burn the entire token budget on reasoning and emit empty `content` with
  `tool_calls: []`, or
- get stuck in a genuine repetitive reasoning loop re-reading/re-guessing
  the tool's exact name ("wait, is it `kanban_complete` or
  `KanbanComplete`... actually reading through very clearly now...")
  without ever emitting a structural tool call, confirmed live in LM
  Studio's own Developer Logs panel.

Verified via direct `/v1/chat/completions` calls with `tools` +
`tool_choice: "required"` (which should make a non-tool-call response
structurally impossible) — it wasn't enforced; the model produced
unrelated hallucinated prose instead. This is not an LM Studio
enforcement bug reserved for edge cases; it happened on real, realistic
investigation-shaped prompts, repeatably.

**Fix**: turn **Enable Thinking OFF** and cap **Reasoning Budget to a
real number** (800, not Unrestricted). Verified before/after:
- Thinking ON: 0/3 real tool calls on a domain-investigation prompt.
- Thinking OFF: 2/3 real, correct tool calls (still not 100% — see
  "still open" below).

**Do not set Structured Output at the same time as this.** LM Studio's
model-level Structured Output setting forces every completion's
`content` into a fixed JSON schema — including tool-calling turns. Live
tested: with Structured Output ON, `tool_calls` was `[]` on every
attempt regardless of the Thinking/Reasoning-Budget fix, because the
model was forced to stuff its output into schema-shaped JSON text
instead of a real function call. **Structured Output and Hermes's
tool-calling mechanism (kanban_complete/kanban_block) are incompatible
on this server — do not enable both on the same model.**

### 2. GPU VRAM overcommit, present since the original gemma→qwopus swap

LM Studio's own `main.log` (see location below) showed, at every model
load:
```
Model load size estimate ... Total: 10.07 GB
GPU 0: RTX 4060, Total: 8.59 GB, Free: 200-311 MB
Strict GPU VRAM cap is OFF: GPU offload layers will not be checked for adjustment
```
Model (6.27-6.75GB depending on which model) + full-precision KV cache
at 65536 context (3.33GB) exceeds the RTX 4060's 8.59GB VRAM, and
`Strict GPU VRAM cap` being OFF means LM Studio doesn't auto-adjust —
it loads anyway and spills into **Shared GPU memory** (confirmed live in
Windows Task Manager's GPU Performance tab: ~1.5GB spilling into shared/
system-RAM-backed memory). Shared GPU memory is dramatically slower
(PCIe round-trip to system RAM), and this has likely been degrading
generation quality/latency since the very first qwopus load, not just
today.

**Do not fix this by reducing Context Length.** Hermes's own
`config.yaml` hard-requires 65536 context (already root-caused once
before — a "Context size has been exceeded" crash at ~9-11K tokens on a
smaller effective budget). Cutting context length to fit VRAM would
silently reintroduce that exact bug.

**Fix: quantize the KV cache instead (K/V Cache Quantization → q4_0).**
This shrinks the *memory representation* of the context, not the
context length itself — Hermes still gets its full 65536-token window.
Verified live: Context memory dropped from 3.33GB (fp16) to 1.04GB
(q4_0), bringing total to 7.81GB — comfortably under 8.59GB, spillover
eliminated.

## Still open / not fully solved

- Even with Thinking OFF, tool-calling isn't 100% reliable (~67% in a
  3-trial sample) and `response_type` values sometimes don't match the
  required enum (e.g. "Finding" instead of `UPDATE`/`RESOLUTION`/etc.).
  This is a lower-severity, safe-failure issue — `Hermes_L2_Publish_
  Response_Usp` already validates `@ResponseType` and rejects bad
  values at publish time rather than corrupting data — but it means the
  pipeline still needs the existing reject/rework/escalation loop to
  actually work, not a "fixed" 100%-clean model.
- Whether this genuinely moves the needle on real ticket resolution
  hasn't been re-measured yet after all three fixes (thinking off,
  reasoning budget capped, KV cache quantized) landed together. Next
  step: re-run `Model_Bench/model_scorecard.py` against a fresh window
  and check real `Hermes_L2_Response_Trn_Tbl` outcomes, not just
  isolated curl tests.

## How to configure these settings — the real gaps LM Studio has

### `lms` CLI (confirmed, from `lms load --help`)
Exposes: `--gpu`, `--context-length`, `--parallel`, `--ttl`,
`--identifier`, speculative-decoding flags. **Does NOT expose**: K/V
cache quantization type, Reasoning Budget, Enable Thinking, Structured
Output. No raw-flag passthrough to llama.cpp either (no
`--extra-flags`/`--llama-args`).

### `@lmstudio/sdk` (Node.js) — confirmed what it does and doesn't cover
Installed at `C:\Users\bhadk\lms-sdk-tool` on the desktop (`npm install
@lmstudio/sdk`), working script at
`C:\Users\bhadk\lms-sdk-tool\load-quantized.js`. Directly verified
against the SDK's own 9920-line `dist/index.d.ts`:

| Setting | SDK support | Verified how |
|---|---|---|
| K/V Cache Quantization | **YES** — `llamaKCacheQuantizationType`/`llamaVCacheQuantizationType` in the model-load `config` object | Live-tested, confirmed via LM Studio's own log showing the memory drop |
| Context Length, GPU offload, Flash Attention, offload-KV-to-GPU | **YES** — same load `config` object | Live-tested, model loaded successfully with these set |
| Structured Output (JSON schema) | **YES** — `structured` field on `LLMPredictionConfigInput`, **per-request** (via `model.respond()`/`model.complete()`), not persistent | Confirmed in type definitions (`structured?: {...} \| LLMStructuredPredictionSetting`) |
| Reasoning Budget | **NO** — grepped the entire SDK type-definition file for `reasoningBudget`/`budgetTokens`/`thinking`/`enableThinking` — zero matches anywhere | Exhaustive grep, not a guess |
| Enable Thinking | **NO** — same exhaustive grep, zero matches | Exhaustive grep |
| Raw/manual tool-calling | **Marked `@deprecated` in the SDK itself** — "Raw tools are currently not well-supported. It may or may not work. If you want to use tools, use `model.act` instead." This doesn't affect Hermes (which talks to LM Studio over plain REST, not this SDK), but matters for any future tooling built with this SDK. | Read directly in the type definitions |

**Conclusion: the SDK is sufficient for KV cache quant + load-time
config + per-request structured output. It is NOT sufficient for
Reasoning Budget / Enable Thinking — those remain GUI-only or
preset-file-only settings**, which is why they had to be set by hand in
LM Studio's Inference tab this session.

### Preset file location — actively being searched, not yet found

A ChatGPT research report claimed presets live at
`%USERPROFILE%\.lmstudio\config-presets\*.preset.json`. **Verified false
for this specific install** — `Test-Path "$env:USERPROFILE\.lmstudio"`
returns `False` on the desktop (`bhadk` account). This LM Studio install
stores its Electron app data under `C:\Users\bhadk\AppData\Roaming\LM
Studio` instead, which contains only `config.json` (window bounds),
`settings.json` (empty), and `logs\main.log` — no preset store found
there either on a targeted name-pattern search.

A full-drive (`C:\`, `D:\`, `F:\`) recursive search for `*.preset.json`
was launched to find the real location; check back for results before
assuming either the `.lmstudio` path or the `AppData\Roaming` path is
correct. **Do not trust an LLM-generated report's specific file paths
without verifying `Test-Path` first** — this is the second time this
session a plausible-sounding but wrong path was caught before being
acted on.

## Reference: working commands used this session

Eject a model:
```powershell
& "C:\Program Files\LM Studio\resources\app\.webpack\lms.exe" unload <model-id>
```

Check what's loaded:
```powershell
& "C:\Program Files\LM Studio\resources\app\.webpack\lms.exe" ps
```

Load with quantized KV cache (the only reliable way found for this):
```javascript
// C:\Users\bhadk\lms-sdk-tool\load-quantized.js
const { LMStudioClient } = require("@lmstudio/sdk");
const client = new LMStudioClient();
const model = await client.llm.load("qwen/qwen3.5-9b", {
  identifier: "qwen/qwen3.5-9b",
  config: {
    contextLength: 65536,
    gpu: { ratio: "max" },
    flashAttention: true,
    offloadKVCacheToGpu: true,
    useFp16ForKVCache: false,
    llamaKCacheQuantizationType: "q4_0",
    llamaVCacheQuantizationType: "q4_0",
  },
});
```
Run via WinRM: `Invoke-Command -ComputerName 100.111.69.102 -Credential
$cred -ScriptBlock { node ~/lms-sdk-tool/load-quantized.js }`.

LM Studio's real log location (for future debugging — don't re-search):
`C:\Users\bhadk\AppData\Roaming\LM Studio\logs\main.log`.
