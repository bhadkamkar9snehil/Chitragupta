---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: shiftdelayentry part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## ShiftDelayEntry.AreaName -> DelayAgency_Master.AreaName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaName-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.DelayAgency -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayAgency-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.DelaySubtypeid -> DelaySubType_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelaySubtypeid-DelaySubType_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.DelayType -> DelayTypeMST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayType-DelayTypeMST
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.EquipmentName -> Equipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentName-Equipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.ID -> RMShiftDelayEntry_CAPA.DelayTransactionid
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.ModifiedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ModifiedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.OperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: OperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.ShiftManager -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ShiftManager-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.SubEquipmentName -> SubEquipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SubEquipmentName-SubEquipment
Provenance: xstudio_configuration_relationship (1 source row(s))
