---
type: table
title: "Billet_Track_Per_Strand"
built: "2026-09-24T11:36:36"
---

# Billet_Track_Per_Strand

Table in XStudio_Xbatch. Rows: 65,510.

## Identifiers it holds

- Status: same values as key `StateName`

## Written by

- XSTUDIO_WORKFLOW_04013B64-BE2F-4813-9888-57B0E66288DB_SP (text)
- XSTUDIO_WORKFLOW_5ACC8A8C-2983-4EEF-ABD3-F027D83F5764_SP (text)

## Read by

- XMES_CCM_BILLET_CUT_USP
- XMES_CCM_BILLET_PRODUCED_USP
- XMES_CREATE_BILLETNO_USP
- XSTUDIO_WORKFLOW_04013B64-BE2F-4813-9888-57B0E66288DB_SP
- XSTUDIO_WORKFLOW_5ACC8A8C-2983-4EEF-ABD3-F027D83F5764_SP

## Rows created by events

- CCM_SMS:Billet Tracking Strandwise

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
- WorkflowStatus varchar(50)
- HeatNo int
- StrandwiseCount int
- S1BilletCount int
- S2BilletCount int
- S3BilletCount int
- S4BilletCount int
- S5BilletCount int
- S6BilletCount int
