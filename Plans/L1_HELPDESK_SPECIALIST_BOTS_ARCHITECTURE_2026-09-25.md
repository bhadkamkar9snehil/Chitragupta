# L1 Helpdesk Architecture: Jev Intake Routing, Hermes Specialist Executives, GBrain, and UI/Product Shell Options

**Status:** Architecture proposal / decision record  
**Date:** 2026-09-25  
**Scope:** Chitragupta L1 user-facing helpdesk and handoff into the existing L2 pipeline  
**Related issue:** #21  
**Implementation status:** Not implemented by this document

---

## 1. Executive summary

The recommended L1 architecture is **not** a generic chatbot attached directly to the database, and it is **not** a swarm of autonomous agents discussing every ticket.

The preferred design is:

1. A user enters through one customer-facing helpdesk/chat surface.
2. Chitragupta owns the L1 application boundary.
3. Jev performs typed intake classification at explicit decision points.
4. One Hermes specialist profile is selected as the primary L1 executive.
5. Specialist profiles share governed organizational knowledge through GBrain.
6. The specialist either:
   - answers from sufficient governed evidence,
   - asks the user for missing information,
   - requests one bounded cross-domain handoff, or
   - escalates by invoking one deterministic ticket-creation path.
7. `dbo.Complaint_Mst_Tbl` remains the authoritative Helpdesk incident store.
8. The existing L2 pipeline remains the authoritative investigation/resolution lifecycle.
9. L2 replies and L2 QUESTIONs return to the same L1 conversation.

The initial specialist set should remain deliberately small:

- `l1-frontdesk`
- `l1-sap`
- `l1-mes`
- `l1-xstudio`

Additional specialists should be created only when toolsets, permissions, evidence sources, or evaluation requirements are materially different.

The recommended architecture is therefore:

```text
                           USER
                            |
                            v
                  Helpdesk / Chat Surface
                            |
                            v
                   Chitragupta L1 API
                            |
                            v
                      Jev Intake
              +-------------+-------------+
              |             |             |
        SystemDomain     PlantArea       Intent
              |
              v
          route ONE
        primary specialist
      +-------+-------+---------+
      |               |         |
      v               v         v
   l1-sap          l1-mes   l1-xstudio
      \               |         /
       \              |        /
        +---------- GBrain -----+
                    |
                    v
              specialist result
                    |
                    v
             Jev answerability
         +----------+-----------+
         |          |           |
       ANSWER     ASK_USER    ESCALATE
         |          |           |
         |          |           v
         |          |   governed ticket create
         |          |           |
         |          |           v
         |          |  dbo.Complaint_Mst_Tbl
         |          |           |
         |          |           v
         |          |       existing L2
         |          |           |
         +----------+-----------+
                    |
                    v
             same user conversation
```

---

## 2. Non-negotiable architectural principles

### 2.1 One authoritative ticket store

The authoritative user-visible incident remains:

```text
XStudio_Helpdesk.dbo.Complaint_Mst_Tbl
```

An external chat/helpdesk shell may store conversation state, contact information, presentation metadata, or correlation IDs, but it must not become an independent source of truth for the Chitragupta ticket lifecycle.

### 2.2 One governed write path

The browser, LibreDesk, ChatterMate, Hermes profile, or language model must **never** receive database credentials and perform arbitrary writes to `Complaint_Mst_Tbl`.

The intended path is conceptually:

```text
external conversation
        |
        v
Chitragupta L1 API
        |
        v
validate + authorize + idempotency
        |
        v
Hermes_L1_Create_Ticket_Usp
(or equivalent governed operation)
        |
        v
Complaint_Mst_Tbl
```

### 2.3 L1 must not duplicate L2

L1 exists to:

- understand the user's issue,
- retrieve governed knowledge,
- resolve simple/known issues,
- collect missing identifiers,
- classify the issue,
- create a complete ticket when needed,
- keep the user in the loop.

L1 must not duplicate:

- world-walk investigation,
- L2 evidence gathering,
- L2 reviewer lifecycle,
- L3 escalation lifecycle,
- publication rules,
- L2 state ownership.

### 2.4 GBrain remains shared organizational truth

