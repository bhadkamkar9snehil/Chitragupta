# XStudio_Xbatch.dbo.XMES_Billet_VS_GLS_Grade_Mapping

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference grade, billet, endproduct, glsgrade.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2026-04-17T08:09:42.0000000 to 2026-08-11T16:47:47.0000000  

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
| BilletGrade | varchar | YES | 36 | — |
| GLSGrade | varchar | YES | 36 | — |
| EndproductGrade | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 88941EC8-49D4-4E5D-BD69-5BF3FC9BFBB6 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-04-17T08:09:42.7730000 | 2026-04-17T08:09:42.0000000 | False | False | NULL |
| 8E0C2D27-863E-4275-9E6C-906BA7AB3CD5 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-24T09:44:35.2400000 | 2026-04-24T09:44:35.0000000 | False | False | NULL |
| 52F0E480-2FB6-49FE-B816-1DF8B294DD08 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-05-06T21:00:11.0230000 | 2026-06-04T10:29:03.7030000 | True | False | NULL |
| 8E02E6A4-7732-40A4-92D8-E8B7C1E21287 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-17T08:08:57.4970000 | 2026-06-12T16:22:52.0000000 | False | False | NULL |
| A66AA6C5-7C28-4D2E-BA2E-D8CE22048CC1 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-11T13:57:28.4600000 | 2026-06-15T09:10:10.0000000 | False | False | NULL |
| AA426E72-06B5-41D4-ABAA-3D9A0DAC7F77 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-17T08:08:40.9030000 | 2026-07-01T08:40:45.0000000 | False | False | NULL |
| 5F4336D7-137C-43B9-A0EC-F87653278C50 | NULL | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-16T09:22:02.4630000 | 2026-08-11T16:47:12.0000000 | False | False | NULL |
| 32DD21CD-961F-4719-A809-F2A00D3EFAC9 | NULL | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-06-02T13:41:07.3900000 | 2026-08-11T16:47:26.0000000 | False | False | NULL |
| A515D39E-D223-4A54-8C4E-01BA7B4BB898 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-17T08:09:24.3600000 | 2026-08-11T16:47:32.0000000 | False | False | NULL |
| 4B50139A-26F9-49ED-B254-0078BC1A8F59 | NULL | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-06-12T15:35:16.9370000 | 2026-08-11T16:47:47.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Billet_VS_GLS_Grade_Mapping.BilletGrade` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_VS_GLS_Grade_Mapping.EndproductGrade` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_VS_GLS_Grade_Mapping.GLSGrade` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
