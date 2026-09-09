---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: D

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.DLBMonitoring
ID:varchar, TicketNo:int, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Entrydatetime:datetime, Remarks:varchar

## dbo.DLBMonitoring_Audit
ID:varchar, TicketNo:int, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Entrydatetime:datetime, Remarks:varchar

