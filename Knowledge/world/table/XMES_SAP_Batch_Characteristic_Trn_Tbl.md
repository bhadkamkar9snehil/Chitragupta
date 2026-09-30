---
type: table
title: "XMES_SAP_Batch_Characteristic_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_Batch_Characteristic_Trn_Tbl

Table in XStudio_Xbatch. Rows: 3,690.

## Identifiers it holds

- BatchNo: same values as key `HeatNo`
- HeatNo: same values as key `HeatNo`

## Written by

- XMES_I_SAP_Billet_Production_Trn
- XMES_SAP_Posting_Sequence_Usp
- XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP
- XSTUDIO_WORKFLOW_3BFFE5C9-33C9-4C50-A0F0-3665571F92D4_SP (text)

## Read by

- XMES_I_API_Transaction_Summary
- XMES_SAP_Batch_Characteristics_API_Error_Usp
- XMES_SAP_Posting_Sequence_Usp
- XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP
- XSTUDIO_WORKFLOW_3BFFE5C9-33C9-4C50-A0F0-3665571F92D4_SP

## Columns

- ID varchar(36)
- Plant varchar(100)
- Saptransactionid varchar(36)
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
- HeatNo varchar(100)
- Product varchar(100)
- Length decimal
- Thickness int
- Width int
- SectionalWeight decimal
- ProductionSectionalWeight decimal
- NoOfPieces int
- TonsPerPiece decimal
- ExternalGrade varchar(100)
- ProcessRoute varchar(100)
- InspectionAgency varchar(100)
- TDCRefNo int
- ColourCode varchar(100)
- Pieces int
- ActualGrade varchar(100)
- HeatSequenceNumber varchar(100)
- BatchNo varchar(100)
- Material varchar(100)
- SAPPostingStatus varchar(50)
- ClassNumber varchar(100)
- ClassType varchar(100)
- ObjectTable varchar(100)
- Message varchar(-1)
