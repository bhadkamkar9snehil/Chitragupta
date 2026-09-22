# XStudio_Xbatch.dbo.XMES_SAP_API_UsageDecision_Error

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference message, body, error, heat, inspection, lot, record, status, success, transaction.

**Primary Key:** ID  
**Row Count:** 335  
**Date Range (ModifiedOn):** 2026-02-20T12:53:33.6300000 to 2026-07-05T12:30:59.2730000  

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
| Status | varchar | YES | 50 | — |
| EntryDateTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| ReportDate | date | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| InspectionLot | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
| Body | varchar | YES | -1 | — |
| Name | varchar | YES | 100 | — |
| ErrorMessage | varchar | YES | -1 | — |
| TransactionID | varchar | YES | 100 | — |
| SuccessMessage | varchar | YES | -1 | — |
| RecordID | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BDD66D58-F582-4F29-9718-3DCD0B93F3C1 | NULL | NULL | 2026-02-20T11:11:18.8400000 | 2026-02-20T12:53:33.6300000 | False | False | NULL | NULL | NULL |
| 2560E77E-7788-42F7-A7EB-2A0105017182 | NULL | NULL | 2026-02-20T12:45:57.7930000 | 2026-02-20T13:08:15.8370000 | False | False | NULL | NULL | NULL |
| 0BC81B3D-7B83-4705-B610-E74F29DE3BA2 | NULL | NULL | 2026-02-20T12:46:00.2870000 | 2026-02-20T13:08:15.8530000 | False | False | NULL | NULL | NULL |
| FA485E5C-094E-46E9-BC57-832C4BD8DA01 | NULL | NULL | 2026-02-20T12:45:04.9430000 | 2026-02-20T13:08:15.8630000 | False | False | NULL | NULL | NULL |
| A9799031-1973-41F7-8431-9F7E4748614A | NULL | NULL | 2026-02-20T12:44:57.8100000 | 2026-02-20T13:08:15.8670000 | False | False | NULL | NULL | NULL |
| 7C6759F7-6EB2-4A6C-9632-507433C0FB18 | NULL | NULL | 2026-02-20T11:09:42.0600000 | 2026-02-20T13:08:15.8700000 | False | False | NULL | NULL | NULL |
| 377A5886-BB0D-426B-9680-2204430E6509 | NULL | NULL | 2026-02-20T02:43:35.3630000 | 2026-02-20T13:08:15.8770000 | False | False | NULL | NULL | NULL |
| 87F41D95-53E9-42F6-ADAC-D8B21B4D7000 | NULL | NULL | 2026-02-20T11:09:19.2270000 | 2026-02-20T13:08:15.8770000 | False | False | NULL | NULL | NULL |
| 81194665-0A5D-4193-B3DC-8440E29A77D4 | NULL | NULL | 2026-02-20T02:42:36.0870000 | 2026-02-20T13:08:15.8800000 | False | False | NULL | NULL | NULL |
| 914AFA8A-0547-4216-AF64-F0BF2B6902ED | NULL | NULL | 2026-02-20T02:42:18.7900000 | 2026-02-20T13:08:15.8800000 | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52D9729C-6481-4424-8361-11EC9FDF6A2B | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-05T12:30:40.2470000 | 2026-07-05T12:30:59.2730000 | False | False | NULL | NULL | NULL |
| 87C0C821-85BC-4771-9273-2614612668FF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-06-25T22:49:33.4770000 | 2026-06-25T22:49:55.1030000 | False | False | NULL | NULL | NULL |
| C0EF887A-D809-4C96-8460-8E4DB7A3F5A1 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-31T15:11:09.2230000 | 2026-05-31T15:11:29.5800000 | False | False | NULL | NULL | NULL |
| 7C2CEDC1-6B4F-46A6-B88C-2A00F71EF643 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-25T23:50:26.9230000 | 2026-05-25T23:50:49.5330000 | False | False | NULL | NULL | NULL |
| D1FC6136-72BC-4531-B54B-48BAD2F6BDF1 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-21T01:57:04.6300000 | 2026-05-21T01:57:28.5730000 | False | False | NULL | NULL | NULL |
| 450AE8EE-E87E-429E-A90C-235F2993C9E4 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-18T15:52:20.0070000 | 2026-05-18T15:52:42.3870000 | False | False | NULL | NULL | NULL |
| C992637C-A691-47A9-9847-F307430ADD5F | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-18T12:42:47.4000000 | 2026-05-18T12:43:06.1230000 | False | False | NULL | NULL | NULL |
| C00E6F9D-42CC-4E99-9E92-FA9EF672FD78 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-17T05:56:21.4130000 | 2026-05-18T00:04:37.2330000 | False | False | NULL | NULL | NULL |
| 759719BC-D110-4607-B21A-5F2BA19C4954 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-17T05:56:21.4130000 | 2026-05-17T05:56:43.5000000 | False | False | NULL | NULL | NULL |
| 7DCD6536-91EF-4A19-9546-A16D9E59D6A2 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-15T00:16:15.2100000 | 2026-05-15T00:16:37.2770000 | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_UsageDecision_Trn_Tbl.SAPTransactionID` -> `XStudio_XBatch.XMES_SAP_API_UsageDecision_Error.TransactionID` (One to One)
