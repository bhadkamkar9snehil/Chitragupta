---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-rm-campaign-plan-trn part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_RM_Campaign_Plan_Trn.Customer -> XBatch_Customer_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Customer-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.MaterialNo -> XBatch_Material_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialNo-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.ParentID -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.SONumber -> XBatch_Sales_Order_Mst_Tbl.SalesOrderNumber
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SONumber-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.WorkorderNo -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkorderNo-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
