# EAF Per Heat Event Doc

*Extracted from `EAF Per Heat Event Doc.docx` -- real vendor handover doc, not invented.*

SITC OF X-FORCE HISTORIAN AND DASHBOARD DEVELOPMENT
SOHAR STEEL OMAN
Declaration
This Project Handover Document is intended only for personnel who already have a working knowledge of the X-Studio framework and related technical concepts.
The reader is expected to have prior knowledge of the X-Studio Event Framework, Workflows, Asset Structure, Database Structure, SQL Logic, and Stored Procedures. This document is prepared as a project-specific technical handover and reference document and is not intended to provide basic or introductory training on these concepts.
The document focuses on the project-specific implementation, configurations, process flows, database objects, SQL logic, workflows, and related technical details required for Project Support, Maintenance, Troubleshooting, and Further Development.
Therefore, readers should have sufficient prior knowledge of X-Studio and the above-mentioned technical areas to effectively understand and utilize the information provided in this document.

# EAF – Per Heat Data Insert Flow


## 1. Overview

This section explains the event configuration and trigger condition for capturing EAF per-heat data. The configuration uses the HeatIDChange event and its state to determine when the data is captured and stored.

## 2. Event Configuration


### 2.1 Event Entity

The main event data is stored in the EAF_PER_HEAT entity. This entity stores all required EAF per-heat data captured for each Heat Number. This data is stored when the HeatIDChange state condition becomes true.

### 2.2 Event Master

The Event Master maps the Event Entity with the event configuration entity. For the EAF per-heat data flow, the HeatIDChange process event is mapped to the EAF_PER_HEAT transaction entity, as shown below.

### 2.3 Event Configuration Entity

The Event Configuration Entity defines the configuration for the HeatIDChange event. In Attributes, the required tag attributes are defined. In Tag Mapping, each tag attribute is mapped to its corresponding tag. In State, the condition that triggers the event is configured.

### 2.4 Event Configuration Tags


## 3. Data Insert Condition

Per-heat data insertion is controlled by the following event state condition:

### 3.1 Condition Logic


## 4. Per Heat Data Insert Flow

When the HeatIDChange event is triggered, the configured tag attributes are evaluated using the event state condition. If the condition evaluates to True, the mapped EAF per-heat tag values that are configured on state are captured and inserted into the EAF_PER_HEAT entity for the current heat.

### 4.1 Workflow Entered State - Stored Procedure Action

When the workflow action runs, it identifies the heat start time and active EAF work order, retrieves the steel grade from the historian, and updates the relevant life-element and life-tracker records.

### 4.2 Workflow Entered SQL Action Details

1. Variable initialization - The first DECLARE statement creates variables used by the workflow action. These include the historian retrieval time range (@Startdate and @Enddate), the historian tag name (@TagName), plant and user details, stored-procedure execution variables, and the workflow status type. The @userid value is used to record who modified the life-element data.
2. Heat start-time identification - The query on EAF_ProcessTime finds the start time of the current heat or the preceding heat. It considers only active records (IsDeleted = 0) with Status = 'heat start'. For the current @HeatID, it selects the earliest start time; for the preceding heat, it selects the latest start time. The latest HeatID is prioritized by ORDER BY eaf.[HeatID] DESC. The selected time defines the reporting date and subsequent historian lookup range.
3. Report date and active work order — The heat start time is converted to a date and assigned to @HeatReportDate. The query on XBatch_Work_Order_Mst_Tbl then retrieves the ID of the running, non-deleted EAF work order and stores it in @WorkOrder.
4. Historian time range and steel-grade retrieval - The action creates a one-minute time window from 10 minutes before the heat start time through 9 minutes before it. It passes this range and @TagName to XHS_Retrieve_Tag_Full_Value_Usp in the Xstudio_Historian database. The returned timestamp and value are inserted into the @Grade table variable. The retrieved value is then assigned to @SteelGrade.
5. Data-list action - The SMS_Data_list_View stored procedure is then executed as part of the workflow action.
6. Life-element batch update - The first UPDATE identifies active life elements that are configured for automatic data capture (LTM.DataCaptureType = 'Auto') under the specified parent ID. It updates LastUsedBatch with the current heat ID and records the modification time and user. The joins ensure that only valid, non-deleted life-element and mapping records are updated.
7. Life-tracker activation - The final UPDATE activates the life-tracker register identified by the same parent ID. It sets Status to 'Active', records the update source as 'T-SQL', and saves the modifying user and timestamp.
Note: This extract depends on variables declared or assigned elsewhere in the complete workflow procedure, including @HeatID, @StartTime/@HeatStart, @HeatReportDate, @WorkOrder, @SteelGrade, and @p_UserId. Before deployment, confirm that @HeatStart and @StartTime refer to the intended same variable, and that @userid and @p_UserId use the intended user identifier.

### 4.3 Workflow Completed State — Stored Procedure Action

