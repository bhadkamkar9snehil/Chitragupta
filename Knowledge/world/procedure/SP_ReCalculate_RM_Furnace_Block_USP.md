---
type: procedure
title: "SP_ReCalculate_RM_Furnace_Block_USP"
built: "2026-09-24T11:36:36"
---

# SP_ReCalculate_RM_Furnace_Block_USP

Parameters: @ReportDate date.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes (named in its SQL text)

- RM_Furnace_Parameter

## Calls

- Xstudio_Historian_RM_Furnace_Logbook_Block_usp
