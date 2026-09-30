---
type: table
title: "XMES_Stage_Position_Mapping_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_Stage_Position_Mapping_Mst_Tbl

Table in XStudio_Xbatch. Rows: 93.

## Read by

- Billet_Furnace_Movement
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- MES_M_Strand
- MES_M_Strand_TMT
- MES_M_Strand_WRM
- XMES_I_Billets_Tracking_Usp
- XMES_I_SAP_Billet_Production_Trn
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xmes_Billet_Tracking_Move_to_Stand_18

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
- StageCode varchar(36)
- PositionType varchar(36)
