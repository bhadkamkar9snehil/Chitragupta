# XStudio_Xbatch.dbo.Chemistry_Deviation_Quality_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** chemistry, quality, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference percentage, per, actual, max, min, shift, smsprotocol, tdc, elements, grade, heat, incharge.

**Primary Key:** ID  
**Row Count:** 3,997  
**Date Range (ModifiedOn):** 2026-03-20T16:47:23.0400000 to 2026-05-01T14:20:14.9730000  

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
| HeatNo | varchar | YES | 36 | — |
| Remarks | varchar | YES | -1 | — |
| Shift | varchar | YES | 100 | — |
| Elements | varchar | YES | 100 | — |
| TundishAtActualPercentage | decimal | YES | 18,4 | — |
| ProductAtActualPercentage | decimal | YES | 18,4 | — |
| MinPercentageAsPerSMSProtocol | decimal | YES | 18,4 | — |
| MinPercentageAsPerTDC | decimal | YES | 18,4 | — |
| MaxPercentageAsPerSMSProtocol | decimal | YES | 18,4 | — |
| ShiftIncharge | varchar | YES | 300 | — |
| LRFAtActualPercentage | decimal | YES | 18,4 | — |
| MaxPercentageAsPerTDC | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Grade | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 005C26B7-9927-4254-BF53-96CE2CA986F7 | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 00458763-54D7-4C13-AA2A-6AB8AED50C65 | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 003BD896-3B03-4E32-89CC-CE1EBCC8FD77 | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 001C240B-6EFA-4CAE-8C85-F50EB768B341 | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 001813BA-BF08-45A2-803C-F40CFFBD98CD | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 00107A79-E0D8-49AD-A9A4-37395C117B4D | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 00100FF3-D0BB-45A0-B750-64EF8B2A419B | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 00073D04-CF1A-460C-AC9C-395169E4AD2D | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 0063259D-46B9-4A67-B100-CA4149549522 | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |
| 00782FAB-15B6-45D4-8870-C05E7EBDCFCF | NULL | NULL | 2026-05-01T14:20:15.0630000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001082C6-DA98-4CB0-AB50-D9A184A1A9C5 | NULL | NULL | 2026-03-26T10:51:23.6300000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 0062BFC7-10D7-457A-9169-080B413D77C8 | NULL | NULL | 2026-03-20T16:11:21.3530000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 00793251-AD04-487C-BCE3-7AEC881AF5C0 | NULL | NULL | 2026-03-26T10:51:23.6300000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 009D1869-5416-40E3-9CBC-921E127A8A5F | NULL | NULL | 2026-03-26T10:51:23.6300000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 00BE336F-0426-4AB0-8A45-086931E7423F | NULL | NULL | 2026-03-20T16:11:21.3530000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 01884C41-961D-49A3-B203-C34E236BA491 | NULL | NULL | 2026-03-26T10:51:23.6300000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 019EFABD-7CB2-4489-B28A-FCED0BBEA083 | NULL | NULL | 2026-03-20T16:11:21.3530000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 021C3F29-2F0B-42E1-9D05-783352700EC0 | NULL | NULL | 2026-03-20T16:11:21.3530000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 024403D3-9D1F-4EF9-9A6E-97FA80104F46 | NULL | NULL | 2026-03-26T10:51:23.6300000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |
| 02971839-6C70-4699-9B50-DED2A52F4595 | NULL | NULL | 2026-03-26T10:51:23.6300000 | 2026-05-01T14:20:14.9730000 | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Chemistry_Deviation_Quality_Data.Grade` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.Chemistry_Deviation_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Chemistry_Deviation_Quality_Data.ShiftIncharge` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.FullName` (Many to One)
