# XStudio_Xbatch.dbo.Transformer_15MVA_Audit

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
| OilLevelTapChanger | decimal | YES | 18,4 | — |
| RatedPrimaryCurrent263AY | decimal | YES | 18,4 | — |
| Attendant | varchar | YES | 36 | — |
| RatedPrimaryCurrentR263A | decimal | YES | 18,4 | — |
| TapChangerCounter | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| Remarks | varchar | YES | -1 | — |
| PrimaryVoltageKV | decimal | YES | 18,4 | — |
| SecondaryVoltageKV | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| SF6Pressure | decimal | YES | 18,4 | — |
| CoolingFansStatus | bit | YES | — | — |
| WTIHV | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| OTI | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |
| BreatherStatusTransformer | bit | YES | — | — |
| BreatherStatusTapChanger | bit | YES | — | — |
| RatedSecondaryCurrent1102AY | decimal | YES | 18,4 | — |
| RatedPrimaryCurrentB263A | decimal | YES | 18,4 | — |
| OilLevelTransformer | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| RatedSecondaryCurrent1102AR | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AB | decimal | YES | 18,4 | — |
| WTILV | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |

---
