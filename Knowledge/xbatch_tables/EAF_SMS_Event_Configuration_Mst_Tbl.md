# XStudio_Xbatch.dbo.EAF_SMS_Event_Configuration_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference event, active, entity, mst, transaction, type.

**Primary Key:** ID  
**Row Count:** 6  

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
| EventMstID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F61D0167-9E6A-412E-85B2-F19BCA123C80 | SMS Delay Data | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2026-01-06T14:05:04.2230000 | NULL | False | False | NULL |
| BAFC3EE8-1CE6-430E-A36F-3776F79AD872 | SMS_Plant_Process_Time | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-31T08:08:11.0200000 | NULL | False | False | NULL |
| 6114AAFB-1F35-4B26-AA15-76A4D15DDF28 | EAF_All_Process_Time | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-21T15:32:05.1800000 | NULL | False | False | NULL |
| 51189FC3-66F2-4026-8237-5AC53F236E28 | LadleAddition | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-09-22T14:50:26.6870000 | NULL | False | False | NULL |
| 3EA30491-0AB9-4B16-9EDF-AC1FB8207658 | EAF Charge Mix Data | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2026-01-02T13:59:52.2570000 | NULL | False | False | NULL |
| 12B718AF-4097-44C1-8113-07D16D082A69 | HeatIDChange | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-11T11:49:27.7870000 | NULL | False | False | NULL |

---
