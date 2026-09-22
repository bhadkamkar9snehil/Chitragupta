# XStudio_Xbatch.dbo.Grade_Master

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference grade, code, color, description, name, type.

**Primary Key:** ID  
**Row Count:** 48  
**Date Range (ModifiedOn):** 2025-12-12T08:49:33.0000000 to 2026-08-17T08:05:28.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| GradeName | varchar | YES | 100 | — |
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
| Description | varchar | YES | 72 | — |
| ColorCode | varchar | YES | 50 | — |
| GradeType | varchar | YES | 36 | — |

### Top 10 Records

| ID | GradeName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E09E3947-03B8-45EA-992B-C49A8C762F91 | 3S1/PS | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-11T10:22:12.1830000 | 2025-12-12T08:49:33.0000000 | False | False | NULL |
| 1286226E-696E-4EBF-A15C-1A4EF01F5A05 | 3SP HC | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-04T08:50:27.9000000 | 2025-12-12T08:49:38.0000000 | False | False | NULL |
| 4F8A149F-5CB3-41DD-AF24-A6842FC2017B | 3SP | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-04T08:50:05.2300000 | 2025-12-12T08:49:42.0000000 | False | False | NULL |
| F73A7538-69D1-404D-8BEC-1CFC7889779B | 3SP/P | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-11T10:27:50.2430000 | 2025-12-12T08:49:47.0000000 | False | False | NULL |
| 0E67C0F3-7EF9-42C6-BA77-8675F3759CB5 | B500BLMNHC | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-09-11T12:55:56.8600000 | 2025-12-12T08:50:06.0000000 | False | False | NULL |
| 14D72E87-61EC-48E1-829F-39DC5378A247 | B500B | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-12T10:33:08.0000000 | 2025-12-12T13:40:00.0000000 | False | False | NULL |
| 2E0E428F-F97B-4271-A294-1CC2A1C66340 | 3SP/PS-M | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-26T12:44:13.8430000 | 2025-12-26T12:44:13.0000000 | False | False | NULL |
| 82DA5875-7DEB-45C1-B042-47D74689B032 | 3SP/RC | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-26T12:45:02.3000000 | 2025-12-26T12:45:02.0000000 | False | False | NULL |
| A2F9BB5D-7DFE-48D0-A968-DE088DFF7BE2 | 4SP | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-26T12:45:27.0030000 | 2025-12-26T12:45:27.0000000 | False | False | NULL |
| 66817AC4-0BED-4B98-8BD2-87A1A89A6025 | A615M | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-26T12:46:19.1330000 | 2025-12-26T12:46:19.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | GradeName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31DC5931-701A-40C2-816B-D48FC7A774AA | FK79 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-17T08:05:28.8400000 | 2026-08-17T08:05:28.0000000 | False | False | NULL |
| 3679C657-0455-4E72-9639-CF58B73581C5 | FT67 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-17T07:58:38.6070000 | 2026-08-17T07:58:38.0000000 | False | False | NULL |
| BFE56B3D-35C2-47D2-AE9B-62D53583B81E | 550DCRS | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-07T15:12:14.7530000 | 2026-08-07T15:12:14.0000000 | False | False | NULL |
| 95583AEB-EA9A-46DF-A81A-88A65936D0E2 | ABC | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-06-06T09:04:21.4600000 | 2026-06-06T09:15:46.0130000 | True | False | NULL |
| 935EA279-F33B-4433-BC20-1363DCC3DF44 | XF1516 | NULL | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-06-04T10:42:29.5200000 | 2026-06-04T10:42:29.0000000 | False | False | NULL |
| FB3F925B-354A-4ACB-B55C-ABC5E7720232 | CRSRM | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-12-26T13:58:04.4330000 | 2026-04-23T23:38:30.0000000 | False | False | NULL |
| 54789AFA-7D60-4439-A968-8119CC66754B | SAE1040 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-04-23T14:20:41.2230000 | 2026-04-23T14:20:41.0000000 | False | False | NULL |
| 1C14DF3B-2EAC-4971-AB39-79AEA3E28F4B | 3SP/PS | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2025-08-19T08:04:31.4100000 | 2026-03-17T15:09:16.0000000 | False | False | NULL |
| 342B9A8A-DEBC-4BE7-B831-ECD577090E7A | GR40AC | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-02-21T11:09:43.2770000 | 2026-02-21T11:09:43.0000000 | False | False | NULL |
| 2B0B2843-C333-4083-920E-0C71A0A20F04 | SAE1008 | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2025-12-26T12:49:06.2400000 | 2026-02-11T13:51:08.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_Per_Heat.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.EAF_LogSheet_Quantity.Grade` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.EAF_PER_HEAT.SteelGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Grade_Master.GradeType` -> `XStudio_XBatch.Grade_Type_Master.GradeType` (Many to One)
- `XStudio_XBatch.Grade_Test_Mapping.GradeName` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.Heat_Chemistry_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.List_Rebar_Coil_Quality_Data_Histroy.BilletGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.List_Rebar_Coil_Quality_Data_Histroy.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.LRF_Chemical_Composition.Grade` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.LRF_Per_Heat.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Coil_Quality_Data.BilletGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Coil_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Quality_Data.BilletGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Round_Bar_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Wire_Rod_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Wire_Rod_Quality_Data_File_Import.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.MaterialGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.MaterialGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
