# Antigravity SDK local-model harness: revisit later

Saved 2026-09-24 (IST) at the user's request, to revisit after the XBatch world + Jev walk work.
Source: an external review the user pasted (not written or verified by us). Claims about the SDK,
its API and its defaults are **unverified** until checked against Google's docs and the SDK repo.

## The pasted review (as given)

Google's September 23 announcement is more important for us than the Gemma headline suggests. They
have effectively published an Antigravity agent runtime/harness specifically optimized for local
models, and it supports LM Studio and arbitrary OpenAI-compatible models, not just Gemma.

### What changed

There are now two local paths:

| Path | What runs the model | Relevant to us |
|---|---|---|
| LiteRTAgentConfig | Google LiteRT + Gemma 4 26B | Not especially attractive for our current hardware |
| LocalOpenAIAgentConfig | LM Studio / Ollama / vLLM | Yes, this is the important one |

For LM Studio, Google's own example is essentially:

```python
config = LocalOpenAIAgentConfig(
    model="your-model-id",
    base_url="http://localhost:1234/v1",
).lightweight()
```

So Qwen can remain exactly where it is: inside LM Studio. Antigravity sits above LM Studio as the
agent harness.

```text
Chitragupta / Hermes
        │
        ├── Jev
        │   deterministic decomposition / routing / validation
        ▼
Antigravity SDK Agent Harness
        ├── lightweight prompt
        ├── tool selection
        ├── context management
        ├── workspace
        ├── policies
        ├── hooks
        ├── MCP
        ├── structured output
        └── bounded subagents where appropriate
        ▼
OpenAI-compatible API
        │
     LM Studio
        ▼
   Qwen 3.5 9B
```

### The .lightweight() part is particularly important

It addresses the question "is our harness the correct way to build around a small model such as
Qwen 3.5 9B?" Google built a preset for smaller/local models. `.lightweight()` reportedly:

- reduces the number of exposed tools;
- uses much smaller system instructions;
- removes unnecessary prompt overhead;
- disables background subagents;
- uses context compaction;
- optimizes model/tool interaction for constrained local models.

Google describes it as a minimal tool set, minimal system prompting, and background subagents
disabled to reduce context exhaustion and latency. External validation of our conclusion: small
models should not get the same giant agent environment built for Gemini/Claude/Codex; the harness
does more so the model does less.

### Other ideas worth taking

- **Context compaction**: older trajectory compacted after a configurable token threshold.
- **Tool-output truncation**: large terminal/database/tool results not pushed verbatim into
  context (valuable for our SQL and GBrain operations).
- **Tool scoping**: a subagent's tools stay invisible to the root agent.
- **Structured tool schemas**: schema normalization for local OpenAI-compatible models, which are
  sensitive to malformed or overly complex tool definitions.
- **Policies and hooks**: rules enforced by the runtime, not remembered by the model.
- **Budget controls**: explicit model-call/token budgets for bounded small-model loops.
- **MCP + local models**: another route to expose GBrain/SQL/Helpdesk without packing
  implementation details into Qwen's context.

### Do not replace Jev with it

Jev keeps deterministic System-One work: classification, decomposition, typed extraction, routing,
validation, evidence shaping, control decisions. Antigravity is interesting as the execution
harness around Qwen once a task actually reaches the model.

```text
                  ┌──── GBrain
Request → Hermes → Jev
                  ├──── deterministic answer/action
                  └──── reasoning required
                           ▼
                 Antigravity lightweight harness
                           ▼
                     Qwen 3.5 9B
                           ▼
                      typed tools
                           ▼
                 validate / execute
                           ▼
                          Jev
```

### Do not switch to Gemma 4 26B because Google demonstrates it

Google recommends at least 24 GB VRAM/shared memory for the 26B LiteRT model; the checkpoint is
about 16.8 GB. On the current RTX 4060 + GTX 1660 Ti / 16 GB RAM setup, stay with LM Studio + Qwen.
The useful part is the harness, not the model.

### Caveat

The SDK repository is Apache-licensed, but the README says it relies on a compiled runtime binary
shipped in platform-specific PyPI wheels; cloning the repo alone is not enough. Do not make the
helpdesk irreversibly dependent on an opaque runtime. Put it behind an adapter:

```text
Hermes
  └── LocalAgentHarness
           ├── AntigravityHarness
           └── ExistingQwenHarness
```

### Suggested next step (from the review)

Use Antigravity as a reference implementation and compare it against the current Chitragupta Qwen
harness before further speculative harness work:

| Area | Compare |
|---|---|
| System prompt | ours vs Antigravity lightweight |
| Tool count | what Qwen actually sees |
| Tool schema | complexity/token cost |
| Tool selection | model vs deterministic routing |
| Tool output | truncation/filtering |
| Context | compaction strategy |
| Memory | GBrain injection strategy |
| Planning | Jev vs model planning |
| Retries | malformed output recovery |
| Structured output | schema enforcement |
| Subagents | whether they are justified at 9B |
| Loops | maximum calls/termination |
| Validation | before tool execution |
| Policies | deterministic enforcement |
| Workspace | filesystem isolation |
| Observability | traces/tool/model steps |
| Failure recovery | invalid calls/context exhaustion |
| Token overhead | tokens before actual task |
| Qwen-specific handling | thinking/tool quirks |

References named in the review: Google's local-model documentation; Antigravity SDK source
repository (links not included in the paste).

## Our notes for when we revisit

- Current direction already matches much of this: Qwen is writer-only, Jev does routing and
  judgement, the harness fires SQL, tools are per-role and minimal.
- First verify the claims (API names, `.lightweight()` behaviour, LM Studio support, binary
  runtime) against the actual docs/wheel before designing anything.
- Research of this kind goes to Antigravity/Codex via Agent_Comms per standing practice.
