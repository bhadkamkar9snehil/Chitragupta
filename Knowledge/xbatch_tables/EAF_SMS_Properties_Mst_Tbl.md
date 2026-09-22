# XStudio_Xbatch.dbo.EAF_SMS_Properties_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference level, type, field, name, tag, weight, conversion, fix, having, look, multiplier, offset.

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
| StorageType | varchar | YES | 100 | — |
| IsHavingWeighingScale | bit | YES | — | — |
| WeighmentType | varchar | YES | 100 | — |
| FixWeightTag | varchar | YES | 100 | — |
| LevelTag | varchar | YES | 100 | — |
| LevelConversionType | varchar | YES | 100 | — |
| Multiplier | decimal | YES | 18,4 | — |
| Offset | decimal | YES | 18,4 | — |
| LevelLookUpTable | varchar | YES | 100 | — |
| LevelFieldName | varchar | YES | 100 | — |
| WeightFieldName | varchar | YES | 100 | — |

---
