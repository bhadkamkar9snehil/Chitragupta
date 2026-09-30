---
type: table
title: "Electricity_Meter_Bill_Amount"
built: "2026-09-24T11:36:36"
---

# Electricity_Meter_Bill_Amount

Table in XStudio_Xbatch. Rows: 16.

## Written by

- SMS_Electricity_Meter_Bill_Amount_USP (text)
- XMES_Electricity_Bill_Calculator_USP
- XMES_U_Actual_Charge_Electricity_Bill_Amount_USP
- Xstudio_Electricity_Meter_Bill_Amount_USP

## Read by

- XMES_Electricity_Bill_Calculator_USP
- XMES_U_Actual_Charge_Electricity_Bill_Amount_USP
- Xstudio_Electricity_Meter_Bill_Amount_USP

## Columns

- ID varchar(36)
- MonthYear varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- TotalEnergyCharge decimal
- TransmissionSystemCharge decimal
- ActualBillAmount decimal
- Month varchar(100)
- Year int
- CalculatedBillAmount decimal
- TotalEngeryConsumptionCalculate decimal
- FeederName varchar(500)
- Difference decimal
- ActualEnergyCharge decimal
- MonthNumber int
- DistributionSystemCharge decimal
- SupplyServiceCharge decimal
- CurrentMonthCharge decimal
- AccountNo varchar(100)
- VAT decimal
- SSRT decimal
- ToURT decimal
- CGRT decimal
- CPRT decimal
- NCPRT decimal
- CurrentMonthVAT decimal
- CalculatedCurrentMonthCharge decimal
- CalculatedVAT decimal
