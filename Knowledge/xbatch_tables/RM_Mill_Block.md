# XStudio_Xbatch.dbo.RM_Mill_Block

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference avg, current, max, min, speed, torque, time, billet, end, equipment, start.

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
| EquipmentID | varchar | YES | 36 | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| MaxTorque | decimal | YES | 18,4 | — |
| MinTorque | decimal | YES | 18,4 | — |
| AvgTorque | decimal | YES | 18,4 | — |
| AvgCurrent | decimal | YES | 18,4 | — |
| MinCurrent | decimal | YES | 18,4 | — |
| MaxCurrent | decimal | YES | 18,4 | — |
| AvgSpeed | decimal | YES | 18,4 | — |
| MinSpeed | decimal | YES | 18,4 | — |
| MaxSpeed | decimal | YES | 18,4 | — |
| BilletNo | varchar | YES | 100 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Mill_Block.EquipmentID` -> `XStudio_XBatch.RM_Mill_Mst_Tbl.ID` (Many to One)
