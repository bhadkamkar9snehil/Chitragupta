# SMS Plant Process Time Doc

*Extracted from `SMS Plant Process Time Doc.docx` -- real vendor handover doc, not invented.*

SITC OF X-FORCE HISTORIAN AND DASHBOARD DEVELOPMENT
SOHAR STEEL OMAN
Declaration
This Project Handover Document is intended only for personnel who already have a working knowledge of the X-Studio framework and related technical concepts.
The reader is expected to have prior knowledge of the X-Studio Event Framework, Workflows, Asset Structure, Database Structure, SQL Logic, and Stored Procedures. This document is prepared as a project-specific technical handover and reference document and is not intended to provide basic or introductory training on these concepts.
The document focuses on the project-specific implementation, configurations, process flows, database objects, SQL logic, workflows, and related technical details required for Project Support, Maintenance, Troubleshooting, and Further Development.
Therefore, readers should have sufficient prior knowledge of X-Studio and the above-mentioned technical areas to effectively understand and utilize the information provided in this document.

# SMS Plant Process Time - Process State Tracking


## 1. Overview

This section describes the event configuration used for tracking the overall plant process timing across EAF, LRF, and CCM. The SMS_Plant_Process_Time event configures a single, ordered chain of process states - from EAF roof opening through CCM billet production and turret control - used to time the process and, for the later states, to trigger downstream heat-ID resolution and data updates via workflow.
States 1 through 10 have WorkFlow disabled. These states do not need a stored-procedure action to resolve which heat they belong to: they simply read the live current value of the heat-number tag EAF_HEAT_NUMBER_PRM at the moment the state condition is evaluated, and use that live value directly as the heat reference. From state 11 onward, WorkFlow is enabled, because by that point CCM is casting a heat that is no longer the live EAF heat, so the stored-procedure action in section 4 is needed to resolve the correct historical heat ID.

## 2. Event Configuration


### 2.1 Event Entity

The main event data is stored in the SMS_Plant_Process_EventTime entity.

### 2.2 Event Master

The SMS_Plant_Process_Time process event is mapped to the SMS_Plant_Process_EventTime transaction entity.

### 2.3 Event Configuration Entity

The Event Configuration Entity defines Attributes, Tag Mapping, and the ordered chain of States for this event.

### 2.4 Event Configuration Tags


## 3. Data Insert Condition - Process States

Each state below is documented in the same structure: the screenshot of its configuration, its Event Status Configuration summary, the exact state condition together with its TRUE / FALSE / NULL transition logic, and the operational meaning of every tag input used in that condition. Casting-arm-specific states (10, 11, 12, 13) are configured once per arm (Arm 1 and Arm 2); both variants are documented. States 15–17 are not used.

### State 1 - EAF Roof Open for Fill Bucket Charging


#### 1.1 Event Status Configuration


#### 1.2 State Condition and Transition Logic


#### 1.3 Meaning of the Condition Inputs


### State 2 - EAF Power On


#### 2.1 Event Status Configuration


#### 2.2 State Condition and Transition Logic


#### 2.3 Meaning of the Condition Inputs


### State 3 - Ladle Car At EAF


#### 3.1 Event Status Configuration


#### 3.2 State Condition and Transition Logic


#### 3.3 Meaning of the Condition Inputs


### State 4 - EAF Tapping


#### 4.1 Event Status Configuration


#### 4.2 State Condition and Transition Logic


#### 4.3 Meaning of the Condition Inputs


### State 5 - Ladle Car Move from EAF To LRF


#### 5.1 Event Status Configuration


#### 5.2 State Condition and Transition Logic


#### 5.3 Meaning of the Condition Inputs


### State 6 - Ladle Car Reach At LRF


#### 6.1 Event Status Configuration


#### 6.2 State Condition and Transition Logic


#### 6.3 Meaning of the Condition Inputs


### State 7 - LRF Roof Close


#### 7.1 Event Status Configuration


#### 7.2 State Condition and Transition Logic


#### 7.3 Meaning of the Condition Inputs


### State 8 - LRF Arcing


#### 8.1 Event Status Configuration


#### 8.2 State Condition and Transition Logic


