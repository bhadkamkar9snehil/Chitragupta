---
type: event
title: "RM_Reheating_Furnace/ChargingBedToFurnance"
built: "2026-09-24T11:36:36"
---

# RM_Reheating_Furnace/ChargingBedToFurnance

Area RM_Reheating_Furnace. Active.
Creates and updates rows in ChargingBedToFurnance.

## State 1: Billet At Section 1

Condition: `IIF({ChargingRollerTable} =1 and {BilletArrivedInSection1} = 0 And {StopperHighLimitSwitch} = 1, True, False)`
Workflow status on: Entered, off: Completed.

## State 2: Billet At Section 2

Condition: `IIF({ChargingPhotocell} = 0 And {BilletArrivedInSection2}=0 And {Head Sensor} = 1, True, False)`
Workflow status on: Entered, off: Completed.

## State 3: Billet In Furnace

Condition: `IIF({FurnanceDoorClose} = 0 And {InternalStart&Stop} = 1 And {FurnaceWallProtection}=1,True, False)`
Workflow status on: Entered, off: Completed.

## State 4: Section 1 Billet Reverse

Condition: `IIF({Section1BilletReverse} = 1, True, False)`
Workflow status on: Entered, off: Completed.

## State 5: Section 2 Billet Reverse

Condition: `IIF({Section2BilletReverse} = 1, True, False)`
Workflow status on: Entered, off: Completed.
