---
type: procedure
title: "Xstudio_Electricity_Meter_Bill_Amount_USP"
built: "2026-09-24T11:36:36"
---

# Xstudio_Electricity_Meter_Bill_Amount_USP

Parameters: @ID varchar, @Mode varchar.

## Writes

- Electricity_Meter_Bill_Amount: ActualBillAmount, CalculatedBillAmount, CalculatedCurrentMonthCharge, CalculatedVAT, CurrentMonthCharge, Difference, Source, TransmissionSystemCharge, VAT

## Reads

- Electricity_Meter_Bill_Amount: ActualEnergyCharge, CGRT, CPRT, DistributionSystemCharge, ID, NCPRT, SSRT, SupplyServiceCharge, ToURT, TotalEnergyCharge
