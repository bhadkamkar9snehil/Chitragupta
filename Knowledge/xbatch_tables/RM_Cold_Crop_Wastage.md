# XStudio_Xbatch.dbo.RM_Cold_Crop_Wastage

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference cut, lastpiecemm, shift, size.

**Primary Key:** ID  
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
| Shift | varchar | YES | 100 | — |
| Size | int | YES | 10,0 | — |
| Cut1mm | decimal | YES | 18,4 | — |
| Cut2mm | decimal | YES | 18,4 | — |
| Cut3mm | decimal | YES | 18,4 | — |
| Cut4mm | decimal | YES | 18,4 | — |
| Cut5mm | decimal | YES | 18,4 | — |
| Cut6mm | decimal | YES | 18,4 | — |
| Cut7mm | decimal | YES | 18,4 | — |
| Cut8mm | decimal | YES | 18,4 | — |
| Cut9mm | decimal | YES | 18,4 | — |
| Cut10mm | decimal | YES | 18,4 | — |
| Lastpiecemm | decimal | YES | 18,4 | — |
| Wt | decimal | YES | 18,4 | — |

---
