# LRF Per Heat Event Doc

*Extracted from `LRF Per Heat Event Doc.docx` -- real vendor handover doc, not invented.*

SITC OF X-FORCE HISTORIAN AND DASHBOARD DEVELOPMENT
SOHAR STEEL OMAN
Declaration
This Project Handover Document is intended only for personnel who already have a working knowledge of the X-Studio framework and related technical concepts.
The reader is expected to have prior knowledge of the X-Studio Event Framework, Workflows, Asset Structure, Database Structure, SQL Logic, and Stored Procedures. This document is prepared as a project-specific technical handover and reference document and is not intended to provide basic or introductory training on these concepts.
The document focuses on the project-specific implementation, configurations, process flows, database objects, SQL logic, workflows, and related technical details required for Project Support, Maintenance, Troubleshooting, and Further Development.
Therefore, readers should have sufficient prior knowledge of X-Studio and the above-mentioned technical areas to effectively understand and utilize the information provided in this document.

# LRF - Per Heat Data Insert Flow


## 1. Overview

This section describes the event configuration and inserts condition used for capturing LRF per-heat data. The event configuration is based on the LRF_Per_HeatData event (event entity LRF_Per_Heat), and the LRF Start state is used to identify the condition under which per-heat data is captured and stored.

## 2. Event Configuration


### 2.1 Event Entity

The main event data is stored in the LRF_Per_Heat entity. This entity stores all required LRF per-heat data captured for each heat. This data is stored when the LRF Start state condition becomes true.

### 2.2 Event Master

The Event Master maps the Event Entity with the event configuration entity. For the LRF per-heat data flow, the LRF_Per_HeatData process event is mapped to the LRF_Per_Heat transaction entity, as shown below.

### 2.3 Event Configuration Entity

The Event Configuration Entity defines the configuration for the LRF_Per_HeatData event. In Attributes, the required tag attributes are defined. In Tag Mapping, each tag attribute is mapped to its corresponding tag. In State, the condition that triggers the event is configured.

### 2.4 Event Configuration Tags


## 3. Data Insert Condition

Per-heat data insertion for LRF is controlled by the LRF Start state, configured against the LRF_Per_HeatData event configuration. Unlike the EAF flow, the LRF state uses a single condition rather than a nested True/False/Null expression:
When {ActualPowerOnTime} is greater than 0, the LRF Start state becomes active and the workflow transitions from Entered to Completed using the WorkFlowStatus attribute. The workflow itself is defined against the LRF_Per_Heat entity under the name "LRF Parameters" (Application: DEFAULT), as shown below.

## 4. Per Heat Data Insert Flow

When the LRF Start state is triggered, the configured tag attributes are evaluated using the event state condition. If the condition evaluates to True, the mapped LRF per-heat tag values are captured and inserted into the LRF_Per_Heat entity for the current heat.

### 4.1 Workflow Entered State - Stored Procedure Action

When the workflow action runs, it identifies the active LRF work order, retrieves the latest heat details from EAF_PER_HEAT (heat ID, liquid metal weight, lot number, and steel grade), updates the LRF steel grade, posts a liquid-metal consumption transaction where applicable, and resolves and applies the correct SMS block data for the current heat.

### 4.2 Workflow Entered SQL Action Details

