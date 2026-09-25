# L1 UI engineering contract

This directory is the user-facing adapter for Chitragupta L1. It is **not** a sixth
architectural responsibility and must not acquire business/workflow ownership.

## Boundaries

- Browser code may call only local server routes under `/api/l1/**`.
- Keep SQL Server, Hermes, Jev, GBrain, LM Studio, and their credentials server-side.
- Never write directly to `dbo.Complaint_Mst_Tbl` from this app.
- Never reproduce the L2 lifecycle or ticket state machine in React/Next.js.
- The upstream Chitragupta L1 API decides routing, answerability, specialist use,
  ticket creation, and L2 question handling.
- Tool UI components render structured interactions; they do not decide policy.
- The in-memory conversation UUID is correlation/idempotency context only. Never
  treat it as requester identity or authorization.
- Ticket status labels, attention state, L2 publications, and L2 questions are
  server-provided facts. The UI may present them but must not infer or mutate
  workflow state.

## Current product-shell acceptance

At this stage the assistant-ui baseline must be able to present, without owning
the backend decision:

- a governed L1 answer with optional approved-knowledge evidence;
- structured missing-context intake;
- the authoritative created-ticket snapshot;
- a user-visible L2 publication;
- an L2 QUESTION with a governed free-text answer result.

Do not fake requester login, persistence, polling, SSE, ticket creation, GBrain
retrieval, Jev decisions, or L2 delivery inside the frontend while those upstream
contracts remain absent.

## UI discipline

This is an **Operate-mode** product surface: design serves the support task.

- Reuse assistant-ui primitives and the vendored Tool UI component before adding
  another chat/component framework.
- Keep Tool UI provenance in `THIRD_PARTY_NOTICES.md`.
- Use semantic theme tokens in app-owned UI.
- No decorative gradients, glass, nested cards, generic icon tiles, or ornamental
  motion. Use elevation or border, not both, unless a real state requires it.
- Primary actions, current state, errors, and focus may use accent color; inactive
  surfaces stay restrained.
- Mobile text inputs remain at least 16px and interactive touch targets at least
  44px.
- User-facing copy must describe the support task, not implementation details such
  as SQL, model routing, pipelines, tools, or framework names.
- If shadcn/ui is changed or extended, keep `@shadcn/lint` enabled and fix its
  findings rather than suppressing them without a documented reason.

## Required Impeccable finish

Every material L1 UI change must receive both passes before the PR is considered
ready:

1. **Critique:** inspect hierarchy, specificity, cognitive load, copy, empty/loading/
   error states, accessibility, keyboard behavior, mobile ergonomics, and edge cases.
2. **Polish:** fix the priority findings at the narrowest correct level, remove
   accidental churn/duplication, and recheck the complete interaction path.

If a rendered browser is available, inspect representative desktop and mobile
sizes. If it is not available, state that limitation and perform the source-level
critique rather than pretending visual verification occurred.

## Verification

Validation is local/manual only. Do **not** add GitHub Actions.

After changes in this directory run:

```bash
npm run check
npm run build
```
