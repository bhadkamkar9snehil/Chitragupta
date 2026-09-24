# How Jev works as the L2 engineer

Written 2026-09-24 after reading the TypeSafe docs (System One, primitives, confidence, fan-out,
hierarchical classification, reranking, skill suggestion, Jev 1.13 limitations) and GBrain 0.50
(hybrid search, typed links, timelines, takes, trajectories). The step-by-step walk was one
suggestion; this is the design that follows from what the two tools are actually good at.

## The division of labour

| Who | Does | Never does |
|---|---|---|
| **Code (harness)** | Every lookup, SQL read, count, time comparison, baseline, index build; keeps state; executes the plan | Semantic judgement |
| **Jev** | Typed judgements over candidates code prepared: which scope, which records matter, what role each finding plays, whether the evidence explains the complaint, which way to go next | Write text, SQL, arithmetic, date comparison |
| **GBrain** | The world: pages (what each thing is, in plain words), typed links (how things connect), hybrid search (user words to pages), timelines/takes (what happened before, what we learned) | Decide anything |
| **Qwen** | Writes the reply from the evidence Jev selected, only when a fixed template cannot | Investigate |

TypeSafe's own guidance: "Code owns the workflow; the model supplies programmable common sense."
Jev 1.13 is documented as weak at arithmetic, dates, indirection and irrelevant context, so code
computes and filters; Jev chooses among prepared options.

## What an L2 engineer does, and the Jev pattern for each step

An L1 escalation arrives as a ticket: the user's words, plus what the L1 chatbot extracted
(`ProblemCategory`, `SuspectedCause`, `ConversationSummary`, `ExtractedEntitiesJson` already exist
in `Complaint_Mst_Tbl`). The L2 engineer then:

1. **Understands the ask** (one fan-out call). Speculative questions asked together, answers used
   by branch: is this about plant data at all, or how-to / access / performance / hardware / change
   request; which area; is there a time window; is it "missing", "wrong value", "error", "slow".
   Pattern: [speculative fan-out](https://docs.typesafe.ai/patterns/fan-out.md) +
   [intent routing](https://docs.typesafe.ai/patterns/intent-routing.md).
2. **Finds the scope** (what the user is looking at). Two anchors:
   - an **identifier** (heat, billet, order, lot, document): code finds spans, the world's keys
     and identifier index say where each value lives, the data confirms it (built, E2E 12/12);
   - **words** ("LRF screen", "charging bed", "production summary", "SAP goods receipt"): GBrain
     hybrid search over world pages, including **screen pages** built from the XStudio menu ->
     page -> grid -> list view configuration, gives ~30 candidates; Jev scores each with a Noul
     ("is this what the requester is looking at?"), then verifies the top 3 with fuller page text.
     Pattern: [skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion.md) (182
     options: wide rank, then verify, 0.30 gates for "nothing fits") and
     [reranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md).
3. **Looks at the evidence for that scope** (code). With an identifier: every table holding it,
   its rows, and what ran for it (log index). Without one: the **health index** of the scope's
   tables, procedures, events and SAP interfaces over the time window: last write vs normal
   cadence, rows per day vs baseline, errors per day vs baseline, event active or not, screen
   filter conditions. Code computes every comparison and states it in words ("LRF_Per_Heat: last
   row 2026-07-08 17:10; normally every 50 min; EAF_PER_HEAT continued to 2026-07-17").
4. **Judges every finding at once** (one batched call): what the user sees / stuck record / cause /
   unrelated, per finding. Pattern: [parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions.md).
5. **Follows the chain** when the cause is not yet visible. From the findings that matter, the
   world's links (who writes it, what feeds it, which event creates it, which screen filters it,
   which other tables hold the same value) are the next candidates. Jev keeps the **3 best paths
   open** and code expands them in parallel, so an early wrong turn is repaired by deeper evidence.
   Pattern: [hierarchical classification beam search](https://docs.typesafe.ai/cookbooks/hierarchical_classification.md)
   (K=3; 4/4 vs greedy 2/4 in TypeSafe's tests). One-step-at-a-time is the K=1 special case.
6. **Decides it is explained** (verify, then act). A Noul per claim: "does this evidence show why
   the requester sees the problem?" and "is anything the requester said still unexplained?".
   Pattern: [citation check](https://docs.typesafe.ai/cookbooks/citation_check.md) +
   [confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing.md):
   high confidence -> answer; missing facts from the user -> QUESTION; plant/SAP/master-data
   action needed -> NEEDS_HUMAN_ACTION; not explained -> L3 with the trail.
7. **Learns** (GBrain). Each resolved ticket adds a timeline entry on the pages involved and a
   *take* ("GoodsMovement 'order status does not allow goods receipt' => work order not Released")
   with a weight; later tickets that confirm or refute it resolve the take, so GBrain's scorecard
   measures which lessons hold. Past takes on the scope's pages become candidates in step 5.

## The indexes (all generated, none hand-written)

| Index | What it answers | Built from | Status |
|---|---|---|---|
| World graph (GBrain) | What is this, what touches it | catalog, procedure code, runtime log, events, API log | built, E2E 19/19 |
| Keys + identifiers | Where does this value live | shared values, membership, distinctness | built |
| Log index | What ran for this value | 216k distinct procedure calls | built |
| **Screen layer** | Which data does "the X screen" show, with which filter | XStudio menu/page/grid/list-view config | to build |
| **Health index** | Is this table/procedure/interface normal right now | per-day rows, last write, per-day errors, event flags, baselines | to build |
| **Time log index** | What ran and failed in a time window | log grouped by procedure and day | to build |
| Lessons (GBrain takes + timelines) | What we learned last time | resolved tickets | to build |

`XStudio_DataSource_Mst_Tbl` stores database credentials in plain text; the builders never copy
that table into the world.

## Kinds of L1 escalation and how each is handled

| Escalation | Example | Anchor | Evidence | Typical outcome |
|---|---|---|---|---|
| Record wrong/missing | "heat 1603945 consumption not in SAP" | identifier | rows + log + errors | RESOLUTION / NEEDS_HUMAN_ACTION |
| Feed stopped | "LRF heats not coming since 8th" | words + time | health: last write vs cadence, event, workflow runs | L3 / NEEDS_HUMAN_ACTION with the stop point |
| Error wave | "many SAP GR errors this week" | words + time | error tables per day, top messages | RESOLUTION (explain) / NEEDS_HUMAN_ACTION (SAP side) |
| Screen does not show it | "billet on bed not on screen" | screen + identifier | list-view filter vs the row's status | RESOLUTION (explain the filter) |
| Report/total mismatch | "production summary lower than SAP" | report words + date | report procedure's sources for the date | QUESTION / L3 |
| Master data | "new grade not in dropdown" | words + name | master table lookup | NEEDS_HUMAN_ACTION |
| Not data | how-to, login, slowness, printer, change request | none | none | not L2: knowledge answer / access team / L3 infra / change process |

## Tests (E2E only)

- `Model_Bench/e2e/run_walk.py`: identifier tickets (8/8 today).
- `Model_Bench/e2e/general_cases.jsonl` + failure modes: tickets without identifiers across the
  rows above, with ground truth taken from real data.
- Held-out set written by Qwen from real faults, scored only at the end.