When the workflow reaches the completed state, this action calculates charge-mix totals and HBI/CDRI consumption, updates the EAF_PER_HEAT record, creates the liquid-metal production transaction, and executes the related EAF calculation procedures.

### 4.4 Workflow Completed SQL Action Details

1. Initial variables - The action declares variables for the lot number, liquid-metal quantity, bin value, and the user who performs the update. The user ID is written to audit fields when the EAF per-heat record is updated.
2. Charge-mix data retrieval - The first SELECT reads the active record for the current heat from SMS_EAF_Per_Heat_ChargeMix. For every scrap material and charge number (Charge 1 to Charge 4), it adds the automatic weight to the manual weight. ISNULL treats missing values as zero, so an unavailable manual or automatic value does not prevent the total from being calculated. The materials included are Copex Scrap, HMS1, HMS1/2, End Cuts, Briquettes, Bundles LMS, HBI/DRI, Shredded material, and Skull.
3. Total material consumption by heat - The next SELECT adds the four charge totals for each material. For example, @CopexScrap is the sum of Copex Scrap charge 1 through charge 4. It also creates the liquid-metal lot number in the format LS_<HeatID> and obtains the liquid-metal quantity from @LiquidMetalWeight. The auto and manual total fields are also read from the charge-mix record for use elsewhere in the complete procedure.
4. HBI and CDRI bin-consumption calculation - The IF block evaluates the material names assigned to bin 3 and bin 4. When both bins contain the same material, their consumption values are combined. When the bins contain different materials, each bin is evaluated separately. A bin whose name is cdri contributes to @CdriConsumption; any other populated bin contributes to @HBIConsumption. Empty bin names are ignored.
5. EAF_PER_HEAT update - The UPDATE writes the calculated HBI/CDRI consumption and all material totals to the EAF_PER_HEAT record identified by @p_RecordId. It also updates ModifiedOn with the current server time and ModifiedBy with the configured user ID. This stores the completed charge-mix values against the current heat record.
6. Charge-mix consumption procedure - HeatChargeMixConsumption is executed for the current heat. This procedure performs the further charge-mix consumption processing required after the EAF_PER_HEAT record has been updated.
7. Liquid-metal production posting - The remaining actions run only when @LiquidMetal is greater than zero. XBatch_I_Material_Produce_NoBOM_USP creates a liquid-metal production transaction for the current heat, using the generated lot number, a quantity in tons, and the temporary grade value TBD.
8. Ladle-addition values - The script retrieves the automatic ladle-addition quantities for the heat from LadleAddition: lime from Silo 3 plus Silo 4, dolomite from Silo 8, silicon manganese from Silo 5 plus Silo 6, and ferrosilicon from Silo 7. Those automatic values are copied into the corresponding ladle-addition variables for subsequent use.
9. Downstream EAF calculations - The action then executes the work-order and sales-order calculation, per-heat temperature calculation, historian attribute calculation, and spray-cooling flow-duration calculation. All time-based procedures use the heat start and end times so that their results relate to the current heat.
10. Final calculated-value retrieval - The final SELECT reads the calculated electrode spray-cooling durations and average flows for electrodes E1, E2, and E3, together with the EAF temperature, from the active EAF_PER_HEAT record for the current heat. These values are placed into variables for any later workflow activity.
Note: This SQL extract relies on additional variables from the surrounding workflow procedure, including @HeatID, @p_RecordId, @LiquidMetalWeight, bin names and consumption values, @WorkOrder, @HeatStart, and @EndTime. Confirm that all these variables are declared and assigned before this action executes.

## 5. EAF Frontend LV

The EAF Frontend LV provides a heat-wise view of the data stored and calculated in the EAF_PER_HEAT table. The screen presents EAF heat records in a tabular format so that users can review heat identification, process timing, charge and production weights, yield, consumption, work-order information, temperature, and other heat-level process parameters.
The following table documents the EAF_PER_HEAT columns available in the supplied source definition. Column Type is based on IsCalculatedColumn: Normal represents a non-calculated column and Calculated represents a column with a supplied ColumnEquation. The source definition does not provide SQL Server data types, so SQL data types are not inferred.

### 5.1. EAF_PER_HEAT Column Details


### 5.2. EAF Frontend LV – Data Presentation

The LV provides a consolidated heat-wise view of EAF_PER_HEAT information. Users can review heat number and grade, process start and end times, power-on and power-off timing, tap timing, charge and liquid-metal weights, yield, material and utility consumption, work-order information, temperature, and calculated performance indicators.
Calculated columns are generated from the ColumnEquation defined in the source configuration. These derived values support presentation and reporting of formatted time values, report date, timing values, tap time, yield percentage, LS DELTA, and throughput.

### 5.3. EAF Frontend LV – Screen


---
## Tables (real technical detail -- tag mappings, state configs, condition logic)


### Table 1

