---
type: Reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: F

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.FCM_Monitoring
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, DateTime:datetime, ClusterName:varchar, DiskName:varchar, Path:varchar, Size:varchar, FreeSpace:varchar, UsedSpace:varchar, PercentFree:varchar, State:varchar, OwnerNode:varchar

## dbo.FCM_Monitoring_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, DateTime:datetime, ClusterName:varchar, DiskName:varchar, Path:varchar, Size:varchar, FreeSpace:varchar, UsedSpace:varchar, PercentFree:varchar, State:varchar, OwnerNode:varchar

## dbo.FCM_Node_Monitoring
ID:varchar, DateTime:datetime, Cluster:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Name:varchar, State:varchar

## dbo.Folder_Monitoring
ID:varchar, EntryDateTime:datetime, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SizeInGB:decimal, FolderName:varchar

## dbo.Folder_Monitoring_Audit
ID:varchar, EntryDateTime:datetime, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SizeInGB:decimal, FolderName:varchar

