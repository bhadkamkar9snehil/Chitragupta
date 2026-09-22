# XStudio_Xbatch.dbo.Procedure_Task_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference page, entity, equipment, isscanable, view.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
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
| EntityID | varchar | YES | 36 | — |
| EquipmentID | varchar | YES | 36 | — |
| PageID | varchar | YES | 36 | — |
| ViewPageID | varchar | YES | 36 | — |
| Isscanable | bit | YES | — | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Procedure_Task_Mst_Tbl.EntityID` -> `XStudio_Configuration_XBatch.XStudio_Entities_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Procedure_Task_Mst_Tbl.PageID` -> `XStudio_Configuration_XBatch.XStudio_Page_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Procedure_Task_Mst_Tbl.ViewPageID` -> `XStudio_Configuration_XBatch.XStudio_Page_Mst_Tbl.ID` (Many to One)
