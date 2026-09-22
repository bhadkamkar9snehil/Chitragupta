---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rmshiftdelayentry-capa part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RMShiftDelayEntry_CAPA.Agency -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Agency-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.AgencyAfterCAPA -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AgencyAfterCAPA-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.AgencyBeforeCAPA -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AgencyBeforeCAPA-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.DelayTransactionid -> ShiftDelayEntry.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayTransactionid-ShiftDelayEntry
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.Equipment -> Equipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Equipment-Equipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.ID -> CAPA_CorrectiveAction.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-CAPA_CorrectiveAction
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.Photos -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Photos-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.ProposedAction -> CAPA_PreventiveAction.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ProposedAction-CAPA_PreventiveAction
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.Responsibility -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Responsibility-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.SubEquipment -> SubEquipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SubEquipment-SubEquipment
Provenance: xstudio_configuration_relationship (1 source row(s))
