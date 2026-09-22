# XStudio_Xbatch.dbo.XBatch_Material_Item_Prod_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference number, quantity, declare, grade, heat, lot, material, sublot, uomid.

**Primary Key:** ID  
**Row Count:** 1,71,218  

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
| LotNumber | varchar | NO | 100 | — |
| SublotNumber | varchar | YES | 100 | — |
| Quantity | decimal | NO | 18,4 | — |
| UOMID | varchar | NO | 36 | — |
| GradeID | varchar | YES | 36 | — |
| HeatNo | int | YES | 10,0 | — |
| MaterialID | varchar | YES | 36 | — |
| DeclareQuantity | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0005B696-7E8D-4BD9-841F-B79E07B576D0 | NULL | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | NULL | 2026-03-18T18:00:28.5870000 | NULL | False | False | NULL | NULL |
| 0003C64D-C140-4A12-917F-AA6DD580FB47 | NULL |  | NULL | 2026-02-28T18:11:59.2430000 | NULL | False | False | NULL | NULL |
| 00038118-94B0-4CD2-BFB4-0602B773175F | NULL |  | NULL | 2025-12-24T18:19:18.3770000 | NULL | False | False | NULL | NULL |
| 00032B7B-C6A0-4BF5-A375-A0B281A99F82 | NULL |  | NULL | 2025-12-21T02:01:43.6730000 | NULL | False | False | NULL | NULL |
| 0002C69A-3A90-4870-8CCE-DE9B7953519F | NULL |  | NULL | 2025-11-16T14:15:42.4300000 | NULL | False | False | NULL | NULL |
| 00026EF9-CC16-4C49-AA8D-AD643A11F598 | NULL |  | NULL | 2025-12-31T19:33:31.6800000 | NULL | False | False | NULL | NULL |
| 00026162-183E-4EFE-9CCE-E03C8A1774E4 | NULL |  | NULL | 2025-11-27T19:26:41.8500000 | NULL | False | False | NULL | NULL |
| 000253D3-5D9F-4604-A974-253DB47BECCD | NULL |  | NULL | 2025-10-12T02:12:21.6730000 | NULL | False | False | NULL | NULL |
| 00024347-B92D-4531-9B52-CFC904473D6B | NULL |  | NULL | 2026-01-09T12:57:17.1670000 | NULL | False | False | NULL | NULL |
| 0001E744-6636-4B7E-B483-75BB06529055 | NULL |  | NULL | 2026-02-11T13:03:07.3770000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0005B696-7E8D-4BD9-841F-B79E07B576D0 | NULL | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | NULL | 2026-03-18T18:00:28.5870000 | NULL | False | False | NULL | NULL |
| 0003C64D-C140-4A12-917F-AA6DD580FB47 | NULL |  | NULL | 2026-02-28T18:11:59.2430000 | NULL | False | False | NULL | NULL |
| 00038118-94B0-4CD2-BFB4-0602B773175F | NULL |  | NULL | 2025-12-24T18:19:18.3770000 | NULL | False | False | NULL | NULL |
| 00032B7B-C6A0-4BF5-A375-A0B281A99F82 | NULL |  | NULL | 2025-12-21T02:01:43.6730000 | NULL | False | False | NULL | NULL |
| 0002C69A-3A90-4870-8CCE-DE9B7953519F | NULL |  | NULL | 2025-11-16T14:15:42.4300000 | NULL | False | False | NULL | NULL |
| 00026EF9-CC16-4C49-AA8D-AD643A11F598 | NULL |  | NULL | 2025-12-31T19:33:31.6800000 | NULL | False | False | NULL | NULL |
| 00026162-183E-4EFE-9CCE-E03C8A1774E4 | NULL |  | NULL | 2025-11-27T19:26:41.8500000 | NULL | False | False | NULL | NULL |
| 000253D3-5D9F-4604-A974-253DB47BECCD | NULL |  | NULL | 2025-10-12T02:12:21.6730000 | NULL | False | False | NULL | NULL |
| 00024347-B92D-4531-9B52-CFC904473D6B | NULL |  | NULL | 2026-01-09T12:57:17.1670000 | NULL | False | False | NULL | NULL |
| 0001E744-6636-4B7E-B483-75BB06529055 | NULL |  | NULL | 2026-02-11T13:03:07.3770000 | NULL | False | False | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Material_Item_Prod_Trn_Tbl.GradeID` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Trn_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
