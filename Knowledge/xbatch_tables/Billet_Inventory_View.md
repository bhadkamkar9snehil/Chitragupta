# XStudio_Xbatch.dbo.Billet_Inventory_View

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference grade, location, number, date, material, qty, allocated, assigned, available, bomid, crosssection, description.

**Primary Key:** ID  
**Row Count:** 220  
**Date Range (ModifiedOn):** 2025-07-09T10:42:06.0000000 to 2025-07-09T10:42:06.0000000  

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
| LocationID | varchar | YES | 36 | — |
| Remark | varchar | YES | 100 | — |
| LocationName | varchar | YES | 100 | — |
| Height | int | YES | 10,0 | — |
| BOMid | varchar | YES | 36 | — |
| Price | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 100 | — |
| PONumber | varchar | YES | 100 | — |
| InvoiceNumber | varchar | YES | 100 | — |
| Description | varchar | YES | 100 | — |
| IsAvailable | varchar | YES | 100 | — |
| ItemSource | varchar | YES | 100 | — |
| MaterialID | varchar | YES | 36 | — |
| Length | int | YES | 10,0 | — |
| ExpiryDate | date | YES | — | — |
| Vendor | varchar | YES | 100 | — |
| Quantity | decimal | YES | 18,4 | — |
| LocationType | varchar | YES | 100 | — |
| SublotNumber | varchar | YES | 100 | — |
| AssignedQty | decimal | YES | 18,4 | — |
| UOMID | varchar | YES | 36 | — |
| GradeID | varchar | YES | 36 | — |
| ParentID | varchar | YES | 36 | — |
| IsAllocated | varchar | YES | 100 | — |
| GRNNumber | varchar | YES | 100 | — |
| Crosssection | varchar | YES | 100 | — |
| ReceivedDate | datetime | YES | — | — |
| LotNumber | varchar | YES | 100 | — |
| TotalQty | int | YES | 10,0 | — |
| OperationID | varchar | YES | 36 | — |
| IsExpired | bit | YES | — | — |
| Status | varchar | YES | 100 | — |
| MaterialGrade | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 078AF998-89FD-41B5-8AD3-8A3E17E65B76 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.6170000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 05DF86FF-03B8-410C-9A55-FBF8D58F3845 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.3100000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 0532B496-279A-4396-A973-70465B7A7D73 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.3470000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 0166A4C6-CAFD-4578-ACE4-F6C1B0B971E9 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.5130000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 0125ABB2-79AE-4F25-B5F9-F37A98E5CD2D | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.3630000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 0F023CFC-EF3D-4764-9D5A-71EBDC49910B | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.6130000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 0D0E3F11-CB50-4F96-9D36-07A94ADC073C | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.3530000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 0C88DD70-C0C7-41C6-844F-11BF70DA0704 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.7030000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 0803CF76-9910-41F2-BF84-F3ED3067A349 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.1200000 | NULL | False | False | NULL | 10.2.6.54 |  |
| 10060AC8-95B5-4F59-B069-9EF6D01A778C | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-07-09T10:42:07.3700000 | NULL | False | False | NULL | 10.2.6.54 |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 07D8D423-B09D-413E-8A08-EAC9610179A5 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.9130000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 0A5B79F9-8388-4243-81EF-3501354C9C04 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.8800000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 0F1F6309-D3AB-4E34-BAB8-C12807032FEA | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.4600000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 101D16A9-B8E9-43C1-A8FA-ED61D6715FBF | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.5000000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 27106837-F211-40AA-A623-1A023A31C0D2 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.4900000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 412E21AF-A297-41CF-B575-A3238FE54878 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.5400000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 4BC99EC0-8A5A-4D19-A7F2-13A6D45FE91D | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.8600000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 54ACDD77-713D-417D-B8FB-CA50ECC50673 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.4730000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 5DABAA2D-5CA7-4844-9081-7CF19F80911B | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.5700000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |
| 61FC1B41-D747-498E-95F3-225B3D86B65F | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T10:45:32.5170000 | 2025-07-09T10:42:06.0000000 | False | False | NULL | 10.2.6.54 |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Billet_Inventory_View.BOMid` -> `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory_View.GradeID` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory_View.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory_View.OperationID` -> `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory_View.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
