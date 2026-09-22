# XStudio_Xbatch.dbo.LRF_Ladle_No_Per_Heat

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ladle, active, count, heat, life.

**Primary Key:** ID  
**Row Count:** 23  
**Date Range (ModifiedOn):** 2025-07-31T16:52:03.0000000 to 2025-07-31T16:52:03.0000000  

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
| HeatID | int | YES | 10,0 | — |
| IsProcessed | bit | YES | — | — |
| ReportDate | date | YES | — | — |
| ActiveLadle | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |
| LadleLifeCount | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8A15CFB3-B33D-4386-9B9C-A18ECC4FD80E | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 86CF8458-5B47-4D79-8FEF-B50B2528AA00 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 84E16144-2E7E-473D-B54B-B701B21F1D91 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 7D4237ED-BE78-4C4D-A9EC-A87552E230BC | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 795D7657-CA7C-48E6-AE94-0829EEA5EB41 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 65A8635C-7988-4ADC-8E5A-A1042D8F46F2 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 6455B3D5-C9CB-4454-96A2-77B7C18BE1E6 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 6209CDAC-6013-4086-AEC1-8C6228999141 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 5537A542-27C2-4A46-A5E9-0A4B62261930 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 2B17EC53-68ED-4062-9592-1CC6520F2893 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9C1B4A27-ABF9-4273-AACA-14E71D834230 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2025-07-31T16:52:03.6130000 | 2025-07-31T16:52:03.0000000 | False | False | NULL | 172.16.4.25 |  |
| 8A15CFB3-B33D-4386-9B9C-A18ECC4FD80E | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 86CF8458-5B47-4D79-8FEF-B50B2528AA00 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 84E16144-2E7E-473D-B54B-B701B21F1D91 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 7D4237ED-BE78-4C4D-A9EC-A87552E230BC | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 795D7657-CA7C-48E6-AE94-0829EEA5EB41 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 65A8635C-7988-4ADC-8E5A-A1042D8F46F2 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 6455B3D5-C9CB-4454-96A2-77B7C18BE1E6 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 6209CDAC-6013-4086-AEC1-8C6228999141 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |
| 5537A542-27C2-4A46-A5E9-0A4B62261930 | NULL | NULL | 2025-07-24T14:17:15.1100000 | NULL | False | False | NULL | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_Ladle_No_Per_Heat.ActiveLadle` -> `XStudio_XBatch.LRF_Ladle_Number_Master.ID` (Many to One)