Hermes specialist profiles may have their own local memory for role-specific working context, but shared support knowledge should remain governed through GBrain.

Do not create separate copies of the same operational truth inside each bot.

### 2.5 The UI/helpdesk product must not become the intelligence authority

LibreDesk, assistant-ui, ChatterMate, or another shell may own:

- conversation rendering,
- user identity,
- inbox UX,
- notifications,
- human handoff,
- chat persistence.

It must not silently take ownership of:

- domain routing,
- ticket semantics,
- operational truth,
- SQL writes,
- L2 lifecycle,
- evidence authority.

---

## 3. Deployment constraints

Current practical constraints:

- Windows host
- WSL available
- no Docker
- SQL Server remains authoritative for Chitragupta application/ticket data
- local inference is available through LM Studio / OpenAI-compatible interfaces
- one small-model inference slot should be treated as scarce
- current architecture already uses Hermes, Jev, GBrain and deterministic SQL procedures

### 3.1 Persistence decision gate

LibreDesk's non-Docker binary installation still requires:

- PostgreSQL
- Redis

Therefore:

- if the rule is **"all Chitragupta/business/plant/ticket data must stay in SQL Server"**, LibreDesk can still be considered because its PostgreSQL/Redis are internal helpdesk product state;
- if the rule is **"SQL Server must be the only persistence technology on the machine"**, LibreDesk is disqualified.

This must be decided explicitly before committing to LibreDesk.

---

# 4. Product-shell options

## 4.1 assistant-ui + Tool UI: backend-preserving option

### Role

assistant-ui is the preferred option when Chitragupta itself remains the application and only the L1 conversational product surface is missing.

### Ownership

assistant-ui owns:

- chat rendering,
- streaming UX,
- thread UX,
- structured tool/result rendering,
- question forms,
- ticket cards,
- retry/error presentation,
- accessibility and interaction state.

Chitragupta owns everything else.

### Proposed topology

```text
assistant-ui
    |
    | REST / SSE / custom runtime
    v
Chitragupta L1 API
    +-- Jev intake
    +-- GBrain
    +-- Hermes specialist profiles
    +-- governed ticket tools
    |
    v
Complaint_Mst_Tbl
    |
    v
existing L2
```

### Advantages

- no Docker
- no second helpdesk state machine
- no extra application database merely for the UI
- maximum control
- easiest fit with the current deterministic architecture
- specialist Hermes profiles can remain entirely hidden behind Chitragupta
- easy to render L2 QUESTION / ticket cards as purpose-built components
- minimal architectural duplication

### Disadvantages

We still need to implement/productize:

- user identity/session handling
- conversation persistence if required
- agent inbox if human L1 staff need one
- notifications
- human takeover UX
- administration
- support analytics
- possibly attachments/history/search

### Use when

> Chitragupta is the product; the missing piece is a high-quality L1 interface.

References:

- https://github.com/assistant-ui/assistant-ui
- https://github.com/assistant-ui/tool-ui

---

## 4.2 LibreDesk: heavy-lifting helpdesk option

### Role

LibreDesk is the preferred heavy-lifting candidate when we want an existing helpdesk product to own much of the customer-support shell while Chitragupta remains the intelligence/ticket engine.

### LibreDesk can own

- live-chat widget
- contact identity
- conversation history
- shared inbox
- human-agent handoff
- unread state
- notifications
- email continuation
- help center
- basic automations
- agent UI
- activity/audit UX
- customer conversation continuity

### Chitragupta should still own

- Jev classification
- GBrain operational knowledge
- Hermes specialist profiles
- deterministic ticket creation
- SQL Server ticket truth
- L2 lifecycle
- World Walk
- audited operational evidence
- final L2 publication semantics

### Preferred integration

```text
LibreDesk
    |
    v
Chitragupta L1 API
    |
    +-- classify_intake
    +-- search_gbrain
    +-- invoke_specialist
    +-- create_ticket
    +-- get_ticket
    +-- answer_l2_question
    |
    v
existing Chitragupta backend
```

### Proposed external tools

Expose narrow tools such as:

