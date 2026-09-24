---
type: event
title: "EAF_SMS/HeatIDChange"
built: "2026-09-24T11:36:36"
---

# EAF_SMS/HeatIDChange

Area EAF_SMS. Active.
Creates and updates rows in EAF_PER_HEAT.

## State 1: HeatDataCapture

Condition: `IIF({Tapping1} = 1 AND {LivePowerONTime} > 0, True, IIF({Tapping1} = 0 AND {LivePowerONTime} = 0, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: DOLOConsumption -> BIN2DoloConsumption, ChargeWeight -> ChargeWeight, HeatID -> HeatID, LIMEConsumption -> BIN1LimeConsumption, Bin4Name -> BIN4Name, Bin3Name -> BIN3Name, BIN4Consumption -> BIN4Consumption, BIN3Consumption -> BIN3Consumption, TotalchargeWeightMT -> TotalChargeWeightMT, PowerOffTimeSecond -> PowerOFFTimeSecond, HeatTimeSecond -> HeatTimeSecond, HeatTimeMinute -> HeatTimeMinute, PowerOffTimeMinute -> PowerOFFTimeMinute, NGConsumption -> NGConsumption, Carbon -> CarbonConsumption, OxygenConsumption -> OxygenConsumption, PowerMWH -> PowerMWH, PowerOnTimeMinute -> PowerOnTimeMinute, PowerOnTimeSecond -> PowerOnTimeSecond, LiquidMetalWeight -> LiquidMetalWeight
