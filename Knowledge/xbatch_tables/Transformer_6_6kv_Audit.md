# XStudio_Xbatch.dbo.Transformer_6_6kv_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ecr, tra, mvapcurrent, mvascurrent, level, status, mvabreather, mvaoil, mvaoti, mvawti, amvapcurrent, amvascurrent.

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
| ECR1Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR1Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR1Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR1Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR1Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR1Tra3MVABreatherStatus | bit | YES | — | — |
| ECR1Tra16MVAOTI | decimal | YES | 18,4 | — |
| ECR1Tra16MVAWTI | decimal | YES | 18,4 | — |
| ECR1Tra16MVAOilLevel | decimal | YES | 18,4 | — |
| ECR1Tra16MVABreatherStatus | bit | YES | — | — |
| ECR1Tra16MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra16MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra16MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR1Tra16MVASCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra16MVASCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra16MVASCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR2Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR2Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR2Tra3MVABreatherStatus | bit | YES | — | — |
| ECR2Tra4MVAOTI | decimal | YES | 18,4 | — |
| ECR2Tra4MVAWTI | decimal | YES | 18,4 | — |
| ECR2Tra4MVAOilLevel | decimal | YES | 18,4 | — |
| ECR2Tra4MVABreatherStatus | bit | YES | — | — |
| ECR2Tra4MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra4MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra4MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra4MVASCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra4MVASCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra4MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR3Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR3Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR3Tra3MVABreatherStatus | bit | YES | — | — |
| ECR3Tra1MVAOTI | decimal | YES | 18,4 | — |
| ECR3Tra1MVAWTI | decimal | YES | 18,4 | — |
| ECR3Tra1MVAOilLevel | decimal | YES | 18,4 | — |
| ECR3Tra1MVABreatherStatus | bit | YES | — | — |
| ECR3Tra1MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra1MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra1MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra1MVASCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra1MVASCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra1MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR3TraBF12MVASCurrentR | decimal | YES | 18,4 | — |
| ECR3TraBF12MVASCurrentY | decimal | YES | 18,4 | — |
| ECR3TraBF12MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAOTI | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAWTI | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAOilLevel | decimal | YES | 18,4 | — |
| ECR3TraBF12MVABreatherStatus | bit | YES | — | — |
| ECR4Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR4Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR4Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR4Tra3MVABreatherStatus | bit | YES | — | — |
| ECR4Tra3AMVAPCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAPCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAPCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3AMVASCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3AMVASCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3AMVASCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAOTI | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAWTI | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAOilLevel | decimal | YES | 18,4 | — |
| ECR4Tra3AMVABreatherStatus | bit | YES | — | — |
| Attendants | varchar | YES | 36 | — |
| Remarks | varchar | YES | -1 | — |
| Shift | varchar | YES | 100 | — |

---
