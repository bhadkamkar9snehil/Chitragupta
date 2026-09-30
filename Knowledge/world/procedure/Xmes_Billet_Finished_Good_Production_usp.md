---
type: procedure
title: "Xmes_Billet_Finished_Good_Production_usp"
built: "2026-09-24T11:36:36"
---

# Xmes_Billet_Finished_Good_Production_usp

Parameters: @systemid varchar, @userid varchar, @RecordId varchar, @status varchar.

## Writes

- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus

## Reads

- Product_Master: ID, Name
- RM_Operator_HeatSelection: CampaignId, ID
- XMES_Billet_Strand_tracking: BIlletNo, ID
- XMES_Campaign_Plan_Mst: ID, Productname
- XMES_Live_Billet_Charging_Bed: BilletNo, ID, IsDeleted, ParentID

## Calls

- MES_M_Strand_TMT
- MES_M_Strand_WRM
