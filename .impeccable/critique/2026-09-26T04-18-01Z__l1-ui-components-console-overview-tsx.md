---
target: Command centre
total_score: 25
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 3
target_identity: "file:C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\l1-ui\\components\\console\\overview.tsx"
target_fingerprint: "sha256:9d42a33c01ed4a17dfc7e2ef87253b4138537e7560b19567de7027678196b063"
target_path: "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\l1-ui\\components\\console\\overview.tsx"
timestamp: 2026-09-26T04-18-01Z
slug: l1-ui-components-console-overview-tsx
closed: true
---
⚠️ DEGRADED: single-context (standing user rule: no self-spawned subagents)

Target: Command centre — l1-ui/components/console/overview.tsx (live at /admin#/overview), against the reference set ~/Downloads/Image (68–78).jpg

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | System status | 2 | No time dimension anywhere: no trend, throughput or duration; "0 resolved in 24 h" is the only temporal signal |
| 2 | Match real world | 3 | "L2 published handed to people · cause open" reads as broken grammar |
| 3 | User control | 3 | Every panel links to its desk |
| 4 | Consistency | 3 | Follows the panel language, but uses only 2 of the reference set's chart forms |
| 5 | Error prevention | 3 | Read-only surface; refresh-failure banner keeps last data |
| 6 | Recognition | 3 | Legends clickable, desks reachable |
| 7 | Efficiency | 2 | You can't see which of 37 open tickets are oldest without scrolling a list of identical rows |
| 8 | Aesthetic / minimalist | 1 | One full-width amber bar that says nothing (37 of 37 with L3); 10 identical "L3 attention" rows; amber everywhere |
| 9 | Error recovery | 3 | Load failure has a retry state |
| 10 | Help | 2 | No definitions for "resolved by L2 alone" etc. |
| **Total** | | **25/40** | **Acceptable** |

Design specificity: reads as a generic ops template filled with lists. Against the references (heatmap, dot-plot, tick gauge, step chart, bump chart, stream graph, node graph, histogram) it uses only the segment bar. Nothing shows how work flows L1 → L2 → L3, which is the one thing only this product has.

Priority issues
1. [P1] No flow view. The suite's core story (conversation → ticket → L2 outcome → L3) is invisible. Fix: a flow/node graph from L1 volume to L2 outcomes to L3 state, like the tool-call graph reference.
2. [P1] No time. Nothing shows volume by hour/day, L2 time-to-outcome, or outcome trend. Fix: 7×24 intake heatmap, time-to-outcome histogram with p50/p95, 14-day outcome columns.
3. [P1] "Needs attention" duplicates the L3 queue: 10 rows, identical pill, identical "open 1d ago · last progress 1d ago". Fix: an aging dot-plot of every open ticket by owner lane, click-through per dot; keep only the 3 most stalled as text.
4. [P2] Open-tickets bar is one solid amber block; legends list four zeros; "0 resolved" is mint (good colour on bad news). Fix: show zeros quietly, tone by meaning.
5. [P2] Layout: max-w-7xl centred with ~600px voids on a 2000px screen; right column ends early leaving a dead zone. Fix: a 12-column grid that fills the width and rows of equal-height panels.

Minor: activity feed shows internal escalation notes as detail text (see REPLY-001); "L2 published <outcome>" grammar; Live engineer idle state is mostly a sentence.

Questions skipped: the user already set the direction (overhaul to the reference set, more visualisations).