| Project | SITC of X-Force Historian and Dashboard Development for Sohar Steel Oman |
|---|---|
| Prepared By | Mahesh Udar |
| Document Type | EAF Per Heat Data Insert Flow |
| Handover Date |  |
| Handover To |  |
| Document Version | 1.0 |

### Table 2

| Attribute | Tag Name |
|---|---|
| BIN3Consumption | EAF_RMH_BIN_3_CONSUMPTION_TON_PRM |
| Bin3Name | EAF_RMH_BIN_3_NAME_PRM |
| BIN4Consumption | EAF_RMH_BIN_4_CONSUMPTION_TON_PRM |
| Bin4Name | EAF_RMH_BIN_4_NAME_PRM |
| BriquetteCH1 | EAF_BRIQUETTE_CHARGE_1_WEIGHT_TON_PRM |
| BriquetteCH2 | EAF_BRIQUETTE_CHARGE_2_WEIGHT_TON_PRM |
| BundleLMSCH1 | EAF_BUNDLE_LMS_CHARGE_1_WEIGHT_TON_PRM |
| BundleLMSCH2 | EAF_BUNDLE_LMS_CHARGE_2_WEIGHT_TON_PRM |
| Carbon | EAF_CARBON_CONSUMPTION_KG_PRM |
| ChargeWeight | EAF_TOTAL_BUKET_CHARGE_WEIGHT_TON_PRM |
| CopexScrapCH1 | EAF_COPEX_SCRAP_CHARGE_1_WEIGHT_TON_PRM |
| CopexScrapCH2 | EAF_COPEX_SCRAP_CHARGE_2_WEIGHT_TON_PRM |
| DOLOConsumption | EAF_RMH_BIN_2_CONSUMPTION_TON_PRM |
| EAFTemperature | EAF_HERAUS_TEMPERATURE_PRM |
| EndCutsCH1 | EAF_END_CUTS_CHARGE_1_WEIGHT_TON_PRM |
| EndCutsCH2 | EAF_END_CUTS_CHARGE_2_WEIGHT_TON_PRM |
| HBIDRICH1 | EAF_HBI_DRI_CHARGE_1_WEIGHT_TON_PRM |
| HBIDRICH2 | EAF_HBI_DRI_CHARGE_2_WEIGHT_TON_PRM |
| HeatID | EAF_HEAT_NUMBER_PRM |
| HeatTimeMinute | EAF_PREV_HEAT_TIME_MIN_PRM |
| HeatTimeSecond | EAF_PREV_HEAT_TIME_SEC_PRM |
| HMS12CH1 | EAF_HMS_1_2_CHARGE_1_WEIGHT_TON_PRM |
| HMS12CH2 | EAF_HMS_1_2_CHARGE_2_WEIGHT_TON_PRM |
| HMS1CH1 | EAF_HMS_1_CHARGE_1_WEIGHT_TON_PRM |
| HMS1CH2 | EAF_HMS_1_CHARGE_2_WEIGHT_TON_PRM |
| LIMEConsumption | EAF_RMH_BIN_1_CONSUMPTION_TON_PRM |
| LiquidMetalWeight | EAF_LIQUID_METAL_WEIGHT_TON_PRM |
| LivePowerONTime | EAF_POWER_ON_TIME_MIN_PRM |
| NGConsumption | EAF_NATURAL_GAS_CONSUMPTION_NM3_PRM |
| OxygenConsumption | EAF_OXYGEN_CONSUMPTION_NM3_PRM |
| PowerMWH | EAF_PREV_ENERGY_MWH_PRM |
| PowerOffTimeMinute | EAF_PREV_POWER_OFF_TIME_MIN_PRM |
| PowerOffTimeSecond | EAF_PREV_POWER_OFF_TIME_SEC_PRM |
| PowerOnTimeMinute | EAF_PREV_POWER_ON_TIME_MIN_PRM |
| PowerOnTimeSecond | EAF_PREV_POWER_ON_TIME_SEC_PRM |
| ScullCH1 | EAF_SCULL_CHARGE_1_WEIGHT_TON_PRM |
| ScullCH2 | EAF_SCULL_CHARGE_2_WEIGHT_TON_PRM |
| ShreddedCH1 | EAF_SHREDDED_CHARGE_1_WEIGHT_TON_PRM |
| ShreddedCH2 | EAF_SHREDDED_CHARGE_2_WEIGHT_TON_PRM |
| Tapping1 | EAF_TAPPING_STATUS |
| TotalchargeWeightMT | EAF_TOTAL_CHARGE_WEIGHT_TON_PRM |

### Table 3

| IIF({Tapping1} = 1 AND {LivePowerONTime} > 0, True, IIF({Tapping1} = 0 AND {LivePowerONTime} = 0, False, Null)) |
|---|

### Table 4

