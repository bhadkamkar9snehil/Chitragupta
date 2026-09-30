---
type: procedure
title: "Quality_Spectro_IsLatestSample_Update_Usp"
built: "2026-09-24T11:36:36"
---

# Quality_Spectro_IsLatestSample_Update_Usp


## Writes

- Heat_Chemistry_Quality_Data: InspOper, IsLatestSample, RRStatus, SAPStatus
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Heat_Chemistry_Quality_Data: HeatNo, ID, IsDeleted, ReceivedTime, ReportedTime, SampleType, XMLCreatedon
- MES_Quality_Configurator: Operation, SampleType

## What its own log shows

27,397 log rows, 2026-05-21 14:59 to 2026-07-08 19:30.

Steps:
- 1 Entered
- 2 Update Is Latest sample in Heat chemistry quality data for product sampletype Start
- 2 Update Is Latest sample in Heat chemistry quality data for product sampletype received from yesterday Start
- 3 Update Is Latest sample in Heat chemistry quality data for product sampletype End
- 3 Update Is Latest sample in Heat chemistry quality data for product sampletype received from yesterday End
- 4 Update RRStatus and SAPstatus to entered of latest sample in heat chemistry quality data Start
- 5 Update RRStatus and SAPstatus to entered of latest sample in heat chemistry quality data End
- 6 Update Inspect Opr in Heat Chemistry quality data Start
- 6 Update Inspect Opr in Heat Chemistry quality data when Inspect Opr is null Start
- 7 Update Inspect Opr in Heat Chemistry quality data End
- 7 Update Inspect Opr in Heat Chemistry quality data when Inspect Opr is null End
- 8 Completed

Example call: `EXEC XStudio_Xbatch.dbo.Quality_Spectro_IsLatestSample_Update_Usp`
