---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-recipe-connection-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Recipe_Connection_Mst_Tbl.ParentID -> XBatch_Recipe_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