| Condition | Result | Meaning |
|---|---|---|
| Tapping1 = 1 AND LivePowerONTime > 0 | True | Heat data capture condition is ON and the event state becomes active. |
| Tapping1 = 0 AND LivePowerONTime = 0 | False | Heat data capture condition is OFF and the event state becomes inactive. |
| Any other combination | Null | Condition does not explicitly evaluate to True or False. |

### Table 5

| DECLARE @Startdate DATETIME, 
@Enddate DATETIME, 
@TagName VARCHAR(MAX), 
@WONO VARCHAR(36), 
@PlantNo VARCHAR(20) = '7502', 
@userid VARCHAR(36) = 'A6E924D5-B2F0-4A5F-9717-3A63F6190358';

SET @HeatStart = (SELECT TOP 1 IIF(eaf.[HeatID] = @HeatID, MIN(eaf.[starttime]), MAX(eaf.[starttime])) AS [StartTime] FROM [EAF_ProcessTime] AS eaf WITH(NOLOCK) 
WHERE eaf.[IsDeleted] = 0 AND eaf.[HeatID] IN (@HeatID, @HeatID - 1) AND [Status] = 'heat start' 
GROUP BY eaf.[HeatID] 
ORDER BY [HeatID] DESC);

SET @HeatReportDate = CAST(@StartTime AS DATE)

SELECT @WorkOrder = [ID] FROM [XBatch_Work_Order_Mst_Tbl] WITH(NOLOCK) 
WHERE [Status] = 'Running' AND [Equipment] = 'EAF' AND [IsDeleted] = 0;

SELECT @Startdate = DATEADD(MINUTE, -10, @StartTime), 
	@Enddate = DATEADD(MINUTE, -9, @StartTime);

DECLARE @Grade AS TABLE ([Timestamp] DATETIME, [Val] VARCHAR(36));

INSERT INTO @Grade ([Timestamp], [Val]) 
EXEC [Xstudio_Historian].[dbo].[XHS_Retrieve_Tag_Full_Value_Usp] 
@StartTime = @Startdate, 
@EndTime = @Enddate, 
@TagName = @TagName, 
@Format = 'wide', 
@HeaderFormat = 'name';

SELECT @SteelGrade = [Val] FROM @Grade;

EXEC [SMS_Data_list_View]

UPDATE AEL SET AEL.LastUsedBatch = CAST(@HeatID AS VARCHAR(36)), AEL.ModifiedOn = GETDATE(), AEL.ModifiedBy = @userid 
FROM [dbo].[XMES_ActiveLife_Element_Mst_Tbl] AEL
JOIN XMES_Life_Element_Mst_Tbl ELM ON ELM.ID = AEL.ElementNameID AND ELM.IsDeleted = 0
JOIN XMES_Element_Life_Type_Mapping_Mst_Tbl LTM ON LTM.ElementType = ELM.ParentID AND LTM.IsDeleted = 0 AND LTM.DataCaptureType = 'Auto'
WHERE LTM.ParentID = '92D612E4-C8EC-4310-A96F-04A5DBD4C861' AND AEL.IsDeleted = 0;

UPDATE XMES_Life_Tracker_Register_Mst_Tbl SET Status = 'Active', Source = 'T-SQL', ModifiedBy = @p_UserId, ModifiedOn = GETDATE() 
WHERE ID = '92D612E4-C8EC-4310-A96F-04A5DBD4C861'; |
|---|

### Table 6

| DECLARE @LotNo VARCHAR(500), 
        @LiquidMetal DECIMAL(18,4), 
        @Bin DECIMAL(18,4), 
        @UserID VARCHAR(36) = 'A6E924D5-B2F0-4A5F-9717-3A63F6190358';

