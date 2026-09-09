---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: agency-wise-delay part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Agency_Wise_Delay.Agency -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Agency-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Agency_Wise_Delay.ID -> RMShiftDelayEntry_CAPA.AgencyTransactionid
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## Agency_Wise_Delay.ParentID -> ShiftDelayEntry.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-ShiftDelayEntry
Provenance: xstudio_configuration_relationship (1 source row(s))
