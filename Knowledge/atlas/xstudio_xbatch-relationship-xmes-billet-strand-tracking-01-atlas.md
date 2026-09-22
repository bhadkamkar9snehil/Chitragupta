---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-billet-strand-tracking part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Billet_Strand_tracking.EndProduct -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndProduct-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Strand_tracking.ParentID -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> Many
Relation: ParentID-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