#### 8.3 Meaning of the Condition Inputs


### State 9 - LRF Roof Open


#### 9.1 Event Status Configuration


#### 9.2 State Condition and Transition Logic


#### 9.3 Meaning of the Condition Inputs


### State 10 (Arm 1) - Ladle Move from LRF To CCM


#### 10 (Arm 1).1 Event Status Configuration


#### 10 (Arm 1).2 State Condition and Transition Logic


#### 10 (Arm 1).3 Meaning of the Condition Inputs


### State 10 (Arm 2) - Ladle Move from LRF To CCM


#### 10 (Arm 2).1 Event Status Configuration


#### 10 (Arm 2).2 State Condition and Transition Logic


#### 10 (Arm 2).3 Meaning of the Condition Inputs


### State 11 (Arm 1) - Ladle At CCM Arm 1 Rest Position


#### 11 (Arm 1).1 Event Status Configuration


#### 11 (Arm 1).2 State Condition and Transition Logic


#### 11 (Arm 1).3 Meaning of the Condition Inputs


### State 11 (Arm 2) - Ladle At CCM Arm 2 Rest Position


#### 11 (Arm 2).1 Event Status Configuration


#### 11 (Arm 2).2 State Condition and Transition Logic


#### 11 (Arm 2).3 Meaning of the Condition Inputs


### State 12 (Arm 1) - Turret Rotation


#### 12 (Arm 1).1 Event Status Configuration


#### 12 (Arm 1).2 State Condition and Transition Logic


#### 12 (Arm 1).3 Meaning of the Condition Inputs


### State 12 (Arm 2) — Turret Rotation


#### 12 (Arm 2).1 Event Status Configuration


#### 12 (Arm 2).2 State Condition and Transition Logic


#### 12 (Arm 2).3 Meaning of the Condition Inputs


### State 13 (Arm 1) — CCM Arm 1 Casting Position


#### 13 (Arm 1).1 Event Status Configuration


#### 13 (Arm 1).2 State Condition and Transition Logic


#### 13 (Arm 1).3 Meaning of the Condition Inputs


### State 13 (Arm 2) — CCM Arm 2 Casting Position


#### 13 (Arm 2).1 Event Status Configuration


#### 13 (Arm 2).2 State Condition and Transition Logic


#### 13 (Arm 2).3 Meaning of the Condition Inputs


### State 14 - Billets Production


#### 14.1 Event Status Configuration


#### 14.2 State Condition and Transition Logic


#### 14.3 Meaning of the Condition Inputs


### State 18 - CCM Turret Control Off


#### 18.1 Event Status Configuration


#### 18.2 State Condition and Transition Logic


#### 18.3 Meaning of the Condition Inputs

The workflow referenced by states 11 onward is defined against the SMS_Plant_Process_EventTime entity under the name "Process Time CCM HeatNo insert" (Application: DEFAULT), as shown below.

## 4. Workflow Entered State - Stored Procedure Action

This single action serves all of the workflow-enabled states (11 onward). It resolves the correct heat ID depending on which state triggered it - carrying the heat ID forward from LRF Roof Open for the CCM-arm states, and from the CCM rest-position states for the casting and billet-production states - decrements it by one to get the actual heat ID, and, for the CCM casting-position states, copies the liquid-metal weight from LRF_Per_Heat into CCM_Data. There is no separate Workflow Completed action for this event.

### 4.1 Workflow Entered SQL Action Details

