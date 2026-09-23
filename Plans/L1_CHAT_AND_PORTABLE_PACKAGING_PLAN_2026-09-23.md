# L1 Chat Layer + Portable Laptop Packaging — Plan (2026-09-23)

Status: PLAN, not yet implemented. Non-normative until reflected in AGENTS.md /
the state machine. Scope Guard applies: reuse Hermes, Jev, GBrain, the typed
bridge and the existing SQL procedures before building anything new.

## 0. Where L2 stands (live, 6h window to 16:00 IST)

- 26 runs: 21 published, 0 failed, 5 in flight. All 10 lifecycle invariants 0.
- Response mix: 12 RESOLUTION, 4 L3, 2 UPDATE, 2 QUESTION, 1 NEEDS_HUMAN_ACTION.
- Cards fixed: review avg 11.8K chars (was 30.5K, max 95K), 0 spills in the last hour.
- Fixed today: `xstudio_select` shape guard still required `columns` (107 failures/6h).
- Still open: 4 canned "Evidence status: INCOMPLETE" replies; 115 spill-file
  reads; avg claim-to-publish 70 min (one 9B slot, WIP 1).

L1 is only worth building on an L2 that answers correctly. Phase L1-0 below is
therefore "L2 quality gate", not chat UI.

## 1. Evaluation of the ChatGPT "Qwen 9B harness" recommendations

Judged against the live report, not taken at face value.

| # | Recommendation | Verdict | Evidence |
|---|---|---|---|
| 1 | One completion path (`xstudio_submit_proposal`) | ADOPT, per role | 27 `kanban_complete` after submit, 9 metadata-less completes, 22 reviewer submit attempts. Investigator = submit only; reviewer = complete/block only. Currently enforced by guards *after* the wrong call; the fix is to not advertise the wrong tool per role. |
| 2 | Don't ask Qwen to re-route what Jev routed | ADOPT (cheap) | Route is already selected by Jev (`_selected_route_skill`); remove any remaining "pick a route" wording from the worker procedure. |
| 3 | Explicit next-action frontier on the card | ADOPT | 19 `42S02 Invalid object` raw queries + 24 blocked script writes = Qwen does not know its next legal step. Jev already produces `next_investigation_step`; render it as 1–3 concrete typed calls. |
| 4 | Fewer visible tools | ADAPT | Hermes only toggles whole toolsets (`file` = read+write+patch+search). Cannot drop `write_file` alone without a plugin tool. Keep `file` (spill reads need `read_file`); block writes in the guard. |
| 5 | Measure the whole model input | ADOPT | Report measures card body only; system prompt + tool schemas + skills are unmeasured. Extend `benchmark_l2_performance.py`, no new script. |
| 6 | Deterministic evidence compaction | DONE | `compact_run_action`, claim-cited `_review_evidence`. |
| 7 | Stable prompt prefix for KV reuse | LOW | One slot, cards differ per ticket; small gain. Revisit only if latency is dominated by prefill. |
| 8 | Executable corrective errors | MOSTLY DONE | Column resolver, outcome-field errors. Remaining: `VERIFIED needs action_id` (7/h) should auto-attach the matching current-run action when unambiguous. |
| 9 | OpenCode-style per-role permissions | SAME AS 1 | No new agents. |
| 10 | MUSE-style experience learning | ALREADY HAVE | Candidate → Approved curation on corroboration. Don't add a second store. |

Net: 1, 2, 3, 5, 8 are real and will be done in the L2 quality phase.

## 2. L1 chat layer

### Goal
A user-facing chat that answers what it can from governed knowledge and
the user's own ticket history, and **writes an L2 ticket** (Complaint_Mst_Tbl
row, status `Enter`) when it cannot. The same chat is where the user sees L2
replies and answers L2 QUESTIONs (AskStatus `Ask`) — otherwise WAITING_USER
tickets have no human channel and the loop is not self-sustaining.

### Architecture (reuse-first)

```
Browser chat UI ──► Hermes "l1-assistant" profile (gateway/API)  ──► tools:
                     model: Qwen 3.5 9B (LM Studio)                 l1_search_kb   (GBrain, Approved only)
                     Jev: ticket_security + L1 answerability        l1_my_tickets  (read own tickets + L2 replies)
                                                                    l1_create_ticket (SP, idempotent)
                                                                    l1_answer_question (SP → requester reply row)
```

- **No new DB transport.** L1 tools go through the existing typed bridge with a
  new, separate `l1` operation allowlist: read Approved KB, read own tickets,
  and exactly two write SPs. No SQL, no L2 tools.
- **Jev decides answer vs escalate.** A new Jev workflow `l1_answerability`
  (same fabric as `ticket_security`): P(answerable from cited Approved KB). Below
  threshold → create ticket. Qwen phrases; it does not decide.
