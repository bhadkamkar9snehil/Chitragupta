---
type: Diagnostic
route: sap_posting
authority: harness-contract
---
# Trace a production or consumption posting from MES state to outbound SAP result.

Recipe ID: xbatch.sap-posting.v1
Typed probes: xstudio_heat_context, xstudio_sap_api_context
Required evidence: sap_posting_state, sap_api_result

## Interpretation rules
- Pending, failed and never-created are different states.
- Absence from one surface does not prove causation.

## Stop conditions
- MES record, outbound posting and API outcome are reconciled.

## Escalation conditions
- Required correction is a production write or identifier remains ambiguous.

