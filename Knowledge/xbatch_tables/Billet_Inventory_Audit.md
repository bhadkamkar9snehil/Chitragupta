# XStudio_Xbatch.dbo.Billet_Inventory_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference grade, location, number, date, material, qty, allocated, assigned, available, bomid, crosssection, description.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
**Row Count:** 0  

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

---