1. Heat ID resolution for LRF-to-CCM and CCM-rest-position states - When the triggering @Status is 'Ladle Move From LRF To CCM', 'Ladle At CCM Arm 1 Rest Position', 'Ladle At CCM Arm 2 Rest Position', or 'Turret Rotation', @HeatID is set from the current record's HeatID if already populated; otherwise it falls back to the HeatID of the most recent 'LRF Roof Open' record with an earlier StartTime, carrying the heat identity forward through the ladle-transfer states.
2. Heat ID resolution for casting and billet-production states - When @Status is 'CCM Arm 2 Casting Position', 'CCM Arm 1 Casting Position', 'Billets Production', or 'CCM Turret Control Off', the same fallback pattern is applied, but this time referencing the most recent 'Ladle At CCM Arm 1 Rest Position' or 'Ladle At CCM Arm 2 Rest Position' record, since those states are the last to resolve the heat ID before casting begins.
3. Actual heat ID and record update - @ActualHeatID is set to @HeatID minus 1, and the current SMS_Plant_Process_EventTime record is updated with this ActualHeatID and the current modification timestamp.
4. Liquid-metal weight copy for casting states - When @Status is one of the two CCM casting-position states, the liquid-metal weight is read from LRF_Per_Heat for the resolved @ActualHeatID and written to CCM_Data.LiquidSteelWeight, so the CCM casting record reflects the correct liquid-metal quantity from the corresponding LRF treatment.
Note:  This extract depends on variables declared or assigned elsewhere in the complete workflow procedure, including @Status, @HeatID, @ActualHeatID, and @p_RecordId. Because @HeatID is decremented by one to produce @ActualHeatID, confirm this offset is intentional and consistent with how HeatID is assigned upstream before relying on this logic elsewhere.

---
## Tables (real technical detail -- tag mappings, state configs, condition logic)


### Table 1

| Project | SITC of X-Force Historian and Dashboard Development for Sohar Steel Oman |
|---|---|
| Prepared By | Mahesh Udar |
| Document Type | SMS Plant Process Time Event |
| Handover Date |  |
| Handover To |  |
| Document Version | 1.0 |

### Table 2

| Attribute | Tag Name |
|---|---|
| SMSLRFPOFF | LRF_ACTUAL_POWER_OFF_TIME_MIN_PRM |
| SMSCCMTotalBillets | CCM_TOTAL_BILLET_COUNT_PRM |
| SMSCCMTurretControlOff | CCM_TURRET_CONTROL_OFF_STATUS |
| SMSEAFRoof | EAF_ROOF_CLOSED_STATUS |
| SMSCCMArm1InstantWieght | CCM_ARM_1_INSTANT_WEIGHT_TON_PRM |
| SMSEAFHeatsec | EAF_HEAT_TIME_SEC_PRM |
| SMSEAFHeatID | EAF_HEAT_NUMBER_PRM |
| SMSEAFActivePower | EAF_TOTAL_ENERGY_MW_PRM |
| SMSLRFPowerOnTime | LRF_ACTUAL_POWER_ON_TIME_MIN_PRM |
| SMSLRFRoofE3 | LRF_ROOF_UP_E3_STATUS |
| SMSEAFPowerONmin | EAF_POWER_ON_TIME_MIN_PRM |
| SMSEAFPowerONsec | EAF_POWER_ON_TIME_SEC_PRM |
| SMSEAFEBT | EAF_EBT_OPEN_STATUS |
| SMSLRFArcTime | LRF_ACTUAL_ARC_TIME_SEC_PRM |
| SMSCCMHeatID | CCM_HEAT_NUMBER_PRM |
| SMSLiquidMatelSteel | EAF_LIQUID_METAL_WEIGHT_TON_PRM |
| SMSCCMTurretLubrication | CCM_TURRET_LUBE_RUNNING_STATUS |
| SMSCCMArm1castPosition | CCM_ARM_1_CAST_POSITION_STATUS |
| SMSLRFLadleCar | LRF_LADLE_CAR_TREATMENT_POSITION_STATUS |
| SMSEAFHeatmin | EAF_HEAT_TIME_MIN_PRM |
| SMSLRFRoofE1 | LRF_ROOF_UP_E1_STATUS |
| SMSEAFLadleCar | EAF_LADLE_CAR_TAPPING_POSITION_STATUS |
| SMSEAFTapping | EAF_TAPPING_STATUS |
| SMSCCMArm2castPosition | CCM_ARM_2_CAST_POSITION_STATUS |
| SMSCCMArm2InstantWieght | CCM_ARM_2_INSTANT_WEIGHT_TON_PRM |

### Table 3

| Event status name | EAF Roof Open For Fill Bucket Charging |
|---|---|
| State sequence | 1 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 4

| IIF({SMSEAFRoof} = 0 AND {SMSEAFPowerONmin} = 0, True, IIF({SMSEAFRoof} = 1 AND {SMSEAFPowerONmin} = 0, False, Null)) |
|---|

