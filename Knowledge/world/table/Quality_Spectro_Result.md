---
type: table
title: "Quality_Spectro_Result"
built: "2026-09-24T11:36:36"
---

# Quality_Spectro_Result

Table in XStudio_Xbatch. Rows: 1,955,354.

## Written by

- usp_Quality_Spectro_Cleanup
- usp_Quality_Spectro_IngestFromPath

## Read by

- usp_Quality_Spectro_BuildWideForSample
- usp_Quality_Spectro_Cleanup

## Columns

- ID varchar(36)
- LineName varchar(100)
- SampleID varchar(36)
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
- ReplicateNo int
- Element varchar(100)
- ResultType varchar(100)
- StatType varchar(100)
- ResultValue decimal
- Unit varchar(20)
- Status varchar(100)
- MinLimit decimal
- MaxLimit decimal
