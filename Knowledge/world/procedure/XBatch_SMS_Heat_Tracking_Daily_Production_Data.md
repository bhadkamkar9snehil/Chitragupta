---
type: procedure
title: "XBatch_SMS_Heat_Tracking_Daily_Production_Data"
built: "2026-09-24T11:36:36"
---

# XBatch_SMS_Heat_Tracking_Daily_Production_Data

Parameters: @HeatID int.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Writes (named in its SQL text)

- XBatch_MES_Heat_Tracking

## What its own log shows

8,080 log rows, 2026-05-20 18:08 to 2026-07-08 19:30.

Steps:
- 1 Entered
- 2 Store data of eaf, lrf, ccm and sms shift incharge into temp table start
- 3 Store data of eaf, lrf, ccm and sms shift incharge into temp table End
- 4 Update Heat tracking for data of eaf, lrf, ccm and sms shift incharge from temp table start
- 5 Update Heat tracking for data of eaf, lrf, ccm and sms shift incharge from temp table start
- 6 Insert into Heat tracking for data of eaf, lrf, ccm and sms shift incharge from temp table start
- 7 Insert into Heat tracking for data of eaf, lrf, ccm and sms shift incharge from temp table end
- 8 Completed
- Completed
- Entered
- Insert into Heat tracking for data of eaf, lrf, ccm and sms shift incharge from temp table end
- Insert into Heat tracking for data of eaf, lrf, ccm and sms shift incharge from temp table start
- Store data of eaf, lrf, ccm and sms shift incharge into temp table End
- Store data of eaf, lrf, ccm and sms shift incharge into temp table start
- Update Heat tracking for data of eaf, lrf, ccm and sms shift incharge from temp table start

Example call: `EXEC XStudio_Xbatch.dbo.XBatch_SMS_Heat_Tracking_Daily_Production_Data @HeatID='1604014'`