### Table 5

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSEAFRoof = 0; SMSEAFPowerONmin = 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSEAFRoof = 1; SMSEAFPowerONmin = 0 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 6

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSEAFRoof | 0 | EAF roof is open, ready for scrap/fill-bucket charging; this participates in the State-On condition. |
| SMSEAFRoof | 1 | EAF roof is closed; this participates in the State-Off condition. |
| SMSEAFPowerONmin | 0 | No accumulated power-on time - confirms the furnace is currently stopped, not mid-heat. |

### Table 7

| Event status name | EAF Power On |
|---|---|
| State sequence | 2 |
| Active | Yes |
| State-On delay | 5 seconds |
| State-Off delay | 10 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 8

| {SMSEAFActivePower} > 10 |
|---|

### Table 9

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSEAFActivePower > 10 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSEAFActivePower <= 10 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Not applicable - this state uses a direct boolean expression, not a nested IIF | - | - |

### Table 10

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSEAFActivePower | > 10 | EAF active power exceeds 10 MW, confirming the furnace is actively melting rather than idling. The 5s on-delay and 10s off-delay filter out momentary power fluctuations. |

### Table 11

| Event status name | Ladle Car At EAF |
|---|---|
| State sequence | 3 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 12

| IIF({SMSEAFLadleCar} = 1 AND {SMSEAFPowerONmin} > 0, True, IIF({SMSEAFLadleCar} = 0 AND {SMSEAFPowerONmin} > 0, False, Null)) |
|---|

### Table 13

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSEAFLadleCar = 1; SMSEAFPowerONmin > 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSEAFLadleCar = 0; SMSEAFPowerONmin > 0 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 14

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSEAFLadleCar | 1 | Ladle car is in position at the EAF tapping point; participates in the State-On condition. |
| SMSEAFLadleCar | 0 | Ladle car has left the EAF tapping point; participates in the State-Off condition. |
| SMSEAFPowerONmin | > 0 | The furnace has accumulated power-on time, confirming an active melt is underway. |

### Table 15

| Event status name | EAF Tapping |
|---|---|
| State sequence | 4 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 16

| IIF({SMSEAFTapping} = 1 AND {SMSEAFPowerONmin} > 0, True, IIF({SMSEAFTapping} = 0 AND {SMSEAFPowerONmin} >= 0, False, Null)) |
|---|

### Table 17

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSEAFTapping = 1; SMSEAFPowerONmin > 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSEAFTapping = 0; SMSEAFPowerONmin >= 0 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 18

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSEAFTapping | 1 | Tapping is in progress - liquid steel is being poured from the furnace into the ladle. |
| SMSEAFTapping | 0 | Tapping has ended. |
| SMSEAFPowerONmin | > 0 / >= 0 | Confirms power-on time is present (TRUE) or at least non-negative (FALSE), tying tapping to the active heat. |

### Table 19

| Event status name | Ladle Car Move From EAF To LRF |
|---|---|
| State sequence | 5 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 20

| IIF({SMSEAFLadleCar} = 0 AND {SMSLRFLadleCar} = 0 AND {SMSEAFTapping}=1, True, IIF({SMSEAFLadleCar}= 0 AND {SMSLRFLadleCar} = 1, False, Null)) |
|---|

### Table 21

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSEAFLadleCar = 0; SMSLRFLadleCar = 0; SMSEAFTapping = 1 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSEAFLadleCar = 0; SMSLRFLadleCar = 1 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 22

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSEAFLadleCar | 0 | Ladle car has left the EAF position - required for both the ON and OFF branches. |
| SMSLRFLadleCar | 0 | Ladle car has not yet reached the LRF position; participates in the State-On condition. |
| SMSLRFLadleCar | 1 | Ladle car has reached the LRF position; participates in the State-Off condition. |
| SMSEAFTapping | 1 | Tapping had occurred, confirming the ladle now in transit actually received liquid steel from this heat. |

### Table 23

| Event status name | Ladle Car Reach At LRF |
|---|---|
| State sequence | 6 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 24

