---
type: event
title: "RM_WRM/XMES_RM_Stand_WRM"
built: "2026-09-24T11:36:36"
---

# RM_WRM/XMES_RM_Stand_WRM

Area RM_WRM. Active.
Creates and updates rows in XMES_RM_Stand_WRM.

## State 1: Arrived At stand 1

Condition: `IIF({ArrivedatStand1} > 200,True,False)`

## State 2: Arrived At Stand 18

Condition: `IIF({MillLastStandStatus} =1,True,False)`
Workflow status on: Entered, off: Completed.

## State 3: Billet Arrived at Stand 1

Condition: `IIF({Stand1TriggerStatus} =1,True,False)`
Workflow status on: Entered, off: Completed.
