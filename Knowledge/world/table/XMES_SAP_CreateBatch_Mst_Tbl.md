---
type: table
title: "XMES_SAP_CreateBatch_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_CreateBatch_Mst_Tbl

Table in XStudio_Xbatch. Rows: 3,616.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- HeatNo: same values as key `HeatNo`

## Written by

- XMES_I_SAP_Billet_Production_Trn

## Read by

- XMES_I_API_Transaction_Summary
- XMES_I_SAP_Billet_Production_Trn
- XMES_SAP_Batch_Creation_API_Error_Usp
- XMES_SAP_Posting_Sequence_Usp

## Columns

- ID varchar(36)
- Batch varchar(100)
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
- Material varchar(100)
- BatchIdentifyingPlant varchar(100)
- BatchIsMarkedForDeletion varchar(100)
- MatlBatchIsInRstrcdUseStock varchar(100)
- Supplier varchar(100)
- BatchBySupplier varchar(100)
- CountryOfOrigin varchar(100)
- RegionOfOrigin varchar(100)
- CreationDateTime datetime
- LastChangeDateTime datetime
- BatchExtWhseMgmtInternalId varchar(100)
- SAPTransactionID varchar(100)
- SAPPostingStatus varchar(50)
- HeatNo int
