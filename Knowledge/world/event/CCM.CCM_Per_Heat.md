---
type: event
title: "CCM/CCM_Per_Heat"
built: "2026-09-24T11:36:36"
---

# CCM/CCM_Per_Heat

Area CCM. Active.
Creates and updates rows in CCM_Per_Heat.

## State 1: Arm 1 Cast Position

Condition: `IIF({CCMArm1CastPosition} = 1 AND {CCM Arm1Ladle Weight} > 10, True, IIF({CCMArm1CastPosition} = 0 AND {CCM Arm1Ladle Weight} = 0, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: CCMLadleSequence -> LadleSequence, TundishTemperature -> TundishTemperature, CCMArm1Consumption -> ArmConsumption

## State 2: Arm 2 Cast Position

Condition: `IIF({CCMArm2CastPosition} = 1 AND {CCM Arm2LadleWeight} > 10, True, IIF({CCMArm2CastPosition} = 0 AND {CCM Arm2LadleWeight} = 0, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: CCMLadleSequence -> LadleSequence, TundishTemperature -> TundishTemperature, CCMArm2Consumption -> ArmConsumption
