---
type: Diagnostic
route: hermes_runtime
authority: harness-contract
---
# Inspect the audited run, action, trace, response and escalation lifecycle.

Recipe ID: xbatch.hermes-runtime.v1
Typed probes: xstudio_get_run_actions, xstudio_get_ticket_context
Required evidence: hermes_run_state

## Interpretation rules
- SQL/Helpdesk state outranks Kanban narration.

## Stop conditions
- Run and Helpdesk state agree or the divergence is identified.

## Escalation conditions
- A lifecycle mutation is required outside reconciliation.

