---
type: procedure
title: "Xmes_Billet_Tracking_Sap_Posted_Usp"
built: "2026-09-24T11:36:36"
---

# Xmes_Billet_Tracking_Sap_Posted_Usp

Parameters: @systemid varchar, @userid varchar, @RecordId varchar, @status varchar.

## Writes

- XMES_Billet_Strand_tracking: ModifiedOn, Status
- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus, ModifiedOn

## Reads

- XMES_Billet_Strand_tracking: BIlletNo, IsDeleted
- XMES_Live_Billet_Charging_Bed: BilletNo, IsDeleted
