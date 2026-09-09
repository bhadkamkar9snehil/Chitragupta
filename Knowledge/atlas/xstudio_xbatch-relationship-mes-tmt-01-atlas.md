---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: mes-tmt part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## MES_TMT.ID -> MES_TMT_Small_Cut.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ID-MES_TMT_Small_Cut
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_TMT.workorder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: workorder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
