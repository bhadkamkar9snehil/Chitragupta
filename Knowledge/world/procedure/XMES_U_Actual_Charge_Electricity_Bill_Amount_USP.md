---
type: procedure
title: "XMES_U_Actual_Charge_Electricity_Bill_Amount_USP"
built: "2026-09-24T11:36:36"
---

# XMES_U_Actual_Charge_Electricity_Bill_Amount_USP

Parameters: @FeederName varchar, @MonthYear varchar.

## Writes

- Electricity_Meter_Bill_Amount: ActualEnergyCharge

## Reads

- Electricity_Meter_Bill_Amount: FeederName, MonthYear
- Electricity_Meter_Bill_Details_Time_Of_Use: Charge, FeederName, MonthYear
