# Autonomous L2 Learning Architecture

Status: **experimental branch contract**  
Branch: `development/autonomous-l2-learning-runtime`  
North star: **an autonomous, AI-driven, deterministic L2 Helpdesk that gets measurably better from experience and can progressively earn the ability to solve XBatch issues itself.**

## 1. The one rule

Everything in this branch is subordinate to one product rule:

> Chitragupta must become an autonomous L2 Helpdesk system whose reasoning can improve continuously while workflow, evidence, side effects, and correctness remain deterministic enough to trust in production.

The existing rules are not discarded because determinism is valuable; they are reclassified as current implementation constraints. Anything may evolve if the replacement gives us a better path to the north star.

## 2. Storage is not authority

The most important architectural distinction in the learning system is:

```text
recording experience != believing experience
retrieving experience != proving a ticket claim
reasoning about an action != permission to execute it
```

This is why this branch records sessions **on** but keeps generic automatic memory prefetch **off**.

### Why session recording stays on

Raw sessions are valuable because they preserve the experience needed to improve the system:

- successful diagnostic paths;
- dead ends and repeated failures;
- rejected reviewer hypotheses;
- tool-call ergonomics problems;
- token/context waste patterns;
- model-specific behavior;
- user/operator corrections;
- evidence-selection strategy;
- the exact language that preceded a good or bad outcome.

If we throw sessions away, we throw away the dataset needed for replay, evaluation, failure mining, retrieval experiments, policy tuning, and eventually self-improvement.

Sessions are therefore recorded as **unverified episodic experience** with provenance and secret redaction.

### Why generic automatic prefetch stays off

A conventional memory provider performs:

```text
new prompt
  -> semantic search over everything remembered
  -> top-k results injected into model context
```

That is dangerous for an autonomous support agent because retrieval silently becomes epistemic privilege. An old assistant statement, a rejected hypothesis, a stale workflow fact, and a verified operating rule can all arrive in the same context before the model has classified their source.

Example:

```text
Ticket A investigator incorrectly says "database access is unavailable"
        |
        v
session is recorded
        |
        v
future ticket automatically prefetches that sentence
        |
        v
model receives its own prior mistake as context before live verification
```

The problem is not recording the mistake. The mistake is useful training data. The problem is **injecting it automatically as if relevance implied trust**.

Chitragupta therefore uses explicit or stage-aware retrieval:

```text
query
  -> choose source class/scope
  -> retrieve candidates
  -> show trust/provenance
  -> reason about applicability
  -> verify ticket-specific claims live
```

Future deterministic stage-aware retrieval may automatically build an investigation packet, but it must choose source classes deliberately. It is not generic top-k memory injection.

## 3. Expand zvec's role: Experience & Retrieval Plane

`zvec-grep` is not treated merely as a replacement for mem0. Its role is expanded into a local **Experience & Retrieval Plane**.

```text
                    CHITRAGUPTA LEARNING VAULT

 sessions/                facts/                 knowledge/
 unverified experience    reviewed heuristics    mirrored Git/skills
        |                    |                      |
        +--------------------+----------------------+
                             |
                      zvec-grep index
                    BM25 + vector + RRF
                             |
                   explicit l2_recall tool
                             |
                    trust-scoped results
```

The shared default vault is:

```text
~/.hermes/l2-learning/
```

It is shared across investigator/reviewer profiles so experience does not fragment by process identity.

### Source classes

| Vault scope | Meaning | Trust |
|---|---|---|
| `knowledge/**` | Mirrored Git reference and deployed skills | Canonical reference lead |
| `facts/**` | Explicitly promoted operational lessons | Reviewed operational heuristic |
| `solutions/approved/**` | Future export of governed approved Solution articles | Governed reusable guidance |
| `sessions/**` | Every completed user/assistant turn | Unverified episodic experience |
| `candidates/**` | Model-proposed lessons awaiting promotion | Unverified candidate |
| `archive/**` | Rejected/superseded learning artifacts | Historical only |

The zvec index is disposable. It does not become a source of truth.

## 4. Keep mem0, but narrow its meaning

This branch does not replace mem0 just because another retrieval engine exists.

A useful target separation is:

```text
mem0
  = compact, high-value operational memory intended to influence routine behavior

zvec learning vault
  = high-recall experience corpus + hybrid search + replay/evaluation substrate

Git / SQL Solution KB
  = governed reusable knowledge

live SQL
  = current-ticket evidence

run ledger / trace
  = authoritative incident execution history
```

This lets us compare mechanisms empirically instead of collapsing all memory into one store.

## 5. Explicit learning tools

The `xstudio-l2-learning` plugin contributes two direct tools.

### `l2_recall`

Searches the local zvec corpus with an explicit scope:

```text
trusted
knowledge
facts
solutions
sessions
candidates
all
```

Every result includes a trust label and warning. `sessions` and `candidates` are never silently treated as facts.

Normal investigation should begin with `trusted` when prior knowledge may help. `sessions` is for questions such as:

- have we seen this failure shape before?
- what dead end did another run hit?
- did an earlier model/tool combination repeatedly fail this way?
- what evidence path worked on a similar incident?

It is not current-ticket proof.

### `l2_lesson`

Allows a worker to propose a reusable lesson with explicit provenance.

The tool writes only to:

```text
candidates/**
```

and labels the result `unverified_candidate`.

The model cannot promote its own lesson into trusted memory. Promotion is a separate control-plane operation.

## 6. Learning lifecycle

The durable learning loop should become:

