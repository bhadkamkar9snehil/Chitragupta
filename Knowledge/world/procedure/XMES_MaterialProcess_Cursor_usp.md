---
type: procedure
title: "XMES_MaterialProcess_Cursor_usp"
built: "2026-09-24T11:36:36"
---

# XMES_MaterialProcess_Cursor_usp

Parameters: @Campaignid varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_RM_Campaign_Plan_Trn: Validation

## Reads

- Product_Master: ID, Name
- XMES_Campaign_Plan_Mst: CampaignId, ID, IsDeleted, Productname, Size
- XMES_RM_Campaign_Plan_Trn: CampaignId, ID, IsDeleted, MaterialNo

## What its own log shows

991 log rows, 2026-05-30 10:46 to 2026-08-21 15:51.

Steps:
- 1 Entered
- 2 Get Size and Product Name From Campaign Plan and Product master using campaingID Start
- 3 Get Size and Product Name From Campaign Plan and Product master using campaingID End
- 4 Set material cursor on id and material of Rm Campaign plan transaction using Campaign ID Start
- 5 Close and deallocate Material Cursor Start
- 5 Set material cursor on id and material of Rm Campaign plan transaction using Campaign ID End
- 5 Update validation in RM Campaign Plan Transaction when Product is Rebar AND Material contains size 25.00 Start
- 5 Update validation in RM Campaign Plan Transaction when Product is Rebar AND Material contains size 8.00 Start
- 5 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 10.00 Start
- 5 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 25.00 Start
- 5 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 5.50 Start
- 5 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 8.00 Start
- 5 Update validation in RM Campaign Plan Transaction when Product is Round Bar but Material does not contain size 8.00 Start
- 5 Update validation in RM Campaign Plan Transaction when Product is WRM AND Material contains size 5.50 Start
- 6 Close and deallocate Material Cursor End
- 6 Open Material Cursor Start
- 6 Update validation in RM Campaign Plan Transaction when Product is Rebar AND Material contains size 25.00 End
- 6 Update validation in RM Campaign Plan Transaction when Product is Rebar AND Material contains size 8.00 End
- 6 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 10.00 End
- 6 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 25.00 End
- 6 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 5.50 End
- 6 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 8.00 End
- 6 Update validation in RM Campaign Plan Transaction when Product is Round Bar but Material does not contain size 8.00 End
- 6 Update validation in RM Campaign Plan Transaction when Product is WRM AND Material contains size 5.50 End
- 7 Close and deallocate Material Cursor End
- 7 Fetch MaterialD and Material Name after Execute Cursor queries Start
- 7 Open Material Cursor End
- 7 Update validation in RM Campaign Plan Transaction when Product is Rebar AND Material contains size 25.00 Start
- 7 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 10.00 Start
- 7 Update validation in RM Campaign Plan Transaction when Product is Rebar but Material does not contain size 25.00 Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_MaterialProcess_Cursor_usp @Campaignid='F979CC93-F7BA-4921-9D5C-A570BA12CA90'`
