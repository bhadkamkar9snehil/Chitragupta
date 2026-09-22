# XStudio_Xbatch.dbo.CCM_Manual_Entry

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference heat, tundish, ash, laddle, liquidus, super, temp, time, turrent, consumption, end, mould.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2025-08-02T10:50:47.0000000 to 2025-11-24T14:32:40.0000000  

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
| Name | varchar | YES | 100 | — |
| LiquidusAsh2 | decimal | YES | 18,4 | — |
| SuperHeatT2 | decimal | YES | 18,4 | — |
| LiquidusAsh1 | decimal | YES | 18,4 | — |
| LaddleOnTurrentEndTime | datetime | YES | — | — |
| SuperHeatT3 | decimal | YES | 18,4 | — |
| TundishTemp2 | decimal | YES | 18,4 | — |
| LaddleOnTurretTime | int | YES | 10,0 | — |
| LiquidusAsh3 | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| TundishTemp3 | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| HeatNo | int | YES | 10,0 | — |
| SuperHeatT1 | decimal | YES | 18,4 | — |
| TundishNumber | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| LaddleOnTurrentStartTime | datetime | YES | — | — |
| TundishTemp1 | decimal | YES | 18,4 | — |
| MouldOilConsumption | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF538883-9CAE-4DBA-91C5-FD604E392E46 | NULL | NULL | 2025-07-24T17:23:45.6900000 | NULL | False | False | NULL | NULL |  |
| DABF7B55-1CD3-4548-8AA9-3FFFFADC170F | NULL | NULL | 2025-07-24T17:23:45.6900000 | NULL | False | False | NULL | NULL |  |
| D93D05F2-DB93-4825-8E9D-D1555AB9FD1A | NULL | NULL | 2025-07-24T17:23:45.6900000 | NULL | False | False | NULL | NULL |  |
| 5C44B489-2C1D-4195-9918-1A82CEBB21F4 | NULL | NULL | 2025-07-24T17:23:45.6900000 | NULL | False | False | NULL | NULL |  |
| 4A1FADCC-69CA-4CF4-952E-92D1E208076D | NULL | NULL | 2025-07-24T17:23:45.6900000 | NULL | False | False | NULL | NULL |  |
| 27C186DA-DE31-4130-A669-4A32A9967C13 | NULL | NULL | 2025-07-24T17:23:45.6900000 | NULL | False | False | NULL | NULL |  |
| B1166413-C32A-43BC-B27D-0E8125831B24 | NULL | NULL | 2025-07-24T17:23:45.6900000 | NULL | False | False | NULL | NULL |  |
| 6AA65B45-B66C-4B17-A809-7AD8C64D34CE | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T17:23:45.6900000 | 2025-08-02T10:50:47.0000000 | False | False | NULL |  |  |
| AE965B69-1B76-49FF-BD9E-A79DA9DBFC94 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-24T14:16:01.6470000 | 2025-11-24T14:16:56.0000000 | False | False | NULL | 10.76.15.11 |  |
| C9782610-D8F4-4702-8264-0262A7D04F63 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-24T14:31:17.8800000 | 2025-11-24T14:32:40.0000000 | False | False | NULL | 10.76.15.11 |  |

---