```text
real ticket
  -> investigation
  -> review
  -> publication / human action / escalation
  -> observed outcome
  -> experience record
  -> candidate lesson(s)
  -> replay / independent evidence / reviewer or policy gate
  -> promote, update, reject, or leave episodic
  -> future retrieval
  -> better next investigation
```

The key is **outcome-conditioned learning**. We should learn more from:

- proposals the reviewer rejected;
- resolutions that remained resolved;
- tickets that reopened;
- diagnostic paths that reached proof quickly;
- tool sequences that caused context blowouts;
- human corrections;
- repeated independent incidents with the same verified root cause.

We should learn less from confident prose.

## 7. Evaluation Plane

A system that "keeps getting better" needs measurements, not vibes.

Build a replay corpus from historical sessions/tickets and continuously measure candidate changes against it.

Minimum metrics:

```text
resolution correctness
review reject rate
reopen rate
false-resolution rate
L3/human-action precision
mean/median tool calls
input tokens per ticket
wall time per ticket
context-overflow rate
retrieval hit@k
false-positive retrieval@1
abstention correctness
live-evidence coverage
unnecessary-query rate
```

For retrieval, adversarial pairs matter more than easy keyword recall:

```text
same symptom, different root cause
same table, different business state
same historical fix, now invalid
same identifier shape, different entity
```

A learning change should be promoted because replay/live outcomes improve, not because its author/model thinks it is clever.

## 8. Control Plane remains deterministic

The existing lifecycle remains useful:

```text
claim
-> investigate
-> normalize
-> independent review of frozen proposal
-> publish OR rework
```

But it is now one plane, not the whole product.

The model may become much more capable without taking ownership of atomic claiming, idempotency, workflow binding, proposal freezing, retry limits, or publication correctness.

Determinism is especially valuable at boundaries where probabilistic reasoning should not decide whether an irreversible state transition happened twice.

## 9. Future Action Plane: from diagnosis to solving XBatch

The long-term system should not stop at `NEEDS_HUMAN_ACTION` forever.

The correct evolution is not to hand the model arbitrary UPDATE/EXEC access. It is to grow a typed capability registry.

```text
investigator proves cause
        |
        v
candidate corrective action
        |
        v
ACTION CAPABILITY REGISTRY
  - exact target
  - risk class
  - preconditions
  - parameter schema
  - supported execution path
  - idempotency key
  - expected postconditions
  - verification reads
  - rollback/compensation
  - approval policy
        |
        v
shadow plan / supervised execute / autonomous execute
        |
        v
postcondition verification
        |
        v
outcome + learning feedback
```

### Autonomy ladder

**A0 — Observe**  
Read-only diagnosis. Current baseline.

**A1 — Recommend**  
Cause and exact action are known; human executes.

**A2 — Shadow-plan**  
Agent selects a registered action and parameters; harness validates everything but does not execute. Compare plan with the human's eventual action.

**A3 — Supervised execute**  
Harness presents the validated action for one-click/operator approval, then executes and verifies.

**A4 — Autonomous low-risk execute**  
Allowlisted, reversible/idempotent actions with strong preconditions execute automatically.

**A5 — Broader autonomous remediation**  
Higher-impact actions become eligible only after evidence from shadow/supervised operation demonstrates acceptable safety and recovery.

Autonomy is earned **per capability**, not granted as one giant database permission.

## 10. Action capability contract

A future executable action should be declarative enough to audit:

```json
{
  "id": "xbatch.retry_sap_posting",
  "risk": "low",
  "mode": "shadow|supervised|autonomous",
  "parameters": {},
  "preconditions": [],
  "execution": {
    "type": "stored_procedure|api|service_action|script",
    "target": "..."
  },
  "idempotency": {},
  "verification": [],
  "rollback": {},
  "required_evidence": [],
  "approval_policy": {}
}
```

No action enters autonomous mode because a prompt says it is safe. It moves up the ladder because deterministic tests, replay, live telemetry, and observed outcomes support that promotion.

## 11. Why this is bigger than a memory plugin

The useful idea from `hermes-zvec-memory` is not "replace mem0 with Markdown."

The larger opportunity is:

```text
record everything useful
classify its authority
search it cheaply and locally
learn from outcomes
promote only what earns trust
replay changes against history
then turn verified knowledge into typed corrective capability
```

That is the path from an L2 chatbot to an adaptive autonomous support system.

## 12. Current branch implementation

This branch introduces the first concrete pieces:

- `Model_Bench/xstudio_l2_learning_plugin/`
  - records every completed L2 turn;
  - redacts common secret shapes before disk;
  - provides explicit `l2_recall` hybrid search;
  - provides `l2_lesson` candidate capture;
  - has **no automatic prefetch hook**.
- `Model_Bench/sync_l2_learning_corpus.py`
  - mirrors current Git/skill reference material into the shared vault;
  - builds/updates the disposable zvec index.
- `Model_Bench/l2_learning_curator.py`
  - promotes/rejects candidates deterministically;
  - keeps promotion provenance.
- deployment/profile wiring
  - makes `l2_learning` a directly available toolset alongside `xstudio_l2`;
  - keeps mem0 independent;
  - shares one learning vault across the active L2 profiles.

The next large increments should be:

1. outcome receipts from the deterministic lifecycle into the experience vault;
2. approved SQL Solution export into `solutions/approved/`;
3. replay/evaluation harness using real historical incidents;
4. automatic candidate mining from reviewer rejection + successful terminal outcomes;
5. capability registry in shadow mode;
6. first low-risk XBatch remediation capability with pre/post verification.
