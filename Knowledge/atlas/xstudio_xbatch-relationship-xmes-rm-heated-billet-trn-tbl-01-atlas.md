---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-rm-heated-billet-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_RM_Heated_Billet_trn_tbl.Campaignid -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Campaignid-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.ProductType -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProductType-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.Workorderid -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Workorderid-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
