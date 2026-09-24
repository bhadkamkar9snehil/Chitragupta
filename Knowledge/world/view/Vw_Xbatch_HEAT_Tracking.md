---
type: view
title: "Vw_Xbatch_HEAT_Tracking"
built: "2026-09-24T11:36:36"
---

# Vw_Xbatch_HEAT_Tracking

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- HeatID: same values as key `HeatNo`

## Reads

- CCM_Per_Heat
- EAF_PER_HEAT
- LRF_Per_Heat
- ShiftDelayEntry

## Columns

- ReportDate varchar(100)
- HeatID int
- SteelGrade varchar(100)
- HeatStart datetime
- TapStart datetime
- TTTMinute varchar(5)
- PowerONTimeMinute varchar(5)
- PowerOffTimeMinute varchar(5)
- TapTimeMinute varchar(5)
- EAFPowerMWH decimal
- OxygenConsumption decimal
- NGConsumption decimal
- LadleAdditionLime decimal
- LadleAdditionDolo decimal
- BIN3Consumption decimal
- BIN4Consumption decimal
- CopexScrap decimal
- HMS12 decimal
- HMS1 decimal
- BundleLMS decimal
- EndCuts decimal
- Scull decimal
- Briquette decimal
- HBIDRI decimal
- Shreedded decimal
- ChargeWeight decimal
- TotalChargeWeightMT decimal
- LiquidMetalWeight decimal
- HeatForTheDay bigint
- Last10_LiquidMetalWeight_Avg decimal
- O2PerTon decimal
- NGPerTon decimal
- LimePerTon decimal
- DoloPerTon decimal
- Tapping Duration decimal
- TreatmentStart datetime
- TreatmentStop datetime
- TreatmentTime varchar(5)
- ArcingTime varchar(5)
- ArgonConsumption decimal
- PowerMWH decimal
- LadleBottomOpenTime nvarchar(8000)
- LadleBottomCloseTime nvarchar(8000)
- ArmPosition varchar(100)
- ArmConsumption decimal
- TotalBilletsCount decimal
- Strand1BilletCounter int
- Strand1CastingSpeed decimal
- Strand2BilletCounter int
- Strand2CastingSpeed decimal
- Strand3BilletCounter int
- Strand3CastingSpeed decimal
- Strand4BilletCounter int
- Strand4CastingSpeed decimal
- Strand5BilletCounter int
- Strand5CastingSpeed decimal
- Strand6BilletCounter int
- Strand6CastingSpeed decimal
- DelayDuration varchar(100)
