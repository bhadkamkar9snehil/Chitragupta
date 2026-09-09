---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rm-operator-heatselection part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RM_Operator_HeatSelection.CampaignId -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignId-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Operator_HeatSelection.length -> XBatch_Work_Order_Mst_Tbl.Length
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> Many
Relation: length-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Operator_HeatSelection.workorder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: workorder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
