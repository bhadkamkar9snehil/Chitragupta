---
type: table
title: "XMES_Billet_Tracking_Per_Strand"
built: "2026-09-24T11:36:36"
---

# XMES_Billet_Tracking_Per_Strand

Table in XStudio_Xbatch. Rows: 35,102.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- MES_M_Strand_Furmace (text)
- XMES_CREATE_BILLETNO_USP

## Read by

- XMES_I_Billet_ChargingBed_Usp
- XMES_I_SAP_Billet_Production_Trn

## Columns

- ID varchar(36)
- HeatNo varchar(100)
- EventID varchar(36)
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
- IsProcessed bit
- BilletNo varchar(100)
- StrandNo varchar(100)
- BilletSequence int
- ChargeType varchar(100)
- Status varchar(50)
- StrandSequence int