| IIF({SMSLRFLadleCar} = 1 AND {SMSLRFRoofE1} = 0 AND {SMSLRFArcTime} = 0, True, IIF({SMSLRFLadleCar} = 1 AND {SMSLRFRoofE1} = 1 AND {SMSLRFArcTime} = 0, False, Null)) |
|---|

### Table 25

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSLRFLadleCar = 1; SMSLRFRoofE1 = 0; SMSLRFArcTime = 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSLRFLadleCar = 1; SMSLRFRoofE1 = 1; SMSLRFArcTime = 0 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 26

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSLRFLadleCar | 1 | Ladle car is at the LRF position - required for both branches. |
| SMSLRFRoofE1 | 0 | LRF roof is still open (not yet lowered for treatment); participates in the State-On condition. |
| SMSLRFRoofE1 | 1 | LRF roof has closed; participates in the State-Off condition, marking the end of this waiting state. |
| SMSLRFArcTime | 0 | No arc time yet recorded - treatment has not started. |

### Table 27

| Event status name | LRF Roof Close |
|---|---|
| State sequence | 7 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 28

| IIF({SMSLRFRoofE1} = 0 AND {SMSLRFRoofE3} = 0, True, IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1, False, Null)) |
|---|

### Table 29

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSLRFRoofE1 = 0; SMSLRFRoofE3 = 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSLRFRoofE1 = 1; SMSLRFRoofE3 = 1 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 30

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSLRFRoofE1 | 0 / 1 | LRF roof position indicator E1: 0 = down/closed, 1 = up/open. |
| SMSLRFRoofE3 | 0 / 1 | LRF roof position indicator E3: 0 = down/closed, 1 = up/open. Both indicators must agree to confirm roof position. |

### Table 31

| Event status name | LRF Arcing |
|---|---|
| State sequence | 8 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 32

| IIF({SMSLRFArcTime} > 0 AND {SMSLRFRoofE1} = 0 AND {SMSLRFRoofE3} = 0, True, IIF({SMSLRFArcTime}>0 and {SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1, False, Null)) |
|---|

### Table 33

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSLRFArcTime > 0; SMSLRFRoofE1 = 0; SMSLRFRoofE3 = 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSLRFArcTime > 0; SMSLRFRoofE1 = 1; SMSLRFRoofE3 = 1 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 34

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSLRFArcTime | > 0 | Arc time is accumulating - required for both branches, confirming arcing has started. |
| SMSLRFRoofE1 | 0 / 1 | Roof closed (0) during active arcing; roof open (1) once arcing has finished. |
| SMSLRFRoofE3 | 0 / 1 | Second roof indicator, must agree with E1. |

### Table 35

| Event status name | LRF Roof Open |
|---|---|
| State sequence | 9 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 36

| IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1, True, IIF({SMSLRFRoofE1} = 0 AND {SMSLRFRoofE3} = 0, False, Null)) |
|---|

### Table 37

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSLRFRoofE1 = 1; SMSLRFRoofE3 = 1 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSLRFRoofE1 = 0; SMSLRFRoofE3 = 0 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 38

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSLRFRoofE1 | 0 / 1 | LRF roof position indicator E1 - the mirror image of state 7. |
| SMSLRFRoofE3 | 0 / 1 | LRF roof position indicator E3, must agree with E1. |

### Table 39

| Event status name | Ladle Move From LRF To CCM |
|---|---|
| State sequence | 10 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 40

| IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm1InstantWieght} < 10 AND {SMSLRFArcTime} > 0, True, IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm1InstantWieght} > 75 AND {SMSLRFArcTime} = 0, False, Null)) |
|---|

### Table 41

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSLRFRoofE1 = 1; SMSLRFRoofE3 = 1; SMSCCMArm1InstantWieght < 10; SMSLRFArcTime > 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSLRFRoofE1 = 1; SMSLRFRoofE3 = 1; SMSCCMArm1InstantWieght > 75; SMSLRFArcTime = 0 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 42

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSLRFRoofE1 / E3 | 1 | LRF roof is open, confirming treatment has finished and the ladle is ready to move. |
| SMSCCMArm1InstantWieght | < 10 | Arm 1 ladle weight is still low - the ladle has not yet arrived at CCM. |
| SMSCCMArm1InstantWieght | > 75 | Arm 1 ladle weight has reached a full ladle - arrival is complete, ending this transit state. |
| SMSLRFArcTime | > 0 / = 0 | Confirms arcing occurred (ON) or has been reset for the new heat (OFF). |

