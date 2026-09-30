---
type: procedure
title: "Sp_Sample_Characteristics_I_Values"
built: "2026-09-24T11:36:36"
---

# Sp_Sample_Characteristics_I_Values

Parameters: @Recordid varchar.

## Writes

- Grade_FillSample_Data: AcceptableLowerLimit, AcceptableUpperLimit, CharacteristicName, Gradename, ParentID, TestName, Value

## Reads

- EAF_LogSheet_Quantity: Grade, ID, TestName
- Grade_Characteristics_Mapping: AcceptableLowerLimit, AcceptableUpperLimit, CharacteristicName, GradeName, IsDeleted, TestName
