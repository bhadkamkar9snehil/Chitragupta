---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-storage-rack-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Storage_Rack_Mst_Tbl.ParentID -> XBatch_Storage_Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Storage_Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
