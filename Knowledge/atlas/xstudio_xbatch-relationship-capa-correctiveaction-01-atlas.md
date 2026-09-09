---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: capa-correctiveaction part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## CAPA_CorrectiveAction.CAPANO -> RMShiftDelayEntry_CAPA.CAPANO
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CAPANO-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## CAPA_CorrectiveAction.ParentID -> RMShiftDelayEntry_CAPA.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))
