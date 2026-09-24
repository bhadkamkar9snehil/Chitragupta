---
type: table
title: "MES_SAP_UsageDecision_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_SAP_UsageDecision_Trn_Tbl

Table in XStudio_Xbatch. Rows: 4,883.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`
- InspectionLot: same values as key `InspectionLot`

## Written by

- XMES_SAP_Posting_Sequence_Usp
- XSTUDIO_WORKFLOW_C5631C30-B02A-4FEF-B2B7-E811DB1A0B59_SP

## Read by

- XMES_I_API_Transaction_Summary
- XMES_SAP_Posting_Sequence_Usp
- XMES_SAP_Usage_Decision_API_Error_Usp

## Columns

- ID varchar(36)
- InspectionLot varchar(100)
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
- UsgDecCode varchar(100)
- Message varchar(100)
- SAPPostingStatus varchar(50)
- SAPTransactionID varchar(100)
- HeatNo int
- MaterialType varchar(100)
