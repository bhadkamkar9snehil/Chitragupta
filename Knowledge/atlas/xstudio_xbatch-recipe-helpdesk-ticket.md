---
type: note
subtype: investigation-recipe
route: helpdesk_ticket
authority: harness-contract
---
# Verify ticket, workflow and response state through the audited Helpdesk context.

Recipe ID: xbatch.helpdesk-ticket.v1
Typed probes: xstudio_get_ticket_context
Required evidence: ticket_state

## Interpretation rules
- Helpdesk and Hermes terminal state must agree.

## Stop conditions
- Current ticket and response state are established.

## Escalation conditions
- Workflow binding is absent or contradictory.
