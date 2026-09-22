# XStudio_Xbatch.dbo.XMES_Billet_Strand_tracking

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference stand, status, datetime, htsample, sample, sampling, ttsample, billet, cobble, end, product.

**Primary Key:** ID  
**Row Count:** 1,415  
**Date Range (ModifiedOn):** 2026-08-07T09:07:45.2570000 to 2026-08-26T15:56:56.3830000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| S1IT | datetime | YES | — | — |
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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| S1OT | datetime | YES | — | — |
| S2OT | datetime | YES | — | — |
| S3OT | datetime | YES | — | — |
| S4OT | datetime | YES | — | — |
| S5OT | date | YES | — | — |
| S6OT | datetime | YES | — | — |
| S7OT | datetime | YES | — | — |
| S8OT | datetime | YES | — | — |
| S9OT | datetime | YES | — | — |
| S10OT | datetime | YES | — | — |
| S11OT | datetime | YES | — | — |
| S12OT | datetime | YES | — | — |
| S13OT | datetime | YES | — | — |
| S14OT | datetime | YES | — | — |
| S15OT | datetime | YES | — | — |
| S16OT | datetime | YES | — | — |
| S2IT | datetime | YES | — | — |
| S3IT | datetime | YES | — | — |
| S4IT | datetime | YES | — | — |
| S5IT | datetime | YES | — | — |
| S6IT | datetime | YES | — | — |
| S7IT | datetime | YES | — | — |
| S8IT | datetime | YES | — | — |
| S9IT | datetime | YES | — | — |
| S10IT | datetime | YES | — | — |
| S11IT | datetime | YES | — | — |
| S12IT | datetime | YES | — | — |
| S13IT | datetime | YES | — | — |
| S14IT | datetime | YES | — | — |
| S15IT | datetime | YES | — | — |
| S16IT | datetime | YES | — | — |
| BIlletNo | varchar | YES | 100 | — |
| Status | varchar | YES | 50 | — |
| S17IT | datetime | YES | — | — |
| S18IT | datetime | YES | — | — |
| S17OT | datetime | YES | — | — |
| S18OT | datetime | YES | — | — |
| S0OT | datetime | YES | — | — |
| Cobble | varchar | YES | 100 | — |
| Stand8HTSample | decimal | YES | 18,4 | — |
| Stand8TTSample | decimal | YES | 18,4 | — |
| Stand14HTSample | decimal | YES | 18,4 | — |
| Stand14TTSample | decimal | YES | 18,4 | — |
| Stand8SamplingDatetime | datetime | YES | — | — |
| Stand14SamplingDatetime | datetime | YES | — | — |
| Sample8Status | varchar | YES | 100 | — |
| Sample14Status | varchar | YES | 100 | — |
| Stand | int | YES | 10,0 | — |
| EndProduct | varchar | YES | 36 | — |

### Top 10 Records

