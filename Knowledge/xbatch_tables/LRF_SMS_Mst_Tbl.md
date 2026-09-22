# XStudio_Xbatch.dbo.LRF_SMS_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference module, type, area, equipment, template.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-07-22T10:36:31.0000000 to 2025-07-22T10:36:31.0000000  

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
| EquipmentTypeID | varchar | YES | 36 | — |
| TemplateID | varchar | YES | 36 | — |
| AreaID | varchar | YES | 36 | — |
| ModuleID | varchar | YES | 36 | — |
| ModuleType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0A625385-4465-4C71-A91C-88743497DD3A | Ladle_Refining_Furnace | NULL | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2025-07-22T10:36:31.6500000 | 2025-07-22T10:36:31.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_Per_Heat.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_ProcessTime.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_SMS_5.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_SMS_Block.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_SMS_Data.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_SMS_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_SMS_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