```text
search_gbrain(query, domain, area, context)

create_chitragupta_ticket(intake)

get_chitragupta_ticket(ticket_id)

answer_chitragupta_question(ticket_id, answer)
```

Do not expose:

- arbitrary SQL
- arbitrary stored-procedure execution
- unrestricted Hermes toolsets
- direct GBrain mutation
- L2 internal state mutation

### GBrain and LibreDesk KB should have different jobs

A clean split is:

```text
LibreDesk KB
------------
static user help
password/reset instructions
how to open Helpdesk
general policies
simple FAQs

GBrain
------
approved XStudio operational knowledge
MES facts
SAP/MES interface knowledge
verified system behavior
curated resolved-case knowledge
technical operational facts
```

Do not duplicate the same support facts in both stores unless there is a deliberate publication process.

### Advantages

- much less L1 product work
- ready-made conversation persistence
- ready-made human-support workflow
- existing agent inbox
- existing contact identity
- easier operational rollout
- OpenAI-compatible AI integration can be used where helpful
- custom HTTP tools can call Chitragupta

### Disadvantages

- PostgreSQL + Redis are introduced
- more application state exists outside SQL Server
- LibreDesk's own AI/automation must be prevented from becoming a second routing authority
- integration must keep `Complaint_Mst_Tbl` authoritative
- some L1 responsibilities become split between two products

### Use when

> Chitragupta is the intelligence/ticket engine; LibreDesk is the user-facing support product.

References:

- https://github.com/abhinavxd/libredesk
- https://support.libredesk.io/

---

## 4.3 ChatterMate: technically compelling, currently not preferred

ChatterMate deserves continued attention because it already includes:

- AI agents
- human handoff
- workflows
- KB grounding
- MCP tools
- ticketing/investigation features
- evidence-oriented AI investigation
- OpenAI-compatible model support

### Why it is attractive

Its MCP support could make GBrain integration elegant.

A future GBrain MCP surface could expose:

```text
search_approved_knowledge
find_known_resolution
get_system_fact
get_domain_context
```

### Why it is not the current selection

#### 1. Docker-first supported deployment

The official self-hosting path is container-centric.

The current deployment constraint is explicitly:

> no Docker

A manually reconstructed native install would increase operational risk and would not be the preferred supported topology.

#### 2. Excessive overlap with Chitragupta

ChatterMate increasingly overlaps with existing Chitragupta responsibilities:

| ChatterMate capability | Existing Chitragupta capability |
|---|---|
| AI ticket triage | Jev / typed intake |
| ticket investigation | World Walk |
| tool investigation | typed bridge |
| evidence capture | Hermes trace |
| root-cause output | L2 response |
| knowledge | GBrain |
| agent orchestration | Hermes profiles |
| ticket lifecycle | Helpdesk SQL + L2 runtime |

Adopting these overlapping features would reintroduce duplicate owners.

### Position

Keep ChatterMate as a watch-list option, especially if:

- native non-Docker deployment becomes officially supported,
- MCP becomes strategically important,
- we decide to replace a larger portion of Chitragupta rather than merely front it.

Reference:

- https://github.com/chattermate/chattermate.chat

---

# 5. Jev's role in L1

Jev should be used as a **typed decision service at explicit boundaries**, not as continuous decorative classification and not as a replacement for deterministic rules.

## 5.1 Do not overload the word "Area"

Chitragupta already has plant/production area concepts.

L1 should classify at least three separate dimensions.

### System domain

```text
SAP
MES
XSTUDIO
INFRASTRUCTURE
GENERAL
UNKNOWN
```

### Plant area

```text
EAF
LRF
CCM
COMMON
UNKNOWN
```

### Intent

```text
INCIDENT
HOW_TO
ACCESS
DATA_CHECK
CHANGE_REQUEST
STATUS
UNKNOWN
```

Optional later dimensions may include:

- urgency/impact
- user role
- entity completeness
- likely cross-domain dependency

## 5.2 Intake classification example

User:

> Heat 1604015 posted from EAF but the material document is not visible in SAP.

Desired typed outcome conceptually:

