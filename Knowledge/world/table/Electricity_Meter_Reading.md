---
type: table
title: "Electricity_Meter_Reading"
built: "2026-09-24T11:36:36"
---

# Electricity_Meter_Reading

Table in XStudio_Xbatch. Rows: 45,120.

## Written by

- XBatch_Electricity_Meter_Consumption_Usp
- XSTUDIO_WORKFLOW_0C110E49-9524-40BE-9C70-4A0BEDB53C79_SP (text)
- XSTUDIO_WORKFLOW_2D29BB58-88E0-4211-B392-36920B94C0F7_SP (text)
- XSTUDIO_WORKFLOW_B0E88401-847E-4370-9B0F-6D0BD87E68E2_SP (text)
- Xstudio_Electricity_Meter_Reading_USP

## Read by

- XBatch_Electricity_Meter_Consumption_Usp
- XMES_Electricity_Bill_Calculator_USP
- XMES_RM_Production_Summary_Usp
- XSTUDIO_WORKFLOW_0C110E49-9524-40BE-9C70-4A0BEDB53C79_SP
- XSTUDIO_WORKFLOW_2D29BB58-88E0-4211-B392-36920B94C0F7_SP
- XSTUDIO_WORKFLOW_B0E88401-847E-4370-9B0F-6D0BD87E68E2_SP
- Xstudio_Electricity_Meter_Reading_USP

## Columns

- ID varchar(36)
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
- EndDateTime datetime
- ReportDate date
- IsProcessed bit
- Position int
- Value decimal
- Quality int
- Price varchar(100)
- FeederName varchar(100)
- Consumption decimal
- Status varchar(50)
- MonthNumber int