SELECT @CopexScrapCH1 = ISNULL([EAFCopexScrapCharge1Weight], 0) + ISNULL([EAFCopexScrapCharge1WeightManual], 0), 
@CopexScrapCH2 = ISNULL([EAFCopexScrapCharge2Weight], 0) + ISNULL([EAFCopexScrapCharge2WeightManual], 0),
@CopexScrapCH3 = ISNULL([EAFCopexScrapCharge3Weight], 0) + ISNULL([EAFCopexScrapCharge3WeightManual], 0),
@CopexScrapCH4 = ISNULL([EAFCopexScrapCharge4Weight], 0) + ISNULL([EAFCopexScrapCharge4WeightManual], 0), 
@HMS1CH1 = ISNULL([EAFHMS1Charge1Weight], 0) + ISNULL([EAFHMS1Charge1WeightManual], 0),
@HMS1CH2 = ISNULL([EAFHMS1Charge2Weight], 0) + ISNULL([EAFHMS1Charge2WeightMaual], 0),
@HMS1CH3 = ISNULL([EAFHMS1Charge3Weight], 0) + ISNULL([EAFHMS1Charge3WeightManaul], 0),
@HMS1CH4 = ISNULL([EAFHMS1Charge4Weight], 0) + ISNULL([EAFHMS1Charge4WeightManual], 0),
@HMS12CH1 = ISNULL([EAFHMS12Charge1Weight], 0) + ISNULL([EAFHMS12Charge1WeightManual], 0), 
@HMS12CH2 = ISNULL([EAFHMS12Charge2Weight], 0) + ISNULL([EAFHMS12Charge2WeightManual], 0),
@HMS12CH3 = ISNULL([EAFHMS12Charge3Weight], 0) + ISNULL([EAFHMS12Charge3WeightManual], 0),
@HMS12CH4 = ISNULL([EAFHMS12Charge4Weight], 0) + ISNULL([EAFHMS12Charge4WeightManual], 0),
@EndCutsCH1 = ISNULL([EAFEndCutsCharge1Weight], 0) + ISNULL([EAFEndCutsCharge1WeightManual], 0),
@EndCutsCH2 = ISNULL([EAFEndCutsCharge2Weight], 0) + ISNULL([EAFEndCutsCharge2WeightManual], 0),
@EndCutsCH3 = ISNULL([EAFEndCutsCharge3Weight], 0) + ISNULL([EAFEndCutsCharge3WeightManual], 0),
@EndCutsCH4 = ISNULL([EAFEndCutsCharge4Weight], 0) + ISNULL([EAFEndCutsCharge4WeightManual], 0),
@BriquetteCH1 = ISNULL([EAFBriquettesCharge1Weight], 0) + ISNULL([EAFBriquettesCharge1WeightManual], 0), @BriquetteCH2 = ISNULL([EAFBriquettesCharge2Weight], 0) + ISNULL([EAFBriquettesCharge2WeightManual], 0),
@BriquetteCH3 = ISNULL([EAFBriquettesCharge3Weight], 0) + ISNULL([EAFBriquettesCharge3WeightManual], 0),
@BriquetteCH4 = ISNULL([EAFBriquettesCharge4Weight], 0) + ISNULL([EAFBriquettesCharge4WeightManual], 0),
@BundleLMSCH1 = ISNULL([EAFBundlesLMSCharge1Weight], 0) + ISNULL([EAFBundlesLMSCharge1WeightManual], 0),
@BundleLMSCH2 = ISNULL([EAFBundlesLMSCharge2Weight], 0) + ISNULL([EAFBundlesLMSCharge2WeightManual], 0),
@BundleLMSCH3 = ISNULL([EAFBundlesLMSCharge3Weight], 0) + ISNULL([EAFBundlesLMSCharge3WeightManual], 0),
@BundleLMSCH4 = ISNULL([EAFBundlesLMSCharge4Weight], 0) + ISNULL([EAFBundlesLMSCharge4WeightManual], 0),
@HBIDRICH1 = ISNULL([EAFHBIDRICharge1Weight], 0) + ISNULL([EAFHBIDRICharge1WeightManual], 0),
@HBIDRICH2 = ISNULL([EAFHBIDRICharge2Weight], 0) + ISNULL([EAFHBIDRICharge2WeightManual], 0),
@HBIDRICH3 = ISNULL([EAFHBIDRICharge3Weight], 0) + ISNULL([EAFHBIDRICharge3WeightManual], 0),
@HBIDRICH4 = ISNULL([EAFHBIDRICharge4Weight], 0) + ISNULL([EAFHBIDRICharge4WeightManual], 0),
@ShreeddedCH1 = ISNULL([EAFShreddedCharge1Weight], 0) + ISNULL([EAFShreddedCharge1WeightManual], 0),
@ShreeddedCH2 = ISNULL([EAFShreddedCharge2Weight], 0) + ISNULL([EAFShreddedCharge2WeightManual], 0),
@ShreeddedCH3 = ISNULL([EAFShreddedCharge3Weight], 0) + ISNULL([EAFShreddedCharge3WeightManual], 0),
@ShreeddedCH4 = ISNULL([EAFShreddedCharge4Weight], 0) + ISNULL([EAFShreddedCharge4WeightManual], 0),
@ScullCH1 = ISNULL([EAFSkullCharge1Weight], 0) + ISNULL([EAFSkullCharge1WeightManual], 0),
@ScullCH2 = ISNULL([EAFSkullCharge2Weight], 0) + ISNULL([EAFSkullCharge2WeightManual], 0),
@ScullCH3 = ISNULL([EAFSkullCharge3Weight], 0) + ISNULL([EAFSkullCharge3WeightManual], 0),
@ScullCH4 = ISNULL([EAFSkullCharge4Weight], 0) + ISNULL([EAFSkullCharge4WeightManual], 0),
@CopexScrapAuto = EAFCopexScrapWeightAutoTotal, 
@CopexScrapManual = EAFCopexScrapWeightManualTotal,
@HMS1Auto = EAFHMS1WeightAutoTotal, 
@HMS1Manual = EAFHMS1WeightManualTotal,
@HMS12Auto = EAFHMS12WeightAutoTotal, 
@HMS12Manual = EAFHMS12WeightManualTotal,
@EndCutsAuto = EAFEndCutsWeightAutoTotal, 
@EndCutsManual = EAFEndCutsWeightManualTotal,
@BriquetteAuto = EAFBriquettesWeightAutoTotal, 
@BriquetteManual = EAFBriquettesWeightManualTotal,
@HBIDRIAuto = EAFHBIDRIWeightAutoTotal, 
@HBIDRIManual = EAFHBIDRIWeightManualTotal,
@BundleLMSAuto = EAFBundlesLMSWeightAutoTotal, 
@BundleLMSManual = EAFBundlesLMSWeightManualTotal,
 @ShreddedAuto = EAFShreddedWeightAutoTotal, 
 @ShreddedManual = EAFShreddedWeightManualTotal,
 @SkullAuto = EAFSkullWeightAutoTotal, 
 @SkullManual = EAFSkullWeightManualTotal