```json
{
  "system_domain": {
    "primary": "SAP",
    "alternatives": ["MES"],
    "confidence": 0.86
  },
  "plant_area": {
    "primary": "EAF",
    "confidence": 0.96
  },
  "intent": {
    "primary": "INCIDENT",
    "confidence": 0.91
  },
  "entities": {
    "HeatNo": "1604015"
  }
}
```

Exact schemas and thresholds must be evaluated on real L1 traffic.

## 5.3 Decision order

Use deterministic routing before Jev when the evidence is explicit.

```text
Strong deterministic route?
       |
  +----+----+
  |         |
 yes        no
  |         |
  v         v
route      Jev
```

Examples of deterministic signals:

- explicit trusted system selection
- known typed error codes
- an operation tied to one system only
- a trusted conversation context already bound to a domain

Use Jev for ambiguous natural language.

---

# 6. Recommended Jev decision points

## 6.1 Decision point A: intake/domain routing

Immediately after normalization:

```text
message
  |
  v
normalize + extract obvious entities
  |
  v
Jev L1 intake classification
  |
  +-- system_domain
  +-- plant_area
  +-- intent
  +-- confidence
  |
  v
route ONE primary specialist
```

## 6.2 Decision point B: answerability

After the specialist retrieves relevant GBrain evidence and/or bounded tool evidence:

```text
specialist evidence
       |
       v
Jev answerability
       |
 +-----+------+----------------+
 |            |                |
ANSWER      ASK_USER       CREATE_TICKET
```

Potential typed outcomes:

```text
ANSWER
ASK_USER
CREATE_TICKET
HUMAN_HANDOFF
```

The model should not decide "I feel confident enough" using free-form self-assessment.

## 6.3 Decision point C: domain transition

If evidence shows that the original domain is no longer the responsible subsystem:

```text
SAP specialist
    |
    | evidence: SAP never received payload
    v
Jev transition decision
    |
    v
MES specialist
```

A cross-domain transition must be justified by evidence or explicit classification, not by unconstrained bot conversation.

## 6.4 Decision point D: escalation completeness

Before ticket creation, Jev can judge whether the intake is complete enough to be useful to L2.

For example:

```text
required:
- symptom
- system domain
- plant area if relevant
- important identifiers (HeatNo / WorkOrder / BatchNo / etc.)
- approximate time if relevant
- user-visible error/message
```

If not complete:

```text
ASK_USER
```

instead of creating a poor ticket that L2 must immediately bounce back.

---

# 7. Hermes specialist executives

Hermes profiles are a strong fit because specialization can vary:

- SOUL
- skills
- toolsets
- MCP servers
- local memory
- model settings
- credentials
- profile description
- persistent role context

The specialist should be treated as an **execution profile**, not merely a persona.

## 7.1 Initial profiles

### l1-frontdesk

Responsibilities:

- preserve conversation continuity
- collect basic context
- call deterministic/Jev intake routing
- dispatch one specialist
- present results
- request missing user inputs
- call the governed ticket operation
- never perform deep system investigation

Tool access should be minimal.

### l1-sap

Responsibilities:

- SAP/MES integration issues
- goods movement
- production posting
- material documents
- result recording
- usage decision
- ERP interface failure evidence

Example allowed tools:

```text
search_gbrain(scope=SAP)
get_ticket_context
sap_get_production_posting
sap_get_material_document
sap_get_goods_movement
sap_get_result_recording
ask_user
return_l1_result
request_domain_transition
```

### l1-mes

Responsibilities:

- production state
- heats
- work orders
- batches
- genealogy
- MES process state

Example allowed tools:

```text
search_gbrain(scope=MES)
get_ticket_context
mes_get_heat
mes_get_work_order
mes_get_batch
mes_get_genealogy
mes_get_process_state
ask_user
return_l1_result
request_domain_transition
```

### l1-xstudio

Responsibilities:

- XStudio application behavior
- page/widget/configuration issues
- data-source wiring
- runtime application problems
- XStudio metadata

Example allowed tools:

```text
search_gbrain(scope=XSTUDIO)
get_ticket_context
xstudio_get_page
xstudio_get_widget
xstudio_get_datasource
xstudio_get_config
xstudio_search_metadata
ask_user
return_l1_result
request_domain_transition
```

