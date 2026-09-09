---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-work-order-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Work_Order_Trn_Tbl.CampaignID -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignID-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Work_Order_Trn_Tbl.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
