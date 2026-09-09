---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: capa-problemsolvingteam part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## CAPA_ProblemSolvingTeam.Name -> XStudio_User_Mst_Tbl.FullName
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Name-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CAPA_ProblemSolvingTeam.ParentID -> RMShiftDelayEntry_CAPA.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))
