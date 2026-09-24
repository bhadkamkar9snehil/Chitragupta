---
type: procedure
title: "Xstudio_Shift_EAF_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Shift_EAF_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- EAF_Summary_Shift: Avg_LiquidMetalWeight, Avg_PowerMW, Avg_PoweroffTIme, Avg_PoweronTIme, Avg_TTT, BIN1LimeConsumption, BIN2DoloConsumption, BIN3Consumption, BIN4Consumption, BriquetteCH1, BriquetteCH2, BundleLMS, BundleLMSCH1, BundleLMSCH2, BundleLMSCH3, BundleLMSCH4, CarbonConsumption, CdriConsumption, ChargeWeight, CopexScrap, CopexScrapCH1, CopexScrapCH2, CopexScrapCH3, CopexScrapCH4, EndCuts, EndCutsCH1, EndCutsCH2, EndCutsCH3, EndCutsCH4, EntryDateTime, HBIConsumption, HBIDRICH1, HBIDRICH2, HMS1, HMS12, HMS12CH1, HMS12CH2, HMS12CH3, HMS12CH4, HMS1CH1, HMS1CH2, HMS1CH3, HMS1CH4, HeatID, LadleAdditionDolo, LadleAdditionFeSi, LadleAdditionLime, LadleAdditionSiMn, LadleAdditionSiMnn, LiquidMetalWeight, ModifiedOn, NGConsumption, NutCokeKgPerTon, OxygenConsumption, PowerMWH, PowerOnTimeMinute, Scull, ScullCH1, ScullCH2, ScullCH3, ScullCH4, ShiftName, Shreedded, ShreeddedCH1, ShreeddedCH2, ShreeddedCH3, ShreeddedCH4, Source, TotalChargeWeightMT, TotalElectrodeConsumption, YieldPerHeat

## Reads

- EAF_PER_HEAT: Avg_PowerMW, Avg_PoweroffTIme, Avg_PoweronTIme, Avg_TTT, BIN1LimeConsumption, BIN2DoloConsumption, BIN3Consumption, BIN4Consumption, BriquetteCH1, BriquetteCH2, BundleLMS, BundleLMSCH1, BundleLMSCH2, BundleLMSCH3, BundleLMSCH4, CarbonConsumption, CdriConsumption, ChargeWeight, CopexScrap, CopexScrapCH1, CopexScrapCH2, CopexScrapCH3, CopexScrapCH4, EndCuts, EndCutsCH1, EndCutsCH2, EndCutsCH3, EndCutsCH4, HBIConsumption, HBIDRICH1, HBIDRICH2, HMS1, HMS12, HMS12CH1, HMS12CH2, HMS12CH3, HMS12CH4, HMS1CH1, HMS1CH2, HMS1CH3, HMS1CH4, HeatID, HeatReportDate, ID, IsDeleted, LadleAdditionDolo, LadleAdditionFeSi, LadleAdditionLime, LadleAdditionSiMn, LadleAdditionSiMnn, LiquidMetalWeight, NGConsumption, NutCokeKgPerTon, OxygenConsumption, PowerMWH, PowerOnTimeMinute, ReportDate, Scull, ScullCH1, ScullCH2, ScullCH3, ScullCH4, Shreedded, ShreeddedCH1, ShreeddedCH2, ShreeddedCH3, ShreeddedCH4, TotalChargeWeightMT, TotalElectrodeConsumption, YieldPerHeat
- EAF_Summary_Shift: ReportDate
- XStudio_Shift_Dtl_Tbl: EndTime, IsDeleted, Name, ParentID, StartTime
- XStudio_Shift_Mst_Tbl: ID
