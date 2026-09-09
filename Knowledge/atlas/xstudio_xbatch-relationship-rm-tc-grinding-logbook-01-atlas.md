---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rm-tc-grinding-logbook part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RM_TC_Grinding_Logbook.CNCOperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CNCOperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_TC_Grinding_Logbook.RingNo -> RM_Ring_No_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: RingNo-RM_Ring_No_MST
Provenance: xstudio_configuration_relationship (1 source row(s))
