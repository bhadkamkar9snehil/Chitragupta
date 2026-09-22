---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: G part 1

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.Get_Monthly_Bill_Details_Summary
Safety: MUTATING
Parameters: @MonthNumber:int, @YearNumber:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Electricity_Meter_Electricity_Rate_Tbl_Mst, XStudio_Xbatch.dbo.Electricity_Meter_Reading, XStudio_Xbatch.dbo.Electricity_Meter_Timing