1. Variable initialization - The DECLARE statement creates variables for the lot number, liquid-metal quantity, work-order identifiers, plant number, user ID, target entity ID (used to resolve the correct SMS block table), dynamic-SQL variables, a sub-serial counter, and the workflow type label.
2. Active work order lookup - The query on XBatch_Work_Order_Mst_Tbl retrieves the ID of the running, non-deleted LRF work order and stores it in @WorkOrder.
3. Latest heat data retrieval - The subquery on EAF_PER_HEAT selects the most recently created heat record and returns its HeatID, liquid-metal weight, a generated lot number in the format LS_<HeatID>, steel grade, and heat report date, which are assigned to the corresponding variables.
4. Report date fallback - If @HeatReportDate is null, it defaults to the current date so that a reporting date is always available for the heat.
5. LRF grade update - The UPDATE sets LRFGrade on LRF_SMS_Data to the steel grade retrieved from the latest EAF_PER_HEAT record.
6. Liquid-metal consumption posting - When @liquidMetal is greater than zero, XBatch_I_Material_Consume_NoBOM_USP posts a liquid-metal consumption transaction for the current heat using the generated lot number and quantity in tons.
7. Data-list action and status - SMS_Data_list_View is executed, and the workflow status and user ID are set to 'Completed' and @userID respectively.
8. Dynamic SMS block resolution - The query against XStudio_Block_Entities_Mst_Tbl and XStudio_Block_Databases_Mst_Tbl resolves the entity and database name of the SMS block configuration that is valid for the current @StartTime, under the parent entity identified by @EntityID.
9. Dynamic update of LRF_Per_Heat - The dynamic SQL string joins the resolved SMS block table to LRF_Per_Heat on matching start and end times, and updates power-on time, arcing time, argon consumption, energy, KWH per ton, purging flow, liquid-metal weight, and the alloy-addition fields (lime, SiMn, SiMnN, FeSi, dolomite) for all other non-deleted records besides the current one, which is then executed with SP_EXECUTESQL.
Note:  This extract depends on variables declared or assigned elsewhere in the complete workflow procedure, including @StartTime, @HeatID, @WorkOrder, @Grade, @p_UserId, and @p_RecordId. Confirm that @EntityID correctly identifies the intended SMS block parent before deployment.

### 4.3 Workflow Completed State - Stored Procedure Action

When the workflow reaches the completed state, this action retrieves treatment timing, posts the liquid-metal production transaction, runs the LRF-specific historian and raw-material calculations, updates life-element and life-tracker records, and calculates the per-heat temperature.

### 4.4 Workflow Completed SQL Action Details

1. Lot number and material variables - The lot number for the completed state uses a GLS_ prefix (CONCAT('GLS_', @HeatID)), distinct from the LS_ prefix used earlier in the flow. A @Material variable is also declared for later use.
2. Treatment time retrieval - The query on LRF_ProcessTime retrieves the start and end time of the 'Treatment Start' status for the current heat, assigning them to @TreatmentStart and @TreatmentStop.
3. Work-order and sales-order calculation - XMES_AUTO_WO_AND_SO_CALCULATION is executed for the LRF plant and the active work order.
4. Tap-start retrieval - The tap start time is read from EAF_PER_HEAT for the current heat and assigned to @TapStart.
5. Liquid-metal production posting - When @LiquidMetalWeight is greater than zero, the material name is resolved from the item configured on the active work order, and XBatch_I_Material_Produce_NoBOM_USP posts a production transaction for that material using the GLS_ lot number and the liquid-metal quantity.
6. Historian SMS block calculation - When both @StartTime and @EndTime are populated, Xstudio_Historian_LRF_SMS_Block_usp is executed for all attributes against the configured LRF equipment ID, calculating the SMS block values for the treatment window.
7. Alloy-addition defaults - @AutoAlloyAdditionCarbon, @AutoAlloyAdditionFlourSpar, and @AutoAlloyAdditionAluminium are defaulted to zero using ISNULL where no automatic value has been captured.
8. Raw-material consumption - XMES_LRF_I_Raw_Material_Cons_Usp is executed for the current heat to process raw-material consumption postings.
9. Spectro sample flag update - Quality_Spectro_IsLatestSample_Update_Usp is executed to update the latest-sample flag used by the quality/spectrometer module.
10. Report date fallback - If @HeatReportDate is still null, it is retrieved from EAF_PER_HEAT for the current heat and, if still unavailable, defaulted to the current date.
11. Life-element batch update - As with the EAF flow, active life elements configured for automatic data capture under the specified parent ID have LastUsedBatch updated to the current heat ID, with the modification timestamp recorded.
12. Life-tracker activation - The corresponding life-tracker register is set to Status = 'Active' with Source = 'T-SQL', and the modifying user and timestamp are recorded.
13. Per-heat temperature calculation - XMES_SMS_Temperature_Per_Heat_USP is executed for the LRF area using the treatment start and stop times, calculating the per-heat temperature for the current heat.
14. Final temperature retrieval - The calculated Temperature value is read back from the active LRF_Per_Heat record for the current heat and assigned to @Temperature for any later workflow activity.
Note:  This SQL extract relies on additional variables from the surrounding workflow procedure, including @HeatID, @WorkOrder, @LiquidMetalWeight, @StartTime, @EndTime, @HeatReportDate, @p_RecordId, and @p_UserId. Confirm that all these variables are declared and assigned before this action executes.