---

# 8. Why specialist profiles help small models

The specialization is primarily valuable because it shrinks the model's action space.

## Single large bot

A general L1 bot might see:

```text
search_gbrain
search_ticket
sap_get_posting
sap_get_material_document
sap_get_goods_movement
mes_get_heat
mes_get_batch
mes_get_work_order
mes_get_genealogy
xstudio_get_page
xstudio_get_widget
xstudio_get_datasource
xstudio_get_config
ticket_create
ticket_answer
...
```

The model must decide:

- what the user means,
- which subsystem applies,
- which tools are relevant,
- which evidence is authoritative,
- whether to hand off,
- whether to escalate.

This increases tool-selection entropy and prompt/schema size.

## Specialist bot

An SAP specialist may see only:

```text
search_gbrain
sap_get_posting
sap_get_material_document
sap_get_goods_movement
sap_get_result_recording
get_ticket_context
ask_user
return_l1_result
```

The model performs a smaller, more bounded job.

This is particularly relevant for Qwen 3.5 9B.

---

# 9. Single bot versus multiple specialist bots

## 9.1 Single bot advantages

### Simpler routing

```text
User -> one bot
```

No classifier can misroute the ticket.

### Continuous context

One agent sees the complete conversation without handoff packaging.

### Cross-domain issues are easy

A single bot can inspect SAP, MES and XStudio without changing profiles.

### Lower configuration overhead

Only one:

- SOUL
- tool configuration
- test harness
- profile lifecycle
- memory store

### Lower orchestration latency

No domain-dispatch step.

---

## 9.2 Single bot disadvantages

### Larger tool space

The model must choose among many unrelated tools.

### Larger prompt/tool-schema context

This is particularly undesirable for a small local model.

### Coarser permissions

An XStudio question may expose SAP or MES tools that are not needed.

### Harder evaluation

A failure may originate from:

- routing,
- retrieval,
- tool selection,
- domain reasoning,
- investigation,
- answerability.

Everything is blended into one profile.

### Larger blast radius

One bad prompt/tool permission affects all domains.

### Harder specialization

SAP-specific instructions compete with MES/XStudio guidance in one system context.

---

## 9.3 Multi-bot advantages

### Smaller action space

Each specialist sees only relevant tools.

### Stronger least privilege

Per-domain tools and credentials can be isolated.

### Smaller prompts

The SOUL and instructions can be narrowly focused.

### Better testing

Maintain independent suites:

```text
tests/l1/sap/
tests/l1/mes/
tests/l1/xstudio/
```

Measure:

- routing accuracy
- retrieval accuracy
- tool-selection accuracy
- answer correctness
- escalation correctness

### Better failure containment

A broken SAP prompt/tool does not change XStudio behavior.

### Better evolution

Specialists can gain domain-specific tools without inflating every other profile.

---

## 9.4 Multi-bot disadvantages

### Routing becomes a failure mode

```text
user -> classifier -> specialist
```

A wrong route can invalidate the whole run.

Mitigation: deterministic signals first, Jev for ambiguity, explicit confidence/fallback.

### Cross-domain incidents require handoff

Industrial application failures are often chains:

```text
XStudio UI
   ->
MES state/procedure
   ->
SAP interface
```

A specialist architecture must support evidence-backed domain transitions.

### More profile configuration

Multiple:

- SOUL files
- tool allowlists
- skills
- tests
- deployments
- observability labels

### Native memory fragmentation

Hermes profile memories are separate.

Mitigation: shared truth is GBrain; local profile memory is not the organizational KB.

### Latency can explode if implemented as a swarm

Do not run:

```text
frontdesk model
  -> SAP model
      -> MES model
          -> XStudio model
```

for routine L1.

The target is:

```text
Jev
 -> ONE specialist
 -> done
```

A second specialist is exceptional and evidence-backed.

---

# 10. Recommended model: bounded specialist routing, not a swarm

The system should not ask all specialists for opinions.

Bad:

```text
SAP bot ----+
MES bot ----+--> debate --> answer
XStudio bot-+
```

Preferred:

