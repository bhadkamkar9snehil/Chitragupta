---
type: procedure
title: "XSTUDIO_WORKFLOW_C7EA6F22-24BB-490A-A748-6AE14C39B81D_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_C7EA6F22-24BB-490A-A748-6AE14C39B81D_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- XMES_Campaign_Plan_Mst: CampaignId, ID, IsDeleted, UploadStatus
- XMES_RM_Campaign_Plan_Trn: AllFIleUpload, BundlesweightTon, CampaignId, ContractNo, Country, Customer, EntryDateTime, Grade, ID, IsProcessed, ItemNo, Length, MaterialNo, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, NegativeTolerance, NumberOfPiecesInBundles, ParentID, PositiveTolerance, Remarks, ReportDate, SONumber, Section, Size, Specification, TagDetails, Validation, WorkorderNo

## Writes (named in its SQL text)

- XMES_RM_Campaign_Plan_Trn
