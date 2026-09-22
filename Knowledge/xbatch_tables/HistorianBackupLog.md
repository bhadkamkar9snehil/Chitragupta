# XStudio_Xbatch.dbo.HistorianBackupLog

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** historian (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference backup, log, date, database, name, notes, path, run, success.

**Primary Key:** LogID  
**Row Count:** 270  
**Date Range (BackupRunDate):** 2025-12-04T03:30:01.6600000 to 2026-09-02T03:30:01.4030000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| LogID | int | NO | 10,0 | — |
| DatabaseName | nvarchar | NO | 255 | — |
| BackupRunDate | datetime | NO | — | (getdate()) |
| BackupPath | nvarchar | YES | 2000 | — |
| Success | bit | NO | — | ((1)) |
| Notes | nvarchar | YES | 1000 | — |
| BackupDate | date | YES | — | — |

### Top 10 Records

| LogID | DatabaseName | BackupRunDate | BackupPath | Success | Notes | BackupDate |
| --- | --- | --- | --- | --- | --- | --- |
| 23 | XHS_History_25120303 | 2025-12-04T03:30:01.6600000 | F:\Database Backup\Historian Full Backup\XHS_History_25120303.BAK | True | Backup OK | 2025-12-04T00:00:00.0000000 |
| 24 | XHS_History_25120404 | 2025-12-05T03:30:01.3700000 | F:\Database Backup\Historian Full Backup\XHS_History_25120404.BAK | True | Backup OK | 2025-12-05T00:00:00.0000000 |
| 25 | XHS_History_25120505 | 2025-12-06T03:30:01.6770000 | F:\Database Backup\Historian Full Backup\XHS_History_25120505.BAK | True | Backup OK | 2025-12-06T00:00:00.0000000 |
| 26 | XHS_History_25120606 | 2025-12-07T03:30:01.7000000 | F:\Database Backup\Historian Full Backup\XHS_History_25120606.BAK | True | Backup OK | 2025-12-07T00:00:00.0000000 |
| 27 | XHS_History_25120707 | 2025-12-08T03:30:01.4600000 | F:\Database Backup\Historian Full Backup\XHS_History_25120707.BAK | True | Backup OK | 2025-12-08T00:00:00.0000000 |
| 28 | XHS_History_25120808 | 2025-12-09T03:30:01.7130000 | F:\Database Backup\Historian Full Backup\XHS_History_25120808.BAK | True | Backup OK | 2025-12-09T00:00:00.0000000 |
| 29 | XHS_History_25120909 | 2025-12-10T03:30:02.1400000 | F:\Database Backup\Historian Full Backup\XHS_History_25120909.BAK | True | Backup OK | 2025-12-10T00:00:00.0000000 |
| 30 | XHS_History_25121010 | 2025-12-11T03:30:01.3870000 | F:\Database Backup\Historian Full Backup\XHS_History_25121010.BAK | True | Backup OK | 2025-12-11T00:00:00.0000000 |
| 31 | XHS_History_25121111 | 2025-12-12T03:30:05.5970000 | F:\Database Backup\Historian Full Backup\XHS_History_25121111.BAK | True | Backup OK | 2025-12-12T00:00:00.0000000 |
| 32 | XHS_History_25121212 | 2025-12-13T03:30:01.7700000 | F:\Database Backup\Historian Full Backup\XHS_History_25121212.BAK | True | Backup OK | 2025-12-13T00:00:00.0000000 |

### Bottom 10 Records

| LogID | DatabaseName | BackupRunDate | BackupPath | Success | Notes | BackupDate |
| --- | --- | --- | --- | --- | --- | --- |
| 292 | XHS_History_26090101 | 2026-09-02T03:30:01.4030000 | F:\Database Backup\Historian Full Backup\XHS_History_26090101.BAK | True | Backup OK | 2026-09-02T00:00:00.0000000 |
| 291 | XHS_History_26083131 | 2026-09-01T03:30:01.3170000 | F:\Database Backup\Historian Full Backup\XHS_History_26083131.BAK | True | Backup OK | 2026-09-01T00:00:00.0000000 |
| 290 | XHS_History_26083030 | 2026-08-31T03:30:02.1470000 | F:\Database Backup\Historian Full Backup\XHS_History_26083030.BAK | True | Backup OK | 2026-08-31T00:00:00.0000000 |
| 289 | XHS_History_26082929 | 2026-08-30T03:30:02.1870000 | F:\Database Backup\Historian Full Backup\XHS_History_26082929.BAK | True | Backup OK | 2026-08-30T00:00:00.0000000 |
| 288 | XHS_History_26082828 | 2026-08-29T03:30:01.9030000 | F:\Database Backup\Historian Full Backup\XHS_History_26082828.BAK | True | Backup OK | 2026-08-29T00:00:00.0000000 |
| 287 | XHS_History_26082727 | 2026-08-28T03:30:02.2500000 | F:\Database Backup\Historian Full Backup\XHS_History_26082727.BAK | True | Backup OK | 2026-08-28T00:00:00.0000000 |
| 286 | XHS_History_26082626 | 2026-08-27T03:30:01.7370000 | F:\Database Backup\Historian Full Backup\XHS_History_26082626.BAK | True | Backup OK | 2026-08-27T00:00:00.0000000 |
| 285 | XHS_History_26082525 | 2026-08-26T03:30:02.1270000 | F:\Database Backup\Historian Full Backup\XHS_History_26082525.BAK | True | Backup OK | 2026-08-26T00:00:00.0000000 |
| 284 | XHS_History_26082424 | 2026-08-25T03:30:02.3970000 | F:\Database Backup\Historian Full Backup\XHS_History_26082424.BAK | True | Backup OK | 2026-08-25T00:00:00.0000000 |
| 283 | XHS_History_26082323 | 2026-08-24T03:30:01.8200000 | F:\Database Backup\Historian Full Backup\XHS_History_26082323.BAK | True | Backup OK | 2026-08-24T00:00:00.0000000 |

---
