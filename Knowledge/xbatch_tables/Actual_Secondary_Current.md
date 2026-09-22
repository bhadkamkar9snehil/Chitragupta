# XStudio_Xbatch.dbo.Actual_Secondary_Current

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference sec, transformer, mvatransformer, mvab, mvar, mvay, eaftransfomer, lrftransfomer, tranboosterfan, name, engineer, shift.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-13T10:55:56.0000000 to 2026-09-02T08:16:02.0000000  

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
| SecTransformer31MVAY | int | YES | 10,0 | — |
| Sec63MVATransformerB | int | YES | 10,0 | — |
| Sec15MVATransformerY | int | YES | 10,0 | — |
| SecTransformer31MVAB | int | YES | 10,0 | — |
| SecEAFTransfomer80MVAB | int | YES | 10,0 | — |
| SecTransformer23MVAY | int | YES | 10,0 | — |
| SecLRFTransfomer30MVAB | decimal | YES | 18,4 | — |
| Sec125MVATransformerB | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| Sec63MVATransformerY | int | YES | 10,0 | — |
| SecEAFTransfomer80MVAR | int | YES | 10,0 | — |
| SecLRFTransfomer30MVAR | decimal | YES | 18,4 | — |
| SecTransformer516MVAB | int | YES | 10,0 | — |
| EntryDateTime | datetime | YES | — | — |
| SecTransformer3a3MVAB | decimal | YES | 18,4 | — |
| SecEAFTransfomer80MVAY | int | YES | 10,0 | — |
| SecTranboosterfan12MVAY | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| SecTransformer13MVAR | int | YES | 10,0 | — |
| Sec24MVATransformerY | int | YES | 10,0 | — |
| SecTransformer4a3MVAB | int | YES | 10,0 | — |
| Sec125MVATransformerY | int | YES | 10,0 | — |
| SecTransformer13MVAY | int | YES | 10,0 | — |
| SecTransformer23MVAR | int | YES | 10,0 | — |
| Sec63MVATransformerR | int | YES | 10,0 | — |
| SecLRFTransfomer30MVAY | decimal | YES | 18,4 | — |
| SecTransformer3a3MVAR | decimal | YES | 18,4 | — |
| Sec125MVATransformerR | int | YES | 10,0 | — |
| SecTransformer2a4MVAB | int | YES | 10,0 | — |
| SecTransformer4a3MVAY | int | YES | 10,0 | — |
| SecTransformer43MVAR | decimal | YES | 18,4 | — |
| SecTranboosterfan12MVAB | decimal | YES | 18,4 | — |
| SecTranboosterfan12MVAR | int | YES | 10,0 | — |
| Sec24MVATransformerR | int | YES | 10,0 | — |
| EngineerName | varchar | YES | 36 | — |
| TechnicianName | varchar | YES | 36 | — |
| SecTransformer2a4MVAR | int | YES | 10,0 | — |
| SecTransformer23MVAB | int | YES | 10,0 | — |
| SecTransformer4a3MVAR | int | YES | 10,0 | — |
| SecTransformer43MVAY | decimal | YES | 18,4 | — |
| SecTransformer31MVAR | int | YES | 10,0 | — |
| SecTransformer43MVAB | decimal | YES | 18,4 | — |
| SecTransformer3a3MVAY | decimal | YES | 18,4 | — |
| Sec15MVATransformerR | int | YES | 10,0 | — |
| SecTransformer516MVAR | int | YES | 10,0 | — |
| Sec24MVATransformerB | int | YES | 10,0 | — |
| SecTransformer516MVAY | int | YES | 10,0 | — |
| SecTransformer2a4MVAY | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| Sec15MVATransformerB | int | YES | 10,0 | — |
| SecTransformer13MVAB | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 072A3C4A-D05F-4D8C-8016-3207F7F3F4CF | NULL | NULL | 2026-07-13T00:50:22.2430000 | NULL | False | False | NULL | NULL | NULL |
| 0957AF8A-C0CE-4572-89E7-A41E263FEB3B | NULL | NULL | 2026-04-30T08:06:41.9300000 | NULL | False | False | NULL | NULL | NULL |
| 0EBAF865-1147-49FB-A636-06A1F501F18C | NULL | NULL | 2026-08-01T23:46:19.6570000 | NULL | False | False | NULL | NULL | NULL |
| 19614ED3-FAB9-4D31-9335-CF7A61AEBCB1 | NULL | NULL | 2026-07-20T00:40:27.0530000 | NULL | False | False | NULL | NULL | NULL |
| 1C466369-E865-49E2-89A7-644932616348 | NULL | NULL | 2026-08-03T22:15:38.5130000 | NULL | False | False | NULL | NULL | NULL |
| 1FB67283-4EFB-49D5-83A2-3F53028ADF5E | NULL | NULL | 2026-07-28T01:22:23.9500000 | NULL | False | False | NULL | NULL | NULL |
| 202F0E34-A041-47AF-8131-1A6513F7CD99 | NULL | NULL | 2026-02-19T22:19:19.6800000 | NULL | False | False | NULL | NULL | NULL |
| 212CF194-D82F-4CB3-B40D-DE71DD94EED5 | NULL | NULL | 2026-01-13T19:50:21.8130000 | NULL | False | False | NULL | NULL | NULL |
| 22F0AC06-B24C-49AB-AAA3-EAB0CB989D12 | NULL | NULL | 2026-09-01T07:57:43.1730000 | NULL | False | False | NULL | NULL | NULL |
| 26ABF478-7798-45B8-97F3-45315314FCD4 | NULL | NULL | 2026-08-01T00:48:30.9400000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FDF7F7C3-5B07-411D-9CAD-D45A3794BD44 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9970000 | 2026-09-02T08:16:02.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| FAC018D0-9D84-4C4B-BFAC-A62A768D8B97 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7400000 | 2026-09-02T01:12:50.0000000 | False | False | NULL |  | NULL |
| 3653FEE3-79DD-400E-BD09-F7FAD2F24AA0 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1900000 | 2026-09-01T00:11:23.0000000 | False | False | NULL |  | NULL |
| E6A7562D-A1E6-4A3E-8AAD-D1DA159F6EE3 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0900000 | 2026-08-30T23:14:02.0000000 | False | False | NULL |  | NULL |
| C1F08717-4A9D-4BD2-9233-0D47EBA8114C | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5170000 | 2026-08-30T01:24:15.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| E7D4149A-42CC-4CAC-A1AB-076CC54435A9 | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.0630000 | 2026-08-29T01:26:16.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 973A1CA9-16D5-4F58-BBAB-1BEF7F545681 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7530000 | 2026-08-28T00:50:14.0000000 | False | False | NULL |  | NULL |
| 0F64E06A-36E7-4407-A6E0-3949B20224A6 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0330000 | 2026-08-26T21:34:41.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 673617E6-4BCA-41DF-9660-D9D24E45D310 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-25T20:01:32.2300000 | 2026-08-25T21:27:12.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 8AB83D25-FED9-4943-8A04-61D3FADE4FBA | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-23T00:12:23.1030000 | 2026-08-23T01:21:21.0000000 | False | False | NULL |  | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Actual_Secondary_Current.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Actual_Secondary_Current.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
