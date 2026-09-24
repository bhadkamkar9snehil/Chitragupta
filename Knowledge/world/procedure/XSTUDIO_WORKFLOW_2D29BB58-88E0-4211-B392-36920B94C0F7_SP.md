---
type: procedure
title: "XSTUDIO_WORKFLOW_2D29BB58-88E0-4211-B392-36920B94C0F7_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_2D29BB58-88E0-4211-B392-36920B94C0F7_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Electricity_Meter_Reading: Consumption, EndDateTime, FeederName, ID, Position, Price, Quality, Value

## Writes (named in its SQL text)

- Electricity_Meter_Reading
