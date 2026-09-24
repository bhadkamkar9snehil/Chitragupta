---
type: procedure
title: "SP_ReCalculate_NG_Configuration_Block_USP"
built: "2026-09-24T11:36:36"
---

# SP_ReCalculate_NG_Configuration_Block_USP

Parameters: @ReportDate date.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes (named in its SQL text)

- RM_NGConsumption

## Calls

- Xstudio_Historian_RM_NGConsumption_Report_usp
