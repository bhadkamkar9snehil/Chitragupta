# CCM Per Heat Event Doc

*Extracted from `CCM Per Heat Event Doc.docx` -- real vendor handover doc, not invented.*

SITC OF X-FORCE HISTORIAN AND DASHBOARD DEVELOPMENT
SOHAR STEEL OMAN
Declaration
This Project Handover Document is intended only for personnel who already have a working knowledge of the X-Studio framework and related technical concepts.
The reader is expected to have prior knowledge of the X-Studio Event Framework, Workflows, Asset Structure, Database Structure, SQL Logic, and Stored Procedures. This document is prepared as a project-specific technical handover and reference document and is not intended to provide basic or introductory training on these concepts.
The document focuses on the project-specific implementation, configurations, process flows, database objects, SQL logic, workflows, and related technical details required for Project Support, Maintenance, Troubleshooting, and Further Development.
Therefore, readers should have sufficient prior knowledge of X-Studio and the above-mentioned technical areas to effectively understand and utilize the information provided in this document.

# CCM – Per Heat Data Insert Flow


## 1. Overview

This section describes the event configuration and insert condition used for capturing CCM per-heat data. The event configuration is based on the CCM_Per_Heat event, and two parallel states - Arm 1 Cast Position and Arm 2 Cast Position - are used to identify the condition under which per-heat data is captured and stored for each casting arm.

## 2. Event Configuration


### 2.1 Event Entity

The main event data is stored in the CCM_Per_Heat entity. This entity stores all required CCM per-heat data captured for each heat. This data is stored when either the Arm 1 Cast Position or Arm 2 Cast Position state condition becomes true.

### 2.2 Event Master

The Event Master maps the Event Entity with the event configuration entity. For the CCM per-heat data flow, the CCM_Per_Heat process event is mapped to the CCM_Per_Heat transaction entity, as shown below.

### 2.3 Event Configuration Entity

The Event Configuration Entity defines the configuration for the CCM_Per_Heat event. In Attributes, the required tag attributes are defined. In Tag Mapping, each tag attribute is mapped to its corresponding tag. In State, the conditions that trigger the event - one per casting arm - are configured.

### 2.4 Event Configuration Tags


## 3. Data Insert Condition

Per-heat data insertion for CCM is controlled by two parallel states configured against the CCM_Per_Heat event configuration - one for each casting arm. Each state uses the same nested True/False/Null structure as the EAF condition, evaluated independently per arm:
Arm 1 Cast Position (State Sequence 1):
Arm 2 Cast Position (State Sequence 2):
For both states, when the respective arm's cast position is 1 and its ladle weight exceeds 10 tons, the state becomes active (True) and the workflow transitions from Entered to Completed using the WorkflowStatus attribute. When the cast position is 0 and the ladle weight is 0, the state is inactive (False). Any other combination evaluates to Null. The workflow itself is defined against the CCM_Per_Heat entity under the name "CCM Per Heat CCM HeatNo insert" (Application: DEFAULT), as shown below.

## 4. Per Heat Data Insert Flow

When either the Arm 1 or Arm 2 Cast Position state is triggered, the configured tag attributes are evaluated using the corresponding event state condition. If the condition evaluates to True, the mapped CCM per-heat tag values are captured and inserted into the CCM_Per_Heat entity for the current heat.

### 4.1 Workflow Entered State - Stored Procedure Action

When the workflow action runs, it resolves the active heat from the most recent CCM casting-position event, retrieves the running CCM work order and sales order details, pulls the liquid-metal weight and lot number from the corresponding LRF_Per_Heat record, posts a liquid-metal consumption transaction where applicable, sets the CCM work order start time, and updates CCM_Data with the heat number and steel grade.

### 4.2 Workflow Entered SQL Action Details

1. Variable initialization - The DECLARE statement creates variables for work-order and sales-order identifiers, a fixed customer ID, the recording user ID, and the plant number used later in the action.
2. Active heat resolution - The subquery on SMS_Plant_Process_EventTime finds the most recently created event with a status of either 'CCM Arm 1 Casting Position' or 'CCM Arm 2 Casting Position', and assigns its ActualHeatID to @HeatID. This allows the same action to serve both casting arms.
3. Work order and sales order retrieval - The query on XBatch_Work_Order_Mst_Tbl retrieves the ID, sales order, grade, and material name of the running, non-deleted CCM work order.
4. Data-list action - SMS_Data_list_View is executed as part of the workflow action.
5. Liquid-metal and lot data retrieval - A further DECLARE block introduces variables for the lot number, liquid-metal quantity, GLS material, and GLS work order. The subquery on LRF_Per_Heat retrieves the most recent record for the current heat, returning the liquid-metal weight, a generated lot number in the format GLS_<HeatID>, the heat report date, and the associated work order.
6. Report date fallback - If @HeatReportDate or @ReportDate is null, they default to the current date and its formatted string equivalent respectively.
7. Liquid-metal consumption posting - When @liquidMetal is greater than zero, the material name is resolved from the item configured on the GLS work order, and XBatch_I_Material_Consume_NoBOM_USP posts a consumption transaction for that material using the generated lot number and quantity.
8. CCM work-order start-time update - The UPDATE sets StartTime on the running CCM work order to @StartTime, but only where StartTime has not already been set, recording the modification time, user, and source as 'T-SQL'.
9. CCM_Data heat and grade update - The final UPDATE writes the resolved heat ID and steel grade to CCM_Data, associating the current heat and grade with the CCM casting record.
Note:  This extract depends on variables declared or assigned elsewhere in the complete workflow procedure, including @StartTime, @HeatID, @WorkOrder, @Grade, @Material, @p_UserId, and @p_RecordId. Because the same action serves both Arm 1 and Arm 2 states, confirm that @HeatID always resolves to the intended heat when both arms are active concurrently.

