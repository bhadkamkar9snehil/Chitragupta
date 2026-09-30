---
type: procedure
title: "XMES_Duplicate_Grade_Protocol_Mst_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Duplicate_Grade_Protocol_Mst_Usp

Parameters: @GradeID varchar, @SectionID varchar, @ID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Grade_Master: GradeName, ID, IsDeleted
- XMES_SMS_Grade_Protocol_Mst_Tbl: ChemistryID, ID, IsDeleted

## Writes (named in its SQL text)

- XMES_Grade_Protocol_CCM_Parameters_Mst_Tbl
- XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl
- XMES_Grade_Protocol_LRF_Parameters_Mst_Tbl
- XMES_Grade_Protocol_Super_Heat_Speed_Nozzle_Mst_Tbl
- XMES_Grade_Protocol_Tapping_Additions_Mst_Tbl
- XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl
- XMES_SMS_Grade_Protocol_Mst_Tbl
