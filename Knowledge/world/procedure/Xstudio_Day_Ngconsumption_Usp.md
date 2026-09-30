---
type: procedure
title: "Xstudio_Day_Ngconsumption_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Day_Ngconsumption_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- Ngconsumption_Summary_Day: AvgResidenceTime, ColdDischargeBillet, Discharged, HotDischargeBillet, ModifiedOn, NGCong, NGCons, ReportDate, Source, TotalBillet, TotalNG

## Reads

- RM_NGConsumption: ColdDischargeBillet, Date, Discharged, HotDischargeBillet, ID, IsDeleted, NGCong, NGCons, TotalBillet
- XMES_Live_Charging_SECT2: BilletNo, OutTime, TotalResidenceTime

## Calls

- XStudio_Update_Day_Ngconsumption_Usp
