---
type: note
subtype: investigation-recipe
route: billet_inventory
authority: harness-contract
---
# Trace billet genealogy, count, transfer and inventory/master relationships.

Recipe ID: xbatch.billet-inventory.v1
Typed probes: xstudio_heat_context
Required evidence: billet_genealogy

## Interpretation rules
- Billet yard and electrical switchyard are unrelated domains.
- Operator and tag-driven billet counts may differ.

## Stop conditions
- Heat, strand, billet and current inventory identity are reconciled.

## Escalation conditions
- Genealogy is absent across all canonical surfaces or repair requires mutation.
