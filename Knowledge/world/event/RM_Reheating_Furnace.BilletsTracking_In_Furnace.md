---
type: event
title: "RM_Reheating_Furnace/BilletsTracking_In_Furnace"
built: "2026-09-24T11:36:36"
---

# RM_Reheating_Furnace/BilletsTracking_In_Furnace

Area RM_Reheating_Furnace. Active.
Creates and updates rows in BilletsTracking_In_Furnace.

## State 1: Charging and Discharging Mode

Condition: `IIF({ChargingDishchargingMode} = 1 AND {ChargingDoorClose} = 1, True, IIF({ChargingDishchargingMode}  = 1 AND {ChargingDoorClose} = 0, False, Null))`

## State 1: Furnace Door Open Billet In

Condition: `{ChargingDoorOpen} = 1`
Workflow status on: Entered, off: Completed.

## State 1: Furnace Door Open Billet Out

Condition: `{ChargingDoorClose} = 1`

## State 1: Only Charging Mode

Condition: `IIF({ChargingOnlyMode} = 1 AND {ChargingDoorOpen} = 1, True, IIF({ChargingOnlyMode} = 0 AND {ChargingDoorOpen} = 0, False, Null))`

## State 1: Only Discharging Mode

Condition: `IIF({DischargingOnlyMode} = 1 AND {ChargingDoorClose} = 1, True, IIF({DischargingOnlyMode} = 0 AND {ChargingDoorClose} = 0, False, Null))`