| ID | S1IT | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00576607-F5F9-42A4-8F4E-9810D1D774E2 | 2026-08-01T09:29:46.5400000 | 8953C204-7F5D-4E1F-A1C4-956A91873A39 | NULL | NULL | 2026-08-01T09:29:21.4030000 | NULL | False | False | NULL |
| 0051CC6F-81DD-4A16-82AC-9462FD547ABA | 2026-07-31T09:30:47.4070000 | B4FDD4F2-E252-4D4F-82EF-7EF7E96C8F7A | NULL | NULL | 2026-07-31T09:30:21.7230000 | NULL | False | False | NULL |
| 004C5C33-F64F-443C-B663-EB6D4B6E2939 | 2026-08-03T10:08:10.8000000 | NULL | NULL | NULL | 2026-08-03T10:07:45.3470000 | NULL | False | False | NULL |
| 004565AA-230D-43DA-8B97-BBECE345044A | 2026-07-31T12:31:16.1670000 | B4FDD4F2-E252-4D4F-82EF-7EF7E96C8F7A | NULL | NULL | 2026-07-31T12:30:51.6530000 | NULL | False | False | NULL |
| 0015106B-344B-448F-812D-C0A574625210 | 2026-08-01T14:24:28.3000000 | 8953C204-7F5D-4E1F-A1C4-956A91873A39 | NULL | NULL | 2026-08-01T14:22:53.8970000 | NULL | False | False | NULL |
| 00ABF0DA-EAE6-4E45-BEC9-D247DAE4033E | 2026-07-31T13:55:03.7430000 | B4FDD4F2-E252-4D4F-82EF-7EF7E96C8F7A | NULL | NULL | 2026-07-31T13:54:36.7430000 | NULL | False | False | NULL |
| 010271CD-37B3-48C8-8026-4AC0F9B71C31 | 2026-08-01T13:06:31.1570000 | 8953C204-7F5D-4E1F-A1C4-956A91873A39 | NULL | NULL | 2026-08-01T13:06:03.6230000 | NULL | False | False | NULL |
| 0109CC8C-5C47-4348-BA4D-9BED058985CF | 2026-08-05T12:59:51.3170000 | NULL | NULL | NULL | 2026-08-05T12:59:59.2930000 | NULL | False | False | NULL |
| 017B7407-EBB9-4F80-8FF0-352A057CAFC5 | 2026-08-03T18:19:22.2030000 | NULL | NULL | NULL | 2026-08-03T18:18:57.8500000 | NULL | False | False | NULL |
| 01B867E4-DB07-46A7-9861-D4F28D155453 | 2026-07-31T12:30:08.5430000 | B4FDD4F2-E252-4D4F-82EF-7EF7E96C8F7A | NULL | NULL | 2026-07-31T12:29:43.9270000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | S1IT | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BA706A48-E8F6-42FD-8BC9-13BE40794076 | 2026-08-24T12:41:46.2230000 | NULL | NULL |  | 2026-08-24T12:35:10.4000000 | 2026-08-26T15:56:56.3830000 | False | False | NULL |
| B95AC948-E13C-4F7A-AFAF-2F75FB3DEC69 | 2026-08-22T11:54:49.8770000 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL |  | 2026-08-22T11:55:06.2970000 | 2026-08-26T15:56:55.5570000 | False | False | NULL |
| 0ADB349C-F6EB-4B6F-AEB4-26C52249B51A | 2026-08-22T11:53:34.6970000 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL |  | 2026-08-22T11:53:53.1900000 | 2026-08-26T15:56:54.6870000 | False | False | NULL |
| 79449551-18CA-43F8-BA9A-2311C85A1599 | 2026-08-22T11:52:21.7730000 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL |  | 2026-08-22T11:52:39.2670000 | 2026-08-26T15:56:53.8430000 | False | False | NULL |
| ED1721D3-C3A8-44F0-A769-87F9AAF00884 | 2026-08-21T19:05:12.9400000 | NULL | NULL |  | 2026-08-21T19:05:31.3530000 | 2026-08-26T15:56:52.8670000 | False | False | NULL |
| 91102C9E-254E-4BD7-8967-0CA1CF488177 | 2026-08-21T19:03:59.9330000 | NULL | NULL |  | 2026-08-21T19:04:18.6600000 | 2026-08-26T15:56:51.3530000 | False | False | NULL |
| 20338B21-375E-48BF-A4D3-DE135FB1E770 | 2026-08-21T19:02:47.0170000 | NULL | NULL |  | 2026-08-21T19:03:05.4330000 | 2026-08-26T15:56:49.9070000 | False | False | NULL |
| E36023E5-CAD8-4BB1-91DE-A1705A6B2F56 | 2026-08-21T19:01:34.0000000 | NULL | NULL |  | 2026-08-21T19:01:51.7000000 | 2026-08-26T15:56:49.0530000 | False | False | NULL |
| E0355C28-2C5B-44C7-BBA1-F908843BA40C | 2026-08-21T19:00:20.4400000 | NULL | NULL |  | 2026-08-21T19:00:37.2330000 | 2026-08-26T15:56:48.1630000 | False | False | NULL |
| B025D0A5-A35F-4B11-861F-53F6924929AB | 2026-08-21T18:59:05.2370000 | NULL | NULL |  | 2026-08-21T18:59:25.0700000 | 2026-08-26T15:56:47.3130000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Product_Master.Name` -> `XStudio_XBatch.XMES_Billet_Strand_tracking.EndProduct` (One to Many)
- `XStudio_XBatch.XMES_Billet_Strand_tracking.EndProduct` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_Strand_tracking.ParentID` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to Many)
