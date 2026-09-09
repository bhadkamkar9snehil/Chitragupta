---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-rm-tag-printing-trn part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_RM_Tag_Printing_TRN.Campaignid -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Campaignid-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Tag_Printing_TRN.Product -> Product_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Product-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
