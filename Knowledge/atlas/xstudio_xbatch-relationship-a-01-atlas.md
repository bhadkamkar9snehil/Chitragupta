---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: A part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Actual_Primary_Current.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Actual_Primary_Current.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Actual_Secondary_Current.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Actual_Secondary_Current.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

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
