# Entity resolution: ways it can fail (written before the code)

The resolver turns ticket text into the plant thing the ticket is about (heat, billet, work order,
material document, ...) and confirms it exists in XBatch. Each failure mode below has at least one
E2E case in `entity_cases.jsonl`.

1. **No identifier in the text** ("one of last night's heats"). Must return nothing, never a guess.
2. **Measurement mistaken for an identifier.** "25 min", "100 t", "37 billets", "carbon 0.07" are
   values, not entities.
3. **Several identifiers in one ticket** (heat + material document). Must return the one the
   question is about, keep the others as related.
4. **Identifier shaped right but absent from the data** (heat 1699999). Must say "not found",
   which becomes a QUESTION to the requester, not an L3 escalation.
5. **Same value in many columns** (1604014 is a HeatID, a HeatNo, a SAP Batch, and a prefix of
   billet numbers). Must resolve to the entity, not to a random column.
6. **Glued or abbreviated forms**: "heat1604015", "ht 1604013", "H1604014".
7. **Composite identifiers**: billet "1604014_S1_29" contains heat 1604014; strand "S5" alone is
   not an identifier.
8. **Dates and times read as identifiers**: "2026-07-08", "19:08".
9. **Long numbers of different kinds confused**: 12-digit work order vs 10-digit material document.
10. **Jev unavailable or slow**: must still return data-confirmed candidates, marked unranked.
11. **Too many existence checks**: bounded; the whole resolution must stay under a few seconds.
