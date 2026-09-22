# XStudio_Xbatch.dbo.RM_Rolling_Standards_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference openingmm, gap, roll, roller, sizemm, stabilizer, static, bottom, delivery, entry, feelermm, guide.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
**Row Count:** 0  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| StandNo | int | YES | 10,0 | — |
| TypeOfPass | varchar | YES | 100 | — |
| Sizemm | decimal | YES | 18,4 | — |
| RollGapFeelermm | decimal | YES | 18,4 | — |
| RollGapRodmm | decimal | YES | 18,4 | — |
| StaticGuideOpeningmm | decimal | YES | 18,4 | — |
| EntryRollerOpening | decimal | YES | 18,4 | — |
| StabilizerStaticOpeningmm | decimal | YES | 18,4 | — |
| StabilizerRollerOpeningmm | decimal | YES | 18,4 | — |
| DeliveryPipeOpeningmm | decimal | YES | 18,4 | — |
| TwisterOpeningmm | decimal | YES | 18,4 | — |
| TopToBottomSizemm | decimal | YES | 18,4 | — |

---
