---
target: L1, L2, L3 console screens
total_score: 23
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 4
target_identity: "file:C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\l1-ui\\components\\console"
timestamp: 2026-09-26T03-59-08Z
slug: l1-ui-components-console
closed: true
---
⚠️ DEGRADED: single-context (standing user rule: no self-spawned subagents; design review finished before detector output was read)

Target: support console L1 / L2 / L3 screens (l1-ui/components/console/{conversations,runs,l3}.tsx + ui/primitives, ui/viz, ui/button, app/globals.css)

## Design Health Score
| # | Heuristic | Score | Key Issue |
|---|---|---|---|
| 1 | Visibility of System Status | 3 | Live/working states are clear; "Led to" skeleton sits unlabeled for 3 chained requests |
| 2 | Match System / Real World | 2 | "Jev", "Writer used", "112 reads", "attempt 1", "L2 #1" are pipeline internals shown to support staff |
| 3 | User Control and Freedom | 3 | Back, drawer toggle, clear filter all present |
| 4 | Consistency and Standards | 1 | Three list-row patterns, three names for one state, green and amber both meaning "escalated" |
| 5 | Error Prevention | 3 | Resolve disabled until text; "Close the ticket" defaults ON with no confirm |
| 6 | Recognition Rather Than Recall | 3 | Labeled nav, counts visible |
| 7 | Flexibility and Efficiency | 2 | Ctrl K exists; no j/k or arrow navigation through queues |
| 8 | Aesthetic and Minimalist Design | 2 | Monospace-everywhere, eyebrow labels, dashed icon tiles, repeated facts |
| 9 | Error Recovery | 2 | Every API failure toasts "Something went wrong. Please try again." |
| 10 | Help and Documentation | 2 | Empty states and L3 step hints; nothing else |
| **Total** | | **23/40** | **Acceptable** |

## Audit Health Score
| # | Dimension | Score | Key Finding |
|---|---|---|---|
| 1 | Accessibility | 2 | Light theme: amber chip 3.11:1, green chip 3.25:1, subtle meta 3.37:1; dark subtle meta 4.18:1 at 11px |
| 2 | Performance | 3 | L1 detail rail does 3 sequential fetches; full conversation list re-polled every 20s |
| 3 | Responsive | 3 | No page overflow at 375; L3 grid fixed to container width this session |
| 4 | Theming | 3 | Clean tokens, but success = signal = progress, so "open", "working", "resolved" and "escalated" share one green |
| 5 | Implementation Integrity | 2 | Pattern drift across sibling screens; "outline" button variant has no outline |
| **Total** | | **13/20** | **Acceptable** |

## Design Specificity Verdict
Category-interchangeable. The shell is a competent dark "AI dev tool" template: graphite panels, one mint accent, Geist Mono on metadata, dashed-outline icon tiles, lowercase mono key/value rails, uppercase tracked micro-labels. Nothing in it is about a steel plant's helpdesk. Detector: 0 findings across components/console, components/ui, components/helpdesk, app — these patterns sit below its rules, so the slop verdict rests on review.

## Priority Issues
1. [P1] Three different list patterns for the same job. L1 rows are inset rounded-xl cards with avatars, no dividers, selected = bg-surface-3; L2/L3 rows are full-bleed, border-b dividers, selected = bg-surface-2, no avatars. Fix: one QueueRow primitive (full-bleed, divider, same selected fill) used by all three.
2. [P1] One state, three names and two colours. Ticket pill "Escalated to specialist" (green, L1/api/Tickets.cs:50 tone "progress"), L2 chip "Handed to people · cause open" (amber), L3 chip "Unresolved by L2" (amber). Fix: one vocabulary map and one tone per state, owned by the API label.
3. [P1] Monospace as costume. Mono on timestamps, counts, page subtitles, attribute keys, "answered by assistant", state pills, "L2 #1 · …". Mono should be ticket numbers, heat numbers, SQL, durations only. Plus 19 uppercase tracked eyebrow labels, 11 dashed-border icon tiles, pulsing dots on attention pills.
4. [P1] Contrast failures on the most common chips in light theme (amber 3.11, green 3.25) and on all 11px subtle meta text in both themes.
5. [P2] Internals leak into support staff's view: "44 Jev · 112 reads · Writer used", "attempt 1", "1.8s" latency under chat bubbles, "L2 #1".

## Persona Red Flags
Alex (power user, works the L3 queue): no keyboard movement through the queue; the note/resolve forms need mouse; Pick up is below the fold at 1024 once the grid stacks.
Sam (keyboard/screen reader): role="tablist" filter rows have no tabpanel or arrow-key handling; state conveyed by chip colour; 11px meta text below AA.

## Minor Observations
- "outline" Button variant is bg-canvas with no border: "Follow live", "Ticket context", "View L2 investigation" read as plain text.
- L1 rail shows "status open" in signal green; open is not good news.
- L2 story uses 1-2-3-4 numbered steps; the sequence carries little the headings don't.
- Ticket numbering: "#35", "Ticket 35", "Ticket_34" (in previews), "L2 #1" (attempt) all coexist.
- Right rail "Other conversations" mixes ticket numbers and relative times in one column.

## Questions to Consider
- What would this console look like if it were built for a steel plant's support desk rather than for an AI company's demo?
- Does a support engineer ever need Jev call counts on the queue row?
- If there were only one list row and one chip, what would they be?
