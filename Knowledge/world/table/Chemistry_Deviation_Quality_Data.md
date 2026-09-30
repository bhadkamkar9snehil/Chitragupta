---
type: table
title: "Chemistry_Deviation_Quality_Data"
built: "2026-09-24T11:36:36"
---

# Chemistry_Deviation_Quality_Data

Table in XStudio_Xbatch. Rows: 3,997.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- XMES_Recalculate_HEAT_CHEMISTRY_DEVIATION_Usp
- XMES_SP_HEAT_CHEMISTRY_DEVIATION

## Read by

- XMES_Recalculate_HEAT_CHEMISTRY_DEVIATION_Usp
- XMES_SP_HEAT_CHEMISTRY_DEVIATION

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
- HeatNo varchar(36)
- Remarks varchar(-1)
- Shift varchar(100)
- Elements varchar(100)
- TundishAtActualPercentage decimal
- ProductAtActualPercentage decimal
- MinPercentageAsPerSMSProtocol decimal
- MinPercentageAsPerTDC decimal
- MaxPercentageAsPerSMSProtocol decimal
- ShiftIncharge varchar(300)
- LRFAtActualPercentage decimal
- MaxPercentageAsPerTDC decimal
- ReportDate date
- IsProcessed bit
- Grade varchar(100)
