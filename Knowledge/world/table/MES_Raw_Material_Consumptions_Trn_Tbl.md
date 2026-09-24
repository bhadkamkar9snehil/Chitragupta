---
type: table
title: "MES_Raw_Material_Consumptions_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_Raw_Material_Consumptions_Trn_Tbl

Table in XStudio_Xbatch. Rows: 11,073.

## Written by

- XMES_RM_Raw_Material_Entry_Usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_entry_for_RAW_Material_Consumption_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP (text)
- Xstudio_MES_Raw_Material_Consumptions_Trn_Tbl_USP

## Read by

- XMES_RM_Raw_Material_Entry_Usp
- XMES_Raw_Material_cons_status_count_usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_entry_for_RAW_Material_Consumption_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP
- Xstudio_MES_Raw_Material_Consumptions_Trn_Tbl_USP

## Columns

- ID varchar(36)
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
- ReportDate date
- CapturedQuantity decimal
- DeclaredQuantity decimal
- Unit varchar(36)
- WorkOrder varchar(36)
- SAPWorkflowStatus varchar(50)
- LotNumber varchar(-1)
- Price decimal
- Difference decimal
- OrderType varchar(100)
- WorkOrderNo varchar(100)