```text
Jev
 |
 v
one primary specialist
 |
 +-- enough evidence -> answer
 |
 +-- missing user info -> ask
 |
 +-- evidence indicates another domain
       |
       v
   one bounded handoff
```

A maximum specialist-hop policy should be considered for L1, for example:

```text
primary specialist
+ at most one cross-domain consultation
```

If the issue remains unresolved after that, create the L2 ticket rather than allowing agent loops.

---

# 11. Multiple bots do not require multiple model instances

Specialization is a profile/runtime concept.

All profiles may use the same inference endpoint:

```text
                     LM Studio
                  Qwen 3.5 9B
                       ^
          +------------+------------+
          |            |            |
       l1-sap       l1-mes      l1-xstudio
```

The profiles differ in:

- tools
- SOUL
- skills
- permissions
- local memory
- role description

They do not need separate loaded copies of the model.

### GPU/concurrency policy

Given a constrained local inference slot:

- do not run specialist turns concurrently by default;
- serialize L1 model use;
- use Jev/deterministic routing before consuming the model slot;
- favor deterministic/GBrain answers when possible;
- avoid bot-to-bot conversations unless needed.

---

# 12. GBrain as the shared organizational memory

This is a central architectural benefit of the specialist model.

```text
                  GBrain
             shared governed truth
          +----------+-----------+
          |          |           |
        SAP         MES       XStudio
      specialist  specialist  specialist
```

### Specialist-local memory should contain

- role-specific working preferences
- temporary interaction patterns
- possibly profile-specific operational hints that are not organizational facts

### GBrain should contain

- approved technical facts
- validated system behavior
- known resolutions
- curated cross-domain knowledge
- promoted lessons
- shared support knowledge

### Do not rely on copying profile memory

Avoid:

```text
copy SAP memory -> MES memory -> XStudio memory
```

That creates synchronization and authority problems.

---

# 13. Cross-domain handoff contract

A specialist must not simply say "ask the MES bot."

The handoff should be typed and evidence-backed.

Conceptually:

```json
{
  "from_domain": "SAP",
  "to_domain": "MES",
  "reason": "No SAP receipt exists for the operation; source outbound record must be checked.",
  "evidence_refs": ["action-123", "gbrain-fact-456"],
  "entities": {
    "HeatNo": "1604015",
    "WorkOrder": "..."
  },
  "question": "Confirm whether the MES outbound posting record was generated."
}
```

The next specialist receives a compact handoff package, not the entire uncontrolled reasoning trace.

---

# 14. L1 answerability contract

The specialist should return a structured result.

Conceptually:

```json
{
  "domain": "SAP",
  "status": "PROPOSED_ANSWER",
  "answer": "...",
  "evidence_refs": ["..."],
  "missing_fields": [],
  "suggested_next_domain": null
}
```

Jev then performs the answerability judgment against evidence and policy.

Possible final actions:

```text
ANSWER
ASK_USER
CREATE_TICKET
HUMAN_HANDOFF
```

The LLM should not be the sole authority deciding whether its own answer is safe/sufficient.

---

# 15. LibreDesk and specialist Hermes bots

LibreDesk should expose **one Chitragupta Helpdesk experience** to users.

Do not start with:

```text
Choose:
[ SAP Executive ]
[ MES Executive ]
[ XStudio Executive ]
```

Users often cannot identify the fault domain.

Example:

> XStudio says posting succeeded, but SAP has no material document.

This spans UI, MES and SAP.

The system should classify internally.

Recommended:

```text
LibreDesk
    |
    v
Chitragupta L1 API
    |
    v
Jev
    |
    v
Hermes specialist
```

LibreDesk's own multiple AI-assistant routing should not become the primary domain router unless Chitragupta explicitly delegates that responsibility.

---

# 16. Why not let LibreDesk route the specialists?

LibreDesk can perform automations and assign conversations to different AI assistants, but using that as the authoritative domain router introduces another decision owner.

Potential conflict:

```text
LibreDesk says: SAP
Chitragupta/Jev says: MES
```

That recreates duplicated routing state.

Better:

