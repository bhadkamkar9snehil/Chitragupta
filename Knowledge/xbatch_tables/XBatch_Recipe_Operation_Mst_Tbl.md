# XStudio_Xbatch.dbo.XBatch_Recipe_Operation_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference material, output, equipment, position, quantity, type.

**Primary Key:** ID  
**Row Count:** 0  

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
| EquipmentTypeID | varchar | NO | 36 | — |
| OutputMaterialID | varchar | NO | 36 | — |
| SrNo | int | YES | 10,0 | — |
| Position | varchar | YES | 100 | — |
| OutputMaterialQuantity | decimal | YES | 18,4 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Recipe_Operation_Mst_Tbl.EquipmentTypeID` -> `XStudio_XBatch.Equipment_Type_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Operation_Mst_Tbl.OutputMaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Operation_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Unit_Procedure_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Phase_Group_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Operation_Mst_Tbl.ID` (Many to One)
