---
type: table
title: "HistorianBackupLog"
built: "2026-09-24T11:36:36"
---

# HistorianBackupLog

Table in XStudio_Xbatch. Rows: 270.

## Written by

- sp_All_Historian_DB_Full_Backup

## Read by

- sp_All_Historian_DB_Full_Backup

## Columns

- LogID int
- DatabaseName nvarchar(510)
- BackupRunDate datetime
- BackupPath nvarchar(4000)
- Success bit
- Notes nvarchar(2000)
- BackupDate date
