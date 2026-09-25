# L1 UI engineering contract

This directory is the user-facing adapter for Chitragupta L1. It is **not** a sixth
architectural responsibility and must not acquire business/workflow ownership.

## Boundaries

- The one owner of L1 behaviour is `L1/api` (.NET): accounts, conversations, Jev's answer/ask/ticket decision,
  GBrain world search + Jev relevance, the writer model (settings-driven), ticket creation in `Complaint_Mst_Tbl`,
  ticket state labels, L2 replies, requester answers/ratings/follow-ups, console stats and settings.
- Browser code calls only `/api/l1/**`; `app/api/l1/[...path]/route.ts` pipes to `L1_API_URL` (SSE included).
  SQL, Jev, GBrain, model keys and every credential stay server-side; API keys are encrypted at rest.
- Never reproduce the L2 lifecycle in React: `StateLabel`/`StateTone` come from the API; the console shows L2 runs
  read-only.
- XStudio's insert trigger rewrites `Complaint_Mst_Tbl.Source`; the chat channel is derived from the L1 session link.
- Identity: `?user=<XStudio user ID>` from the embedding page, else a remembered account pick. Identification only;
  never read or show the XStudio `Password` column.

## Surfaces

- `/` requester helpdesk (embeddable; rail at >=768px, bottom tabs below): Home, Messages (streaming replies,
  XBatch sources, feedback, Talk to support handoff, solved + rating), Tickets (filters, timeline, reply,
  rating, still-not-fixed follow-up). Deep links: `#/messages[/id]`, `#/tickets[/id]`; `?theme=light|dark`.
- `/admin` support console: Command centre, Live engineer (the investigation circuit, live or replayed step by step),
  Tickets (journey: L1 chat -> ticket -> L2 investigations -> state, each step opens its record), Conversations,
  L2 investigations (same circuit + what was told + audited reads), L3 escalations, Agents & tools (tool call graph),
  Reports, Settings. **New chat** (nav, Ctrl+K, Conversations) opens a new thread in Conversations: the same requester
  chat component embedded as the acting engineer (never a new tab); its ticket links open the console ticket record.
- `public/embed.js` floating launcher.
- AI providers: OpenAI-compatible (LM Studio, Ollama, OpenAI, Gemini, Groq, OpenRouter, custom), Anthropic, and
  the Codex CLI for a ChatGPT plan (the only official route for a plan).

## UI discipline

This is an **Operate-mode** product surface: design serves the support task.

- Use semantic theme tokens in app-owned UI. The palette is neutral graphite plus ONE accent (`--brand`, set in
  Settings → Appearance, default `#4ceea8`); `--signal`, `--signal-soft`, `--success`, `--primary-soft` and the focus
  ring are all derived from its hue in `app/globals.css`. Never hard-code an accent; primary actions are the contrast
  pill (`bg-foreground text-background`), not the accent.
- The same visual language applies to both surfaces (requester helpdesk and console): `PageTitle` opens every screen,
  sections are `Panel`s, identifiers/times/counts are mono, avatars are neutral.
- No decorative gradients, glass, or ornamental motion. Use elevation or border, not both, unless a real state
  requires it. Motion is allowed only when it carries state (a live stage pulsing, a wire the work is crossing).
- Console visual language lives in `components/ui/viz.tsx` (reuse it, do not fork it): a `Panel` shell with a dashed
  `IconTile`, title and mono meta around one inset body; mono numerals; **one mint `signal` colour** for the thing that
  matters in any chart and greys for everything else; `SegmentBar`/`Legend`, `TickGauge`, `ProbBars`, `Waterfall`,
  `Attributes`, `Segmented`, `HeatCalendar`. Prefer these over tables wherever the data is a composition, a
  distribution, a decision or a timeline; keep tables for genuinely tabular records (audited reads).
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