- **Ticket writing is deterministic.** `Hermes_L1_Create_Ticket_Usp` takes the
  structured intake (area, complaint type, heat/WO identifiers, symptom,
  conversation transcript) and inserts one Complaint_Mst_Tbl row. Idempotency key
  = chat session + intake hash. L1 must collect identifiers (heat no, work
  order, time) the L2 evidence planner needs — that is L1's main value to L2.
- **Identity.** The chat must know which requester it is talking to (Complaint
  rows are per requester). Start with the existing XStudio user list + a simple
  login; SSO is out of scope.

### Open decision: the single GPU slot
L2 holds the only 9B slot (WIP 1), with investigations running minutes. An L1 chat
waiting behind that is unusable. Options:
1. **L1 preempts at the admission queue** (priority above review 30) and L2 cards
   yield between turns — keeps one model, adds latency to L2. *Recommended first.*
2. Load a second small model (e.g. Qwen 3.5 4B) for L1 only — needs VRAM check on
   the desktop (see `lm_studio_load_settings` notes).
3. LM Studio parallel predictions on the same model — KV cache per slot halves
   the usable context; conflicts with the 65K window the cards are sized for.

### Chat UI
Verify first (docs-first rule) what Hermes ships: gateway platforms / any
OpenAI-compatible API server. If Hermes exposes an OpenAI-compatible endpoint,
front it with an existing chat UI rather than writing one. Only if neither works,
a small single-page chat served by the same host.

### Phases
- **L1-0 L2 quality gate** — items 1,2,3,5,8 above; target: 0 canned INCOMPLETE
  replies, <20 min claim-to-publish on RESOLUTION tickets.
- **L1-1 Intake SPs** — `Hermes_L1_Create_Ticket_Usp`, `Hermes_L1_Answer_Question_Usp`
  (numbered SQL source + regenerated bundle, drift-checked), tests.
- **L1-2 l1-assistant profile + tools** — bridge `l1` allowlist, plugin tools,
  Jev `l1_answerability`, admission priority.
- **L1-3 Chat front-end + identity.**
- **L1-4 Loop closure** — L2 QUESTION → shown in chat → user answer → ticket
  re-eligible (existing Ask binding). Report gets an L1 section (answered vs
  escalated, deflection accuracy after L2 outcome).

## 3. Portable packaging (laptop)

### What the system actually is
| Component | Where today | Portable form |
|---|---|---|
| SQL Server: XStudio_Helpdesk, XStudio_Xbatch | Windows host | `.bak` backups + `00_Hermes_L2_FULL_INSTALL.sql` + postflight |
| Hermes agent + 8 profiles, GBrain, plugin, runtime | WSL (`~/.hermes`) | `wsl --export` tarball *or* rebuild via deploy script (preferred: reproducible) |
| Jev bridge + runtime code | this repo | git clone |
| Jev (TypeSafe) | `https://api.typesafe.ai` (cloud) | **needs internet + API key** |
| Qwen 3.5 9B | LM Studio on desktop (Tailscale) | laptop LM Studio + GGUF, or keep Tailscale to desktop |
| Secrets | profile `.env` (CRLF!), SQL creds | never in git; one `secrets.env.template` |

### Deliverable: `deploy/portable/`
1. `bootstrap.ps1` (Windows, idempotent): checks prerequisites (SQL Server
   Express/Developer, ODBC 18, WSL2, Python, LM Studio), restores DBs, applies SQL
   bundle + postflight, writes secrets from template (LF line endings — the CRLF
   `.env` bug), clones/updates repo.
2. `bootstrap_wsl.sh`: installs pinned Hermes version, runs
   `deploy_l2_pipeline_runtime.sh`, GBrain sync.
3. `MODEL_ENDPOINT` switch: `local` (laptop LM Studio) or `tailscale` (desktop);
   the config + restart order follows the model-switch protocol.
4. Acceptance = `validate_l2_pipeline_local.sh --full` + one seeded ticket through
   the benchmark report with invariants 0.
5. Data hygiene: the XStudio_Xbatch copy carries plant data — decide whether the
   laptop gets a full copy, a date-bounded subset, or synthetic data.

### Laptop constraint to check before anything else
A 9B model at 65K context needs a GPU with ~10–12 GB VRAM to be usable. If the
laptop cannot, the portable box runs everything except inference and reaches
the desktop over Tailscale — which is the current topology anyway.

## 4. Decisions needed from the owner
1. GPU slot policy for L1 (preempt / second model / parallel).
2. Laptop hardware (VRAM) → local vs Tailscale inference.
3. XStudio_Xbatch data on the laptop: full, subset, or synthetic.
4. L1 users: who logs in, and against which user list.
