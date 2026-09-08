---
type: Reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: T

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.TicketScheme_Mst_Tbl
ID:varchar, SrNo:int, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Name:varchar

## dbo.TicketScheme_Mst_Tbl_Audit
ID:varchar, SrNo:int, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Name:varchar

