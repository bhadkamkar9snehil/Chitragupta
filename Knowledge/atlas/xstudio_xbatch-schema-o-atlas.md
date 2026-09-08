---
type: Reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: O

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Order_Type_MST
ID:varchar, OrderType:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, ColourCode:varchar

## dbo.Organisation_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.Organization_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.Outdoor_SwitchYard_Status
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, IsProcessed:bit, PhysicalandVisualChckingSwitchYardF1:varchar, CircuitBreakerStatusCounterReadingF2:int, TechnicianName:varchar, BreakerPressureF1:int, ParentID:varchar, ReportDate:date, PhysicalandVisualChckingSwitchYardF2:varchar, EntryDateTime:datetime, BreakerPressureF2:int, Shift:varchar, CircuitBreakerStatusF2:varchar, CircuitBreakerStatusCounterReadingF1:int, CircuitBreakerStatusF1:varchar, EngineerName:varchar, Name:varchar