FROM [SMS_EAF_Per_Heat_ChargeMix] WITH(NOLOCK) 
WHERE [EAFHeatNo] = @HeatID AND [IsDeleted] = 0;
 
SELECT @CopexScrap = (@CopexScrapCH1 + @CopexScrapCH2 + @CopexScrapCH3 + @CopexScrapCH4),
       @HMS1 = (@HMS1CH1 + @HMS1CH2 + @HMS1CH3 + @HMS1CH4),
       @HMS12 = (@HMS12CH1 + @HMS12CH2 + @HMS12CH3 + @HMS12CH4),
       @EndCuts = (@EndCutsCH1 + @EndCutsCH2 + @EndCutsCH3 + @EndCutsCH4),
       @Briquette = (@BriquetteCH1 + @BriquetteCH2 + @BriquetteCH3 + @BriquetteCH4),
       @BundleLMS = (@BundleLMSCH1 + @BundleLMSCH2 + @BundleLMSCH3 + @BundleLMSCH4),
       @HBIDRI = (@HBIDRICH1 + @HBIDRICH2 + @HBIDRICH3 + @HBIDRICH4),
       @Shreedded = (@ShreeddedCH1 + @ShreeddedCH2 + @ShreeddedCH3 + @ShreeddedCH4),
       @Scull = (@ScullCH1 + @ScullCH2 + @ScullCH3 + @ScullCH4),
       @LotNo = CONCAT('LS_', CAST(@HeatID AS INT)),
       @LiquidMetal = ISNULL(@LiquidMetalWeight, 0);
 
IF @Bin3Name = @Bin4Name
BEGIN
    IF ISNULL(@Bin3Name, '') != ''
    BEGIN
        SELECT @HBIConsumption = CASE WHEN @Bin3Name != 'cdri' 
        THEN CAST(ISNULL(@Bin3Consumption, 0) AS FLOAT) + CAST(ISNULL(@Bin4Consumption, 0) AS FLOAT) END,
        @CdriConsumption = CASE WHEN @Bin3Name = 'cdri' 
        THEN CAST(ISNULL(@Bin3Consumption, 0) AS FLOAT) + CAST(ISNULL(@Bin4Consumption, 0) AS FLOAT) END;
    END
END
ELSE
BEGIN
    IF ISNULL(@Bin3Name, '') != ''
        SELECT @HBIConsumption = CASE WHEN @Bin3Name != 'cdri' 
        THEN CAST(ISNULL(@Bin3Consumption, 0) AS FLOAT) ELSE @HBIConsumption END,
               @CdriConsumption = CASE WHEN @Bin3Name = 'cdri' 
               THEN CAST(ISNULL(@Bin3Consumption, 0) AS FLOAT) ELSE @CdriConsumption END;
    IF ISNULL(@Bin4Name, '') != ''
        SELECT @HBIConsumption = CASE WHEN @Bin4Name != 'cdri' 
        THEN CAST(ISNULL(@Bin4Consumption, 0) AS FLOAT) ELSE @HBIConsumption END,
               @CdriConsumption = CASE WHEN @Bin4Name = 'cdri' 
               THEN CAST(ISNULL(@Bin4Consumption, 0) AS FLOAT) ELSE @CdriConsumption END;
END
 
UPDATE [dbo].[EAF_PER_HEAT] SET 
    [HBIConsumption] = @HBIConsumption, 
    [CdriConsumption] = @CdriConsumption, 
    [CopexScrap] = @CopexScrap,
    [HMS1] = @HMS1, 
    [HMS12] = @HMS12, 
    [EndCuts] = @EndCuts, 
    [Briquette] = @Briquette, 
    [BundleLMS] = @BundleLMS,
    [HBIDRI] = @HBIDRI, 
    [Shreedded] = @Shreedded, 
    [Scull] = @Scull, 
    ModifiedOn = GETDATE(), 
    ModifiedBy = @UserID
WHERE [ID] = @p_RecordId;
 
