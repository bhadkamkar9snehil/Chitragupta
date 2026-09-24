---
type: procedure
title: "XMES_RM_Tag_Printing_I_TRN"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Tag_Printing_I_TRN

Parameters: @Productid varchar, @CampaignID varchar.

## Writes

- XMES_RM_Tag_Printing_TRN: AssignedUserID, Campaignid, CreatedBy, CreatedOn, DbSyncStatus, Entrydatetime, Heading1, Heading10, Heading11, Heading12, Heading13, Heading14, Heading2, Heading3, Heading4, Heading5, Heading6, Heading7, Heading8, Heading9, HostAddress, ID, IsDeleted, IsSystem, Material, MobileSyncStatus, ModifiedBy, ModifiedOn, Product, Sequence1, Sequence10, Sequence11, Sequence12, Sequence13, Sequence14, Sequence2, Sequence3, Sequence4, Sequence5, Sequence6, Sequence7, Sequence8, Sequence9, Source, Specification, isVisible1, isVisible10, isVisible11, isVisible12, isVisible13, isVisible14, isVisible2, isVisible3, isVisible4, isVisible5, isVisible6, isVisible7, isVisible8, isVisible9

## Reads

- Product_Master: ID, IsDeleted, Name
- XMES_RM_Tag_Printing_MST: IsDeleted, Product
