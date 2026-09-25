# L1 UI engineering contract

This directory is the user-facing adapter for Chitragupta L1. It is **not** a sixth
architectural responsibility and must not acquire business/workflow ownership.

## Boundaries

- The one owner of L1 behaviour is `L1/api/Program.cs` (.NET): accounts, chat sessions and history,
  Jev's answer/ask/ticket decision, ticket creation in `Complaint_Mst_Tbl`, ticket state labels,
  L2 replies and the requester's answers. This app renders it.
- Browser code calls only `/api/l1/**`; `app/api/l1/[...path]/route.ts` forwards to `L1_API_URL`.
  SQL, Jev, LM Studio and every credential stay server-side.
- Never reproduce the L2 lifecycle or infer ticket state in React: `StateLabel`/`StateTone` come from the API.
- Account pick is identification, not authentication. Never read or show the XStudio `Password` column.

## Screens

- Sign-in: search XStudio accounts, pick one (remembered per browser).
- Sidebar: new chat, My tickets (count needing a reply), searchable chat history with rename/delete.
- Chat: persisted conversation, example prompts, Markdown replies, raised-ticket card with live state.
- My tickets: filters (all / needs your reply / open / resolved), ticket detail with every published
  L2 reply, and a reply box that returns the ticket to the support team.

## UI discipline

This is an **Operate-mode** product surface: design serves the support task.

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
