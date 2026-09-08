---
type: Reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: B

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Backup_Monitoring
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CurrentDate:date, SubfolderName:varchar, FullBackupCount:int, DifferentialCount:int, TransactionCount:int

## dbo.Backup_Monitoring_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CurrentDate:date, SubfolderName:varchar, FullBackupCount:int, DifferentialCount:int, TransactionCount:int

