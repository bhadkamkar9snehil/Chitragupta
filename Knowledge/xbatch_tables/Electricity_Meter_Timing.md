# XStudio_Xbatch.dbo.Electricity_Meter_Timing

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, band, code, color, day, from, rate, week, weekdays, year.

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2026-03-26T16:45:12.7230000 to 2026-03-26T16:49:07.0000000  

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
| RateBand | varchar | YES | 36 | — |
| FromTime | time | YES | — | — |
| ToTime | time | YES | — | — |
| DayOfWeek | varchar | YES | 100 | — |
| SrNo | int | YES | 10,0 | — |
| Year | varchar | YES | -1 | — |
| EntryDatetime | datetime | YES | — | — |
| Weekdays | varchar | YES | 100 | — |
| ColorCode | varchar | YES | 50 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18397E56-74C9-4CA1-BCB0-F69F4D5DCAE6 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-01T10:49:21.6670000 | 2026-03-26T16:45:12.7230000 | True | False | NULL | 100.110.190.241 |  |
| 36728152-7487-417C-930D-9AD9756DEBF0 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-01T10:50:26.4230000 | 2026-03-26T16:45:19.9630000 | True | False | NULL | 100.110.190.241 |  |
| 4B54BC17-A3D0-44D6-BF90-0C0CB81974DB | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-01T10:52:09.0400000 | 2026-03-26T16:45:24.2400000 | True | False | NULL | 100.110.190.241 |  |
| 1DBF7E13-BBEC-45AA-85C4-82404E2EF8D1 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-01T10:54:56.0670000 | 2026-03-26T16:46:42.0000000 | False | False | NULL | 100.110.190.241 |  |
| 1D3B2F38-AA70-472B-9316-6053AE149635 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:28:22.2370000 | 2026-03-26T16:47:12.0000000 | False | False | NULL | 100.110.190.241 | NULL |
| 68CB49DC-86F2-40BF-B01B-B484AE8F125A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-01T10:48:00.6870000 | 2026-03-26T16:47:42.0000000 | False | False | NULL | 100.110.190.241 |  |
| F8D0AE88-2419-4C5D-944C-8C384058A6E1 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:26:56.7000000 | 2026-03-26T16:48:34.0000000 | False | False | NULL | 100.110.190.241 | NULL |
| 2630486B-4226-4F23-983F-A86674FDF550 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:27:46.0170000 | 2026-03-26T16:49:07.0000000 | False | False | NULL | 100.110.190.241 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Electricity_Meter_Timing.RateBand` -> `XStudio_XBatch.Rate_Band_Master.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Timing.Year` -> `XStudio_XBatch.Year_Master.Name` (Many to One)
