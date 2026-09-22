---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-billet-movement-dtl-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Billet_Movement_Dtl_Tbl.ChargingBedBilletNo -> XMES_Live_Billet_Charging_Bed.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ChargingBedBilletNo-XMES_Live_Billet_Charging_Bed
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.Section1BilletNo -> XMES_Live_Charging_SECT1.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section1BilletNo-XMES_Live_Charging_SECT1
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.Section2BilletNo -> XMES_Live_Charging_SECT2.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section2BilletNo-XMES_Live_Charging_SECT2
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.ZonewiseBilletNo -> XMES_RM_Furnace_Billet_Trn_Tbl.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ZonewiseBilletNo-XMES_RM_Furnace_Billet_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
