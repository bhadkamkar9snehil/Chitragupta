---
type: note
subtype: investigation-recipe
route: api_transaction
authority: harness-contract
---
# Determine whether a named API transaction ran and its latest recorded result.

Recipe ID: xbatch.api-transaction.v1
Typed probes: xstudio_sap_api_context
Required evidence: sap_api_result

## Interpretation rules
- Use the latest row per transaction and exclude test/configuration noise.

## Stop conditions
- Latest live API result for the requested identifier is established.

## Escalation conditions
- API type cannot be identified safely.
