# XStudio_Xbatch.dbo.Billet_Inventory

**table_kind:** production_data

### What this table is for

- **Curated domain match (billet_inventory):** Billet missing, wrong location/furnace/yard/transfer, genealogy, count, or weight issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** billet, core, cross, domain, identifier, inventory, routing, yard (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference location, grade, number, date, material, qty, allocated, assigned, available, bomid, crosssection, description.

**Primary Key:** ID  
**Row Count:** 142  
**Date Range (ModifiedOn):** 2025-07-04T09:43:56.0000000 to 2025-07-04T14:11:31.0000000  

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
| Description | varchar | YES | 100 | — |
| ExpiryDate | date | YES | — | — |
| GradeID | varchar | YES | 36 | — |
| GRNNumber | varchar | YES | 100 | — |
| InvoiceNumber | varchar | YES | 100 | — |
| IsExpired | bit | YES | — | — |
| ItemSource | varchar | YES | 100 | — |
| LocationID | varchar | YES | 36 | — |
| LocationName | varchar | YES | 100 | — |
| LocationType | varchar | YES | 100 | — |
| LotNumber | varchar | YES | 100 | — |
| OperationID | varchar | YES | 36 | — |
| PONumber | varchar | YES | 100 | — |
| Price | decimal | YES | 18,4 | — |
| Quantity | decimal | YES | 18,4 | — |
| ReceivedDate | datetime | YES | — | — |
| Remark | varchar | YES | 100 | — |
| SublotNumber | varchar | YES | 100 | — |
| UOMID | varchar | YES | 36 | — |
| Vendor | varchar | YES | 100 | — |
| Height | int | YES | 10,0 | — |
| Length | int | YES | 10,0 | — |
| Crosssection | varchar | YES | 100 | — |
| MaterialID | varchar | YES | 36 | — |
| Grade | varchar | YES | 100 | — |
| IsAllocated | varchar | YES | 100 | — |
| IsAvailable | varchar | YES | 100 | — |
| TotalQty | int | YES | 10,0 | — |
| BOMid | varchar | YES | -1 | — |
| AssignedQty | decimal | YES | 18,4 | — |
| MaterialGrade | varchar | YES | 100 | — |
| Plant | varchar | YES | 100 | — |
| StorageLocation | varchar | YES | 100 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 099D1B24-D36E-4908-B947-65F5227DAFC6 | NULL | NULL | NULL | 2025-07-07T11:54:21.9270000 | NULL | False | False | NULL | NULL |
| 05782158-B5B2-4D72-8EF1-FC536CE8FCDE | NULL | NULL | NULL | 2025-07-04T12:32:20.8770000 | NULL | False | False | NULL | NULL |
| 040197D3-B754-4A2C-8790-E1C95B93FED8 | NULL | NULL | NULL | 2025-07-04T12:41:14.8970000 | NULL | False | False | NULL | NULL |
| 03714AA3-5F1A-4699-9880-6C9B5DF6491F | NULL | NULL | NULL | 2025-07-04T12:40:17.6700000 | NULL | False | False | NULL | NULL |
| 030C69AB-BA6A-4869-8E4E-98875C5691CB | NULL | NULL | NULL | 2025-07-04T12:50:32.2370000 | NULL | False | False | NULL | NULL |
| 0204A31E-5D82-48C8-A701-0D8E2C039E53 | NULL | NULL | NULL | 2025-07-09T16:58:21.6530000 | NULL | False | False | NULL | NULL |
| 004E82B1-3734-432D-819F-DDFF8831D8EE | NULL | NULL | NULL | 2025-07-07T12:47:10.3600000 | NULL | False | False | NULL | NULL |
| 0E7882CB-EB7D-4841-8DFC-7A03F0ABF021 | NULL | NULL | NULL | 2025-07-03T18:06:17.7100000 | NULL | False | False | NULL | NULL |
| 0C42327D-1C28-4CFC-A378-D17B4A5088C2 | NULL | NULL | NULL | 2025-07-05T09:51:23.9330000 | NULL | False | False | NULL | NULL |
| 0C3EBE4F-526F-439B-8AC1-3C4B0CEFD9A5 | NULL | NULL | NULL | 2025-07-04T12:10:51.4430000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5C97708E-6C4E-4624-967C-6CE734937390 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-04T11:14:01.5470000 | 2025-07-04T14:11:31.0000000 | False | False | NULL |  |
| CABE69DC-C125-4D73-8F32-829DB9C1635C | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-04T12:44:38.3900000 | 2025-07-04T13:01:36.3100000 | True | False | NULL | NULL |
| 3789C6A3-185B-4D1B-BCC1-9F04C82B8333 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-04T11:19:25.6900000 | 2025-07-04T11:54:55.0000000 | False | False | NULL |  |
| 69754B89-434C-4074-B9BB-3109DDA59621 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-04T11:04:30.4730000 | 2025-07-04T11:54:40.0000000 | False | False | NULL |  |
| A45F2622-EF3F-43E9-9CA7-977E6C9208DD | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-03T17:59:22.5800000 | 2025-07-04T10:49:55.0000000 | False | False | NULL |  |
| 09AB765B-8EED-4AC0-A64D-7D5F64E9D5B1 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-03T18:02:44.2070000 | 2025-07-04T09:44:19.0000000 | False | False | NULL | 10.2.8.74 |
| EFB1E255-2627-474D-B276-F7337EDE536C | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-03T17:51:03.6500000 | 2025-07-04T09:43:56.0000000 | False | False | NULL | 10.2.8.74 |
| 0E7882CB-EB7D-4841-8DFC-7A03F0ABF021 | NULL | NULL | NULL | 2025-07-03T18:06:17.7100000 | NULL | False | False | NULL | NULL |
| 0C42327D-1C28-4CFC-A378-D17B4A5088C2 | NULL | NULL | NULL | 2025-07-05T09:51:23.9330000 | NULL | False | False | NULL | NULL |
| 0C3EBE4F-526F-439B-8AC1-3C4B0CEFD9A5 | NULL | NULL | NULL | 2025-07-04T12:10:51.4430000 | NULL | False | False | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Billet_Inventory.BOMid` -> `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory.GradeID` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory.OperationID` -> `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
