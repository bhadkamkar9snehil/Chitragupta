# XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference location, date, billet, number, grade, inward, outward, price, quantity, received, type, available.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
**Row Count:** 155  
**Date Range (ModifiedOn):** 2025-07-03T17:51:02.0000000 to 2025-07-08T12:34:11.0000000  

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
| LotNumber | varchar | NO | 100 | — |
| SublotNumber | varchar | YES | 100 | — |
| Quantity | decimal | NO | 18,4 | — |
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
| Price | decimal | YES | 18,4 | — |
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

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BCD60209-1B45-40CD-A1E6-D75EB2A1389A | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:22:05.7200000 | NULL | False | False | NULL | NULL |
| 96654239-4F7A-4C5A-824F-40AC157281F4 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:24:00.8530000 | NULL | False | False | NULL | NULL |
| B9F659C6-361F-493B-B834-F79D52AE7C7E | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:24:00.8530000 | NULL | False | False | NULL | NULL |
| 305312F3-2372-4716-9534-0AE457753B8D | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:24:00.8530000 | NULL | False | False | NULL | NULL |
| 3633764A-A704-402B-A6D1-552C3F4618B5 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:24:00.8530000 | NULL | False | False | NULL | NULL |
| 08C25410-9CF8-492B-A98A-644F3356944B | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:24:00.8530000 | NULL | False | False | NULL | NULL |
| 49A6BA46-5FA4-49C7-8991-5D480797BFB7 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:24:00.8530000 | NULL | False | False | NULL | NULL |
| 0A5F7D55-A16D-48E3-A3AD-DD045A1FDF50 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | NULL | 2025-07-08T10:24:00.8530000 | NULL | False | False | NULL | NULL |
| 71AFD3D3-0BC3-4B0D-A679-493C3015496F | BBAFDCB6-BC99-4D80-81AB-7610EC6EDF6C | NULL | NULL | 2025-07-08T17:08:43.2970000 | NULL | False | False | NULL | NULL |
| 002E5014-4D8D-4132-9FDF-002D80CC775F | BBAFDCB6-BC99-4D80-81AB-7610EC6EDF6C | NULL | NULL | 2025-07-08T17:08:43.0930000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7EB0BBD7-61CA-4C61-8D5E-41A2834D8FC8 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T10:22:05.7200000 | 2025-07-08T12:34:11.0000000 | False | False | NULL | 10.2.6.54 |
| 3227F1F5-EF28-4F03-AC40-89EF7F945BE9 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T12:45:12.0930000 | 2025-07-08T12:32:17.0000000 | False | False | NULL | 10.2.6.54 |
| 3227F1F5-EF28-4F03-AC40-89EF7F945BE9 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T12:45:12.0930000 | 2025-07-08T12:30:02.0000000 | False | False | NULL | 10.2.6.54 |
| 3227F1F5-EF28-4F03-AC40-89EF7F945BE9 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T12:45:12.0930000 | 2025-07-08T12:26:32.0000000 | False | False | NULL | 10.2.6.54 |
| 3227F1F5-EF28-4F03-AC40-89EF7F945BE9 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T12:45:12.0930000 | 2025-07-08T12:22:48.0000000 | False | False | NULL | 10.2.6.54 |
| 3227F1F5-EF28-4F03-AC40-89EF7F945BE9 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-07T12:45:12.0930000 | 2025-07-08T12:21:45.0000000 | False | False | NULL | 10.2.6.54 |
| 0A5F7D55-A16D-48E3-A3AD-DD045A1FDF50 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T10:24:00.8530000 | 2025-07-08T10:26:31.0000000 | False | False | NULL | 10.2.6.54 |
| 49A6BA46-5FA4-49C7-8991-5D480797BFB7 | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T10:24:00.8530000 | 2025-07-08T10:26:24.0000000 | False | False | NULL | 10.2.6.54 |
| 35506A07-E969-465C-A719-67D1E15914FF | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T10:24:00.8530000 | 2025-07-08T10:26:12.0000000 | False | False | NULL | 10.2.6.54 |
| 08C25410-9CF8-492B-A98A-644F3356944B | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T10:24:00.8530000 | 2025-07-08T10:26:06.0000000 | False | False | NULL | 10.2.6.54 |

---
