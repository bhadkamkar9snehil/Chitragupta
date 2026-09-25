# Chitragupta L1 UI

A deliberately thin L1 chat surface using assistant-ui plus Tool UI.

## Ownership boundary

This app owns presentation only:

- assistant-ui thread/composer state
- Tool UI structured intake rendering
- browser-to-server requests

It does **not** own:

- L1 routing/classification
- GBrain retrieval policy
- Hermes specialist selection
- ticket state transitions
- SQL writes
- the L2 lifecycle

The browser only calls `/api/l1/message`. That Next.js server route forwards the
typed request to one configured Chitragupta L1 message endpoint.

## Run without Docker

Requirements:

- Node.js 20.19+
- npm
- a running Chitragupta L1 API

From this directory:

```bash
cp .env.example .env.local
npm install
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

Both values stay server-side. Do not convert them to `NEXT_PUBLIC_*`.

## L1 API contract used by this route

Request:

```json
{
  "messages": [],
  "toolResults": [
    {
      "toolCallId": "intake-123",
      "result": {
        "system": ["sap"],
        "identifier": ["heat"]
      }
    }
  ]
}
```

The upstream response is one of two shapes.

Normal response:

```json
{
  "type": "message",
  "text": "I found the known resolution..."
}
```

Structured intake request:

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

assistant-ui pauses the run for `collect_intake`. Tool UI renders the Question
Flow, and the user's selections are returned in `toolResults` on the resumed
request.

This is an interaction contract only. The upstream Chitragupta L1 API remains
responsible for Jev classification, Hermes/GBrain work, and deciding whether to
answer, ask again, hand off, or create a ticket.

## Local validation

This app registers `@shadcn/lint` and enables token/style checks for app-owned
UI code. Vendored Tool UI/shadcn component source is excluded from local restyle
rules but remains subject to ordinary TypeScript/runtime validation.

Validation is local/manual only. Do not add GitHub Actions for this project.

```bash
npm run lint
npm run typecheck
npm run check
npm run build
```

## Tool UI provenance

See `THIRD_PARTY_NOTICES.md`.
