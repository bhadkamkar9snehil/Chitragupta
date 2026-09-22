# XStudio_Xbatch.dbo.Xbatch_Material_Inventory_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference material, quantity, billet, count, external, grade, ismodified, location, lot, name, number, plant.

**Primary Key:** ID  
**Row Count:** 1,300  
**Date Range (ModifiedOn):** 2026-07-18T11:23:43.6070000 to 2026-07-18T11:23:43.6070000  

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
| MaterialGrade | varchar | YES | 100 | — |
| PostingMaterialType | varchar | YES | 100 | — |
| PlantName | varchar | YES | 36 | — |
| ParentID | varchar | NO | 36 | — |
| Quantity | decimal | NO | 18,3 | — |
| StorageLocation | varchar | YES | 36 | — |
| QuantityinCount | int | YES | 10,0 | — |
| UOMID | varchar | NO | 36 | — |
| LotNumber | varchar | NO | 100 | — |
| Ismodified | bit | YES | — | — |
| BilletNo | varchar | YES | 100 | — |
| isExternal | bit | YES | — | — |
| TotalQuantity | decimal | YES | 18,3 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00602046-61B7-44A1-AAFF-8A088E28A5BF | NULL | NULL | 2026-08-23T09:25:09.3000000 | NULL | False | False | NULL | NULL | NULL |
| 005CC3B3-D6E0-4D3A-85D6-142A0EF33701 | NULL | NULL | 2026-08-08T09:42:23.3070000 | NULL | False | False | NULL | NULL | NULL |
| 01D0A93D-44AF-431F-9E5A-25BE512EA51E | NULL | NULL | 2026-08-13T09:25:13.0100000 | NULL | False | False | NULL | NULL | NULL |
| 01B23CA4-2C00-4DFC-A515-E24F715B59B7 | NULL | NULL | 2026-08-24T08:50:22.8530000 | NULL | False | False | NULL | NULL | NULL |
| 01A6CC82-BD8B-4B36-A972-6F18653215C3 | NULL | NULL | 2026-08-31T09:25:06.9930000 | NULL | False | False | NULL | NULL | NULL |
| 01829A83-7388-4CD2-BC6E-AE8772E56AE0 | NULL | NULL | 2026-08-24T16:41:15.3030000 | NULL | False | False | NULL | NULL | NULL |
| 01441C9D-16B2-43E7-81F9-F9E005559AF5 | NULL | NULL | 2026-08-07T11:23:20.3430000 | NULL | False | False | NULL | NULL | NULL |
| 01004E03-533D-47E6-9C8C-0006266FB43B | NULL | NULL | 2026-08-24T18:12:35.1930000 | NULL | False | False | NULL | NULL | NULL |
| 00FC0E8E-DF61-41A8-A522-82F43A4DF40D | NULL | NULL | 2026-08-24T16:03:14.2300000 | NULL | False | False | NULL | NULL | NULL |
| 00E0C7B2-9E32-4AE1-8FEF-F6F9BDCEF36B | NULL | NULL | 2026-08-19T20:39:31.9530000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00A57608-9ECC-49D2-8F58-F5BA7D332351 | NULL | NULL | 2026-07-08T23:43:08.6200000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 0498C01C-1248-4399-B463-2C0EB0CC6547 | NULL | NULL | 2026-07-07T01:09:31.5870000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 04F87EC8-D3AD-4D73-93CC-2596D9DBD6BB | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-07T11:32:44.3270000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 05FE156F-BC46-4C05-9CDF-E4C56C84CA2D | NULL | NULL | 2026-07-07T17:38:46.0530000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 06FDFF36-2AB6-4CCF-9D44-9280A6DD497B | NULL | NULL | 2026-07-08T11:31:56.3300000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 07446936-A5AC-439A-9C1C-F620177F033B | NULL | NULL | 2026-07-08T06:03:00.1730000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 09C0C989-BCE4-4C08-90E1-F75BAEF6F975 | NULL | NULL | 2026-07-07T22:47:35.1470000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 09CC9D70-8544-4815-892A-842BCA678256 | NULL | NULL | 2026-07-08T11:43:47.2330000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 0A05679B-3A69-4B7B-849C-0F07F0639319 | NULL | NULL | 2026-07-07T13:08:00.8970000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 0AD28BB2-D0B7-4FF4-A421-D0A73241AB37 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-07T10:37:46.6900000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.MaterialGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.PlantName` -> `XStudio_XBatch.Plant_Name_MST.Plant` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.StorageLocation` -> `XStudio_XBatch.Storage_Location_MST.StorageLocation` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
