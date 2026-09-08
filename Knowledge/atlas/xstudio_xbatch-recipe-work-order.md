---
type: Diagnostic
route: work_order
authority: harness-contract
---
# Trace campaign membership, work-order master state and SAP-side creation state.

Recipe ID: xbatch.work-order.v1
Typed probes: xstudio_work_order_context
Required evidence: work_order_state

## Interpretation rules
- Internal ID, WorkOrderNumber and MESWorkOrderNumber are distinct identifiers.
- HeatNo may contain a comma-separated allocation.

## Stop conditions
- Campaign, master and external work-order identity are reconciled.

## Escalation conditions
- Creation logic requires mutation or product branch is not safely identifiable.

