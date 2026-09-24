---
type: procedure
title: "Sp_Grade_Test_Mapping"
built: "2026-09-24T11:36:36"
---

# Sp_Grade_Test_Mapping

Parameters: @RecordId varchar.

## Writes

- Grade_Characteristics_Mapping: AcceptableLowerLimit, AcceptableUpperLimit, CharacteristicName, GradeName, ParentID, TestName

## Reads

- Grade_Characteristics: CharacteristicName, IsDeleted
- Grade_Characteristics_Mapping: IsDeleted
- Grade_Test_Mapping: GradeName, ID, IsDeleted, TestName
