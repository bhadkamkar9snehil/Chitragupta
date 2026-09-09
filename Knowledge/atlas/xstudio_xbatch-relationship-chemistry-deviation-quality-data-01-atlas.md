---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: chemistry-deviation-quality-data part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Chemistry_Deviation_Quality_Data.Grade -> XMES_SMS_Grade_Protocol_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Chemistry_Deviation_Quality_Data.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## Chemistry_Deviation_Quality_Data.ShiftIncharge -> XStudio_User_Mst_Tbl.FullName
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ShiftIncharge-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
