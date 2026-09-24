---
type: table
title: "XMES_CCM_Billet_Sequence_New"
built: "2026-09-24T11:36:36"
---

# XMES_CCM_Billet_Sequence_New

Table in XStudio_Xbatch. Rows: 14,245.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- XMES_CCM_BILLET_CUT_USP

## Read by

- XMES_CCM_BILLET_CUT_USP

## Columns

- ID varchar(36)
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
- CurrentSequence int
- StrandNo varchar(100)
- StrandSequence int
- HeatNo varchar(100)