- LibreDesk owns conversation UX;
- Chitragupta/Jev owns domain classification;
- Hermes profiles own domain execution.

LibreDesk may display the current domain/specialist as metadata, but should not authoritatively choose it.

---

# 17. ChatterMate integration if reconsidered later

If ChatterMate becomes viable under deployment constraints, prefer:

```text
ChatterMate
   |
   v
Chitragupta L1 API / MCP
   |
   +-- GBrain
   +-- Jev
   +-- Hermes specialists
   +-- ticket operations
```

Do not enable a parallel ChatterMate AI investigation stack that duplicates World Walk/L2 unless replacing those Chitragupta components is an explicit project decision.

### Potential future GBrain MCP

Useful MCP tools could include:

```text
gbrain_search_approved
gbrain_get_fact
gbrain_find_resolution
gbrain_get_domain_context
```

MCP should be an interface to GBrain, not a second knowledge store.

---

# 18. Human L1 executives

The term "executive" should distinguish two concepts.

## AI specialist executive

A Hermes profile responsible for a technical domain.

## Human support executive

A real support person taking over the conversation.

The helpdesk shell (LibreDesk or another product) is best suited to human handoff, assignment and inbox UX.

Chitragupta should pass:

- ticket ID
- domain
- plant area
- extracted identifiers
- current L1 evidence summary
- reason for human handoff

The human should not have to reconstruct the entire conversation from scratch.

---

# 19. Failure modes and guardrails

## 19.1 Wrong Jev classification

Mitigation:

- preserve probabilities/typed scores;
- apply minimum confidence;
- allow `UNKNOWN`;
- ask user instead of forcing a domain;
- reclassify after new evidence;
- track routing accuracy.

## 19.2 Specialist loops

Mitigation:

- max handoff count;
- only evidence-backed transitions;
- no uncontrolled bot debate;
- unresolved -> L2.

## 19.3 Duplicate ticket creation

Mitigation:

- idempotency key from conversation/session + intake hash;
- one governed ticket SP;
- external product stores the returned Chitragupta ticket ID.

## 19.4 Conflicting helpdesk/product state

Mitigation:

- `Complaint_Mst_Tbl` authoritative;
- external status is derived/correlated;
- never implement independent business-state transitions in LibreDesk/ChatterMate.

## 19.5 GBrain versus product KB divergence

Mitigation:

- separate purposes;
- GBrain owns operational facts;
- product KB owns general/public help;
- if knowledge is promoted between them, implement an explicit publication process.

## 19.6 Overuse of Qwen

Mitigation:

- deterministic rules first;
- Jev at classification gates;
- GBrain retrieval before model reasoning;
- narrow specialist tools;
- no swarm behavior.

## 19.7 Untrusted user content

Existing Chitragupta security rules remain applicable.

User-provided text is untrusted input and must not directly:

- choose arbitrary SQL,
- invoke unrestricted tools,
- alter routing policy,
- mutate GBrain,
- override authoritative status.

---

# 20. Observability and audit

Every L1 decision should be auditable.

Suggested trace categories:

```text
L1_INTAKE_CLASSIFICATION
L1_DOMAIN_ROUTE
L1_GBRAIN_RETRIEVAL
L1_SPECIALIST_START
L1_SPECIALIST_RESULT
L1_DOMAIN_TRANSITION
L1_ANSWERABILITY
L1_USER_QUESTION
L1_TICKET_CREATE
L1_HUMAN_HANDOFF
```

Useful fields:

- conversation ID
- requester ID
- selected domain
- alternative domains
- Jev confidence
- plant area
- intent
- Hermes profile
- GBrain evidence IDs
- tool/action IDs
- ticket ID
- outcome
- latency
- number of specialist hops

Do not store hidden model chain-of-thought.

Store auditable actions, evidence, classifications and final structured decisions.

---

# 21. Evaluation strategy

Do not evaluate this only by subjective chat quality.

## 21.1 Intake-routing set

Create real/synthetic utterances covering:

- obvious SAP
- obvious MES
- obvious XStudio
- cross-domain ambiguity
- incomplete messages
- misleading UI symptoms
- generic how-to
- access issues
- infrastructure issues

Measure:

