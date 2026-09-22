# XStudio_Xbatch.dbo.Transformer_Capacitor_Bank_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ecr, kvarstatus, shift.

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
| ECR1800KVARStatus | bit | YES | — | — |
| ECR1400KVARStatus | bit | YES | — | — |
| ECR1400KVARStatusPF | decimal | YES | 18,4 | — |
| ECR1800KVARStatusPF | decimal | YES | 18,4 | — |
| ECR21000KVARStatus | bit | YES | — | — |
| ECR21000KVARStatusPF | decimal | YES | 18,4 | — |
| ECR41000KVARStatus | bit | YES | — | — |
| ECR41000KVARStatusPF | decimal | YES | 18,4 | — |
| ECR2A1000KVARStatusPF | decimal | YES | 18,4 | — |
| ECR2A1000KVARStatus | bit | YES | — | — |
| ECR3300KVARStatusPF | decimal | YES | 18,4 | — |
| ECR3A800KVARStatusPF | decimal | YES | 18,4 | — |
| ECR3300KVARStatus | bit | YES | — | — |
| ECR3A800KVARStatus | bit | YES | — | — |
| ECR4A1000KVARStatus | bit | YES | — | — |
| ECR4A1000KVARStatusPF | decimal | YES | 18,4 | — |

---