### Table 43

| Event status name | Ladle Move From LRF To CCM |
|---|---|
| State sequence | 10 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | No |
| Workflow type | - |
| State-On workflow | - |
| State-Off workflow | - |

### Table 44

| IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm2InstantWieght} < 10 AND {SMSLRFArcTime} > 0, True, IIF({SMSLRFRoofE1} = 1 AND {SMSLRFRoofE3} = 1 AND {SMSCCMArm2InstantWieght} > 75 AND {SMSLRFArcTime} = 0, False, Null)) |
|---|

### Table 45

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSLRFRoofE1 = 1; SMSLRFRoofE3 = 1; SMSCCMArm2InstantWieght < 10; SMSLRFArcTime > 0 | Turn the event state ON | No workflow (live tag read) |
| FALSE | SMSLRFRoofE1 = 1; SMSLRFRoofE3 = 1; SMSCCMArm2InstantWieght > 75; SMSLRFArcTime = 0 | Turn the event state OFF | No workflow (live tag read) |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 46

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSLRFRoofE1 / E3 | 1 | LRF roof is open, confirming treatment has finished and the ladle is ready to move. |
| SMSCCMArm2InstantWieght | < 10 | Arm 2 ladle weight is still low - the ladle has not yet arrived at CCM. |
| SMSCCMArm2InstantWieght | > 75 | Arm 2 ladle weight has reached a full ladle - arrival is complete, ending this transit state. |
| SMSLRFArcTime | > 0 / = 0 | Confirms arcing occurred (ON) or has been reset for the new heat (OFF). |

### Table 47

| Event status name | Ladle At CCM Arm 1 Rest Position |
|---|---|
| State sequence | 11 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 48

| IIF({SMSCCMArm1InstantWieght} > 75 AND {SMSCCMArm1castPosition} = 0, True, IIF({SMSCCMArm1InstantWieght} > 75 AND {SMSCCMArm1castPosition} = 1, False, Null)) |
|---|

### Table 49

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMArm1InstantWieght > 75; SMSCCMArm1castPosition = 0 | Turn the event state ON | Entered |
| FALSE | SMSCCMArm1InstantWieght > 75; SMSCCMArm1castPosition = 1 | Turn the event state OFF | Completed |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 50

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMArm1InstantWieght | > 75 | A full ladle (over 75 tons) is present on Arm 1 - required for both branches. |
| SMSCCMArm1castPosition | 0 | Arm 1 is still in its rest position, before casting; participates in the State-On (Entered) condition. |
| SMSCCMArm1castPosition | 1 | Arm 1 has rotated into the casting position; participates in the State-Off (Completed) condition. |

### Table 51

| Event status name | Ladle At CCM Arm 2 Rest Position |
|---|---|
| State sequence | 11 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 52

| IIF({SMSCCMArm2InstantWieght} > 75 AND {SMSCCMArm2castPosition} = 0, True, IIF({SMSCCMArm2InstantWieght} > 75 AND {SMSCCMArm2castPosition} = 1, False, Null)) |
|---|

### Table 53

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMArm2InstantWieght > 75; SMSCCMArm2castPosition = 0 | Turn the event state ON | Entered |
| FALSE | SMSCCMArm2InstantWieght > 75; SMSCCMArm2castPosition = 1 | Turn the event state OFF | Completed |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 54

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMArm2InstantWieght | > 75 | A full ladle (over 75 tons) is present on Arm 2 - required for both branches. |
| SMSCCMArm2castPosition | 0 | Arm 2 is still in its rest position, before casting; participates in the State-On (Entered) condition. |
| SMSCCMArm2castPosition | 1 | Arm 2 has rotated into the casting position; participates in the State-Off (Completed) condition. |

### Table 55

| Event status name | Turret Rotation |
|---|---|
| State sequence | 12 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 56

