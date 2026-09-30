---
type: table
title: "XMES_CCM_Billet_Genealogy_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_CCM_Billet_Genealogy_Trn_Tbl

Table in XStudio_Xbatch. Rows: 14,245.

## Identifiers it holds

- BilletNo: same values as key `BilletNo-2`
- HeatNo: same values as key `HeatNo`

## Written by

- XMES_CCM_BILLET_CUT_USP
- XMES_CCM_BILLET_PRODUCED_USP

## Read by

- XMES_CCM_BILLET_MASTER_CREATE_USP
- XMES_CCM_BILLET_PRODUCED_USP

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
- CutEventID varchar(36)
- Status varchar(50)
- ChargeType varchar(100)
- StrandSequence int
- IsProcessed bit
- StrandNo varchar(100)
- BilletSequence int
- HeatNo varchar(100)
- BilletNo varchar(100)
- CutStartTime datetime
- CutEndTime datetime
- ProducedStartTime datetime
- ProducedEndTime datetime
- ProducedEventID varchar(36)
