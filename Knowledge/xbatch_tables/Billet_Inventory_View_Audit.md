# XStudio_Xbatch.dbo.Billet_Inventory_View_Audit

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

---
