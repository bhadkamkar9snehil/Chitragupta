---
type: procedure
title: "XSTUDIO_WORKFLOW_B0E88401-847E-4370-9B0F-6D0BD87E68E2_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_B0E88401-847E-4370-9B0F-6D0BD87E68E2_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Electricity_Meter_Reading: Consumption, EndDateTime, FeederName, ID, IsProcessed, Position, Price, Quality, ReportDate, Value

## Writes (named in its SQL text)

- Electricity_Meter_Reading
