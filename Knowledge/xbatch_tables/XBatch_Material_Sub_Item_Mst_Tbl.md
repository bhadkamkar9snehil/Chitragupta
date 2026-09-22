# XStudio_Xbatch.dbo.XBatch_Material_Sub_Item_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference lot, number, quantity, sub, uomid.

**Primary Key:** ID  
**Row Count:** 4,436  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| Quantity | decimal | NO | 18,4 | — |
| UOMID | varchar | NO | 36 | — |
| SubLotNumber | varchar | YES | 100 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00D2EEF0-8715-4FD9-A2BC-BAE44BD0372A | E0C4C90F-E642-4C67-AEA2-F6E3531D7B63 | NULL | NULL | 2026-03-07T20:39:04.9900000 | NULL | False | False | NULL | NULL |
| 00BB49B0-0A7E-4BF4-9594-3A4C529E9EB4 | 393C9AE0-BABD-49A6-88E5-02A0F27172E4 | NULL | NULL | 2026-02-18T02:58:37.4930000 | NULL | False | False | NULL | NULL |
| 00AC1967-4E1B-4E0C-83DE-C980A5A07901 | AF93E363-F559-42B4-A41B-738C0E78B14A | NULL | NULL | 2026-03-28T21:02:26.7230000 | NULL | False | False | NULL | NULL |
| 00A483D1-24F7-4480-A423-A523ED60875B | 2736B93B-A9A2-4AAE-9083-595FAC47DF9E | NULL | NULL | 2025-09-23T21:57:21.6970000 | NULL | False | False | NULL | NULL |
| 00994072-3955-432B-87DA-3F55549B9F26 | E27AAD32-22B4-4AFB-B6A0-C3ED508119B1 | NULL | NULL | 2026-03-03T06:00:17.5430000 | NULL | False | False | NULL | NULL |
| 00892878-D3E8-4B0B-9283-BE40B8E4CC2C | FBD1FA36-9B9E-4A79-A527-81D13185EA09 | NULL | NULL | 2025-10-13T07:39:17.9270000 | NULL | False | False | NULL | NULL |
| 0070280D-B69A-4F40-B3CB-EF04606DEF51 | 1A916858-200F-4058-A0E1-0077EA4FBFE7 | NULL | NULL | 2025-07-09T16:00:08.9270000 | NULL | False | False | NULL | NULL |
| 006E14D3-85E6-47DB-B441-4B2ECB25DF50 | 6BDC248D-3CB9-49D4-A36E-B953A92EE462 | NULL | NULL | 2025-10-12T22:09:25.1000000 | NULL | False | False | NULL | NULL |
| 00571FB1-4D6B-4E66-91D3-5D1E17285DD8 | FA7A79C6-F0A4-45CE-9748-D05A515814CF | NULL | NULL | 2026-02-15T21:01:12.9830000 | NULL | False | False | NULL | NULL |
| 001EA3CC-D480-44C0-8250-40825F698854 | D2B86176-1F26-4D19-9291-9EE9E1F2B8A6 | NULL | NULL | 2025-11-01T18:58:16.7300000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00D2EEF0-8715-4FD9-A2BC-BAE44BD0372A | E0C4C90F-E642-4C67-AEA2-F6E3531D7B63 | NULL | NULL | 2026-03-07T20:39:04.9900000 | NULL | False | False | NULL | NULL |
| 00BB49B0-0A7E-4BF4-9594-3A4C529E9EB4 | 393C9AE0-BABD-49A6-88E5-02A0F27172E4 | NULL | NULL | 2026-02-18T02:58:37.4930000 | NULL | False | False | NULL | NULL |
| 00AC1967-4E1B-4E0C-83DE-C980A5A07901 | AF93E363-F559-42B4-A41B-738C0E78B14A | NULL | NULL | 2026-03-28T21:02:26.7230000 | NULL | False | False | NULL | NULL |
| 00A483D1-24F7-4480-A423-A523ED60875B | 2736B93B-A9A2-4AAE-9083-595FAC47DF9E | NULL | NULL | 2025-09-23T21:57:21.6970000 | NULL | False | False | NULL | NULL |
| 00994072-3955-432B-87DA-3F55549B9F26 | E27AAD32-22B4-4AFB-B6A0-C3ED508119B1 | NULL | NULL | 2026-03-03T06:00:17.5430000 | NULL | False | False | NULL | NULL |
| 00892878-D3E8-4B0B-9283-BE40B8E4CC2C | FBD1FA36-9B9E-4A79-A527-81D13185EA09 | NULL | NULL | 2025-10-13T07:39:17.9270000 | NULL | False | False | NULL | NULL |
| 0070280D-B69A-4F40-B3CB-EF04606DEF51 | 1A916858-200F-4058-A0E1-0077EA4FBFE7 | NULL | NULL | 2025-07-09T16:00:08.9270000 | NULL | False | False | NULL | NULL |
| 006E14D3-85E6-47DB-B441-4B2ECB25DF50 | 6BDC248D-3CB9-49D4-A36E-B953A92EE462 | NULL | NULL | 2025-10-12T22:09:25.1000000 | NULL | False | False | NULL | NULL |
| 00571FB1-4D6B-4E66-91D3-5D1E17285DD8 | FA7A79C6-F0A4-45CE-9748-D05A515814CF | NULL | NULL | 2026-02-15T21:01:12.9830000 | NULL | False | False | NULL | NULL |
| 001EA3CC-D480-44C0-8250-40825F698854 | D2B86176-1F26-4D19-9291-9EE9E1F2B8A6 | NULL | NULL | 2025-11-01T18:58:16.7300000 | NULL | False | False | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Material_Sub_Item_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Item_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Sub_Item_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
