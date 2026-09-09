---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: area-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Area_Mst_Tbl.ParentID -> Plant_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-Plant_Mst_Tbl
Provenance: xstudio_configuration_relationship (2 source row(s))

## Area_Mst_Tbl.ShiftID -> XStudio_Shift_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ShiftID-XStudio_Shift_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
