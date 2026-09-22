# XStudio_Xbatch.dbo.Transformer_63MVA_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference current, rated, primary, secondary, changer, status, tap, breather, level, oil, transformer, voltage.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
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
| PrimaryVoltageKV | decimal | YES | 18,4 | — |
| SecondaryVoltageKV | decimal | YES | 18,4 | — |
| RatedPrimaryCurrentR276A | decimal | YES | 18,4 | — |
| RatedPrimaryCurrent276AY | decimal | YES | 18,4 | — |
| RatedPrimaryCurrentB276A | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AR | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AY | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AB | decimal | YES | 18,4 | — |
| TapChangerCounter | decimal | YES | 18,4 | — |
| OTI | decimal | YES | 18,4 | — |
| WTIHV | decimal | YES | 18,4 | — |
| SF6Pressure | decimal | YES | 18,4 | — |
| OilLevelTransformer | decimal | YES | 18,4 | — |
| OilLevelTapChanger | decimal | YES | 18,4 | — |
| BreatherStatusTransformer | bit | YES | — | — |
| BreatherStatusTapChanger | bit | YES | — | — |
| CoolingFansStatus | bit | YES | — | — |
| Remarks | varchar | YES | -1 | — |
| Attendant | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |
| WTILV | decimal | YES | 18,4 | — |

---
