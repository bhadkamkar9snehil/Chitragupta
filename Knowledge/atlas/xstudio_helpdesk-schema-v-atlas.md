---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: V

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.VM_Monitoring
ID:varchar, TaskManagerCPU:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TaskManagerRAM:varchar, TaskManagerNetwork:varchar, Entrydatetime:datetime, TaskManagerCPURemarks:varchar, TaskManagerRAMRemarks:varchar, TaskManagerNetworkRemarks:varchar

## dbo.VM_Monitoring_Audit
ID:varchar, TaskManagerCPU:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TaskManagerRAM:varchar, TaskManagerNetwork:varchar, Entrydatetime:datetime, TaskManagerCPURemarks:varchar, TaskManagerRAMRemarks:varchar, TaskManagerNetworkRemarks:varchar