### 4.3 Workflow Completed State - Stored Procedure Action

When the workflow reaches the completed state, this action records the casting date and time for the first ladle in the sequence, updates the latest spectro sample flag, falls back to the EAF heat report date if needed, updates life-element and life-tracker records, and calculates the per-heat temperature for CCM.

### 4.4 Workflow Completed SQL Action Details

1. First-ladle casting date/time - When @LadleSequence is 0 - indicating the first ladle in the casting sequence - CCM_Data is updated with the casting date and time, formatted from @StartTime, so the sequence's start is recorded only once.
2. Spectro sample flag update - Quality_Spectro_IsLatestSample_Update_Usp is executed to update the latest-sample flag used by the quality/spectrometer module.
3. Heat report date fallback from EAF - If @HeatReportDate is still null and a non-null heat report date exists on the corresponding EAF_PER_HEAT record, that date and report-date string are retrieved and used, with a further fall back to the current date if still unavailable.
4. Life-element batch update - As with the EAF and LRF flows, active life elements configured for automatic data capture under the specified parent ID have LastUsedBatch updated to the current heat ID, with the modification timestamp and source recorded.
5. Life-tracker activation - The corresponding life-tracker register is set to Status = 'Active' with Source = 'T-SQL', and the modifying user and timestamp are recorded.
6. Per-heat temperature calculation - XMES_SMS_Temperature_Per_Heat_USP is executed for the CCM area using the current heat's start and end times, calculating the per-heat temperature for CCM.
Note:  This SQL extract relies on additional variables from the surrounding workflow procedure, including @HeatID, @LadleSequence, @StartTime, @EndTime, @HeatReportDate, @ReportDate, and @p_UserId. Confirm that all these variables are declared and assigned before this action executes.

---
## Tables (real technical detail -- tag mappings, state configs, condition logic)


### Table 1

| Project | SITC of X-Force Historian and Dashboard Development for Sohar Steel Oman |
|---|---|
| Prepared By | Mahesh Udar |
| Document Type | CCM Per Heat Data Insert Flow |
| Handover Date |  |
| Handover To |  |
| Document Version | 1.0 |

### Table 2

| Attribute | Tag Name |
|---|---|
| CCM Arm1Ladle Weight | CCM_ARM_1_LADLE_WEIGHT_TON_PRM |
| CCM Arm2LadleWeight | CCM_ARM_2_LADLE_WEIGHT_TON_PRM |
| CCMArm1CastPosition | CCM_ARM_1_CAST_POSITION_STATUS |
| CCMArm1Consumption | CCM_TURRET_ARM_1_CONSUMED_TON_PRM |
| CCMArm2CastPosition | CCM_ARM_2_CAST_POSITION_STATUS |
| CCMArm2Consumption | CCM_TURRET_ARM_2_CONSUMED_TON_PRM |
| CCMHeatID | CCM_HEAT_NUMBER_PRM |
| CCMLadleSequence | CCM_LADLE_SEQUENCE_PRM |
| TundishTemperature | CCM_TUNDISH_TEMPERATURE_PRM |

### Table 3

| IIF({CCMArm1CastPosition} = 1 AND {CCM Arm1Ladle Weight} > 10, True, IIF({CCMArm1CastPosition} = 0 AND {CCM Arm1Ladle Weight} = 0, False, Null)) |
|---|

### Table 4

| IIF({CCMArm2CastPosition} = 1 AND {CCM Arm2LadleWeight} > 10, True, IIF({CCMArm2CastPosition} = 0 AND {CCM Arm2LadleWeight} = 0, False, Null)) |
|---|

### Table 5

| DECLARE @WORID VARCHAR(36), 
        @WONO VARCHAR(36), 
        @SalesNo VARCHAR(100), 
        @SalesID VARCHAR(36), 
        @CustomerID VARCHAR(36) = 'C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3', 
        @UserID VARCHAR(36) = 'A6E924D5-B2F0-4A5F-9717-3A63F6190358', 
        @PlantNo VARCHAR(100) = '7502';
 
SET @HeatID = (SELECT TOP 1 [ActualHeatID] FROM [SMS_Plant_Process_EventTime] WITH(NOLOCK) 
WHERE [Status] IN ('CCM Arm 1 Casting Position','CCM Arm 2 Casting Position') 
ORDER BY CreatedOn DESC);
 
SELECT @WorkOrder = [ID], 
       @SalesOrder = [SalesOrder], 
       @Grade = [Grade], 
       @Material = [MaterialName] 
