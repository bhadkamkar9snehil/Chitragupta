---
type: table
title: "Quality_Spectro_File"
built: "2026-09-24T11:36:36"
---

# Quality_Spectro_File

Table in XStudio_Xbatch. Rows: 23,023.

## Written by

- usp_Quality_Spectro_Cleanup
- usp_Quality_Spectro_IngestFromPath

## Read by

- usp_Quality_Spectro_Cleanup

## Columns

- ID varchar(36)
- FileName varchar(1000)
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
- Importedon datetime
- IsProcessed bit
- FilePath varchar(4000)
- Checksum varchar(100)
- FileStatus varchar(30)
- STatusNote varchar(500)
