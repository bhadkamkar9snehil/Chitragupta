---
type: procedure
title: "XMES_Recalculate_HEAT_CHEMISTRY_DEVIATION_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Recalculate_HEAT_CHEMISTRY_DEVIATION_Usp

Parameters: @Reportdate date.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- Chemistry_Deviation_Quality_Data: CreatedOn, Elements, Grade, HeatNo, LRFAtActualPercentage, ModifiedOn, ReportDate, Shift, ShiftIncharge, Source, TundishAtActualPercentage

## Reads

- Chemistry_Deviation_Quality_Data: Elements, Grade, HeatNo, ID, IsDeleted, ReportDate, Shift, ShiftIncharge
- Heat_Chemistry_Quality_Data: HeatNo, IsDeleted, SampleType, Status
- Heat_End_Selection_Trn_Tbl: FirstHeatNo, IsDeleted, LastHeatNo, ReportDate
