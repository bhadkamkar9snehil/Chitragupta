---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: G part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Grade_Characteristics_Mapping.CharacteristicName -> Grade_Characteristics.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CharacteristicName-Grade_Characteristics
Provenance: xstudio_configuration_relationship (1 source row(s))

## Grade_Characteristics_Mapping.GradeName -> Steel_Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeName-Steel_Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Grade_Characteristics_Mapping.TestName -> Grade_Test_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TestName-Grade_Test_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Grade_FillSample_Data.ParentID -> Steel_Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-Steel_Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Grade_Master.GradeType -> Grade_Type_Master.GradeType
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeType-Grade_Type_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Grade_Test_Mapping.GradeName -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeName-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Grade_Test_Mapping.TestName -> Grade_Test_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TestName-Grade_Test_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
