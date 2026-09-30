---
type: table
title: "Per_Heat_LadleNo"
built: "2026-09-24T11:36:36"
---

# Per_Heat_LadleNo

Table in XStudio_Xbatch. Rows: 38.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- Per_Heat_LadleNo_Conformation_usp
- SMS_Ladle_Life_Tracking

## Read by

- Per_Heat_LadleNo_Conformation_usp
- SMS_Ladle_Life_Tracking
- XMES_Dashboard_LRF_Live_USP

## Columns

- ID varchar(36)
- HeatNo int
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
- LadleNo varchar(-1)
- LadleNoAtEAF bit
- LadleNoAtLRF bit
- LadleNoAtCCM bit
- EntryTime datetime
- LadleNoAtEAFDatetime datetime
- LadleNoAtLRFDatetime datetime
- LadleNoAtCCMDatetime datetime
- EAFShellNo varchar(36)
- TundishNo varchar(36)
