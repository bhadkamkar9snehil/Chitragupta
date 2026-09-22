# XStudio_Xbatch.dbo.XMES_Live_Charging_SECT2

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, out, billet, furnace, residence, status, total, weighment.

**Primary Key:** ID  
**Row Count:** 1,599  
**Date Range (ModifiedOn):** 2026-07-30T13:05:48.5670000 to 2026-08-31T10:30:41.3970000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| BilletNo | varchar | YES | 100 | — |
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
| IsProcessed | bit | YES | — | — |
| InTIme | datetime | YES | — | — |
| OutTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| Weighment | decimal | YES | 18,4 | — |
| FurnaceOutTime | datetime | YES | — | — |
| TotalResidenceTime | int | YES | 10,0 | — |

### Top 10 Records

| ID | BilletNo | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D59B0310-E104-4E16-BAB1-1B3B54D9CE05 | 1603166_S5_01 | E4FD4F3A-EBAC-4BD1-8EF5-3AE190613FD2 | NULL | NULL | 2026-07-30T12:59:12.2200000 | 2026-07-30T13:05:48.5670000 | False | False | NULL |
| E4547119-7BEC-4F09-B80B-82AFC2896184 | 1603166_S4_02 | 87443FB2-2524-4DC2-8CD6-79784D4A4327 | NULL | NULL | 2026-07-30T13:05:58.0600000 | 2026-07-30T13:06:16.6000000 | False | False | NULL |
| AAC98192-4BA7-4AA2-9140-D7B1D1D4EFC4 | 1603166_S1_03 | F695CFF5-9757-43BC-8F97-AB733F17D7E1 | NULL | NULL | 2026-07-30T13:07:06.1300000 | 2026-07-30T13:07:25.8470000 | False | False | NULL |
| 4A510FD5-3C17-4E48-A955-C6F5C346812B | 1603166_S3_04 | 4DC965FF-31F0-402B-8224-EDD1231E42D0 | NULL | NULL | 2026-07-30T13:08:15.1170000 | 2026-07-30T13:08:35.3030000 | False | False | NULL |
| 595CA00D-9978-4625-BE32-0DDA55A0C09C | 1603166_S2_05 | F12AD0CA-41B9-4EFC-9FB6-0069F24B7CBC | NULL | NULL | 2026-07-30T13:09:22.3470000 | 2026-07-30T13:09:42.9770000 | False | False | NULL |
| 460EC7EA-A679-4225-AE08-4EE47496968B | 1603166_S4_06 | 65F88272-3973-49CF-ADA7-16AFCE9DA860 | NULL | NULL | 2026-07-30T13:10:31.3630000 | 2026-07-30T13:10:51.6530000 | False | False | NULL |
| 4D0653D4-7A44-4B26-9B51-89F817BE0329 | 1603166_S5_07 | 4533072D-B0D3-4EE5-8C8B-99A34C436BBC | NULL | NULL | 2026-07-30T13:15:06.9570000 | 2026-07-30T13:15:27.4670000 | False | False | NULL |
| 5E37A3C9-180B-49B9-82E2-E984DBE1582D | 1603166_S1_08 | 1CC8A912-A3BD-4CD7-BB09-932ECF68A513 | NULL | NULL | 2026-07-30T13:16:15.8770000 | 2026-07-30T13:16:36.4300000 | False | False | NULL |
| 0A0F794E-26EC-42AB-B58F-7B831794F7E6 | 1603166_S3_09 | 96796989-F200-47DB-95A3-D3FFB30C7139 | NULL | NULL | 2026-07-30T13:18:33.1370000 | 2026-07-30T13:18:53.7670000 | False | False | NULL |
| 9FF2B007-4890-4E2F-8270-E75569CB41B6 | 1603166_S2_10 | CE1B08D9-0761-459C-A5B1-A9E1CFB9C491 | NULL | NULL | 2026-07-30T13:19:41.2030000 | 2026-07-30T13:20:00.9700000 | False | False | NULL |

### Bottom 10 Records

| ID | BilletNo | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9990AC20-8674-4E38-93CE-46F7F3F4B331 | 2603931_00_01 | EF12C871-EA85-46A6-9F33-81037C0DBD74 | NULL | NULL | 2026-08-31T03:40:07.7600000 | 2026-08-31T10:30:41.3970000 | False | False | NULL |
| 5CB9B9AA-D8EC-408E-A8E6-DA48104088FF | 1260781_00_01 | 59859D22-7575-445B-96E4-92E11C3AC96C | NULL | NULL | 2026-08-25T14:49:49.4030000 | 2026-08-25T14:50:11.0500000 | False | False | NULL |
| 22568EEE-DEFD-41B4-AD03-2DE2249E4D23 | 1260773_00_01 | E423E32B-F5B9-4B97-97EC-22A5F3F4C2D4 | NULL | NULL | 2026-08-25T13:54:51.6070000 | 2026-08-25T13:55:14.2970000 | False | False | NULL |
| 1BE81BBD-7B9C-4874-8983-CC22E3624432 | 1260817_00_46 | 23CA200F-329E-47EA-B304-F123E72C35C5 | NULL | NULL | 2026-08-25T13:07:22.9970000 | 2026-08-25T13:07:44.6300000 | False | False | NULL |
| B4865385-49A8-461D-8402-B580FF82E751 | 1260817_00_45 | 026C7A2D-ED8A-4E40-AD8F-69F8D3593B70 | NULL | NULL | 2026-08-24T17:20:50.6600000 | 2026-08-24T17:21:12.4570000 | False | False | NULL |
| CA1C0470-A7B9-4636-AD47-C71619A3E6EE | 1260817_00_44 | A4544DFA-BE3B-42F6-A1CD-FE5CBF5F095D | NULL | NULL | 2026-08-24T17:19:18.4600000 | 2026-08-24T17:19:40.4930000 | False | False | NULL |
| 28708052-C604-448E-9393-EAEB3BCD500F | 1260817_00_43 | 36D5C3E2-5315-4DA7-A4E9-4EB2F57A0912 | NULL | NULL | 2026-08-24T17:17:45.8330000 | 2026-08-24T17:18:07.0870000 | False | False | NULL |
| DC4C073F-D4DC-43EE-88F4-1D5489035D68 | 1260817_00_42 | 1B51AF17-70DD-4D31-A7D9-48434D60645A | NULL | NULL | 2026-08-24T17:16:16.5170000 | 2026-08-24T17:16:38.4730000 | False | False | NULL |
| F73E141C-9380-469C-B57A-CF34386C105E | 1260817_00_41 | A9F4AA56-53ED-45C8-B3F4-6C36725A234E | NULL | NULL | 2026-08-24T17:14:43.9000000 | 2026-08-24T17:15:05.3200000 | False | False | NULL |
| 0862D0AC-BC3D-4BE6-A71C-4CBB29185E96 | 1260817_00_40 | 7A5AE7FD-8BA6-43D0-90EB-2E60C6AE0D83 | NULL | NULL | 2026-08-24T17:13:10.5430000 | 2026-08-24T17:13:32.3630000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Billet_Movement_Dtl_Tbl.Section2BilletNo` -> `XStudio_XBatch.XMES_Live_Charging_SECT2.BilletNo` (Many to One)
- `XStudio_XBatch.XMES_Live_Charging_SECT2.ID` -> `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.ParentID` (One to Many)
- `XStudio_XBatch.XMES_Live_Charging_SECT2.ParentID` -> `XStudio_XBatch.XMES_Live_Charging_SECT1.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.ParentID` -> `XStudio_XBatch.XMES_Live_Charging_SECT2.ID` (Many to One)
