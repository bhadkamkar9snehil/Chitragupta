# XStudio_Xbatch.dbo.SMS_DelayEntry_CAPA

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** delay, oee (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference reason, action, capano, corrective, date, delay, file, proposed, responsibility, stepstorestartmill, target, transactionid.

**Primary Key:** ID  
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
| TargetDate | date | YES | — | — |
| CAPANO | varchar | YES | 100 | — |
| Reason3 | varchar | YES | -1 | — |
| DelayTransactionid | varchar | YES | 36 | — |
| Stepstorestartmill | varchar | YES | -1 | — |
| Reason1 | varchar | YES | -1 | — |
| ProposedAction | varchar | YES | -1 | — |
| Reason4 | varchar | YES | -1 | — |
| CorrectiveAction | varchar | YES | -1 | — |
| File | varchar | YES | 8000 | — |
| Reason5 | varchar | YES | -1 | — |
| Reason2 | varchar | YES | -1 | — |
| Responsibility | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SMS_DelayEntry_CAPA.DelayTransactionid` -> `XStudio_XBatch.ShiftDelayEntry.ID` (Many to One)
- `XStudio_XBatch.SMS_DelayEntry_CAPA.Responsibility` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
