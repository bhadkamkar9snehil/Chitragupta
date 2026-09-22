# XStudio_Xbatch.dbo.XBatch_Unit_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference current, batch, description, enabled, procedure, status, unit.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-07-01T12:44:38.0000000 to 2025-07-01T12:44:38.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | NO | 100 | — |
| ParentID | varchar | NO | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Description | varchar | YES | -1 | — |
| IsEnabled | bit | YES | — | — |
| Status | varchar | YES | 100 | — |
| CurrentBatchID | varchar | YES | 36 | — |
| CurrentUnitProcedureID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6FE26AD3-1023-46F9-979E-4B25C05EB7FB | RM | F495EBC2-57EE-4571-BCA6-E7047E3688F0 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-01T12:44:39.0400000 | 2025-07-01T12:44:38.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_Unit_Procedure_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Mst_Tbl.CurrentBatchID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Mst_Tbl.CurrentUnitProcedureID` -> `XStudio_XBatch.XBatch_Batch_Unit_Procedure_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
