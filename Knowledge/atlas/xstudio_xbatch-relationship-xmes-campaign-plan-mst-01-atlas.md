---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-campaign-plan-mst part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Campaign_Plan_Mst.ID -> XMES_RM_Campaign_Plan_Trn.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_RM_Campaign_Plan_Trn
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Campaign_Plan_Mst.Productname -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Productname-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
