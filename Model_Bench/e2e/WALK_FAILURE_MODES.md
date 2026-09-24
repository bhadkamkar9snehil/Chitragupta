# Evidence walk: ways it can fail (written before the code)

The walk takes a resolved entity (a heat), finds every table in the process world that holds it,
lets code summarise each hit in plain words, and asks Jev which hit explains the ticket.
Each failure mode below has at least one E2E case in `walk_cases.jsonl`.

1. **Heat touches many tables.** Dozens of hits; the explaining one must still be picked. Options
   stay short, since Jev is weak with long context.
2. **Heat stored under another shape.** SAP batches carry suffixes ("1603937_12"); genealogy uses
   HeatNo, CCM uses HeatID, SMS uses ActualHeatID. Matching must cover the exact value and the
   `<heat>_<n>` form.
3. **Type mismatch.** HeatID is int in one table and varchar in another; comparison must not fail
   or silently drop the table.
4. **Question is not about data** (how-to, reprint, access). Jev must be able to say "none of
   these" instead of picking the noisiest table.
5. **Several real faults on one heat** (1603945 has SAP errors and a billet-count gap). The pick
   must follow the ticket's wording, not the loudest fault.
6. **Slow scan.** 266 tables, some with millions of rows. The whole walk must stay within ~15 s;
   one table's timeout must not sink the walk.
7. **Numbers.** Counts and comparisons are computed by code and shown as words; Jev never does
   arithmetic.
8. **Jev unavailable.** Return the hits unranked and say so; the case fails honestly.
9. **Heat not in XBatch.** No hits: the answer is "not found", not a guess.
10. **Forced single choice.** One pick out of ~30 findings cannot describe a chain (what the user sees,
    then the stuck record, then the error behind it) and pushes Jev into swapping cause and effect.
    Every finding gets its own role judgement in one batched call.
11. **Two numbers from two sources** ("report says 42, tracking shows 41"). Each number must be traced
    to where it is stored (a column value or a row count); Jev matches each source to the requester's
    wording; code compares. Picking one table cannot answer it.
12. **Requester's number not stored anywhere.** Say so; do not attach it to the nearest table.

## Step-by-step walk over the GBrain world (Jev picks one step at a time)

13. **Loops.** Jev revisits a node it has already seen. Visited nodes never reappear as options.
14. **Too many options.** A table read by 60 procedures gives 60+ options; Jev's choice tops out at
    255 and gets worse long before that. Options are the links of visited nodes only; if still too
    many, Jev first picks the link type (writes / reads / calls / holds / events) and then the node.
15. **Stopping too early.** Jev stops at the first stuck record without reaching the error behind it.
    The stop option is judged like any other option, and the trail keeps every role so the test can
    see a missing cause.
16. **Never stopping.** A hard step limit ends the walk and says so in the trail.
17. **Dead end.** A node with no unvisited links: the walk continues from the other open links.
18. **A step the data cannot show.** A procedure with no runtime log for this identifier: the
    observation says "no runs logged for this value", which is itself evidence, not an error.
