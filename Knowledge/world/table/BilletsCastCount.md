---
type: table
title: "BilletsCastCount"
built: "2026-09-24T11:36:36"
---

# BilletsCastCount

Table in XStudio_Xbatch. Rows: 7,245.

## Written by

- XMES_Missing_Heat_Entry_USP
- XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP (text)
- XSTUDIO_WORKFLOW_B4724DFC-A609-44DA-A6D1-899EF9A79C90_SP (text)

## Read by

- SP_GET_AREAWISE_TAG_TREND
- SP_ReCalculate_CCM_SMS_Block_USP
- XMES_CCM_BILLET_CUT_USP
- XMES_CCM_BILLET_PRODUCED_USP
- XMES_CREATE_BILLETNO_USP
- XMES_Missing_Heat_Entry_USP
- XSTUDIO_WORKFLOW_5ACC8A8C-2983-4EEF-ABD3-F027D83F5764_SP
- XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP
- XSTUDIO_WORKFLOW_B4724DFC-A609-44DA-A6D1-899EF9A79C90_SP
- Xstudio_Historian_CCM_SMS_Block_usp

## Rows created by events

- CCM:Cast Billets Count

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
- EquipmentID varchar(36)
- ReportDate date
- IsProcessed bit
- StartTime datetime
- EndTime datetime
- Status varchar(100)
- HeatID decimal
- WorkFlowStatus varchar(50)
- ActualBilletsCountbyOperator decimal
