---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: S part 1

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.SQL_Monitoring
ID:varchar, EntryDateTime:datetime, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SQLServerMonitoringImage:varchar, Parentid:varchar, SQLServerMonitoringRemarks:varchar

## dbo.SQL_Monitoring_Audit
ID:varchar, EntryDateTime:datetime, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SQLServerMonitoringImage:varchar, Parentid:varchar, SQLServerMonitoringRemarks:varchar

## dbo.Services_Monitoring
ID:varchar, EntryDateTime:datetime, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, FailoverClusterManager:varchar, HyperV:varchar, KernelPower:varchar, KernelBoot:varchar, XStudioSyncService:varchar, XStudioSchedulersService:varchar, FailoverClusterManagerRemarks:varchar, HyperVRemarks:varchar, KernelPowerRemarks:varchar, KernelBootRemarks:varchar, XStudioSyncServiceRemarks:varchar, XStudioSchedulersServiceRemarks:varchar

## dbo.Services_Monitoring_Audit
ID:varchar, EntryDateTime:datetime, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, FailoverClusterManager:varchar, HyperV:varchar, KernelPower:varchar, KernelBoot:varchar, XStudioSyncService:varchar, XStudioSchedulersService:varchar, FailoverClusterManagerRemarks:varchar, HyperVRemarks:varchar, KernelPowerRemarks:varchar, KernelBootRemarks:varchar, XStudioSyncServiceRemarks:varchar, XStudioSchedulersServiceRemarks:varchar

## dbo.Station_Mst_Tbl
ID:varchar, Name:varchar, CentralDispatchID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:decimal

## dbo.Station_Mst_Tbl_Audit
ID:varchar, Name:varchar, CentralDispatchID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:decimal

## dbo.Storage_Monitoring
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, DateTime:datetime, PSComputerName:varchar, HealthStatus:varchar, DriveLetter:varchar, Size:decimal, SizeRemaining:decimal

## dbo.Storage_Monitoring_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, DateTime:datetime, PSComputerName:varchar, HealthStatus:varchar, DriveLetter:varchar, Size:decimal, SizeRemaining:decimal

## dbo.Support_Executive_Mst_Tbl
ID:varchar, Name:varchar, Area:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, UserID:varchar

## dbo.Support_Executive_Mst_Tbl_Audit
ID:varchar, Name:varchar, Area:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, UserID:varchar

## dbo.SystemDetails
ID:varchar, HostName:varchar, IPAddress:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Station:varchar, MACAddress:varchar

## dbo.SystemDetails_Audit
ID:varchar, HostName:varchar, IPAddress:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Station:varchar, MACAddress:varchar

## dbo.System_Mst_Tbl
ID:varchar, Name:varchar, StationID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:decimal, State:varchar

## dbo.System_Mst_Tbl_Audit
ID:varchar, Name:varchar, StationID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:decimal, State:varchar

## dbo.subarea
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, area:varchar

## dbo.subarea_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, area:varchar

## dbo.subareadetails
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, subarea:varchar

## dbo.subareadetails_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, subarea:varchar

## dbo.systemreferencedocuments
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, versionno:varchar, Description:varchar, releasedate:date, document:varchar, documenttype:varchar, srno:int, DOCXDocument:varchar

## dbo.systemreferencedocuments_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, versionno:varchar, Description:varchar, releasedate:date, document:varchar, documenttype:varchar, srno:int, DOCXDocument:varchar
