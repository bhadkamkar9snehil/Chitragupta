---
type: table
title: "Electricity_Meter_Bill_Details_Time_Of_Use"
built: "2026-09-24T11:36:36"
---

# Electricity_Meter_Bill_Details_Time_Of_Use

Table in XStudio_Xbatch. Rows: 56.

## Written by

- XMES_Electricity_Bill_Calculator_USP
- Xstudio_Electricity_Meter_Bill_Details_Time_Of_Use_USP

## Read by

- XMES_Electricity_Bill_Calculator_USP
- XMES_U_Actual_Charge_Electricity_Bill_Amount_USP
- Xstudio_Electricity_Meter_Bill_Details_Time_Of_Use_USP

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Charge decimal
- Rate varchar(100)
- Consumption decimal
- TimeofUse varchar(-1)
- FeederName varchar(100)
- Year int
- MonthNumber int
- Month varchar(100)
- MonthYear varchar(-1)
