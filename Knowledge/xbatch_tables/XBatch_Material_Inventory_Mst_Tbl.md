# XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference location, date, billet, number, plant, type, grade, inward, material, name, outward, price.

**Primary Key:** ID  
**Row Count:** 2,046  
**Date Range (ModifiedOn):** 2026-01-06T12:43:59.0000000 to 2026-07-30T01:40:23.0700000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| ParentID | varchar | NO | 36 | — |
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
| Quantity | decimal | NO | 18,2 | — |
| UOMID | varchar | NO | 36 | — |
| LocationType | varchar | YES | 100 | — |
| LocationID | varchar | YES | 36 | — |
| LocationName | varchar | YES | 100 | — |
| IsExpired | bit | YES | — | — |
| ExpiryDate | date | YES | — | — |
| ReceivedDate | datetime | YES | — | — |
| Vendor | varchar | YES | 100 | — |
| PONumber | varchar | YES | 100 | — |
| GRNNumber | varchar | YES | 100 | — |
| InvoiceNumber | varchar | YES | 100 | — |
| Price | decimal | YES | 18,8 | — |
| Description | varchar | YES | 1000 | — |
| OperationID | varchar | YES | 36 | — |
| ItemSource | varchar | YES | 50 | — |
| Remark | varchar | YES | 1000 | — |
| LotwiseBillet | varchar | YES | 100 | — |
| SrNo | varchar | YES | 100 | — |
| MaterialGrade | varchar | YES | 100 | — |
| AvailableQuantityPrice | decimal | YES | 18,4 | — |
| BilletReceivedBy | varchar | YES | 100 | — |
| StackLocation | varchar | YES | 100 | — |
| InwardDate | datetime | YES | — | — |
| InwardBy | varchar | YES | 36 | — |
| MovementType | varchar | YES | 100 | — |
| OutwardLocation | varchar | YES | 36 | — |
| Outwardby | varchar | YES | 36 | — |
| OutwardDate | datetime | YES | — | — |
| GradeID | varchar | YES | 50 | — |
| outwardremarks | varchar | YES | -1 | — |
| Color | varchar | YES | 100 | — |
| LayerNo | varchar | YES | 100 | — |
| BilletLength | int | YES | 10,0 | — |
| PlantName | varchar | YES | 36 | — |
| StorageLocation | varchar | YES | 36 | — |
| IsPlantToPlantTransfer | bit | YES | — | — |
| QuantityinCount | int | YES | 10,0 | — |
| PostingMaterialType | varchar | YES | 100 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00B3D3F3-4E8F-4D1B-84CE-BFEF39B3A261 | 7EAD0236-546E-4793-9454-FE721DFAACEC | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-07T08:00:27.1130000 | NULL | False | False | NULL | NULL |
| 008E878C-2397-4575-BA26-3D06E4529087 | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-01T09:31:48.0800000 | NULL | False | False | NULL | NULL |
| 008A2044-6FCD-4017-ACC7-6DFDAE56F2E6 | 7EAD0236-546E-4793-9454-FE721DFAACEC | NULL | NULL | 2026-06-27T14:26:13.7830000 | NULL | False | False | NULL | NULL |
| 007F94A7-5D02-4809-8F89-A2F0409AF352 | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-11T16:11:47.4030000 | NULL | False | False | NULL | NULL |
| 007D0B4F-CBB7-4526-A7ED-B07CAA4EA446 | 7EAD0236-546E-4793-9454-FE721DFAACEC | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-07-02T11:34:05.7700000 | NULL | False | False | NULL | NULL |
| 006634F9-FA5A-436B-AC79-E07095BE8E18 | DF156813-F1E8-427B-989F-D9834DE13B8E | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-26T20:20:30.6770000 | NULL | False | False | NULL | NULL |
| 0060EE2D-DC87-4915-AEC5-B9A7A2A3747D | 7EAD0236-546E-4793-9454-FE721DFAACEC | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-02T09:46:32.5870000 | NULL | False | False | NULL | NULL |
| 005E3967-34BA-4479-9A13-05650A6DEFD0 | DF156813-F1E8-427B-989F-D9834DE13B8E | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-29T05:35:26.8170000 | NULL | False | False | NULL | NULL |
| 0043E0EC-13BE-4E98-8378-BB25D25FD9C7 | 7EAD0236-546E-4793-9454-FE721DFAACEC | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-03T20:49:49.3530000 | NULL | False | False | NULL | NULL |
| 00201B9D-DB52-4E7A-9CA5-F963589FC025 | 9EAADBD5-E037-4BA4-BA9A-0C7388295644 | 1CCC2FD3-7917-41ED-B570-39440703F6CC | NULL | 2026-06-15T00:47:52.2630000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2A642473-94AD-4034-96B7-5EAC9838E6B4 | 3D1481E6-2DAE-45F2-BAF3-849C4D126C1D | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2026-01-06T14:03:34.3100000 | 2026-07-30T01:40:23.0700000 | False | False | NULL | 172.16.3.201 |
| 7876493E-17B6-482F-AF53-0EA8EB07AEC6 | 2598E7D9-E86D-43D4-888E-B3371841CF30 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2026-01-06T14:04:14.3300000 | 2026-07-30T01:40:23.0700000 | False | False | NULL | 172.16.3.201 |
| B7572D2D-3AFD-4A3D-9B3F-0C66B9FC6DF6 | 623C1A28-8F7B-411B-8187-2A20854182DB | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:42:14.5430000 | 2026-07-30T01:40:23.0700000 | False | False | NULL |  |
| C138A7A9-8E63-4476-A408-FCF870F28C24 | 83528728-8810-43DB-A13B-EE9CBDF72FC7 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:41:07.9230000 | 2026-07-30T01:40:23.0700000 | False | False | NULL |  |
| 8CBD6BBE-4581-4937-A07A-8B0DCDE881F3 | 0924E17A-FCBB-46BA-9CEB-FA718C19773D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-29T14:27:53.8300000 | 2026-07-29T14:27:53.0000000 | False | False | NULL | 100.110.123.120 |
| 66EF70AC-FF13-4AF5-B6D7-7BBE5A1A707C | 466154FE-4E29-4BBC-97D0-D73812E0DC6E | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-29T14:26:42.4570000 | 2026-07-29T14:26:42.0000000 | False | False | NULL | 100.110.123.120 |
| EF326D8C-07CF-4758-A9BF-67CBC9C1F8FB | 4617BA9E-2211-49B7-8AD1-A9CB138344BF | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T13:39:53.6570000 | 2026-07-28T14:20:31.0000000 | False | False | NULL |  |
| 17E2C759-0A33-4C2C-BDA7-4F4437F85691 | BA3AA53B-D072-47D0-87FD-F414DE15918A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-06T11:12:11.8230000 | 2026-07-18T11:23:43.5230000 | False | False | NULL | 100.110.190.241 |
| 22742E1E-129A-4773-803E-84899FE1CA8C | 438AD51B-27AD-4873-8942-E93D80CF79EF | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-06T11:08:40.8730000 | 2026-07-18T11:23:43.5230000 | False | False | NULL | 100.110.190.241 |
| B008F8C1-F4EB-46DB-BD9D-E6C1ADBDEE03 | 2979D331-03C3-460D-9ED3-10A4C8757365 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-06T11:11:11.3630000 | 2026-07-18T11:23:43.5230000 | False | False | NULL | 100.110.190.241 |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Billets_Transfer_History_Tbl.InventoryID` -> `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.GradeID` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.InwardBy` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.LocationID` -> `XStudio_XBatch.XBatch_Storage_Rack_Mst_Tbl.ID` (Many to Many)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.MaterialGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.OperationID` -> `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.Outwardby` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.OutwardLocation` -> `XStudio_XBatch.XBatch_OutwardLocation_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.PlantName` -> `XStudio_XBatch.Plant_Name_MST.Plant` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.StorageLocation` -> `XStudio_XBatch.Storage_Location_MST.StorageLocation` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.HeatNo` -> `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.ID` (Many to One)
