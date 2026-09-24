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
