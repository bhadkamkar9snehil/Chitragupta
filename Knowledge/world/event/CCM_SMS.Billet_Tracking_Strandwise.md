---
type: event
title: "CCM_SMS/Billet Tracking Strandwise"
built: "2026-09-24T11:36:36"
---

# CCM_SMS/Billet Tracking Strandwise

Area CCM_SMS. Active.
Creates and updates rows in Billet_Track_Per_Strand.

## State 1: Strand 1 Billet Cut

Condition: `{Std1BilletCutCompleted}=1`
Workflow status on: Entered, off: Completed.

## State 1: Strand 1 Billet Generate

Condition: `IIF({Std1BilletCounter} >= 0 AND {Std1BilletLiftDown} = 0, True, IIF({Std1BilletCounter} >= 0 AND {Std1BilletLiftDown} = 1, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: TotalBilletCounter -> StrandwiseCount, Std1BilletCounter -> S1BilletCount

## State 1: Strand 2 Billet Cut

Condition: `{Std2BilletCutCompleted}=1`
Workflow status on: Entered, off: Completed.

## State 1: Strand 2 Billet Generate

Condition: `IIF({Std2BilletCounter} >= 0 AND {Std2BilletLiftDown} = 0, True, IIF({Std2BilletCounter} >= 0 AND {Std2BilletLiftDown} = 1, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: Std2BilletCounter -> S2BilletCount, TotalBilletCounter -> StrandwiseCount

## State 1: Strand 3 Billet Cut

Condition: `{Std3BilletCutCompleted}=1`
Workflow status on: Entered, off: Completed.

## State 1: Strand 3 Billet Generate

Condition: `IIF({Std3BilletCounter} >= 0 AND {Std3BilletLiftDown} = 0, True, IIF({Std3BilletCounter} >= 0 AND {Std3BilletLiftDown} = 1, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: TotalBilletCounter -> StrandwiseCount, Std3BilletCounter -> S3BilletCount

## State 1: Strand 4 Billet Cut

Condition: `{Std4BilletCutCompleted}=1`
Workflow status on: Entered, off: Completed.

## State 1: Strand 4 Billet Generate

Condition: `IIF({Std4BilletCounter} >= 0 AND {Std4BilletLiftDown} = 0, True, IIF({Std4BilletCounter} >= 0 AND {Std4BilletLiftDown} = 1, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: Std4BilletCounter -> S4BilletCount, TotalBilletCounter -> StrandwiseCount

## State 1: Strand 5 Billet Cut

Condition: `{Std5BilletCutCompleted}=1`
Workflow status on: Entered, off: Completed.

## State 1: Strand 5 Billet Generate

Condition: `IIF({Std5BilletCounter} >= 0 AND {Std5BilletLiftDown} = 0, True, IIF({Std5BilletCounter} >= 0 AND {Std5BilletLiftDown} = 1, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: Std5BilletCounter -> S5BilletCount, TotalBilletCounter -> StrandwiseCount

## State 1: Strand 6 Billet Cut

Condition: `{Std6BilletCutCompleted}=1`
Workflow status on: Entered, off: Completed.

## State 1: Strand 6 Billet Generate

Condition: `IIF({Std6BilletCounter} >= 0 AND {Std6BilletLiftDown} = 0, True, IIF({Std6BilletCounter} >=0 AND {Std6BilletLiftDown} = 1, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: Std6BilletCounter -> S6BilletCount, TotalBilletCounter -> StrandwiseCount

## State 2: Heat Change

Condition: `{TotalBilletCounter} = 0 and {Std1BilletCounter} = 0 and {Std2BilletCounter} = 0 and {Std3BilletCounter} = 0 and {Std4BilletCounter} = 0 and {Std5BilletCounter} = 0 and {Std6BilletCounter} = 0`
Workflow status on: Entered, off: Completed.

## State 2: Strand 1 Billet Produced

Condition: `{Std1BilletLiftDown}=0`
Workflow status on: Entered, off: Completed.

## State 2: Strand 2 Billet Produced

Condition: `{Std2BilletLiftDown}=0`
Workflow status on: Entered, off: Completed.

## State 2: Strand 3 Billet Produced

Condition: `{Std3BilletLiftDown}=0`
Workflow status on: Entered, off: Completed.

## State 2: Strand 4 Billet Produced

Condition: `{Std4BilletLiftDown}=0`
Workflow status on: Entered, off: Completed.

## State 2: Strand 5 Billet Produced

Condition: `{Std5BilletLiftDown}=0`
Workflow status on: Entered, off: Completed.

## State 2: Strand 6 Billet Produced

Condition: `{Std6BilletLiftDown}=0`
Workflow status on: Entered, off: Completed.