---
## Tables (real technical detail -- tag mappings, state configs, condition logic)


### Table 1

| Project | SITC of X-Force Historian and Dashboard Development for Sohar Steel Oman |
|---|---|
| Prepared By | Mahesh Udar |
| Document Type | LRF Per Heat Data Insert Flow |
| Handover Date |  |
| Handover To |  |
| Document Version | 1.0 |

### Table 2

| Attribute | Tag Name |
|---|---|
| ActualPowerOnTime | LRF_ACTUAL_POWER_ON_TIME_MIN_PRM |
| ArcingTime | LRF_PREV_ARC_TIME_SEC_PRM |
| ArgonConsumption | LRF_PREV_ARGON_CONSUMPTION_NM3_PRM |
| Energy | LRF_PREV_ENERGY_KWH_PRM |
| LRFHeatID | EAF_HEAT_NUMBER_PRM |
| LRFLiquidMetalWeight | EAF_LIQUID_METAL_WEIGHT_TON_PRM |
| LRFPOFFTime | LRF_ACTUAL_POWER_OFF_TIME_MIN_PRM |
| LRFTemperature | LRF_TEMPERATURE_PRM |
| PerLRFLadleCar | LRF_LADLE_CAR_TREATMENT_POSITION_STATUS |
| PowerOFFTime | LRF_PREV_POWER_OFF_TIME_MIN_PRM |
| PowerOnTime | LRF_PREV_POWER_ON_TIME_MIN_PRM |

### Table 3

| {ActualPowerOnTime} > 0 |
|---|

### Table 4

| DECLARE @LotNo VARCHAR(500),
        @liquidMetal DECIMAL(18,4), 
        @WORID VARCHAR(36),
        @WONO VARCHAR(36), 
        @PlantNo VARCHAR(100) = '7502', 
        @userID VARCHAR(36) = 'A6E924D5-B2F0-4A5F-9717-3A63F6190358', 
        @EntityID VARCHAR(36) = 'A5B50AA4-07E1-45A5-BE43-AB83242A7EA8', 
        @STR NVARCHAR(MAX), 
        @TableName VARCHAR(200), 
        @Database VARCHAR(200);
 
SELECT @WorkOrder = [ID] FROM [XBatch_Work_Order_Mst_Tbl] WITH(NOLOCK) 
WHERE [Status] = 'Running' AND [Equipment] = 'LRF' AND [IsDeleted] = 0;
 
SELECT @HeatID = [HeatID], 
       @liquidMetal = [LiquidMetalWeight],
       @LotNo = [LotNo], 
       @Grade = [SteelGrade], 
       @HeatReportDate = [HeatReportDate] 
 FROM (SELECT TOP 1 [HeatID], 
                    ISNULL([LiquidMetalWeight], 0) AS [LiquidMetalWeight], 
                    CONCAT('LS_', CAST(HeatID AS INT)) AS [LotNo], 
                    [SteelGrade], 
                    [HeatReportDate] 
        FROM [EAF_PER_HEAT] WITH(NOLOCK) 
        WHERE [IsDeleted] = 0 ORDER BY [CreatedOn] DESC) AS t;
 
SET @HeatReportDate = ISNULL(@HeatReportDate, CAST(GETDATE() AS DATE))
 
UPDATE [XStudio_Xbatch].[dbo].[LRF_SMS_Data] SET [LRFGrade] = @Grade;
 
