---
type: table
title: "MES_Raw_Material_Consumptions_Mapping_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_Raw_Material_Consumptions_Mapping_Mst_Tbl

Table in XStudio_Xbatch. Rows: 57.

## Read by

- HeatChargeMixConsumption
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_RM_Raw_Material_Entry_Usp
- XMES_entry_for_RAW_Material_Consumption_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP

## Columns

- ID varchar(36)
- RawMaterialName varchar(100)
- Materialid varchar(-1)
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
- MaterialType varchar(100)
- Srno int
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Unitid varchar(36)
- Entityids varchar(-1)
- Attributeids varchar(-1)
