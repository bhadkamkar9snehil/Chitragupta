---
type: Diagnostic
route: performance
authority: harness-contract
---
# Trace delay/OEE events, classification, equipment and aggregate projections.

Recipe ID: xbatch.performance.v1
Typed probes: xstudio_suggest_tables
Required evidence: delay_event, delay_classification

## Interpretation rules
- Event rows and aggregate rows are not interchangeable.
- Area determines the applicable shift-delay family.

## Stop conditions
- Event, equipment, classification and report window are reconciled.

## Escalation conditions
- Affected time window or equipment identity is missing.