FROM [XBatch_Work_Order_Mst_Tbl] WITH(NOLOCK)
WHERE [Status] = 'Running' AND [Equipment] = 'CCM' AND [IsDeleted] = 0;
 
EXEC [SMS_Data_list_View];
 
DECLARE @LotNo VARCHAR(500), 
        @liquidMetal DECIMAL(18,4),
        @glsMAterial varchar(200),
        @glsWorkOrder varchar(36);
 
SELECT @glsWorkOrder=WorkOrder,
       @liquidMetal = [LiquidMetalWeight],
       @LotNo = [LotNo], 
       @HeatReportDate = [HeatReportDate], 
       @ReportDate = [HeatReportDate] 
FROM (SELECT TOP 1 ISNULL([LiquidMetalWeight], 0) AS [LiquidMetalWeight], CONCAT('GLS_', CAST(@HeatID AS INT)) AS [LotNo], [HeatReportDate],WorkOrder FROM LRF_Per_Heat WITH(NOLOCK) 
WHERE [HeatID] = @HeatID AND [IsDeleted] = 0 
ORDER BY [CreatedOn] DESC) AS t;
 
SELECT @HeatReportDate = ISNULL(@HeatReportDate, CAST(GETDATE() AS DATE)), 
       @ReportDate = ISNULL(@ReportDate, FORMAT(GETDATE(), 'yyyy-MM-dd'))
 
IF(@liquidMetal > 0)

BEGIN
    SELECT @glsMAterial = [Name] FROM [XBatch_Material_Mst_Tbl] WITH(NOLOCK) 
    WHERE [ID] IN (SELECT [ItemID] FROM xstudio_Xbatch.dbo.xbatch_work_order_mst_tbl 
    WHERE [id] = @glsWorkOrder );
 
    EXEC [XBatch_I_Material_Consume_NoBOM_USP] 
    @Grade = 'TBD', 
    @HeatNo = @HeatID, 
    @ItemName = @glsMAterial, 
    @LotNumber = @LotNo, 
    @ProduceItem = 1, 
    @Quantity = @liquidMetal, 
    @SublotNumber = NULL, 
    @UOMName = 'ton', 
    @UserID = @p_UserId;

END
 
UPDATE [XBatch_Work_Order_Mst_Tbl] SET [StartTime] = @StartTime,ModifiedOn = GETDATE(),ModifiedBy = @UserID, [Source] = 'T-SQL' 
WHERE [Status] = 'Running' AND [Equipment] = 'CCM' AND [starttime] IS NULL;
 
UPDATE CCM_Data set CCMHeatNo=@HeatID ,SteelGrade = @Grade |
|---|

### Table 6

| IF (@LadleSequence=0)
BEGIN
    UPDATE [XStudio_Xbatch].[dbo].[CCM_Data] SET 
    CCMCastingDate=FORMAT(@StartTime,'dd-MMM-yyyy'), CCMCastingTime =FORMAT(@StartTime,'HH:mm:ss')
END

EXEC [Quality_Spectro_IsLatestSample_Update_Usp]

IF(@HeatReportDate IS NULL) AND EXISTS (SELECT 1 FROM xstudio_xbatch.dbo.eaf_per_heat WITH(NOLOCK) 
WHERE heatid = @heatid and heatreportdate IS NOT NULL)

BEGIN
    SELECT @HeatReportDate=HeatReportDate, @ReportDate=ReportDate 
    FROM Xstudio_Xbatch.dbo.EAF_Per_Heat WITH(NOLOCK)
    WHERE HeatID=@HeatID;
 
    SELECT @HeatReportDate = ISNULL(@HeatReportDate, CAST(GETDATE() AS DATE)), 
           @ReportDate = ISNULL(@ReportDate, FORMAT(GETDATE(), 'yyyy-MM-dd'))
END
 
UPDATE AEL SET AEL.LastUsedBatch=CAST(@HeatID AS VARCHAR(36)), AEL.ModifiedOn = GETDATE(), [Source] = 'T-SQL' 
FROM [dbo].[XMES_ActiveLife_Element_Mst_Tbl] AEL
JOIN XMES_Life_Element_Mst_Tbl ELM ON ELM.ID=AEL.ElementNameID AND ELM.IsDeleted=0
JOIN XMES_Element_Life_Type_Mapping_Mst_Tbl LTM ON LTM.ElementType=ELM.ParentID AND LTM.IsDeleted=0 AND ltm.DataCaptureType='Auto'
WHERE LTM.ParentID='8D0E1442-1B43-4281-AC79-F68EB569AF51' AND AEL.IsDeleted=0;
 
UPDATE XMES_Life_Tracker_Register_Mst_Tbl SET Status='Active', Source='T-SQL', ModifiedBy=@p_UserId ,ModifiedOn = GETDATE() 
WHERE ID='8D0E1442-1B43-4281-AC79-F68EB569AF51'
 
EXEC [XMES_SMS_Temperature_Per_Heat_USP] 
@Area='CCM',
@EndTime=@EndTime,
@HeatID=@HeatID,
@StartTime=@StartTime; |
|---|