IF (@liquidMetal > 0)
BEGIN
    EXEC [XBatch_I_Material_Consume_NoBOM_USP] 
    @Grade = 'TBD', 
    @HeatNo = @HeatID, 
    @ItemName = 'LIQUID METAL', 
    @LotNumber = @LotNo, 
    @ProduceItem = 1, 
    @Quantity = @liquidMetal, 
    @SublotNumber = NULL, 
    @UOMName = 'ton', 
    @UserID = @p_UserId;
END
 
EXEC [SMS_Data_list_View];

SELECT @p_Status = 'Completed', @p_UserId = @userID;
 
SET @ReportDate = Format(@HeatReportDate, 'yyyy-MM-dd');
 
SELECT @TableName = [EntityName], @Database = [DatabaseName] 
FROM (SELECT TOP 1 BEM.[Name] AS [EntityName], BDM.[Name] AS [DatabaseName] 
FROM [XStudio_Configuration_XBatch].[dbo].[XStudio_Block_Entities_Mst_Tbl] AS BEM WITH(NOLOCK) 
JOIN [XStudio_Configuration_Xbatch].[dbo].[XStudio_Block_Databases_Mst_Tbl] AS BDM WITH(NOLOCK) ON BEM.[DatabaseName] = BDM.[Name] 
WHERE BEM.[IsDeleted] = 0 AND BDM.[IsDeleted] = 0 AND BEM.[ParentID] = @EntityID AND BEM.[StartTime] <= @StartTime AND BEM.[EndTime] > @StartTime) AS t;
 
SET @STR = 'UPDATE LPH SET LPH.[PowerONTime] = ISNULL(Main.[PowerOnTime], 0), LPH.[ArcingTime] = ISNULL(Main.[ArcingTime], 0), LPH.[ArgonConsumption] = ISNULL(Main.[ArgonConsumption], 0), LPH.[PowerMWH] = ISNULL(Main.[LRFActualEnergy], 0), LPH.[KWHPerTon] = ISNULL(Main.[KWHPerTon], 0), LPH.[PurgingFlowLPM] = ISNULL(Main.[PurgingFlowLPM], 0), LPH.[LiquidMetalWeight] = ISNULL(main.[LiquidMetalWeight],0), LPH.[Lime] = ISNULL(Main.[Lime], 0) + ISNULL(Main.[Lime1], 0), LPH.[SiMnN] = ISNULL(Main.[SiMnn], 0), LPH.[SiMn] = ISNULL(Main.[SiMn],0), LPH.[FeSi] = ISNULL(Main.[FeSi],0), LPH.[Dolo] = ISNULL(Main.[Dolo],0), LPH.[AutoAlloyAdditionLime] = ISNULL(Main.[Lime], 0) + ISNULL(Main.[Lime1], 0), LPH.[AutoAlloyAdditionDolo] = ISNULL(Main.[Dolo],0), LPH.[AutoAlloyAdditionFeSi] = ISNULL(Main.[FeSi],0), LPH.[AutoAlloyAdditionSiMn] = ISNULL(Main.[SiMn],0),LPH.[ModifiedOn] = GETDATE() FROM [XStudio_Xbatch].[dbo].[LRF_Per_Heat] AS LPH INNER JOIN [' + @Database + '].[dbo].[' + @TableName + '] AS Main ON Main.[StartTime] = LPH.[StartTime]  AND Main.[EndTime] = LPH.[EndTime] WHERE LPH.[IsDeleted] = 0 AND LPH.[ID] != @p_RecordId;'
 
EXEC SP_EXECUTESQL @STR, N'@p_RecordId VARCHAR(36)', @p_RecordId; |
|---|

### Table 5

| DECLARE @LotNo VARCHAR(500) = CONCAT('GLS_', CAST(@HeatID AS INT)), 
        @Material VARCHAR(200);
 
SELECT @TreatmentStart = P.[StartTime], @TreatmentStop = P.[EndTime] 
FROM [LRF_ProcessTime] P WITH(NOLOCK) 
WHERE P.[Status] = 'Treatment Start' AND P.[IsDeleted] = 0 AND P.[LRFHeatID] = @HeatID;
 
