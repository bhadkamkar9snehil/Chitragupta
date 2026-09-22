# XStudio_Xbatch.dbo.XBatch_Material_Item_Cons_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference number, quantity, declare, grade, heat, lot, material, price, sublot, uomid.

**Primary Key:** ID  
**Row Count:** 96,143  
**Date Range (ModifiedOn):** 2026-05-20T18:03:55.5530000 to 2026-07-08T18:04:23.7670000  

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
| LotNumber | varchar | YES | 100 | — |
| SublotNumber | varchar | YES | 100 | — |
| Quantity | decimal | NO | 18,4 | — |
| UOMID | varchar | NO | 36 | — |
| GradeID | varchar | YES | 36 | — |
| MaterialID | varchar | YES | 36 | — |
| HeatNo | int | YES | 10,0 | — |
| Price | decimal | YES | 18,2 | — |
| DeclareQuantity | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0007DEBC-0A74-43E8-8FFC-283F76DD535D | 59800A39-5A5D-4477-89E2-8C94FC61085B | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-02-04T10:05:25.9400000 | NULL | False | False | NULL | NULL |
| 00071885-3634-4624-A98A-0EA3E8AD0206 | EADA1951-EAA7-450F-9EE2-3A5BF1F8CCF0 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-03-15T10:03:40.7630000 | NULL | False | False | NULL | NULL |
| 0006A2FF-EDFA-4729-89F1-0ADA71C36453 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-10-05T13:21:54.9030000 | NULL | False | False | NULL | NULL |
| 0006427C-9BCB-4427-844A-A92793D2EB04 | 2D0E3829-1635-4B93-8206-715527C37818 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-01-31T05:47:40.1370000 | NULL | False | False | NULL | NULL |
| 0005F6B4-F122-4BCB-A48E-E719884379E4 | 971FEE96-B8EA-4247-8D17-975ED69AA1EA | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-05-15T22:03:36.2470000 | NULL | False | False | NULL | NULL |
| 0004BA45-2151-40FE-99BB-6C438EAC1DCA | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-11-21T14:36:19.7500000 | NULL | False | False | NULL | NULL |
| 00038C37-AE30-42D7-8EB0-CB9E8F71F080 | 4CFB0485-5DA7-4A41-AF68-1C823F385256 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-04-10T02:48:23.1400000 | NULL | False | False | NULL | NULL |
| 0002183E-510B-477C-824A-49EE85E14B63 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-11-09T04:50:26.9900000 | NULL | False | False | NULL | NULL |
| 00006070-43C8-49D5-BD09-F6B9457E8AFC | EC0F7FD8-4821-483D-8368-8F4A4C222E88 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-04-08T06:51:12.9100000 | NULL | False | False | NULL | NULL |
| 00005849-B866-456B-9F97-777D667470C9 | NULL |  | NULL | 2026-02-11T12:27:24.4270000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6581D6B1-AB41-4EE0-88EC-BB70D4AFC24E | 6C897D7F-2B8E-4BB0-8235-0A3EDD8CAE4C | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| 724CAB01-3E15-447B-8EC6-11E9418C8E49 | EADA1951-EAA7-450F-9EE2-3A5BF1F8CCF0 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| 775986C8-8502-4193-9E5E-DDFB719E370A | F32E4149-BCE6-4B87-8D12-03A0449EB010 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| 86B60ED5-C6FC-4BA8-B5EB-5ED3E18EFBA1 | E7DDDF6E-F56C-4E38-9462-86114BFD625D | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| 8DDCC117-47BC-41CE-91CD-48ABBD717C4E | 2D0E3829-1635-4B93-8206-715527C37818 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| AA07261D-9069-48B3-826E-50480CE3B2F5 | 3189E856-BAA1-4AC1-92F6-C722D6028AEC | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| D5ADAC48-CED6-438A-911C-2FDB51F7B5ED | 971FEE96-B8EA-4247-8D17-975ED69AA1EA | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| FD7A759A-7779-4BFB-9991-2AE2970063B0 | 38DF1616-9A77-4AF6-A54E-4991BE0A26BC | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T18:04:23.6300000 | 2026-07-08T18:04:23.7670000 | False | False | NULL | NULL |
| 00AB6ADB-1DB8-4B14-9798-895A4219DFFC | 38DF1616-9A77-4AF6-A54E-4991BE0A26BC | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T17:08:10.8130000 | 2026-07-08T17:08:10.9070000 | False | False | NULL | NULL |
| 0577FCFB-3CE0-4F5D-AC25-3A8663A39CFC | 2D0E3829-1635-4B93-8206-715527C37818 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T17:08:10.8130000 | 2026-07-08T17:08:10.9070000 | False | False | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Material_Item_Cons_Trn_Tbl.GradeID` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Trn_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
