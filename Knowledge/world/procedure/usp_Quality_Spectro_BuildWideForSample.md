---
type: procedure
title: "usp_Quality_Spectro_BuildWideForSample"
built: "2026-09-24T11:36:36"
---

# usp_Quality_Spectro_BuildWideForSample

Parameters: @SampleID varchar.

## Writes

- Heat_Chemistry_Quality_Data: Ag, Al, As, B, Bi, C, Ca, Ce, Ceq, Chemist, Co, Cr, CreatedBy, CreatedOn, Cu, Fe, Grade, HeatNo, ID, Instrument, MethodName, Mn, MnPerS, MnPerSi, Mo, N2, N2PPM, Nb, Ni, P, Pb, ReceivedTime, ReportedTime, S, SampleID, SampleName, SampleType, Sb, Si, Sn, Status, TI, Ta, V, W, XMLCreatedon, Zr

## Reads

- Quality_Spectro_Result: Element, ResultType, ResultValue, SampleID, StatType
- Quality_Spectro_Sample: HeatNo, ID, Instrument, MethodName, OperatorName, SampleName, SampleReceivedTime, SampleType, XMLCreatedAt