EXEC [XMES_AUTO_WO_AND_SO_CALCULATION] 
@Plant = 'LRF', 
@WorkOrder = @WorkOrder;
 
SELECT @TapStart = P.[TapStart] FROM [EAF_PER_HEAT] AS P WITH(NOLOCK) 
WHERE P.[HeatID] = @HeatID AND P.[IsDeleted] = 0;
 
IF (@LiquidMetalWeight > 0)
BEGIN
    SELECT @Material = [Name] FROM [XBatch_Material_Mst_Tbl] WITH(NOLOCK) 
    WHERE [ID] IN (SELECT [ItemID] FROM xstudio_Xbatch.dbo.xbatch_work_order_mst_tbl 
    WHERE [id] = @WorkOrder );
 
    EXEC [XBatch_I_Material_Produce_NoBOM_USP] 
    @Grade = 'TBD', 
    @HeatNo = @HeatID, 
    @ItemName = @Material, 
    @LotNumber = @LotNo, 
    @Quantity = @LiquidMetalWeight, 
    @SublotNumber = NULL, 
    @UOMName = 'ton', 
    @UserID = @p_UserId;
END
 
IF (@StartTime IS NOT NULL AND @EndTime IS NOT NULL)
BEGIN
    EXEC [Xstudio_Historian_LRF_SMS_Block_usp] 
    @Attribute = 'All', 
    @CollectorID = NULL, 
    @EndTime = @EndTime, 
    @Equipment = '0A625385-4465-4C71-A91C-88743497DD3A', 
    @StartTime = @StartTime;
END
 
SELECT @AutoAlloyAdditionCarbon=ISNULL(@AutoAlloyAdditionCarbon,0), 
       @AutoAlloyAdditionFlourSpar=ISNULL(@AutoAlloyAdditionFlourSpar,0), 
       @AutoAlloyAdditionAluminium=ISNULL(@AutoAlloyAdditionAluminium,0)
 
EXEC [XMES_LRF_I_Raw_Material_Cons_Usp] @HeatID;
 
EXEC [Quality_Spectro_IsLatestSample_Update_Usp];

IF (@HeatReportDate IS NULL)
BEGIN
    SELECT @HeatReportDate=HeatReportDate FROM Xstudio_Xbatch.dbo.EAF_Per_Heat WITH(NOLOCK) 
    WHERE HeatID=@HeatID;
    SET @HeatReportDate = ISNULL(@HeatReportDate, CAST(GETDATE() AS DATE))
END

SELECT @ReportDate=FORMAT(@HeatReportDate,'yyyy-MM-dd');
 
UPDATE AEL SET AEL.LastUsedBatch=Cast(@HeatID AS VARCHAR(36)), AEL.ModifiedOn = GETDATE() 
FROM [dbo].[XMES_ActiveLife_Element_Mst_Tbl] AEL
Join XMES_Life_Element_Mst_Tbl ELM ON ELM.ID=AEL.ElementNameID AND ELM.IsDeleted=0
Join XMES_Element_Life_Type_Mapping_Mst_Tbl LTM ON LTM.ElementType=ELM.ParentID AND LTM.IsDeleted=0 and ltm.DataCaptureType='Auto'
WHERE LTM.ParentID='FD0085B5-3530-45EA-8A6B-6685FFE484F4' and AEL.IsDeleted=0
 
UPDATE XMES_Life_Tracker_Register_Mst_Tbl SET Status='Active', Source='T-SQL', ModifiedBy=@p_UserId ,ModifiedOn = GETDATE() 
WHERE ID='FD0085B5-3530-45EA-8A6B-6685FFE484F4'
 
EXEC [XMES_SMS_Temperature_Per_Heat_USP] 
@Area='LRF',
@EndTime=@TreatmentStop,
@HeatID=@HeatID,
@StartTime=@TreatmentStart;
SELECT @Temperature = Temperature FROM LRF_Per_Heat WITH(NOLOCK)
WHERE HeatID=@HeatID and isdeleted=0; |
|---|