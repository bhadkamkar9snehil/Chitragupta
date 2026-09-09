---
type: note
subtype: investigation-recipe
route: heat_execution
authority: harness-contract
---
# Trace a heat through EAF, LRF, CCM, billet and related work-order state.

Recipe ID: xbatch.heat-execution.v1
Typed probes: xstudio_heat_context
Required evidence: heat_process_state

## Interpretation rules
- Multiple rows may represent workflow stages.
- Reference formulas require current-definition verification before causal use.

## Stop conditions
- The heat stage and disputed value are established from current rows.

## Escalation conditions
- Heat identity is ambiguous or correction requires a write.
