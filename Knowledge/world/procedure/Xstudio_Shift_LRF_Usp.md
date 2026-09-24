---
type: procedure
title: "Xstudio_Shift_LRF_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Shift_LRF_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- LRF_Summary_Shift: Aluminium, ArgonConsumption, Avg_CalcLiquidMetalWeight, Avg_LiquidMetalWeight, CalcLiquidMetalWeight, Carbon, Dolo, Entrydatetime, FeSi, FlourSpar, HeatID, Lime, LiquidMetalWeight, ModifiedOn, PowerMWH, ShiftName, SiMn, SiMnn, Source, TotalElectrodeConsumptionKg

## Reads

- LRF_Per_Heat: Aluminium, ArgonConsumption, Avg_CalcLiquidMetalWeight, Avg_LiquidMetalWeight, CalcLiquidMetalWeight, Carbon, Dolo, FeSi, FlourSpar, HeatID, HeatReportDate, ID, IsDeleted, Lime, LiquidMetalWeight, PowerMWH, SiMn, SiMnn, TotalElectrodeConsumptionKg
- XStudio_Shift_Dtl_Tbl: EndTime, IsDeleted, Name, ParentID, StartTime
- XStudio_Shift_Mst_Tbl: ID
