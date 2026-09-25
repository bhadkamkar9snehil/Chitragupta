# Chitragupta L1 UI

A deliberately thin L1 Helpdesk surface using assistant-ui plus a small set of
purpose-built Tool UI interactions.

## Ownership boundary

This app owns presentation only:

- assistant-ui conversation/composer state
- structured incident intake
- approved-knowledge attribution display
- ticket snapshot display
- L2 publication display
- L2 QUESTION answer capture
- browser-to-server requests

It does **not** own:

- requester authentication/authorization
- L1 routing or answerability
- GBrain retrieval policy
- Hermes specialist selection
- deterministic ticket creation
- ticket status transitions
- SQL writes
- L2 lifecycle/publication
- asynchronous L2 event delivery

The browser calls only `/api/l1/message`. That Next.js server route validates
and bounds the payload, then forwards it to one configured Chitragupta L1
message endpoint.

## Product-shell acceptance covered here

The UI contract can represent the complete assistant-ui spike required by #21:

1. answer from governed knowledge, with approved sources when supplied;
2. collect missing structured context;
3. render the authoritative ticket returned after deterministic creation;
4. render the requester's current ticket/status list;
5. render an L2 publication;
6. render an L2 QUESTION and return the requester's free-text answer.

Those are interaction capabilities. This UI does not pretend the corresponding
backend services already exist.

## Run without Docker

Requirements:

- Node.js 20.19+
- npm
- a running Chitragupta L1 API

From this directory:

```bash
cp .env.example .env.local
npm install --no-audit --no-fund
npm run check
npm run dev
```

Open:

```text
http://localhost:3000/l1
```

## Server configuration

```text
CHITRAGUPTA_L1_MESSAGES_URL=http://127.0.0.1:8787/api/l1/messages
CHITRAGUPTA_L1_API_TOKEN=
```

Both values stay server-side. Never convert them to `NEXT_PUBLIC_*`.

## Request contract

The browser adapter creates one UUID per in-memory conversation. It is sent as a
correlation/idempotency input only; it is **not requester identity** and must
never be treated by the backend as authentication.

```json
{
  "conversationId": "8318d8a5-70d1-40be-92de-d2373a232bed",
  "messages": [],
  "toolResults": [
    {
      "toolCallId": "intake-123",
      "toolName": "collect_intake",
      "result": {
        "system": ["sap"],
        "identifier": ["heat"]
      }
    }
  ]
}
```

Human tool results are restricted to:

```text
collect_intake
answer_l2_question
```

The real Chitragupta L1 API must resolve the authenticated requester
server-side before reading or mutating any ticket data.

## Response contract

### Governed answer

```json
{
  "type": "message",
  "text": "The approved resolution is ...",
  "sources": [
    {
      "id": "gbrain-fact-123",
      "title": "SAP posting recovery",
      "section": "Known resolution",
      "excerpt": "..."
    }
  ]
}
```

Sources are display-only evidence references. The UI never invents a source URL
or promotes knowledge.

### Structured intake

```json
{
  "type": "collect_intake",
  "toolCallId": "intake-123",
  "flow": {
    "id": "intake-123",
    "role": "decision",
    "steps": [
      {
        "id": "system",
        "title": "Where did you see the problem?",
        "selectionMode": "single",
        "options": [
          { "id": "sap", "label": "SAP" },
          { "id": "mes", "label": "MES" },
          { "id": "xstudio", "label": "XStudio" },
          { "id": "unknown", "label": "Not sure" }
        ]
      }
    ]
  }
}
```

assistant-ui pauses only for an interactive human tool call. Tool UI renders the
flow; the user's selection is returned as a typed tool result; the same runtime
then resumes.

### Ticket snapshot

```json
{
  "type": "ticket",
  "ticket": {
    "ticketId": "232",
    "ticketNo": "Ticket_232",
    "summary": "Material document is not visible in SAP.",
    "statusLabel": "Submitted",
    "attentionRequired": false,
    "systemLabel": "SAP",
    "area": "EAF",
    "createdOn": "2026-09-25T08:15:00+05:30"
  }
}
```

`statusLabel` is authoritative server-provided presentation text. The browser
must not derive ticket workflow state from internal L2 fields.

### Ticket/status list

```json
{
  "type": "tickets",
  "tickets": [
    {
      "ticketId": "232",
      "ticketNo": "Ticket_232",
      "summary": "Material document is not visible in SAP.",
      "statusLabel": "Submitted",
      "attentionRequired": false,
      "systemLabel": "SAP",
      "area": "EAF",
      "updatedOn": "2026-09-25T08:20:00+05:30"
    }
  ]
}
```

The list is bounded to 20 ticket snapshots per response. Authentication,
authorization, paging, and which tickets are visible remain upstream
responsibilities.

### L2 publication

```json
{
  "type": "l2_reply",
  "reply": {
    "replyId": "run-123",
    "ticketId": "232",
    "ticketNo": "Ticket_232",
    "kind": "UPDATE",
    "text": "Support has verified ...",
    "publishedOn": "2026-09-25T08:20:00+05:30"
  }
}
```

The allowed publication kinds are the existing user-visible L2 outcomes:
`UPDATE`, `RESOLUTION`, `L3_ESCALATION`, and
`NEEDS_HUMAN_ACTION`.

### L2 QUESTION

```json
{
  "type": "l2_question",
  "toolCallId": "question-run-123",
  "prompt": {
    "questionId": "run-123",
    "ticketId": "232",
    "ticketNo": "Ticket_232",
    "question": "What time did the posting attempt occur?"
  }
}
```

assistant-ui pauses the run until the requester sends a non-empty answer. The
result returned upstream is:

```json
{
  "toolCallId": "question-run-123",
  "toolName": "answer_l2_question",
  "result": {
    "questionId": "run-123",
    "ticketId": "232",
    "answer": "Around 07:45."
  }
}
```

The upstream API is responsible for validating requester ownership and invoking
the governed answer operation. The UI never updates `AskStatus` or L2 state.

## Session and asynchronous-event boundary

The current assistant-ui baseline intentionally keeps one in-memory conversation
UUID. Production conversation persistence, reloading prior tickets, and
unsolicited L2 publications/questions require an authenticated upstream
session/event transport (for example REST plus SSE). This PR does not fabricate a
browser persistence layer or a polling lifecycle before that backend contract
exists.

When the backend session/event contract is added, it should remain the sole
owner of requester identity, replay/deduplication, ticket visibility, and event
ordering.

## Security and hardening

The local proxy:

- validates request and response shapes with Zod;
- bounds messages, human-tool results, structured intake, free text, and evidence;
- rejects request/response bodies above 512 KiB;
- forwards the optional bearer token only server-to-server;
- returns generic browser-facing service errors;
- never exposes the configured upstream URL to browser code.

## Local validation

This app registers `@shadcn/lint` and enables token/style checks for app-owned
UI code. Vendored Tool UI/shadcn source is excluded from local restyle rules but
remains subject to TypeScript/runtime validation.

Validation is local/manual only. Do not add GitHub Actions.

```bash
npm run lint
npm run typecheck
npm run check
npm run build
```

A real local `npm install` should generate the lockfile. Do not hand-author one.

## Tool UI provenance

See `THIRD_PARTY_NOTICES.md`.
