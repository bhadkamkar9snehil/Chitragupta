# XStudio_Xbatch.dbo.RM_Stock_And_Parting_Register_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference partingmm, block, stands, pinch, roll, bottom, finished, remarks, round, sample, shear, side.

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
| Shift | varchar | YES | 100 | — |
| Size | decimal | YES | 18,4 | — |
| Shear3SampleTopOrBottom | int | YES | 10,0 | — |
| Shear3SampleSide | int | YES | 10,0 | — |
| FinishedRoundTopOrBottom | int | YES | 10,0 | — |
| FinishedRoundSide | int | YES | 10,0 | — |
| PinchRollPartingmmPR0 | decimal | YES | 18,4 | — |
| PinchRollPartingmmPR1 | decimal | YES | 18,4 | — |
| PinchRollPartingmmPR2 | decimal | YES | 18,4 | — |
| PinchRollPartingmmPR3 | decimal | YES | 18,4 | — |
| PinchRollPartingmmPR4 | decimal | YES | 18,4 | — |
| PinchRollPartingmmRemarks | varchar | YES | 100 | — |
| BlockStandsPartingmm19 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm20 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm21 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm22 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm23 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm24 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm25 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm26 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm27 | decimal | YES | 18,4 | — |
| BlockStandsPartingmm28 | decimal | YES | 18,4 | — |
| BlockStandsPartingmmRemarks | varchar | YES | 100 | — |

---
