# XStudio_Xbatch.dbo.XBatch_Unit_Equipment_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference current, equipment, batch, enabled, operation, procedure, status, template, type, unit.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
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
| EquipmentTypeID | varchar | NO | 36 | — |
| TemplateID | varchar | YES | 36 | — |
| EquipmentID | varchar | NO | 36 | — |
| IsEnabled | bit | YES | — | — |
| Status | varchar | YES | 100 | — |
| CurrentBatchID | varchar | YES | 36 | — |
| CurrentUnitProcedureID | varchar | YES | 36 | — |
| CurrentOperationID | varchar | YES | 36 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.CurrentBatchID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.CurrentOperationID` -> `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.CurrentUnitProcedureID` -> `XStudio_XBatch.XBatch_Batch_Unit_Procedure_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.EquipmentTypeID` -> `XStudio_XBatch.Equipment_Type_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Unit_Mst_Tbl.ID` (Many to One)
