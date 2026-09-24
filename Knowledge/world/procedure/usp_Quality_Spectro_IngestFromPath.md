---
type: procedure
title: "usp_Quality_Spectro_IngestFromPath"
built: "2026-09-24T11:36:36"
---

# usp_Quality_Spectro_IngestFromPath

Parameters: @FullPath nvarchar, @Checksum varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- Quality_Spectro_File: Checksum, CreatedOn, DbSyncStatus, FileName, FilePath, ID, Importedon, IsProcessed, ModifiedOn, Source
- Quality_Spectro_Result: CreatedOn, Element, ID, LineName, MaxLimit, MinLimit, ReplicateNo, ResultType, ResultValue, SampleID, StatType, Status, Unit
- Quality_Spectro_Sample: CreatedOn, FileID, HeatNo, ID, Instrument, InstrumentNumber, MethodName, MethodVersion, OperatorName, SampleName, SamplePoint, SampleReceivedTime, SampleType, XMLCreatedAt

## Calls

- usp_Quality_Spectro_BuildWideForSample
