# XStudio_Xbatch.dbo.XBatch_Batch_BOM_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference quantity, phase, actual, deviation, group, item, operation, procedure, source, type, unit, uomid.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| ItemID | varchar | NO | 36 | — |
| Quantity | decimal | NO | 18,4 | — |
| UOMID | varchar | NO | 36 | — |
| UnitProcedureID | varchar | NO | 36 | — |
| OperationID | varchar | NO | 36 | — |
| PhaseGroupID | varchar | YES | 36 | — |
| PhaseID | varchar | YES | 36 | — |
| ActualQuantity | decimal | YES | 18,4 | — |
| QuantityDeviation | decimal | YES | 18,4 | — |
| SourceType | varchar | YES | 100 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ItemID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.OperationID` -> `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.PhaseGroupID` -> `XStudio_XBatch.XBatch_Batch_Phase_Group_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.PhaseID` -> `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.UnitProcedureID` -> `XStudio_XBatch.XBatch_Batch_Unit_Procedure_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ID` (Many to One)
