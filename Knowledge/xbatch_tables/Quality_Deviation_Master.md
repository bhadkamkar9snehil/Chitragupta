# XStudio_Xbatch.dbo.Quality_Deviation_Master

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** chemistry, quality, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference area, high, low, name, parameter, product, size.

**Primary Key:** ID  
**Row Count:** 91  
**Date Range (ModifiedOn):** 2026-01-12T13:55:56.0000000 to 2026-03-13T08:20:03.0000000  

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
| Size | varchar | YES | 36 | — |
| ParameterName | varchar | YES | 100 | — |
| High | varchar | YES | 100 | — |
| Low | varchar | YES | 100 | — |
| Product | varchar | YES | 36 | — |
| Area | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49AECE04-2B13-4276-A7E7-563A381B81FE | NULL | NULL | NULL | NULL | 2026-03-13T08:22:00.2630000 | NULL | False | False | NULL |
| 5CBBAB58-465C-4C5B-91D8-252AEF94FFF3 | NULL | NULL | NULL | NULL | 2026-03-13T08:22:00.2630000 | NULL | False | False | NULL |
| 7803B844-1ABE-47C8-8BB7-952F8290F99F | NULL | NULL | NULL | NULL | 2026-03-13T08:18:44.9600000 | NULL | False | False | NULL |
| AE498EFA-D1AA-49F7-8D6C-971CA2C769C9 | NULL | NULL | NULL | NULL | 2026-03-13T08:22:00.2630000 | NULL | False | False | NULL |
| D8C8B569-BD67-4529-A52B-6489568F39AC | NULL | NULL | NULL | NULL | 2026-03-13T08:22:00.2630000 | NULL | False | False | NULL |
| F730944A-C072-4401-8331-10736493A2D7 | NULL | NULL | NULL | NULL | 2026-03-13T08:22:00.2630000 | NULL | False | False | NULL |
| 4A67EB43-565D-4F65-91D0-4A49A54E566A | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T13:55:56.1370000 | 2026-01-12T13:55:56.0000000 | False | False | NULL |
| D0E240CE-94F0-4836-B6F7-5416C3C4330D | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T13:56:31.3430000 | 2026-01-12T13:56:31.0000000 | False | False | NULL |
| DAA5F262-211A-4513-B80D-F72B8FEBD844 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T13:57:06.6900000 | 2026-01-12T13:57:06.0000000 | False | False | NULL |
| B9707F9E-453E-49C3-AC3A-FB1943B4E775 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T13:57:34.8300000 | 2026-01-12T13:57:34.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0EE3040A-D9DC-4091-94F1-49D0447BF274 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-13T08:20:03.1230000 | 2026-03-13T08:20:03.0000000 | False | False | NULL |
| A9F3A1C3-D079-4C5F-B93D-28F4A4728609 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-13T08:19:41.0200000 | 2026-03-13T08:19:41.0000000 | False | False | NULL |
| 151F3BF6-55CE-47A3-8F77-45A12B86748E | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-13T08:15:46.2370000 | 2026-03-13T08:16:17.0000000 | False | False | NULL |
| DF839DCE-B9C2-4904-8EC8-89B419956E0D | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-13T08:14:09.0470000 | 2026-03-13T08:14:09.0000000 | False | False | NULL |
| 508DFD3D-5049-4807-A881-4E5250792F70 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-12T14:43:22.0800000 | 2026-01-17T08:24:14.0000000 | False | False | NULL |
| 5B830CAB-85D2-4F06-908A-A7DE6DFCE6F4 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-12T14:44:22.2200000 | 2026-01-17T08:24:14.0000000 | False | False | NULL |
| 713D1AEB-4C8F-4F99-A071-A275EC410DE4 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-12T14:43:33.1930000 | 2026-01-17T08:24:14.0000000 | False | False | NULL |
| 88B1BE28-8DD2-40DA-AA6C-80E2640ED4E4 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-12T14:44:43.8530000 | 2026-01-17T08:24:14.0000000 | False | False | NULL |
| EE785FC3-B140-4A8C-A44A-6F9B44411250 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-12T14:43:50.6900000 | 2026-01-17T08:24:14.0000000 | False | False | NULL |
| F1704875-B69C-4466-912F-632E2397A681 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-12T14:44:33.9030000 | 2026-01-17T08:24:14.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Quality_Deviation_Master.Product` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.Quality_Deviation_Master.Size` -> `XStudio_XBatch.Size_Nominal_Wt_Value_Master.ID` (Many to One)
