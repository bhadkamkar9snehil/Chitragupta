# XStudio_Xbatch.dbo.RM_Reheating_Furnace_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference module, type, area, equipment, template.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-09-03T15:11:36.0000000 to 2025-09-03T15:11:36.0000000  

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
| 0728EBC6-7855-4EFE-ACBE-8D986A0DB1C7 | Furnace | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-03T15:11:36.8700000 | 2025-09-03T15:11:36.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Billet_Weight_Block.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Furnace_Logbook_Block.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_NGConsumption_Report.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Reheating_Furnace_Block.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Reheating_Furnace_Data.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Reheating_Furnace_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
