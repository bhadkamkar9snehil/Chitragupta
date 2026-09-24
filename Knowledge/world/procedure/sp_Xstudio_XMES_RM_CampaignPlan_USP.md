---
type: procedure
title: "sp_Xstudio_XMES_RM_CampaignPlan_USP"
built: "2026-09-24T11:36:36"
---

# sp_Xstudio_XMES_RM_CampaignPlan_USP

Parameters: @recordid varchar.

## Writes

- XMES_Campaign_Plan_Mst: MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Status
- XMES_RM_Campaign_Plan_Trn: CampaignId

## Reads

- XMES_Campaign_Plan_Mst: CampaignId, CreatedOn, IsDeleted
- XMES_RM_Campaign_Plan_Trn: IsDeleted, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT
