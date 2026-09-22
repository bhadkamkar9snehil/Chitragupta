---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: U part 1

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.usp_Quality_Spectro_BuildWideForSample
Safety: MUTATING
Parameters: @SampleID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.Quality_Spectro_Result, XStudio_Xbatch.dbo.Quality_Spectro_Sample

## dbo.usp_Quality_Spectro_Cleanup
Safety: MUTATING
Parameters: @BufferDays:int, @Source:varchar(50)
Referenced objects: XStudio_Xbatch.dbo.Quality_Spectro_File, XStudio_Xbatch.dbo.Quality_Spectro_Result, XStudio_Xbatch.dbo.Quality_Spectro_Sample

## dbo.usp_Quality_Spectro_IngestFromPath
Safety: MUTATING
Parameters: @FullPath:nvarchar(4000), @Checksum:varchar(100)
Referenced objects: XStudio_Xbatch.dbo.Quality_Spectro_File, XStudio_Xbatch.dbo.Quality_Spectro_Result, XStudio_Xbatch.dbo.Quality_Spectro_Sample, XStudio_Xbatch.dbo.usp_Quality_Spectro_BuildWideForSample

## dbo.usp_Quality_Spectro_RebuildWide
Safety: MUTATING
Parameters: @SampleID:varchar(36), @FromDate:datetime, @ToDate:datetime, @HeatNo:varchar(100)
Referenced objects: XStudio_Xbatch.dbo.Quality_Spectro_Sample, XStudio_Xbatch.dbo.usp_Quality_Spectro_BuildWideForSample

## dbo.usp_SMS_EAF_LRF_CCM_KPI_PerDate
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Xbatch.dbo.XStudio_List_CCM_Per_Heat_Vw, XStudio_Xbatch.dbo.XStudio_List_EAF_PER_HEAT_Vw, XStudio_Xbatch.dbo.XStudio_List_EAF_Per_Heat_Vw, XStudio_Xbatch.dbo.XStudio_List_LRF_Per_Heat_Vw
