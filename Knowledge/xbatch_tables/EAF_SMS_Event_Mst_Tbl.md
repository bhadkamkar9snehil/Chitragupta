# XStudio_Xbatch.dbo.EAF_SMS_Event_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference active, entity, event, transaction, type.

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2025-07-12T12:48:37.0000000 to 2025-08-05T09:08:21.0000000  

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
| EventType | varchar | YES | 100 | — |
| TransactionEntity | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7DC1FBC3-A188-4A36-8765-FAAAD5856EF7 | SMS Delay Data | 554bd194-561d-4b7c-a4f3-711d5fd0756b | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-01-06T14:05:04.0000000 | NULL | False | False | NULL |
| 6EC7CC36-6204-4E8B-8355-050565857346 | EAF Charge Mix Data | 554bd194-561d-4b7c-a4f3-711d5fd0756b | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2026-01-02T13:59:52.0000000 | NULL | False | False | NULL |
| 53680994-EC89-40F2-AFE0-D35F9EAC3F7D | SMS_Plant_Process_Time | 554bd194-561d-4b7c-a4f3-711d5fd0756b | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2025-07-31T08:08:10.0000000 | NULL | False | False | NULL |
| 0EAF8A4D-326C-479B-B9CB-94145610153E | LadleAddition | 554bd194-561d-4b7c-a4f3-711d5fd0756b | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-09-22T14:50:26.0000000 | NULL | False | False | NULL |
| F4B1E9DB-CA75-4500-8909-F7DCC4C1C262 | HeatIDChange | 554bd194-561d-4b7c-a4f3-711d5fd0756b | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11T11:49:27.0000000 | 2025-07-12T12:48:37.0000000 | False | False | NULL |
| 860B1ADF-F63D-42CF-94C7-F81415E97C2E | EAF_All_Process_Time | 554bd194-561d-4b7c-a4f3-711d5fd0756b | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T15:32:05.0000000 | 2025-08-05T09:08:21.0000000 | False | False | NULL |

---
