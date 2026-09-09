---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: A

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Actual_Primary_Current
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Pri15MVATransformerR:int, PriEAFTransfomer80MVAY:int, PriTransformer2a4MVAB:int, EntryDateTime:datetime, Pri125MVATransformerB:int, PriTransformer13MVAB:int, EngineerName:varchar, PriTransformer516MVAY:int, PriTransformer23MVAR:int, Pri24MVATransformerB:int, Pri63MVATransformerR:int, Shift:varchar, PriTransformer13MVAR:int, PriTransformer43MVAY:decimal, ParentID:varchar, PriTransformer516MVAR:int, PriTransformer4a3MVAB:int, PriLRFTransfomer30MVAR:decimal, PriTransformer516MVAB:int, Pri125MVATransformerR:int, PriTransformer2a4MVAY:int, PriTransformer31MVAY:int, Pri15MVATransformerY:int, PriLRFTransfomer30MVAY:decimal, PriTransformer4a3MVAR:int, Pri24MVATransformerR:int, PriTransformer31MVAB:int, PriTransformer43MVAR:decimal, Pri63MVATransformerY:int, PriTranboosterfan12MVAB:decimal, PriLRFTransfomer30MVAB:decimal, Pri125MVATransformerY:int, PriTranboosterfan12MVAR:int, PriTransformer23MVAB:int, IsProcessed:bit, PriTransformer4a3MVAY:int, PriTransformer3a3MVAY:decimal, ReportDate:date, PriTransformer23MVAY:int, PriTransformer3a3MVAB:decimal, PriEAFTransfomer80MVAR:int, Pri15MVATransformerB:int, Pri24MVATransformerY:int, PriTranboosterfan12MVAY:decimal, PriTransformer2a4MVAR:int, Pri63MVATransformerB:int, PriTransformer13MVAY:int, PriEAFTransfomer80MVAB:int, PriTransformer31MVAR:int, PriTransformer3a3MVAR:decimal, PriTransformer43MVAB:decimal, Name:varchar, TechnicianName:varchar

## dbo.Actual_Secondary_Current
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SecTransformer31MVAY:int, Sec63MVATransformerB:int, Sec15MVATransformerY:int, SecTransformer31MVAB:int, SecEAFTransfomer80MVAB:int, SecTransformer23MVAY:int, SecLRFTransfomer30MVAB:decimal, Sec125MVATransformerB:int, Shift:varchar, IsProcessed:bit, Sec63MVATransformerY:int, SecEAFTransfomer80MVAR:int, SecLRFTransfomer30MVAR:decimal, SecTransformer516MVAB:int, EntryDateTime:datetime, SecTransformer3a3MVAB:decimal, SecEAFTransfomer80MVAY:int, SecTranboosterfan12MVAY:decimal, Name:varchar, ReportDate:date, SecTransformer13MVAR:int, Sec24MVATransformerY:int, SecTransformer4a3MVAB:int, Sec125MVATransformerY:int, SecTransformer13MVAY:int, SecTransformer23MVAR:int, Sec63MVATransformerR:int, SecLRFTransfomer30MVAY:decimal, SecTransformer3a3MVAR:decimal, Sec125MVATransformerR:int, SecTransformer2a4MVAB:int, SecTransformer4a3MVAY:int, SecTransformer43MVAR:decimal, SecTranboosterfan12MVAB:decimal, SecTranboosterfan12MVAR:int, Sec24MVATransformerR:int, EngineerName:varchar, TechnicianName:varchar, SecTransformer2a4MVAR:int, SecTransformer23MVAB:int, SecTransformer4a3MVAR:int, SecTransformer43MVAY:decimal, SecTransformer31MVAR:int, SecTransformer43MVAB:decimal, SecTransformer3a3MVAY:decimal, Sec15MVATransformerR:int, SecTransformer516MVAR:int, Sec24MVATransformerB:int, SecTransformer516MVAY:int, SecTransformer2a4MVAY:int, ParentID:varchar, Sec15MVATransformerB:int, SecTransformer13MVAB:int

## dbo.Agency_Wise_Delay
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Agency:varchar, Duration:decimal, Remark:varchar, RemainingDuration:decimal, Durationmmss:varchar, DurationInSecond:int

## dbo.Area_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, AssetIdentificationProperties:varchar, ShiftID:varchar, RoleIDList:varchar, IsHandoverEnabled:bit, ModuleID:varchar, ModuleType:varchar

## dbo.Asset_Hierarchy_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SerialNumber:int

