---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: E part 2

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Electricity_Meter_Timing.RateBand -> Rate_Band_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: RateBand-Rate_Band_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Timing.Year -> Year_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Year-Year_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Equipment_Wise_Delay.DelayAgency -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayAgency-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Equipment_Wise_Delay.EquipmentName -> Equipment.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentName-Equipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## Equipment_Wise_Delay.ParentID -> Agency_Wise_Delay.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-Agency_Wise_Delay
Provenance: xstudio_configuration_relationship (1 source row(s))

## Equipment_Wise_Delay.SubEquipmentName -> SubEquipment.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SubEquipmentName-SubEquipment
Provenance: xstudio_configuration_relationship (1 source row(s))
