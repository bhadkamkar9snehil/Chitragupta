---
type: Reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: R

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Region_Mst_Tbl
ID:varchar, Name:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.Region_Mst_Tbl_Audit
ID:varchar, Name:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.Replica_Monitoring
ID:varchar, ComputerName:varchar, DateTime:datetime, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CurrentReplicaServerName:varchar, State:varchar, Health:varchar, ReplicationState:varchar, LastReplicationTime:varchar

## dbo.Round_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, AreaID:varchar, ProcedureID:varchar, EntryDateTime:datetime, Status:varchar

## dbo.Round_Steps_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, RoundID:varchar, EntityID:varchar, EquipmentID:varchar, PageID:varchar, ViewPageID:varchar, RecordID:varchar, EntryDateTime:datetime, Status:varchar, Isscanable:bit, PhysicalTag:varchar

