# XStudio_Xbatch.dbo.RM_Mill_Pass_Card

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference roll, bottom, diameter, name, number, rolling, section, top, casset, date, expected, groove.

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
| StandNo | int | YES | 10,0 | — |
| Section | varchar | YES | 100 | — |
| RollNumberTop | int | YES | 10,0 | — |
| RollNumberBottom | int | YES | 10,0 | — |
| RollDiameterTop | int | YES | 10,0 | — |
| RollDiameterBottom | int | YES | 10,0 | — |
| Hardness | decimal | YES | 18,4 | — |
| PassNo | int | YES | 10,0 | — |
| NameOfGroove | varchar | YES | 100 | — |
| ExpectedTonnage | int | YES | 10,0 | — |
| SectionName | varchar | YES | 100 | — |
| DateOfRolling | datetime | YES | — | — |
| RollingSize | decimal | YES | 18,4 | — |
| CassetNo | int | YES | 10,0 | — |

---
