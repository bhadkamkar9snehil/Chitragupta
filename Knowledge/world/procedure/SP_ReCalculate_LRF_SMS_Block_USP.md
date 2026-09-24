---
type: procedure
title: "SP_ReCalculate_LRF_SMS_Block_USP"
built: "2026-09-24T11:36:36"
---

# SP_ReCalculate_LRF_SMS_Block_USP

Parameters: @ReportDate date.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- LRF_Per_Heat: EndTime, ID, IsDeleted, StartTime

## Calls

- Xstudio_Historian_LRF_SMS_Block_usp
- Xstudio_Summary_LRF_Usp
