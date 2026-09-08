---
type: Diagnostic
route: quality
authority: harness-contract
---
# Trace chemistry, spectro, quality deviation and SAP quality-decision evidence.

Recipe ID: xbatch.quality.v1
Typed probes: xstudio_heat_context, xstudio_sap_api_context
Required evidence: quality_result, sap_api_result

## Interpretation rules
- File, sample and result are separate stages.
- Configuration thresholds are not transaction results.

## Stop conditions
- The failed or completed quality stage is identified.

## Escalation conditions
- The relevant product/quality path is ambiguous or needs configuration mutation.

