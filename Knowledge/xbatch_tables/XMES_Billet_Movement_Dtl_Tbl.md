# XStudio_Xbatch.dbo.XMES_Billet_Movement_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, section, bed, charging, zonewise.

**Primary Key:** ID  
**Row Count:** 1,903  

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
| ChargingBedBilletNo | varchar | YES | 36 | — |
| Section1BilletNo | varchar | YES | 36 | — |
| Section2BilletNo | varchar | YES | 36 | — |
| ZonewiseBilletNo | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 014B1704-F960-429A-9EC3-324A2857E3BF | NULL | NULL | NULL | NULL | 2026-07-31T16:46:10.7900000 | NULL | False | False | NULL |
| 0119C37F-7225-410C-A20C-4B379C00D017 | NULL | NULL | NULL | NULL | 2026-08-19T16:24:56.6570000 | NULL | False | False | NULL |
| 010007A2-4491-457C-82AC-C71190E27AF0 | NULL | NULL | NULL | NULL | 2026-08-01T07:55:52.9430000 | NULL | False | False | NULL |
| 00A52246-ADC0-42D8-8B5A-67AA236145C7 | NULL | NULL | NULL | NULL | 2026-08-01T09:03:39.1030000 | NULL | False | False | NULL |
| 009CD9A2-A2C7-4A61-BA6A-AF76C13EF28F | NULL | NULL | NULL | NULL | 2026-08-18T15:28:11.2400000 | NULL | False | False | NULL |
| 00681F71-4CB3-400C-9D50-D3C49415255B | NULL | NULL | NULL | NULL | 2026-07-30T17:17:07.2130000 | NULL | False | False | NULL |
| 00664B51-273A-469A-BFD2-125B54BD46BF | NULL | NULL | NULL | NULL | 2026-07-30T17:18:16.8170000 | NULL | False | False | NULL |
| 0019D02F-3883-4DD6-80B7-A33B7CE77E0E | NULL | NULL | NULL | NULL | 2026-07-30T17:18:59.9300000 | NULL | False | False | NULL |
| 00166803-2B71-4014-A4D0-908BE86F2A49 | NULL | NULL | NULL | NULL | 2026-07-30T17:15:55.1130000 | NULL | False | False | NULL |
| 000CB6D6-182B-4711-A403-0215941A588B | NULL | NULL | NULL | NULL | 2026-08-07T16:22:42.0130000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 014B1704-F960-429A-9EC3-324A2857E3BF | NULL | NULL | NULL | NULL | 2026-07-31T16:46:10.7900000 | NULL | False | False | NULL |
| 0119C37F-7225-410C-A20C-4B379C00D017 | NULL | NULL | NULL | NULL | 2026-08-19T16:24:56.6570000 | NULL | False | False | NULL |
| 010007A2-4491-457C-82AC-C71190E27AF0 | NULL | NULL | NULL | NULL | 2026-08-01T07:55:52.9430000 | NULL | False | False | NULL |
| 00A52246-ADC0-42D8-8B5A-67AA236145C7 | NULL | NULL | NULL | NULL | 2026-08-01T09:03:39.1030000 | NULL | False | False | NULL |
| 009CD9A2-A2C7-4A61-BA6A-AF76C13EF28F | NULL | NULL | NULL | NULL | 2026-08-18T15:28:11.2400000 | NULL | False | False | NULL |
| 00681F71-4CB3-400C-9D50-D3C49415255B | NULL | NULL | NULL | NULL | 2026-07-30T17:17:07.2130000 | NULL | False | False | NULL |
| 00664B51-273A-469A-BFD2-125B54BD46BF | NULL | NULL | NULL | NULL | 2026-07-30T17:18:16.8170000 | NULL | False | False | NULL |
| 0019D02F-3883-4DD6-80B7-A33B7CE77E0E | NULL | NULL | NULL | NULL | 2026-07-30T17:18:59.9300000 | NULL | False | False | NULL |
| 00166803-2B71-4014-A4D0-908BE86F2A49 | NULL | NULL | NULL | NULL | 2026-07-30T17:15:55.1130000 | NULL | False | False | NULL |
| 000CB6D6-182B-4711-A403-0215941A588B | NULL | NULL | NULL | NULL | 2026-08-07T16:22:42.0130000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Billet_Movement_Dtl_Tbl.ChargingBedBilletNo` -> `XStudio_XBatch.XMES_Live_Billet_Charging_Bed.BilletNo` (Many to One)
- `XStudio_XBatch.XMES_Billet_Movement_Dtl_Tbl.Section1BilletNo` -> `XStudio_XBatch.XMES_Live_Charging_SECT1.BilletNo` (Many to One)
- `XStudio_XBatch.XMES_Billet_Movement_Dtl_Tbl.Section2BilletNo` -> `XStudio_XBatch.XMES_Live_Charging_SECT2.BilletNo` (Many to One)
- `XStudio_XBatch.XMES_Billet_Movement_Dtl_Tbl.ZonewiseBilletNo` -> `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.BilletNo` (Many to One)
