---
type: table
title: "Electricity_Meter_Electricity_Bill_Details"
built: "2026-09-24T11:36:36"
---

# Electricity_Meter_Electricity_Bill_Details

Table in XStudio_Xbatch. Rows: 1,236.

## Written by

- XBatch_Electricity_Bill_Calculator_USP (text)
- XMES_Electricity_Bill_Calculator_USP

## Read by

- SMS_Electricity_Meter_Bill_Amount_USP
- XMES_Electricity_Bill_Calculator_USP

## Columns

- ID varchar(36)
- Name varchar(100)
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
- Month varchar(100)
- ReportDate date
- IsProcessed bit
- Charge decimal
- Rate decimal
- Consumption decimal
- TimeOfUse varchar(100)
- Year int
- MonthNumber int
- FeederName varchar(500)
- ConsumptionKWh decimal
