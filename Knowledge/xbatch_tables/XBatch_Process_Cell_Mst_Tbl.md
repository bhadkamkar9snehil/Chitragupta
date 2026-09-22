# XStudio_Xbatch.dbo.XBatch_Process_Cell_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference capacity, available, batch, collector, current, description, enabled, max, min, name, next, status.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-07-01T12:44:15.0000000 to 2025-07-01T12:44:15.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | NO | 100 | — |
| ParentID | varchar | YES | 36 | — |
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
| Capacity | decimal | NO | 18,4 | — |
| UnitID | varchar | NO | 36 | — |
| Description | varchar | YES | -1 | — |
| IsEnabled | bit | YES | — | — |
| Status | varchar | YES | 36 | — |
| CurrentBatchID | varchar | YES | 36 | — |
| MinCapacity | decimal | YES | 18,4 | — |
| MaxCapacity | decimal | YES | 18,4 | — |
| CollectorName | varchar | YES | 100 | — |
| NextAvailableTime | datetime | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F495EBC2-57EE-4571-BCA6-E7047E3688F0 | RM Rolling Plan | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-01T12:44:16.0400000 | 2025-07-01T12:44:15.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ProcessCellID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Connection_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.CurrentBatchID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Mst_Tbl.ProcessCellID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
