---
type: procedure
title: "Xstudio_RM_NGConsumption_USP"
built: "2026-09-24T11:36:36"
---

# Xstudio_RM_NGConsumption_USP

Parameters: @ID varchar, @Mode varchar.

## Writes

- RM_NGConsumption: AvgResidenceTime, ColdDischargeBillet, HotDischargeBillet, NGCong, Shift, Source, TotalNG

## Reads

- NM3_To_MMBTU_Factor: CreatedOn, IsDeleted, ModifiedOn, Nm3toMMBTUFactor
- RM_NGConsumption: Billet130Cold, Billet130Hot, Billet140Cold, Billet140Hot, Billet150Cold, Billet150Hot, FromTime, ID, NGCons, ReportDate, TotalBillet
- XMES_Live_Charging_SECT2: BilletNo, OutTime, TotalResidenceTime
