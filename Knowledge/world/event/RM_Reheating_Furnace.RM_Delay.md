---
type: event
title: "RM_Reheating_Furnace/RM Delay"
built: "2026-09-24T11:36:36"
---

# RM_Reheating_Furnace/RM Delay

Area RM_Reheating_Furnace. Active.
Creates and updates rows in RM_Delays.

## State 1: Accumulative Delay

Condition: `{MILL_ACTUALROLLING_LV3} = 1`
Workflow status on: Entered, off: Completed.

## State 1: Billets Gap

Condition: `{RM_Billets_Gap} > 45`
Workflow status on: Entered, off: Completed.

## State 1: Delay Trigger

Condition: `{RM_Delay_Trigger} = 1`
Workflow status on: Entered, off: Completed.

## State 2: Delay for RM

Condition: `IIF({RM_Mill_Ready_Status} = 0, True, IIF({RM_Mill_Stand_01_Billets_Trigger_Status} = 1 AND {RM_Mill_Ready_Status} = 1, False, Null))`
Workflow status on: Entered, off: Completed.

## State 3: Cummulative Delay

Condition: `IIF({RM_Mill_Ready_Status} = 1 AND {RM_Mill_Stand_01_Billets_Trigger_Status} = 0 ,True ,IIF ({RM_Mill_Ready_Status}=0 OR ({RM_Mill_Ready_Status} = 1 AND {RM_Mill_Stand_01_Billets_Trigger_Status} = 1),False, Null))`
