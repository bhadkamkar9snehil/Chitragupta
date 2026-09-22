---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: procedure-task-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Procedure_Task_Mst_Tbl.EntityID -> XStudio_Entities_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EntityID-XStudio_Entities_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Procedure_Task_Mst_Tbl.PageID -> XStudio_Page_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: PageID-XStudio_Page_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Procedure_Task_Mst_Tbl.ViewPageID -> XStudio_Page_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ViewPageID-XStudio_Page_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
