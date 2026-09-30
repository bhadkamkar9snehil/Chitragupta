---
type: procedure
title: "XStudio_Update_Day_Ngconsumption_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Update_Day_Ngconsumption_Usp

Parameters: @ReportDate date.

## Writes

- Ngconsumption_Summary_Day: ColdDischargeBillet_MTD, ColdDischargeBillet_YTD, Discharged_MTD, Discharged_YTD, HotDischargeBillet_MTD, HotDischargeBillet_YTD, ModifiedOn, NGCong_MTD, NGCong_YTD, NGCons_MTD, NGCons_YTD, Source, TotalBillet_MTD, TotalBillet_YTD, TotalNG_MTD, TotalNG_YTD

## Reads

- Ngconsumption_Summary_Day: ColdDischargeBillet, Discharged, HotDischargeBillet, IsDeleted, NGCong, NGCons, ReportDate, TotalBillet, TotalNG
