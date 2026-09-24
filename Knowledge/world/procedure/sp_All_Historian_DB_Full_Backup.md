---
type: procedure
title: "sp_All_Historian_DB_Full_Backup"
built: "2026-09-24T11:36:36"
---

# sp_All_Historian_DB_Full_Backup

Parameters: @Mode varchar, @RunDate date, @BackupRootPath nvarchar, @LookbackDays int, @ForceAll bit.

## Writes

- HistorianBackupLog: BackupPath, BackupRunDate, DatabaseName, Notes, Success

## Reads

- HistorianBackupLog: BackupDate
