# XStudio_Xbatch.dbo.XBatch_Recipe_Phase_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference capability, material, position, quantity, template, type.

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
| Type | varchar | NO | 100 | — |
| TemplateID | varchar | YES | 36 | — |
| CapabilityID | varchar | YES | 36 | — |
| MaterialID | varchar | YES | 36 | — |
| Quantity | decimal | YES | 18,4 | — |
| SrNo | int | NO | 10,0 | — |
| Position | varchar | YES | -1 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Recipe_Phase_Mst_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Phase_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Phase_Group_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Phase_Parameter_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Phase_Mst_Tbl.ID` (Many to One)
