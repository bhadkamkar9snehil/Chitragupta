# XStudio_Xbatch.dbo.SMS_Temperature_Per_Heat

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temp, area, datetime, degc, heat, sequence.

**Primary Key:** ID  
**Row Count:** 8,173  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| HeatID | varchar | YES | 100 | — |
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
| TempDatetime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TempDegc | decimal | YES | 18,4 | — |
| Area | varchar | YES | 100 | — |
| TempSequence | varchar | YES | 100 | — |

### Top 10 Records

| ID | HeatID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 006FC794-E1AA-4450-817E-A7866F6BB0CF | 1603893 | NULL | NULL | 2026-07-03T03:08:19.9830000 | NULL | False | False | NULL | NULL |
| 006E42CB-67F1-43DA-9A77-8BE8A15D827D | 1603532 | NULL | NULL | 2026-06-25T09:24:43.0030000 | NULL | False | False | NULL | NULL |
| 0063CF5A-2A13-4502-A62C-0C2214997111 | 1603825 | NULL | NULL | 2026-06-29T16:56:56.5570000 | NULL | False | False | NULL | NULL |
| 00603972-73F1-418C-8903-3DC83D596BD9 | 1603425 | NULL | NULL | 2026-06-25T09:25:00.5400000 | NULL | False | False | NULL | NULL |
| 004C751A-5E6C-401C-ACB4-F51A1F2779A2 | 1603709 | NULL | NULL | 2026-06-25T09:25:28.5370000 | NULL | False | False | NULL | NULL |
| 003CF063-D3FF-453C-A934-3811EE82AA19 | 1603807 | NULL | NULL | 2026-06-28T21:15:52.6130000 | NULL | False | False | NULL | NULL |
| 00321E80-AFFC-4AD5-A0ED-5C893D7FFE22 | 1603533 | NULL | NULL | 2026-06-25T09:24:43.0400000 | NULL | False | False | NULL | NULL |
| 0031C7A4-C90B-4515-BF07-911FE924059A | 1603312 | NULL | NULL | 2026-06-25T09:24:11.9430000 | NULL | False | False | NULL | NULL |
| 001F5FED-E681-4F36-BC57-F1B0F86B7079 | 1603536 | NULL | NULL | 2026-06-25T09:24:23.4700000 | NULL | False | False | NULL | NULL |
| 00114026-C83D-43A7-84B3-7F1204428058 | 1603538 | NULL | NULL | 2026-06-25T09:24:43.2300000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | HeatID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 006FC794-E1AA-4450-817E-A7866F6BB0CF | 1603893 | NULL | NULL | 2026-07-03T03:08:19.9830000 | NULL | False | False | NULL | NULL |
| 006E42CB-67F1-43DA-9A77-8BE8A15D827D | 1603532 | NULL | NULL | 2026-06-25T09:24:43.0030000 | NULL | False | False | NULL | NULL |
| 0063CF5A-2A13-4502-A62C-0C2214997111 | 1603825 | NULL | NULL | 2026-06-29T16:56:56.5570000 | NULL | False | False | NULL | NULL |
| 00603972-73F1-418C-8903-3DC83D596BD9 | 1603425 | NULL | NULL | 2026-06-25T09:25:00.5400000 | NULL | False | False | NULL | NULL |
| 004C751A-5E6C-401C-ACB4-F51A1F2779A2 | 1603709 | NULL | NULL | 2026-06-25T09:25:28.5370000 | NULL | False | False | NULL | NULL |
| 003CF063-D3FF-453C-A934-3811EE82AA19 | 1603807 | NULL | NULL | 2026-06-28T21:15:52.6130000 | NULL | False | False | NULL | NULL |
| 00321E80-AFFC-4AD5-A0ED-5C893D7FFE22 | 1603533 | NULL | NULL | 2026-06-25T09:24:43.0400000 | NULL | False | False | NULL | NULL |
| 0031C7A4-C90B-4515-BF07-911FE924059A | 1603312 | NULL | NULL | 2026-06-25T09:24:11.9430000 | NULL | False | False | NULL | NULL |
| 001F5FED-E681-4F36-BC57-F1B0F86B7079 | 1603536 | NULL | NULL | 2026-06-25T09:24:23.4700000 | NULL | False | False | NULL | NULL |
| 00114026-C83D-43A7-84B3-7F1204428058 | 1603538 | NULL | NULL | 2026-06-25T09:24:43.2300000 | NULL | False | False | NULL | NULL |

---
