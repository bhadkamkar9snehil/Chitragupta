---
type: procedure
title: "XStudio_Inventory_Pull_Schedule_TSQL_Task_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Inventory_Pull_Schedule_TSQL_Task_Usp

Parameters: @Plant nvarchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- MES_SAP_Inventory_Stock_Tbl

## Reads

- MES_SAP_Inventory_Stock_Tbl: CreatedOn, Plant