| IIF({SMSCCMTurretLubrication} = 1 AND {SMSCCMArm1InstantWieght} > 75, True, IIF({SMSCCMTurretLubrication} = 0 AND {SMSCCMArm1InstantWieght} >75, False, Null)) |
|---|

### Table 57

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMTurretLubrication = 1; SMSCCMArm1InstantWieght > 75 | Turn the event state ON | Entered |
| FALSE | SMSCCMTurretLubrication = 0; SMSCCMArm1InstantWieght > 75 | Turn the event state OFF | Completed |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 58

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMTurretLubrication | 1 | Turret lubrication is running, indicating the turret is actively rotating; participates in the State-On (Entered) condition. |
| SMSCCMTurretLubrication | 0 | Turret lubrication has stopped, indicating rotation has finished; participates in the State-Off (Completed) condition. |
| SMSCCMArm1InstantWieght | > 75 | Confirms a full ladle is being rotated on Arm 1 - required for both branches. |

### Table 59

| Event status name | Turret Rotation |
|---|---|
| State sequence | 12 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 60

| IIF({SMSCCMTurretLubrication} = 1 AND {SMSCCMArm2InstantWieght} > 75, True, IIF({SMSCCMTurretLubrication} = 0 AND {SMSCCMArm2InstantWieght} >75, False, Null)) |
|---|

### Table 61

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMTurretLubrication = 1; SMSCCMArm2InstantWieght > 75 | Turn the event state ON | Entered |
| FALSE | SMSCCMTurretLubrication = 0; SMSCCMArm2InstantWieght > 75 | Turn the event state OFF | Completed |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 62

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMTurretLubrication | 1 | Turret lubrication is running, indicating the turret is actively rotating; participates in the State-On (Entered) condition. |
| SMSCCMTurretLubrication | 0 | Turret lubrication has stopped, indicating rotation has finished; participates in the State-Off (Completed) condition. |
| SMSCCMArm2InstantWieght | > 75 | Confirms a full ladle is being rotated on Arm 2 - required for both branches. |

### Table 63

| Event status name | CCM Arm 1 Casting Position |
|---|---|
| State sequence | 13 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 64

| IIF({SMSCCMArm1castPosition} = 1 and {SMSCCMArm1InstantWieght} > 50, True, IIF({SMSCCMArm1castPosition} = 0 and {SMSCCMArm1InstantWieght} < 50, False, Null)) |
|---|

### Table 65

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMArm1castPosition = 1; SMSCCMArm1InstantWieght > 50 | Turn the event state ON | Entered |
| FALSE | SMSCCMArm1castPosition = 0; SMSCCMArm1InstantWieght < 50 | Turn the event state OFF | Completed |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 66

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMArm1castPosition | 1 | Arm 1 is in the casting position; participates in the State-On (Entered) condition. |
| SMSCCMArm1castPosition | 0 | Arm 1 has left the casting position; participates in the State-Off (Completed) condition. |
| SMSCCMArm1InstantWieght | > 50 | Ladle still holds a significant quantity of liquid steel - casting is genuinely underway. |
| SMSCCMArm1InstantWieght | < 50 | Ladle weight has dropped below half - the ladle is empty or nearly empty, casting is ending. |

### Table 67

| Event status name | CCM Arm 2 Casting Position |
|---|---|
| State sequence | 13 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 68

| IIF({SMSCCMArm2castPosition} = 1 and {SMSCCMArm2InstantWieght} > 50, True, IIF({SMSCCMArm2castPosition} = 0 and {SMSCCMArm2InstantWieght} < 50, False, Null)) |
|---|

### Table 69

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMArm2castPosition = 1; SMSCCMArm2InstantWieght > 50 | Turn the event state ON | Entered |
| FALSE | SMSCCMArm2castPosition = 0; SMSCCMArm2InstantWieght < 50 | Turn the event state OFF | Completed |
| NULL | Neither ON nor OFF condition is satisfied | No explicit transition for this evaluation | No workflow selected |

### Table 70

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMArm2castPosition | 1 | Arm 2 is in the casting position; participates in the State-On (Entered) condition. |
| SMSCCMArm2castPosition | 0 | Arm 2 has left the casting position; participates in the State-Off (Completed) condition. |
| SMSCCMArm2InstantWieght | > 50 | Ladle still holds a significant quantity of liquid steel - casting is genuinely underway. |
| SMSCCMArm2InstantWieght | < 50 | Ladle weight has dropped below half - the ladle is empty or nearly empty, casting is ending. |