EXEC [HeatChargeMixConsumption] @HeatNo = @HeatID;
 
IF (@LiquidMetal > 0)
BEGIN
    EXEC [XBatch_I_Material_Produce_NoBOM_USP] 
    @Grade = 'TBD', 
    @HeatNo = @HeatID, 
    @ItemName = 'LIQUID METAL', 
    @LotNumber = @LotNo, 
    @Quantity = @LiquidMetal, 
    @SublotNumber = NULL, 
    @UOMName = 'ton', 
    @UserID = @UserId;
 
    SELECT @AutoLadleAdditionLime = [Silo3KG] + [Silo4KG], 
           @AutoLadleAdditionDolo = [Silo8KG],
           @AutoLadleAdditionSiMn = [Silo5KG] + [Silo6KG], 
           @AutoLadleAdditionFesi = [Silo7KG]
    FROM [LadleAddition] WITH(NOLOCK) 
    WHERE [HeatNo] = @HeatID AND [IsDeleted] = 0;
 
    SELECT @LadleAdditionLime = @AutoLadleAdditionLime, 
           @LadleAdditionDolo = @AutoLadleAdditionDolo,
           @LadleAdditionSiMn = @AutoLadleAdditionSiMn, 
           @LadleAdditionFeSi = @AutoLadleAdditionFesi;
 
    EXEC [XMES_AUTO_WO_AND_SO_CALCULATION] 
    @Plant = 'EAF', 
    @WorkOrder = @WorkOrder;

    EXEC [XMES_SMS_Temperature_Per_Heat_USP] 
    @Area = 'EAF', 
    @EndTime = @EndTime, 
    @HeatID = @HeatID, 
    @StartTime = @HeatStart;

    EXEC [Xstudio_Historian_EAF_Custom_usp] 
    @Attribute = 'All', 
    @EndTime = 
    @EndTime, 
    @Equipment = 'BCC64E43-7BF7-47FF-8A35-BCA3B6F4DAEB', 
    @StartTime = 
    @HeatStart;

    EXEC [XMES_EAF_SprayCoolingFlowDuration_USP] 
    @EndTime = 
    @EndTime, 
    @HeatID = 
    @HeatID, 
    @StartTime = @HeatStart;
 
    SELECT @E1SprayCollingFlowDurationSec = E1SprayCollingFlowDurationSec, 
           @E2SprayCollingFlowDurationSec = E2SprayCollingFlowDurationSec,
           @E3SprayCollingFlowDurationSec = E3SprayCollingFlowDurationSec, 
           @E1SprayCoolingFlowAvg = E1SprayCoolingFlowAvg,
           @E2SprayCoolingFlowAvg = E2SprayCoolingFlowAvg, 
           @E3SprayCoolingFlowAvg = E3SprayCoolingFlowAvg, 
           @EAFTemperature = EAFTemperature
    FROM EAF_PER_HEAT WITH(NOLOCK) 
    WHERE HeatID = @HeatID AND IsDeleted = 0;
END |
|---|

### Table 7

