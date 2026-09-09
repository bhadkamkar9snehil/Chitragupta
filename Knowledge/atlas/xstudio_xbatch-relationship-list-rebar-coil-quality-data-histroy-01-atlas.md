---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: list-rebar-coil-quality-data-histroy part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## List_Rebar_Coil_Quality_Data_Histroy.BilletGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## List_Rebar_Coil_Quality_Data_Histroy.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## List_Rebar_Coil_Quality_Data_Histroy.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## List_Rebar_Coil_Quality_Data_Histroy.ShiftInChargeOperation -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ShiftInChargeOperation-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
