---
type: procedure
title: "XMES_Recalculate_heat_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Recalculate_heat_Usp

Parameters: @id varchar, @type varchar.

## Reads

- CCM_Per_Heat: HeatReportDate, ID, IsDeleted
- EAF_PER_HEAT: HeatID, HeatReportDate, ID, IsDeleted
- LRF_Per_Heat: HeatID, HeatReportDate, ID, IsDeleted

## Calls

- XStudio_Schedule_TSQL_Task_Usp
