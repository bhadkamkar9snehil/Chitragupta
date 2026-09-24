---
type: event
title: "EAF_SMS/SMS_Plant_Process_Time"
built: "2026-09-24T11:36:36"
---

# EAF_SMS/SMS_Plant_Process_Time

Area EAF_SMS. Active.
Creates and updates rows in SMS_Plant_Process_EventTime.

## State 1: EAF Roof Open For Fill Bucket Charging

Condition: `IIF({SMSEAFRoof} = 0 AND {SMSEAFPowerONmin} = 0, True, IIF({SMSEAFRoof} = 1 AND {SMSEAFPowerONmin} = 0, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 2: EAF Power On

Condition: `{SMSEAFActivePower}>10`
Captures: SMSEAFHeatID -> HeatID

## State 3: Ladle Car At EAF

Condition: `IIF({SMSEAFLadleCar} = 1 AND {SMSEAFPowerONmin} > 0, True, IIF({SMSEAFLadleCar} = 0 AND {SMSEAFPowerONmin} > 0, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 4: EAF Tapping

Condition: `IIF({SMSEAFTapping} = 1 AND {SMSEAFPowerONmin} > 0, True, IIF({SMSEAFTapping} = 0 AND {SMSEAFPowerONmin} >= 0, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 5: Ladle Car Move From EAF To LRF

Condition: `IIF({SMSEAFLadleCar} = 0 AND {SMSLRFLadleCar} = 0 AND {SMSEAFTapping}=1, True, IIF({SMSEAFLadleCar}= 0 AND {SMSLRFLadleCar} = 1, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 6: Ladle Car Reach At LRF

Condition: `IIF({SMSLRFLadleCar} = 1 AND {SMSLRFRoofE1} = 0 AND {SMSLRFArcTime} = 0, True, IIF({SMSLRFLadleCar} = 1 AND {SMSLRFRoofE1} = 1 AND {SMSLRFArcTime} = 0, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 7: LRF Roof Close

Condition: `IIF({SMSLRFRoofE1} = 0 AND {SMSLRFRoofE3} = 0, True, IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 8: LRF Arcing

Condition: `IIF({SMSLRFArcTime} > 0 AND {SMSLRFRoofE1} = 0 AND {SMSLRFRoofE3} = 0, True, IIF({SMSLRFArcTime}>0 and {SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 9: LRF Roof Open

Condition: `IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1, True, IIF({SMSLRFRoofE1} = 0 AND {SMSLRFRoofE3} = 0, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 10: Ladle Move From LRF To CCM

Condition: `IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm2InstantWieght} < 10 AND {SMSLRFArcTime} > 0, True, IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm2InstantWieght} > 75 AND {SMSLRFArcTime} = 0, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 10: Ladle Move From LRF To CCM

Condition: `IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm1InstantWieght} < 10 AND {SMSLRFArcTime} > 0, True, IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm1InstantWieght} > 75 AND {SMSLRFArcTime} = 0, False, Null))`
Captures: SMSEAFHeatID -> HeatID

## State 11: Ladle At CCM Arm 1 Rest Position

Condition: `IIF({SMSCCMArm1InstantWieght} > 75 AND {SMSCCMArm1castPosition} = 0, True, IIF({SMSCCMArm1InstantWieght} > 75 AND {SMSCCMArm1castPosition} = 1, False, Null))`
Workflow status on: Entered, off: Completed.

## State 11: Ladle At CCM Arm 2 Rest Position

Condition: `IIF({SMSCCMArm2InstantWieght} > 75 AND {SMSCCMArm2castPosition} = 0, True, IIF({SMSCCMArm2InstantWieght} > 75 AND {SMSCCMArm2castPosition} = 1, False, Null))`
Workflow status on: Entered, off: Completed.

## State 12: Turret Rotation

Condition: `IIF({SMSCCMTurretLubrication} = 1 AND {SMSCCMArm1InstantWieght} > 75, True, IIF({SMSCCMTurretLubrication} = 0 AND {SMSCCMArm1InstantWieght} >75, False, Null))`
Workflow status on: Entered, off: Completed.

## State 12: Turret Rotation

Condition: `IIF({SMSCCMTurretLubrication} = 1 AND {SMSCCMArm2InstantWieght} > 75, True, IIF({SMSCCMTurretLubrication} = 0 AND {SMSCCMArm2InstantWieght} >75, False, Null))`
Workflow status on: Entered, off: Completed.

## State 13: CCM Arm 1 Casting Position

Condition: `IIF({SMSCCMArm1castPosition} = 1 and {SMSCCMArm1InstantWieght} > 50, True, IIF({SMSCCMArm1castPosition} = 0 and {SMSCCMArm1InstantWieght} < 50, False, Null))`
Workflow status on: Entered, off: Completed.

## State 13: CCM Arm 2 Casting Position

Condition: `IIF({SMSCCMArm2castPosition} = 1 and {SMSCCMArm2InstantWieght} > 50, True, IIF({SMSCCMArm2castPosition} = 0 and {SMSCCMArm2InstantWieght} < 50, False, Null))`
Workflow status on: Entered, off: Completed.

## State 14: Billets Production

Condition: `{SMSCCMTotalBillets} > 0 AND {SMSCCMTurretControlOff} = 0`
Workflow status on: Entered, off: Completed.

## State 18: CCM Turret Control Off

Condition: `{SMSCCMTurretControlOff} = 1`
Workflow status on: Entered, off: Completed.