| Column Name | Display Name | Column Type | Column Equation |
|---|---|---|---|
| CreatedOn | CreatedOn | Normal |  |
| ModifiedOn | ModifiedOn | Normal |  |
| ID | ID | Normal |  |
| HeatReportDate | Heat Report Date | Normal |  |
| StartTime | StartTime | Normal |  |
| EndTime | EndTime | Normal |  |
| HeatID | Heat ID | Normal |  |
| CopexScrapCH1 | Copex Scrap CH1 | Normal |  |
| CopexScrapCH2 | Copex Scrap CH2 | Normal |  |
| BundleLMSCH1 | Bundle LMS CH1 | Normal |  |
| BundleLMSCH2 | Bundle LMS CH2 | Normal |  |
| HMS12CH1 | HMS 1 2 CH1 | Normal |  |
| HMS12CH2 | HMS 1 2 CH2 | Normal |  |
| PowerMWH | Power MWH | Normal |  |
| OxygenConsumption | Oxygen Consumption | Normal |  |
| HeatTime | HeatTime | Calculated | RIGHT('0' + CAST(CAST([EAF_PER_HEAT].[HeatTimeMinute] AS INT) AS VARCHAR), 2) + ':' + RIGHT('0' + CAST(CAST([EAF_PER_HEAT].[HeatTimeSecond] AS INT) AS VARCHAR), 2) |
| NGConsumption | NG Consumption | Normal | - |
| ChargeWeight | Charge Weight | Normal | - |
| HeatTimeMinute | Heat Time in Minute | Normal | - |
| HeatTimeSecond | Heat Time in Second | Normal | - |
| PowerOnTimeMinute | Power On Time in Minute | Normal | - |
| PowerOFFTimeMinute | Power OFF Time in Minute | Normal | - |
| PoweronTime | Power On Time | Calculated | CONCAT(cast([EAF_PER_HEAT].[PowerOnTimeMinute] as int),':',cast([EAF_PER_HEAT].[PowerOnTimeSecond] as int)) |
| PowerOffTime | Power Off Time | Calculated | CONCAT(cast([EAF_PER_HEAT].[PowerOffTimeMinute] as int),':',cast([EAF_PER_HEAT].[PowerOffTimeSecond] as int)) |
| ReportDate | ReportDate | Calculated | format([EAF_PER_HEAT].[HeatReportDate],'yyyy-MM-dd') |
| BIN1LimeConsumption | BIN1 Lime Consumption | Normal | - |
| BIN2DoloConsumption | BIN2 Dolo Consumption | Normal | - |
| BIN3Consumption | BIN3 Consumption | Normal | - |
| BIN4Consumption | BIN4 Consumption | Normal | - |
| HeattimeTotalSeconds | Heat time Total Seconds | Calculated | (([EAF_PER_HEAT].[HeatTimeMinute] * 60) + ([EAF_PER_HEAT].[HeatTimeSecond]))/60 |
| PoweronTimeTotalSeconds | Power on Time Total Seconds | Calculated | (([EAF_PER_HEAT].[PowerOnTimeMinute] * 60) + ([EAF_PER_HEAT].[PowerOnTimeSecond]))/60 |
| PowerOffTimeTotalSeconds | Power Off Time Total Seconds | Calculated | (([EAF_PER_HEAT].[PowerOFFTimeMinute] * 60) + ([EAF_PER_HEAT].[PowerOFFTimeSecond]))/60 |
| TotalChargeWeightMT | Total Charge Weight MT | Normal | - |
| SteelGrade | Steel Grade | Normal | - |
| TapTimeMinute | Tap Time in Minute | Calculated | cast(DATEDIFF(SECOND, [EAF_PER_HEAT].[StartTime], [EAF_PER_HEAT].[EndTime]) as decimal(18,2))/60.00 |
| TapStart | Tap Start Time | Calculated | [EAF_PER_HEAT].[StartTime] |
| HeatStart | Heat Start Time | Normal | - |
| Briquette | Briquette in Ton | Normal | - |
| BundleLMS | Bundle LMS in Ton | Normal | - |
| CopexScrap | Copex Scrap in Ton | Normal | - |
| EndCuts | End Cuts in Ton | Normal | - |
| HBIDRI | HBI DRI in Ton | Normal | - |
| HMS12 | HMS 1 2 in Ton | Normal | - |
| HMS1 | HMS 1 in Ton | Normal | - |
| Scull | Scull in Ton | Normal | - |
| Shreedded | Shreedded in Ton | Normal | - |
| LiquidMetalWeight | Liquid Metal Weight in Ton | Normal | - |
| YieldPerHeat | Yield Percentage Per Heat | Calculated | CAST((ISNULL(ISNULL([EAF_PER_HEAT].[CalcLiquidMetalWeight],[EAF_PER_HEAT].[LiquidMetalWeight]),0)/NULLIF([EAF_PER_HEAT].[TotalChargeWeightMT],0))*100.00 AS DECIMAL(18,2)) |
| NGconsumptionpertonofsteel | NG consumption per ton of steel | Normal | - |
| Limepertonofsteel | Lime per ton of steel | Normal | - |
| Dololimepertonofsteel | Dolo lime per ton of steel | Normal | - |
| PowerPerTonofSteel | Power Per Ton | Normal | - |
| CarbonConsumption | Carbon Consumption | Normal | - |
| WorkOrder | Work Order | Normal | - |
| CalcLiquidMetalWeight | Calc Liquid Metal Weight Ton | Normal | - |
| SAPWorkflowStatus | SAPWorkflowStatus | Normal | - |
| LSDELTA | LS DELTA | Calculated | Cast(isnull([EAF_PER_HEAT].[CalcLiquidMetalWeight],0)-isnull([EAF_PER_HEAT].[LiquidMetalWeight],0) as decimal(18,2)) |
| TempTips | Temp Tips | Normal | - |
| EBTFilter | EBT Filter | Normal | - |
| RamMass | Ram Mass | Normal | - |
| GunningMass | Gunning Mass | Normal | - |
| FettlingMass | Fettling Mass | Normal | - |
| TapTemp | Tap Temp | Normal | - |
| ThroughputTPH | Throughput TPH | Calculated | COALESCE([EAF_PER_HEAT].[CalcLiquidMetalWeight],[EAF_PER_HEAT].[LiquidMetalWeight]) *60 / ([EAF_PER_HEAT].[PoweronTimeTotalSeconds] + [EAF_PER_HEAT].[PowerOffTimeTotalSeconds]) |
| PowerOnCharge | Power On Charge | Normal | - |
| CokeInjection | Coke Injection | Normal | - |
| TotalElectrodeConsumption | Total Electrode Consumption | Normal | - |
| EAFTemperature | EAF Temperature | Normal | - |