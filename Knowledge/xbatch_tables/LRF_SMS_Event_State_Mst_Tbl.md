# XStudio_Xbatch.dbo.LRF_SMS_Event_State_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference state, flow, off, work, condition, delay, active, attribute, different, enable, error, name.

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2025-07-22T13:09:17.0000000 to 2025-09-09T11:36:57.0000000  

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
| StateName | varchar | YES | 100 | — |
| StateSequence | int | YES | 10,0 | — |
| StateCondition | varchar | YES | -1 | — |
| IsErrorState | bit | YES | — | — |
| StateOnWorkFlow | varchar | YES | 100 | — |
| StateOffWorkFlow | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |
| WorkFlowAttribute | varchar | YES | 100 | — |
| IsWorkFlowEnable | bit | YES | — | — |
| StateOnDelay | int | YES | 10,0 | — |
| StateOffDelay | int | YES | 10,0 | — |
| IsDifferentOffCondition | bit | YES | — | — |
| StateOffCondition | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9587B66B-79F0-48C2-912A-D0DF1C1A2289 | NULL | 3A4A0C4A-249A-4772-A956-38A6FC8699DF | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-24T10:16:04.0000000 | 2025-07-22T13:09:17.0000000 | False | False | NULL |
| 16A442A1-9A6C-4E28-ABEC-CDAFA0AE41DF | NULL | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-08T17:18:27.0000000 | 2025-08-19T12:49:05.0000000 | False | False | NULL |
| B372CF79-07A6-46AC-9B25-51B2058BFA66 | NULL | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-09T14:05:55.0000000 | 2025-08-19T12:57:46.0000000 | False | False | NULL |
| 5AF76A08-D39E-4018-9148-9A4FD5EFEFD3 | NULL | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-08T17:21:56.0000000 | 2025-08-19T13:06:31.0000000 | False | False | NULL |
| 311275C8-B592-496E-BE41-AAA60F7E88C0 | NULL | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-08T17:24:09.0000000 | 2025-08-19T13:08:45.0000000 | False | False | NULL |
| E2618875-C022-4F31-8D27-B25DD9F808CF | NULL | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-08T21:46:53.0000000 | 2025-09-08T17:26:06.0000000 | False | False | NULL |
| 680611AF-A542-4757-97F3-2E49C9E2ACEC | NULL | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-08T21:45:48.0000000 | 2025-09-08T17:30:50.0000000 | False | False | NULL |
| D76FE321-F394-477A-8953-1BEF5B24A363 | NULL | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-13T09:32:49.0000000 | 2025-09-09T11:36:57.0000000 | False | False | NULL |

---