### Table 71

| Event status name | Billets Production |
|---|---|
| State sequence | 14 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 72

| {SMSCCMTotalBillets} > 0 AND {SMSCCMTurretControlOff} = 0 |
|---|

### Table 73

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMTotalBillets > 0 AND SMSCCMTurretControlOff = 0 | Turn the event state ON | Entered |
| FALSE | NOT (SMSCCMTotalBillets > 0 AND SMSCCMTurretControlOff = 0) | Turn the event state OFF | Completed |
| NULL | Not applicable — this state uses a direct boolean expression, not a nested IIF | - | - |

### Table 74

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMTotalBillets | > 0 | Billets are being counted, confirming production output exists for the current cast. |
| SMSCCMTurretControlOff | = 0 | Turret control is still active (automatic), confirming billet counting reflects normal production rather than a manual/stopped state. |

### Table 75

| Event status name | CCM Turret Control Off |
|---|---|
| State sequence | 18 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 76

| {SMSCCMTurretControlOff} = 1 |
|---|

### Table 77

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | SMSCCMTurretControlOff = 1 | Turn the event state ON | Entered |
| FALSE | SMSCCMTurretControlOff = 0 | Turn the event state OFF | Completed |
| NULL | Not applicable — this state uses a direct boolean expression, not a nested IIF | - | - |

### Table 78

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| SMSCCMTurretControlOff | 1 | Turret control has been switched off - for example during manual intervention or at the end of a casting sequence. |

### Table 79

| IF(@Status in ('Ladle Move From LRF To CCM','Ladle At CCM Arm 1 Rest Position','Ladle At CCM Arm 2 Rest Position','Turret Rotation'))
BEGIN

    SELECT TOP 1 
    @HeatID = ISNULL(heatid,(
    SELECT TOP 1 A.HeatID 
    FROM [Xstudio_xbatch].[dbo].[SMS_Plant_Process_EventTime] AS A WITH(NOLOCK)
    WHERE A.[Status] IN ('LRF Roof Open') AND A.[StartTime]<b.[StartTime]
    ORDER BY A.CreatedOn DESC))
    FROM [SMS_Plant_Process_EventTime] b WITH(NOLOCK)
    WHERE ID=@p_RecordId 
    ORDER BY CreatedOn DESC

END
 
IF(@Status IN ('CCM Arm 2 Casting Position','CCM Arm 1 Casting Position','Billets Production','CCM Turret Control Off'))
BEGIN

    SELECT TOP 1 @HeatID=ISNULL(heatid,(
    SELECT TOP 1 A.HeatID 
    FROM [Xstudio_xbatch].[dbo].[SMS_Plant_Process_EventTime] AS A WITH(NOLOCK)
    WHERE A.[Status] IN ('Ladle At CCM Arm 1 Rest Position','Ladle At CCM Arm 2 Rest Position') AND A.[StartTime]<b.[StartTime] ORDER BY A.CreatedOn DESC))
    FROM [SMS_Plant_Process_EventTime] b WITH(NOLOCK)
    WHERE ID=@p_RecordId ORDER BY CreatedOn DESC

END
 
SELECT @ActualHeatID = @HeatID - 1
 
UPDATE [Xstudio_xbatch].[dbo].[SMS_Plant_Process_EventTime] 
SET ActualHeatID = @ActualHeatID, ModifiedOn = GETDATE() 
WHERE ID=@p_RecordId
 
IF(@Status in ('CCM Arm 2 Casting Position','CCM Arm 1 Casting Position'))
BEGIN

    DECLARE @LiquidMetalWeight DECIMAL(18,4)
 
    SELECT @LiquidMetalWeight=LiquidMetalWeight 
    FROM LRF_Per_Heat WITH(NOLOCK) 
    WHERE HeatID=@ActualHeatID
 
    UPDATE CCM_Data SET LiquidSteelWeight=@LiquidMetalWeight
 
END |
|---|