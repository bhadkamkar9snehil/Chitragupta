# XStudio_Xbatch.dbo.Rate_Band_Master

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference code, color.

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2026-03-26T16:31:06.0970000 to 2026-03-26T16:33:15.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
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
| ColorCode | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8AEF574C-DD76-4B6E-A72C-8A35A2D0F1CF | Off-Peak Afternoon | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:11:13.1200000 | 2026-03-26T16:31:06.0970000 | True | False | NULL | 100.110.190.241 |
| 5F71AB44-4CE7-405D-8E8A-6FB12DFAD64D | Off-Peak | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:10:33.2770000 | 2026-03-26T16:31:17.0000000 | False | False | NULL | 100.110.190.241 |
| 5A338799-005E-43EE-9090-D2DCD6BB396C | Night-Peak | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:10:10.5870000 | 2026-03-26T16:32:18.0000000 | False | False | NULL | 100.110.190.241 |
| FBDB9CC0-DD90-4716-9A87-54A1C77A487A | Weekday Day-Peak | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:10:45.5170000 | 2026-03-26T16:32:38.0000000 | False | False | NULL | 100.110.190.241 |
| 6C194936-053D-4E13-9FCB-CC7E0D0009B9 | Night-Peak Weekend | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:10:21.5930000 | 2026-03-26T16:32:55.5970000 | True | False | NULL | 100.110.190.241 |
| 6098FE7F-B5DE-43C1-919C-AF5FB0CE10D9 | Weekend Day-Peak | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-10T14:10:54.5400000 | 2026-03-26T16:33:15.0000000 | False | False | NULL | 100.110.190.241 |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Electricity_Meter_Electricity_Bill_Details.TimeOfUse` -> `XStudio_XBatch.Rate_Band_Master.Name` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Timing.RateBand` -> `XStudio_XBatch.Rate_Band_Master.ID` (Many to One)
