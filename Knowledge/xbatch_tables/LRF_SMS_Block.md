# XStudio_Xbatch.dbo.LRF_SMS_Block

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, lime, power, arcing, argon, consumption, dolo, end, energy, equipment, flow, kwh.

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
| Lime | decimal | YES | 18,4 | — |
| SiMnn | decimal | YES | 18,4 | — |
| SiMn | decimal | YES | 18,4 | — |
| FeSi | decimal | YES | 18,4 | — |
| Dolo | decimal | YES | 18,4 | — |
| Lime1 | decimal | YES | 18,4 | — |
| ArcingTime | decimal | YES | 18,4 | — |
| LRFActualEnergy | decimal | YES | 18,4 | — |
| PowerOnTime | decimal | YES | 18,4 | — |
| PowerOffTime | decimal | YES | 18,4 | — |
| KWhPerTon | decimal | YES | 18,4 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| ArgonConsumption | decimal | YES | 18,4 | — |
| PurgingFlowLPM | decimal | YES | 18,4 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_SMS_Block.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
