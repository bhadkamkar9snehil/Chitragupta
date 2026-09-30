---
type: table
title: "Particulars_Masters"
built: "2026-09-24T11:36:36"
---

# Particulars_Masters

Table in XStudio_Xbatch. Rows: 62.

## Identifiers it holds

- Particulars: same values as key `Particulars`

## Read by

- SP_SMS_Producation_Summary
- XBatch_I_Particular_Master_Trn_Usp
- XBatch_Particular_Target_Usp
- XBatch_SMS_Production_Details_ForTheDay_Usp
- XMES_I_Particulars_for_BestData_Usp
- XStudio_Get_SMS_Monthly_Production_Summary

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
- ParentID varchar(36)
- UOM varchar(100)
- Type varchar(100)
- SrNo int
- Name varchar(100)
- ReportDate datetime
- Particulars varchar(100)
