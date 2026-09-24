---
type: procedure
title: "XSTUDIO_WORKFLOW_C5631C30-B02A-4FEF-B2B7-E811DB1A0B59_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_C5631C30-B02A-4FEF-B2B7-E811DB1A0B59_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- MES_SAP_UsageDecision_Trn_Tbl: HeatNo, InspectionLot, MaterialType, SAPPostingStatus, UsgDecCode
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Heat_Chemistry_Quality_Data: Ag, Al, As, B, Bi, C, Ca, Ce, Ceq, Chemist, Co, Cr, Cu, Date, Fe, Grade, HeatNo, ID, InspOper, InspectionLot, Instrument, IsLatestSample, IsUDStatus, Message, MethodName, Mn, MnPerS, MnPerSi, Mo, N2, N2PPM, Nb, Ni, P, Pb, RRStatus, ReceivedTime, Remarks, ReportedTime, S, SAPTransactionID, SampleID, SampleName, SampleType, Sb, Section, Shift, Si, Sn, SrNo, TI, Ta, V, W, XMLCreatedon, Zr

## Writes (named in its SQL text)

- Heat_Chemistry_Quality_Data

## What its own log shows

9,256 log rows, 2026-03-20 00:41 to 2026-07-08 23:44.

Steps:
- Completed
- Entered
- Store Entered state of GLS in Usage Decision process End
- Store Entered state of GLS in Usage Decision process Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_C5631C30-B02A-4FEF-B2B7-E811DB1A0B59_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='C9710FC1-E4FF-4FDC-991A-A1B54F059E59', @p_RecordId='Posted', @p_StatusAttributeName='52DB91A9-80E2-4B5C-8C1D-84167CF9A823', @p_Status='SAPStatus'`
