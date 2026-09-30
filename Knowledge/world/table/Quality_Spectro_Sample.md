---
type: table
title: "Quality_Spectro_Sample"
built: "2026-09-24T11:36:36"
---

# Quality_Spectro_Sample

Table in XStudio_Xbatch. Rows: 23,023.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- usp_Quality_Spectro_Cleanup
- usp_Quality_Spectro_IngestFromPath

## Read by

- usp_Quality_Spectro_BuildWideForSample
- usp_Quality_Spectro_Cleanup
- usp_Quality_Spectro_RebuildWide

## Columns

- ID varchar(36)
- SampleName varchar(100)
- FileID varchar(36)
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
- XMLCreatedAt datetime
- HeatNo varchar(100)
- SamplePoint varchar(100)
- OperatorName varchar(100)
- MethodName varchar(100)
- MethodVersion varchar(100)
- Instrument varchar(100)
- InstrumentNumber varchar(100)
- SampleType varchar(100)
- SampleReceivedTime datetime
