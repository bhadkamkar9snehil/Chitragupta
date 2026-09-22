# XStudio_Xbatch.dbo.Transformer_BATTERY_BANK_DG_STATUS_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ecr, auto, man, voltage, oper, pcurrent, pvoltage, wtpdg, aoper, mrssoper, remarks, shift.

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
| ECR1OperPVoltage | decimal | YES | 18,4 | — |
| ECR1OperPCurrent | decimal | YES | 18,4 | — |
| ECR4OperPCurrent | decimal | YES | 18,4 | — |
| ECR4OperPVoltage | decimal | YES | 18,4 | — |
| MRSSOperPVoltage | decimal | YES | 18,4 | — |
| MRSSOperPCurrent | decimal | YES | 18,4 | — |
| ECR5AOperPCurrent | decimal | YES | 18,4 | — |
| ECR5AOperPVoltage | decimal | YES | 18,4 | — |
| DG1Voltage | decimal | YES | 18,4 | — |
| DG1AutoMan | bit | YES | — | — |
| DG2Voltage | decimal | YES | 18,4 | — |
| DG3Voltage | decimal | YES | 18,4 | — |
| DG2AutoMan | bit | YES | — | — |
| DG3AutoMan | bit | YES | — | — |
| WTPDG1Voltage | decimal | YES | 18,4 | — |
| WTPDG1AutoMan | bit | YES | — | — |
| WTPDG2Voltage | decimal | YES | 18,4 | — |
| WTPDG2AutoMan | bit | YES | — | — |
| Remarks | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |

---
