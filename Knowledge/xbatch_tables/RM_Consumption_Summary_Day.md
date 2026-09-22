# XStudio_Xbatch.dbo.RM_Consumption_Summary_Day

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ngcons, mtd, ytd.

**Primary Key:** ID  
**Row Count:** 326  
**Date Range (ModifiedOn):** 2026-08-06T12:53:53.0100000 to 2026-09-02T10:00:11.9430000  

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
| ReportDate | date | YES | — | — |
| NGCons | int | YES | 10,0 | — |
| NGCons_MTD | int | YES | 10,0 | — |
| NGCons_YTD | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 02F9CF6D-E5A6-4038-92D3-7A8615FB7F83 | NULL | NULL | 2026-07-18T10:34:29.6670000 | NULL | False | False | NULL | NULL | NULL |
| 07E015BC-A5E9-4F65-B59F-D006C4E89DA4 | NULL | NULL | 2026-07-18T10:33:59.1370000 | NULL | False | False | NULL | NULL | NULL |
| 07345CB1-3E18-49E5-8BA2-9CAC3685FB8D | NULL | NULL | 2026-07-18T10:33:49.5270000 | NULL | False | False | NULL | NULL | NULL |
| 0ADB2413-4E57-4819-B461-820C027A68D0 | NULL | NULL | 2026-07-18T10:33:29.3870000 | NULL | False | False | NULL | NULL | NULL |
| 029B4817-61F5-405B-B507-4011ED2A779E | NULL | NULL | 2026-07-18T10:34:19.3200000 | NULL | False | False | NULL | NULL | NULL |
| 0E22DA97-DA56-4987-9783-C76FCB113DDD | NULL | NULL | 2026-07-30T09:27:14.8370000 | NULL | False | False | NULL | NULL | NULL |
| 13E863A4-96C4-4FD4-A515-3218F7EC7AB3 | NULL | NULL | 2026-07-30T09:27:14.8030000 | NULL | False | False | NULL | NULL | NULL |
| 14A3183E-04F1-4091-AA5E-A86448C6C061 | NULL | NULL | 2026-07-18T10:33:39.6100000 | NULL | False | False | NULL | NULL | NULL |
| 14FAFDCA-1EC5-445A-AD6A-470EBA4BC06C | NULL | NULL | 2026-07-18T10:33:39.2530000 | NULL | False | False | NULL | NULL | NULL |
| 1866D5CE-8BA1-456B-B52D-6505A35C2C26 | NULL | NULL | 2026-07-18T10:34:10.2630000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BA40A43E-5E13-4B36-A881-126272610727 | NULL | NULL | 2026-09-02T01:00:04.9430000 | 2026-09-02T10:00:11.9430000 | False | False | NULL | NULL | NULL |
| EB1EB11E-C183-4396-AB60-062E5728568F | NULL | NULL | 2026-09-01T01:00:07.1500000 | 2026-09-02T00:00:10.3200000 | False | False | NULL | NULL | NULL |
| F0A64438-BA06-4E71-B791-210981D6BFA4 | NULL | NULL | 2026-08-31T01:00:10.1400000 | 2026-09-01T00:00:11.1930000 | False | False | NULL | NULL | NULL |
| EC1EEB32-F984-4D88-BF8F-8DC6C6A4C17A | NULL | NULL | 2026-08-30T01:00:08.1700000 | 2026-08-31T00:00:06.4700000 | False | False | NULL | NULL | NULL |
| 8E0781B3-E878-4E99-AA4A-B1D824752483 | NULL | NULL | 2026-08-29T01:00:07.7270000 | 2026-08-30T00:00:03.4400000 | False | False | NULL | NULL | NULL |
| 97C4668E-F012-46E8-A394-AB4C0E825200 | NULL | NULL | 2026-08-28T01:00:10.2000000 | 2026-08-29T00:00:11.3730000 | False | False | NULL | NULL | NULL |
| 97231920-F01A-4187-B382-8F32680F5A18 | NULL | NULL | 2026-08-27T01:00:10.0000000 | 2026-08-28T00:00:05.2500000 | False | False | NULL | NULL | NULL |
| A0C1FF1C-806B-4C34-A50E-48D47F956E03 | NULL | NULL | 2026-08-26T01:00:11.7130000 | 2026-08-27T00:00:03.0930000 | False | False | NULL | NULL | NULL |
| 1BC4F029-7375-4C95-8C7B-E237B2CF4438 | NULL | NULL | 2026-08-25T01:00:06.9730000 | 2026-08-26T00:00:04.3100000 | False | False | NULL | NULL | NULL |
| E2A1D7E1-11E5-4D3C-87D8-33F02CC54299 | NULL | NULL | 2026-08-24T01:00:10.3500000 | 2026-08-25T00:00:11.2100000 | False | False | NULL | NULL | NULL |

---
