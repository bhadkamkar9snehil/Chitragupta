# XStudio_Xbatch.dbo.RM_WRM_Event_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference attribute, channel, collector, equipment, name, tag.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2026-07-03T09:11:27.8100000 to 2026-07-30T17:08:07.2230000  

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
| Attribute | varchar | YES | 100 | — |
| TagName | varchar | YES | 100 | — |
| CollectorID | varchar | YES | 36 | — |
| ChannelID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 77CF939A-820E-48D5-840A-5FDBAF93D2D9 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-07-03T09:09:44.5570000 | 2026-07-03T09:11:27.8100000 | False | False | NULL |
| 53AA8E13-08CC-4083-80C2-DCDD279D4D7F | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | NULL | NULL | 2026-07-06T08:04:02.3270000 | 2026-07-06T08:05:16.0300000 | True | False | NULL |
| 93A818B5-B7E4-4800-ACD5-CBA0485AD6AE | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-07-06T08:06:07.3030000 | 2026-07-06T08:06:27.6900000 | False | False | NULL |
| 162D5055-11DB-4B26-8BEC-45627BF0D5E4 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-03T09:14:32.0130000 | 2026-07-30T17:08:07.2230000 | False | False | NULL |

---
