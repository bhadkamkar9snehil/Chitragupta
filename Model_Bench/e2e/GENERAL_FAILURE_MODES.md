# Tickets without an identifier: ways the investigation can fail (written before the code)

L1 (the chatbot) escalates when it cannot answer from instant knowledge. Many escalations name no
heat, billet, order or document. Each mode has at least one case in `general_cases.jsonl`.

1. **Not a data problem, investigated anyway.** How-to, login, slowness, printer, change request:
   must be routed away (knowledge / access / infra / change process), not answered with table rows.
2. **Scope never found.** "LRF screen", "charging bed", "delay report": user words must map to world
   pages (screens, tables, procedures). No match means QUESTION to the requester, not a guess.
3. **Wrong scope picked.** Search returns many near misses (LRF_ProcessTime vs LRF_Per_Heat, three
   grade masters). Candidates are judged one by one, then the top few verified.
4. **Relative time misread.** "since 8th", "last night", "this week" vs a plant snapshot that ends
   on different dates per table. Dates are parsed and compared in code, never by Jev.
5. **Stale vs normal.** A table with no rows since the 8th is only a fault if it normally gets rows
   every hour. Code needs the table's normal cadence (baseline), not just its last row.
6. **Comparison target missing.** "EAF is fine, LRF is not": the evidence must include both sides.
7. **Error wave vs single error.** "Many SAP errors this week" needs counts per day and the top
   messages, not one example row.
8. **Screen filter.** Rows exist but the screen hides them; the answer is the list view's filter
   condition, found in the XStudio configuration, not in the data tables.
9. **Master data absent.** "Grade not in dropdown": the right answer is "not present in the master
   table the screen reads" plus NEEDS_HUMAN_ACTION, not an L3 escalation.
10. **Slow or heavy probes.** Health checks over big tables must come from a prebuilt index, never a
    live full scan per ticket (the shared server starved when scans overlapped).
11. **Credentials leak.** The XStudio data source table stores passwords; nothing from it may enter
    pages, evidence or replies.
