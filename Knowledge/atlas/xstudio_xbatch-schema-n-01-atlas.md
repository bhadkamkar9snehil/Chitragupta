---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: N part 1

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.NM3_To_MMBTU_Factor
ID:varchar, Month:date, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Nm3toMMBTUFactor:decimal, RebarTieRodFactor:decimal, WRMTieRodFactor:decimal, RebarCoilTieRodFactor:decimal, ScalelossFactor:decimal, EndCutFactor:decimal

## dbo.Ngconsumption_Summary_Day
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, NGCong:decimal, Discharged:int, NGCons:decimal, NGconsMMBTPerTon:decimal, ColdDischargeBillet:int, HotDischargeBillet:int, Discharged_MTD:int, HotDischargeBillet_YTD:int, HotDischargeBillet_MTD:int, Discharged_YTD:int, TotalBillet:decimal, TotalNG:decimal, NGCons_MTD:int, TotalNG_YTD:decimal, NGCong_MTD:decimal, ColdDischargeBillet_MTD:int, ColdDischargeBillet_YTD:int, TotalNG_MTD:decimal, NGCong_YTD:decimal, TotalBillet_YTD:decimal, NGCons_YTD:int, TotalBillet_MTD:decimal, AvgResidenceTime:int
