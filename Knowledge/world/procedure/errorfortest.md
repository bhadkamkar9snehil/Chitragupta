---
type: procedure
title: "errorfortest"
built: "2026-09-24T11:36:36"
---

# errorfortest

Parameters: @SYSTEMID varchar, @USERID varchar, @RECORDID varchar, @STATUS varchar.

## Writes

- XMES_Campaign_Plan_Mst: Status

## Reads

- XMES_Campaign_Plan_Mst: CampaignId, ID, IsDeleted
- XMES_RM_Campaign_Plan_Trn: CampaignId, IsDeleted, Validation
