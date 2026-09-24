---
type: event
title: "CCM/CCM_ProcessTime"
built: "2026-09-24T11:36:36"
---

# CCM/CCM_ProcessTime

Area CCM. Active.
Creates and updates rows in CCM_ProcessTime.

## State 1: Ladle At CCM Arm 1 Rest Position

Condition: `IIF({PTArm1CastPosition} = 0 AND {PTArm1InstantWieght} > 75, True, IIF({PTArm1CastPosition} = 1 AND {PTArm1InstantWieght} > 50, False, Null))`
Workflow status on: Entered, off: Completed.

## State 1: Ladle At CCM Arm 2 Rest Position

Condition: `IIF({PTArm2CastPosition} = 0 AND {PTArm2InstantWieght} > 70, True, IIF({PTArm2CastPosition} = 1 AND {PTArm2InstantWieght} > 50, False, Null))`
Workflow status on: Entered, off: Completed.

## State 2: Turret Rotation

Condition: `IIF({PTArm1InstantWieght} > 75 AND {PTTurretLubrication} = 1, True, IIF({PTArm1InstantWieght} >75 AND {PTTurretLubrication} = 0, False, Null))`
Workflow status on: Entered, off: Completed.

## State 2: Turret Rotation

Condition: `IIF({PTArm2InstantWieght} > 75 AND {PTTurretLubrication} = 1, True, IIF({PTArm2InstantWieght} >75 AND {PTTurretLubrication} = 0, False, Null))`
Workflow status on: Entered, off: Completed.

## State 3: CCM Arm 1 Casting Position

Condition: `IIF({PTArm1CastPosition} = 1 AND {PTArm1InstantWieght} > 50, True, IIF({PTArm1CastPosition} = 0 AND {PTArm1InstantWieght} < 50, False, Null))`
Workflow status on: Entered, off: Completed.

## State 3: CCM Arm 2 Casting Position

Condition: `IIF({PTArm2CastPosition} = 1 AND {PTArm2InstantWieght} > 50, True, IIF({PTArm2CastPosition} = 0 AND {PTArm2InstantWieght} < 50, False, Null))`
Workflow status on: Entered, off: Completed.

## State 4: Billets Production

Condition: `IIF({TotalBillets} > 0 AND {TurretControlOff} = 0, True, IIF({TotalBillets} = 0 AND {TurretControlOff} = 0, False, Null))`
Workflow status on: Entered, off: Completed.

## State 5: CCM Turret Control Off

Condition: `{TurretControlOff} = 1`
Workflow status on: Entered, off: Completed.
