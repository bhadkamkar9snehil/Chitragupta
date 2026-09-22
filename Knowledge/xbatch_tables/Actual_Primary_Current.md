# XStudio_Xbatch.dbo.Actual_Primary_Current

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference pri, transformer, mvatransformer, mvab, mvar, mvay, eaftransfomer, lrftransfomer, tranboosterfan, name, engineer, shift.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-13T10:55:02.0000000 to 2026-09-02T08:12:43.0000000  

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
| Pri15MVATransformerR | int | YES | 10,0 | — |
| PriEAFTransfomer80MVAY | int | YES | 10,0 | — |
| PriTransformer2a4MVAB | int | YES | 10,0 | — |
| EntryDateTime | datetime | YES | — | — |
| Pri125MVATransformerB | int | YES | 10,0 | — |
| PriTransformer13MVAB | int | YES | 10,0 | — |
| EngineerName | varchar | YES | 36 | — |
| PriTransformer516MVAY | int | YES | 10,0 | — |
| PriTransformer23MVAR | int | YES | 10,0 | — |
| Pri24MVATransformerB | int | YES | 10,0 | — |
| Pri63MVATransformerR | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |
| PriTransformer13MVAR | int | YES | 10,0 | — |
| PriTransformer43MVAY | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| PriTransformer516MVAR | int | YES | 10,0 | — |
| PriTransformer4a3MVAB | int | YES | 10,0 | — |
| PriLRFTransfomer30MVAR | decimal | YES | 18,4 | — |
| PriTransformer516MVAB | int | YES | 10,0 | — |
| Pri125MVATransformerR | int | YES | 10,0 | — |
| PriTransformer2a4MVAY | int | YES | 10,0 | — |
| PriTransformer31MVAY | int | YES | 10,0 | — |
| Pri15MVATransformerY | int | YES | 10,0 | — |
| PriLRFTransfomer30MVAY | decimal | YES | 18,2 | — |
| PriTransformer4a3MVAR | int | YES | 10,0 | — |
| Pri24MVATransformerR | int | YES | 10,0 | — |
| PriTransformer31MVAB | int | YES | 10,0 | — |
| PriTransformer43MVAR | decimal | YES | 18,4 | — |
| Pri63MVATransformerY | int | YES | 10,0 | — |
| PriTranboosterfan12MVAB | decimal | YES | 18,4 | — |
| PriLRFTransfomer30MVAB | decimal | YES | 18,4 | — |
| Pri125MVATransformerY | int | YES | 10,0 | — |
| PriTranboosterfan12MVAR | int | YES | 10,0 | — |
| PriTransformer23MVAB | int | YES | 10,0 | — |
| IsProcessed | bit | YES | — | — |
| PriTransformer4a3MVAY | int | YES | 10,0 | — |
| PriTransformer3a3MVAY | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| PriTransformer23MVAY | int | YES | 10,0 | — |
| PriTransformer3a3MVAB | decimal | YES | 18,4 | — |
| PriEAFTransfomer80MVAR | int | YES | 10,0 | — |
| Pri15MVATransformerB | int | YES | 10,0 | — |
| Pri24MVATransformerY | int | YES | 10,0 | — |
| PriTranboosterfan12MVAY | decimal | YES | 18,4 | — |
| PriTransformer2a4MVAR | int | YES | 10,0 | — |
| Pri63MVATransformerB | int | YES | 10,0 | — |
| PriTransformer13MVAY | int | YES | 10,0 | — |
| PriEAFTransfomer80MVAB | int | YES | 10,0 | — |
| PriTransformer31MVAR | int | YES | 10,0 | — |
| PriTransformer3a3MVAR | decimal | YES | 18,4 | — |
| PriTransformer43MVAB | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| TechnicianName | varchar | YES | 36 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0F439BF5-FC1D-4FAB-A6A2-C8BF151744DC | NULL | NULL | 2026-03-24T21:11:53.5030000 | NULL | False | False | NULL | NULL | NULL |
| 1E83C41C-E1BC-434A-BD9F-358EC9B6AC7A | NULL | NULL | 2026-08-12T18:58:52.5970000 | NULL | False | False | NULL | NULL | NULL |
| 20B85DE0-D856-4363-900A-53222D060224 | NULL | NULL | 2026-02-13T10:33:43.0070000 | NULL | False | False | NULL | NULL | NULL |
| 2125D3DE-3C01-455B-A427-BA6C110022A8 | NULL | NULL | 2026-08-14T00:44:39.3030000 | NULL | False | False | NULL | NULL | NULL |
| 2622E2BD-5DA8-45F5-8123-F17DEE790286 | NULL | NULL | 2026-08-01T00:48:30.9230000 | NULL | False | False | NULL | NULL | NULL |
| 297358A6-A96A-41B3-8645-53192DB030FD | NULL | NULL | 2026-08-15T00:12:41.3500000 | NULL | False | False | NULL | NULL | NULL |
| 2D70DC4F-A6BD-4053-99B8-7C6BAB107586 | NULL | NULL | 2026-01-14T08:40:14.5430000 | NULL | False | False | NULL | NULL | NULL |
| 31AE5667-B68B-4CE9-97FF-D1AEC91CF8D5 | NULL | NULL | 2025-12-28T23:20:36.5900000 | NULL | False | False | NULL | NULL | NULL |
| 3ECAC69B-11B1-4C62-89E0-7A2570B02CBF | NULL | NULL | 2025-12-29T22:36:43.2300000 | NULL | False | False | NULL | NULL | NULL |
| 42D37D25-E1DE-48F9-9C72-0283FE07A09C | NULL | NULL | 2026-01-29T20:19:52.3870000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59A52B4E-6BA3-48D7-B946-95139744CB53 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9830000 | 2026-09-02T08:12:43.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 3EA62925-DAFD-4CC8-AD99-0AD3F62C2356 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7270000 | 2026-09-02T01:07:24.0000000 | False | False | NULL |  | NULL |
| 203D3B51-29BE-45AF-B179-3C434E4938AA | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1800000 | 2026-09-01T00:10:06.0000000 | False | False | NULL |  | NULL |
| 7C287801-97B6-4521-9103-A66C76F08C21 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0770000 | 2026-08-30T23:12:39.0000000 | False | False | NULL |  | NULL |
| 0F8376F2-8B2E-4D38-8D6E-8C17377F7C5A | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5030000 | 2026-08-30T01:22:51.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 4D37F7AD-D9F6-488C-B7CB-3296E69D354A | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.0500000 | 2026-08-29T01:23:38.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| AD5EB1A7-1CA2-4F6B-88E7-7C7694800A4E | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7400000 | 2026-08-28T00:47:03.0000000 | False | False | NULL |  | NULL |
| 3EC19F30-6755-40DA-8A03-C865866D24E7 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0200000 | 2026-08-26T21:29:37.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| BBF6F03A-77A1-4509-BFE4-0D89E6E80B98 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-25T20:01:32.2200000 | 2026-08-25T21:24:42.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 52555796-8484-44E8-B305-0D59CAB35C4E | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-23T00:12:23.0870000 | 2026-08-23T01:01:49.0000000 | False | False | NULL | 172.16.4.185 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Actual_Primary_Current.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Actual_Primary_Current.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
