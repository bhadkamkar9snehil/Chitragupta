---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: Q part 1

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Quality_Deviation_Master
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Size:varchar, ParameterName:varchar, High:varchar, Low:varchar, Product:varchar, Area:varchar

## dbo.Quality_Spectro_File
ID:varchar, FileName:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Importedon:datetime, IsProcessed:bit, FilePath:varchar, Checksum:varchar, FileStatus:varchar, STatusNote:varchar

## dbo.Quality_Spectro_Result
ID:varchar, LineName:varchar, SampleID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReplicateNo:int, Element:varchar, ResultType:varchar, StatType:varchar, ResultValue:decimal, Unit:varchar, Status:varchar, MinLimit:decimal, MaxLimit:decimal

## dbo.Quality_Spectro_Sample
ID:varchar, SampleName:varchar, FileID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, XMLCreatedAt:datetime, HeatNo:varchar, SamplePoint:varchar, OperatorName:varchar, MethodName:varchar, MethodVersion:varchar, Instrument:varchar, InstrumentNumber:varchar, SampleType:varchar, SampleReceivedTime:datetime
