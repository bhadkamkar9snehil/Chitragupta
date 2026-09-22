# XStudio_Xbatch.dbo.ShiftDelayEntry_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference delay, name, agency, duration, equipment, other, shift, time, area, cobble, electrical, end.

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
| DelayStartTime | datetime | NO | — | — |
| DelayInMinutes | decimal | YES | 18,2 | — |
| ParentID | varchar | YES | 36 | — |
| DelayEndTime | datetime | NO | — | — |
| DelayReason | varchar | YES | -1 | — |
| DelayType | varchar | YES | 36 | — |
| DelayAgency | varchar | YES | 36 | — |
| AgencyOther | varchar | YES | 100 | — |
| HeatNo | int | YES | 10,0 | — |
| EquipmentName | varchar | YES | -1 | — |
| SubEquipmentName | varchar | YES | 36 | — |
| ReportDate | varchar | YES | 100 | — |
| AreaName | varchar | YES | -1 | — |
| ShiftManager | varchar | YES | 36 | — |
| OperatorName | varchar | YES | 36 | — |
| RMProduct | varchar | YES | 100 | — |
| DelaySubtypeid | varchar | YES | 36 | — |
| DelayInSecond | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |
| RMSection | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| Cobble | int | YES | 10,0 | — |
| Hotout | int | YES | 10,0 | — |
| Refractory | int | YES | 10,0 | — |
| Mechanical | int | YES | 10,0 | — |
| Electrical | int | YES | 10,0 | — |
| Operation | int | YES | 10,0 | — |
| OtherDelay | int | YES | 10,0 | — |
| RemainingDuration | decimal | YES | 18,4 | — |
| DelayDuration | varchar | YES | 100 | — |

---
