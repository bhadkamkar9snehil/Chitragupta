---
type: table
title: "SAP_Posting_Tbl"
built: "2026-09-24T11:36:36"
---

# SAP_Posting_Tbl

Table in XStudio_Xbatch. Rows: 84.

## Identifiers it holds

- BatchNo: same values as key `HeatNo`

## Written by

- SAP_Posting_Data_ByHeat_Usp

## Columns

- ID varchar(36)
- WorkOrderNo varchar(100)
- HeatNo varchar(100)
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
- PlantCode varchar(100)
- StorageLocation varchar(100)
- MaterialCode varchar(100)
- BatchNo varchar(100)
- Quantity decimal
- UOM varchar(100)
- MovementType varchar(100)
- PostingType varchar(100)
- PostingDate datetime
- SAP_Status varchar(100)
- SAP_DocumentNo varchar(100)
- SAP_Message varchar(100)
- SAP_PayloadJson varchar(-1)
