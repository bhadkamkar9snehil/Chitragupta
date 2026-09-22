# XStudio_Xbatch.dbo.RM_Roll_History_Card

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference tonnage, rolled, diameter, roll, barrel, cummulative, discard, drawing, final, hardness, initial, length.

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| RollNumbers | int | YES | 10,0 | — |
| SupplierName | varchar | YES | 100 | — |
| RollDiameter | int | YES | 10,0 | — |
| RollDiameterMax | int | YES | 10,0 | — |
| RollDrawingNo | int | YES | 10,0 | — |
| StandNo | int | YES | 10,0 | — |
| DiscardDiameter | int | YES | 10,0 | — |
| RollMaterial | int | YES | 10,0 | — |
| BarrelHardness | decimal | YES | 18,4 | — |
| BarrelLength | decimal | YES | 18,4 | — |
| SlNo | int | YES | 10,0 | — |
| InitialDiameter | int | YES | 10,0 | — |
| FinalDiameter | int | YES | 10,0 | — |
| TotalTonnage | int | YES | 10,0 | — |
| CummulativeTonnage | int | YES | 10,0 | — |
| Remarks | varchar | YES | 100 | — |
| TonnageRolled1 | decimal | YES | 18,4 | — |
| TonnageRolled2 | decimal | YES | 18,4 | — |
| TonnageRolled3 | decimal | YES | 18,4 | — |
| TonnageRolled4 | decimal | YES | 18,4 | — |
| TonnageRolled5 | decimal | YES | 18,4 | — |
| TonnageRolled6 | decimal | YES | 18,4 | — |
| TonnageRolled7 | decimal | YES | 18,4 | — |
| TonnageRolled8 | decimal | YES | 18,4 | — |
| TonnageRolled9 | decimal | YES | 18,4 | — |
| TonnageRolled10 | decimal | YES | 18,4 | — |
| TonnageRolled11 | decimal | YES | 18,4 | — |
| TonnageRolled12 | decimal | YES | 18,4 | — |
| TonnageRolled13 | decimal | YES | 18,4 | — |

---
