---
type: table
title: "XMES_SMS_Grade_Protocol_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_SMS_Grade_Protocol_Mst_Tbl

Table in XStudio_Xbatch. Rows: 9.

## Written by

- XMES_Duplicate_Grade_Protocol_Mst_Usp (text)

## Read by

- XMES_Duplicate_Grade_Protocol_Mst_Usp
- XMES_I_Grade_Protocol_Chemistry_USP
- XMES_SP_HEAT_CHEMISTRY_REPORT_DATA

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
- SectionID varchar(36)
- GradeID varchar(36)
- ChemistryID varchar(100)
- EAFRemarks varchar(-1)
- LRFRemarks varchar(-1)
- CCMRemarks varchar(-1)
- SignedFileUpload varchar(8000)
