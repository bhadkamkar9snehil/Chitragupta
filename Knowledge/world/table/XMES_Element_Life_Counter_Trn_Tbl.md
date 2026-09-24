---
type: table
title: "XMES_Element_Life_Counter_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_Element_Life_Counter_Trn_Tbl

Table in XStudio_Xbatch. Rows: 29.

## Identifiers it holds

- LastUsedBatch: same values as key `HeatNo`

## Written by

- SMS_Reset_Life_Tracking_Status
- XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP

## Read by

- SMS_Reset_Life_Tracking_Status
- XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP

## Columns

- ID varchar(36)
- CurrentLife int
- ElementNameID varchar(-1)
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
- ConsumeLifepercentage decimal
- AlertPercentage int
- LastUsedBatch varchar(100)
- MaximumLife int