- correct primary domain
- correct `UNKNOWN`
- correct plant area
- correct intent
- inappropriate forced classifications

## 21.2 Specialist evaluation

Per domain:

- correct tool selection
- correct GBrain retrieval
- evidence citation
- correct user clarification
- correct known-issue resolution
- correct escalation
- no forbidden tools

## 21.3 Cross-domain evaluation

Cases such as:

```text
XStudio symptom -> MES cause
MES symptom -> SAP cause
SAP symptom -> MES outbound missing
```

Measure:

- whether transition occurs only when evidence supports it;
- whether context survives handoff;
- whether loops are avoided.

## 21.4 End-to-end L1 -> L2

Acceptance case:

1. user opens chat;
2. identity is resolved;
3. Jev classifies intake;
4. primary specialist runs;
5. GBrain is searched;
6. specialist cannot safely resolve;
7. missing identifiers are collected;
8. exactly one ticket is created;
9. external conversation stores Chitragupta ticket ID;
10. L2 claims the ticket;
11. L2 QUESTION appears in same chat;
12. user answer returns through governed path;
13. L2 continues;
14. final L2 response appears in same conversation.

---

# 22. Phased implementation

## Phase 0 — settle product-shell constraint

Decide:

- assistant-ui versus LibreDesk spike;
- whether PostgreSQL/Redis are acceptable;
- whether SQL Server-only persistence is absolute.

## Phase 1 — L1 contracts before UI

Implement typed contracts:

- intake classification
- specialist request
- specialist result
- answerability result
- ticket intake
- question answer
- domain transition

## Phase 2 — Jev intake classifier

Implement and test:

- system domain
- plant area
- intent
- confidence
- UNKNOWN behavior

## Phase 3 — initial Hermes specialists

Create:

- `l1-frontdesk`
- `l1-sap`
- `l1-mes`
- `l1-xstudio`

Keep toolsets deliberately small.

## Phase 4 — GBrain integration

Expose consistent approved retrieval to every specialist.

Do not duplicate the KB per profile.

## Phase 5 — deterministic L1 ticket write

Implement:

```text
Hermes_L1_Create_Ticket_Usp
```

or equivalent governed operation with idempotency.

## Phase 6 — same-conversation L2 loop

Implement:

- L2 response -> conversation
- L2 QUESTION -> conversation
- user reply -> governed L1 answer operation

## Phase 7 — product shell comparison

Wire the same L1 API to:

1. assistant-ui baseline
2. LibreDesk heavy-lifting candidate

Compare actual code removed/added and operational burden.

---

# 23. Recommended decision

The architecture should proceed with:

### Intelligence/orchestration

```text
Jev = classifier/judge at explicit decision boundaries
Hermes = specialist execution profiles
GBrain = shared governed knowledge
Chitragupta = application/controller and authoritative integration boundary
SQL Server = authoritative ticket/business state
existing L2 = investigation/resolution owner
```

### User-facing shell

Two implementation tracks remain worth validating:

1. **assistant-ui** if Chitragupta should remain the entire application backend and we only need a polished conversational frontend;
2. **LibreDesk** if PostgreSQL/Redis are acceptable and we want the external product to own chat, inbox, identity, human handoff and other Helpdesk UX.

### ChatterMate

Keep on the watch list because its MCP and AI-support capabilities are technically relevant, but do not select it while:

- Docker remains prohibited;
- its investigation/ticket intelligence substantially duplicates Chitragupta.

---

# 24. Concise architecture statement

The intended L1 should behave like a **support organization**, not like a multi-agent demo.

The user talks to one Helpdesk.

Jev decides what kind of problem it is.

One bounded Hermes specialist handles it.

All specialists consult the same governed GBrain.

The model sees only the tools appropriate to its specialty.

Cross-domain handoff is exceptional and evidence-backed.

If L1 cannot safely resolve the issue, Chitragupta creates one authoritative Helpdesk ticket.

The existing L2 pipeline then owns the investigation.

The user sees the result in the same conversation.

That preserves the current Chitragupta design while giving L1 clear specialization, a small-model-friendly harness, and a practical path to a production Helpdesk.
