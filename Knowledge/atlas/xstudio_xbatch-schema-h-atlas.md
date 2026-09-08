---
type: Reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: H

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Heat_Chemistry_Quality_Data
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Ceq:decimal, W:decimal, ReportedTime:datetime, Nb:decimal, HeatNo:varchar, Chemist:varchar, Pb:decimal, Grade:varchar, Sn:decimal, Shift:varchar, Remarks:varchar, Ca:decimal, MnPerSi:decimal, Al:decimal, Si:decimal, SampleType:varchar, C:decimal, Cu:decimal, V:decimal, N2PPM:decimal, SampleName:varchar, SampleID:varchar, Section:varchar, TI:decimal, Date:datetime, S:decimal, SrNo:int, Mo:decimal, ReportDate:varchar, Ni:decimal, Cr:decimal, Co:decimal, MnPerS:decimal, P:decimal, ReceivedTime:datetime, B:decimal, As:decimal, Mn:decimal, XMLCreatedon:datetime, MethodName:varchar, Instrument:varchar, Status:varchar, Ag:decimal, Bi:decimal, Fe:decimal, Sb:decimal, Ta:decimal, Zr:decimal, Ce:decimal, SampleNo:varchar, IsLatestSample:bit, InspectionLot:varchar, IsUDStatus:bit, RRStatus:varchar, SAPTransactionID:varchar, Message:varchar, SAPStatus:varchar, InspOper:varchar, N2:decimal, HeatSequence:varchar

## dbo.Heat_End_Selection_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, FirstHeatNo:int, LastHeatNo:int, Dateyyyymmdd:varchar, FIrstHeatStartTime:datetime, LastHeatTapTime:datetime, CalTimeinMinutes:int, CalTimeinSecond:int

## dbo.Highest_Production_Entry
ID:varchar, HighestProduction:decimal, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Availability:decimal, DayProduction:decimal, Rejections:decimal, LongestSequence:decimal, LadleLife:decimal, ShellLife:decimal, HIghestproductionCalc:varchar, AvailabilityCalc:varchar, DayProductionCalc:varchar, RejectionsCalc:varchar, LongestSequenceCalc:varchar, LadleLifeCalc:varchar, ShellLifeCalc:varchar, Status:varchar, HighestProductionDate:date, DayProductionDate:date, LongestSequenceDate:date, AvailabilityDate:date, BestAspect:varchar

## dbo.HistorianBackupLog
LogID:int, DatabaseName:nvarchar, BackupRunDate:datetime, BackupPath:nvarchar, Success:bit, Notes:nvarchar, BackupDate:date

