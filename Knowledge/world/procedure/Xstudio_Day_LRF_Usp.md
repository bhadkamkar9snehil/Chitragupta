---
type: procedure
title: "Xstudio_Day_LRF_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Day_LRF_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- LRF_Summary_Day: Aluminium, ArgonConsumption, Avg_CalcLiquidMetalWeight, Avg_LiquidMetalWeight, CalcLiquidMetalWeight, Carbon, Dolo, FeSi, FlourSpar, HeatID, Lime, LiquidMetalWeight, ModifiedOn, PowerMWH, ReportDate, SiMn, SiMnn, Source, TotalElectrodeConsumptionKg

## Reads

- LRF_Per_Heat: Aluminium, ArgonConsumption, CalcLiquidMetalWeight, Carbon, Dolo, FeSi, FlourSpar, HeatID, HeatReportDate, ID, IsDeleted, Lime, LiquidMetalWeight, PowerMWH, ReportDate, SiMn, SiMnn, TotalElectrodeConsumptionKg

## Calls

- XStudio_Update_Day_LRF_Usp
