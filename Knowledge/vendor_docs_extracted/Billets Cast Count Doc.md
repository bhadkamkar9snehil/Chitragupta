# Billets Cast Count Doc

*Extracted from `Billets Cast Count Doc.docx` -- real vendor handover doc, not invented.*

SITC OF X-FORCE HISTORIAN AND DASHBOARD DEVELOPMENT
SOHAR STEEL OMAN
Declaration
This Project Handover Document is intended only for personnel who already have a working knowledge of the X-Studio framework and related technical concepts.
The reader is expected to have prior knowledge of the X-Studio Event Framework, Workflows, Asset Structure, Database Structure, SQL Logic, and Stored Procedures. This document is prepared as a project-specific technical handover and reference document and is not intended to provide basic or introductory training on these concepts.
The document focuses on the project-specific implementation, configurations, process flows, database objects, SQL logic, workflows, and related technical details required for Project Support, Maintenance, Troubleshooting, and Further Development.
Therefore, readers should have sufficient prior knowledge of X-Studio and the above-mentioned technical areas to effectively understand and utilize the information provided in this document.

# Billets Cast Count – Data Insert Flow


## 1. Overview

This section describes the event configuration and insert condition used for capturing CCM billet cast-count data. The event configuration is based on the Cast Billets Count process event, and the Billets Produces Start state is used to identify the condition under which billet-count data is captured and stored for the current heat.

## 2. Event Configuration


### 2.1 Event Entity

The main event data is stored in the BilletsCastCount entity. This entity stores the required billet-count data captured for each heat. The Event Entity is configured as a Process event.

### 2.2 Event Master

The Event Master maps the Cast Billets Count process event with the BilletsCastCount transaction entity. The configuration identifies Cast Billets Count as the process event and BilletsCastCount as the transaction entity.

### 2.3 Event Configuration Entity

The Event Configuration Entity defines the configuration for the Cast Billets Count event. In Attributes, the required billet-count attributes are defined. In Tag Mapping, each attribute is mapped to its corresponding CCM tag. In State, the condition that triggers the event is configured.

### 2.4 Event Configuration Tags


## 3. Data Insert Condition

Per-heat billet-count data insertion is controlled by the Billets Produces Start state configured against the Cast Billets Count event configuration. The state uses the total billet count as its trigger condition.

### 3.1 Event Status Configuration


### 3.2 State Condition and Transition Logic


### 3.3 Meaning of the Condition Inputs

The state is configured with State Sequence 1, zero seconds of State On Delay and State Off Delay, workflow processing enabled, State On Workflow as Entered, and State Off Workflow as Completed.

## 4. Per Heat Data Insert Flow

When the Cast Billets Count event is triggered, the configured tag attributes are evaluated using the Billets Produces Start state condition. If the condition evaluates to True, the mapped billet-count values are captured for the current heat and the configured workflow processing is executed.

### 4.1 Workflow Configuration

The workflow for the BilletsCastCount entity is configured under the DEFAULT application. The Work Flow List identifies the workflow as "CCM_Trigger_Workflow", as shown below.

### 4.2 Workflow Entered State — Stored Procedure Action

When the workflow action runs, it resolves the relevant CCM heat from CCM_PER_HEAT, synchronizes the CCM heat-report date and report date from EAF_PER_HEAT when required, retrieves billet-related values from CCM_Per_Heat, derives the billet item and material grade, and updates the latest spectrometer sample status.

### 4.3 Workflow Entered SQL Action Details

1. Heat identification — @HeatID is resolved from the most recently created CCM_PER_HEAT record whose Starttime is earlier than @StartTime.
2. Heat-report date synchronization — CCM_PER_HEAT is joined to EAF_PER_HEAT by HeatID. Missing CCM HeatReportDate or ReportDate values are filled from EAF_PER_HEAT, with current-date fallbacks. ModifiedOn and Source are also updated.
3. Variable initialization — Variables are declared for item name, material grade, grade, billet quantity, heat number, total production, work order, cross-section, and set weight.
4. Billet item and grade resolution — CrossSection 130 maps to Billet_130X130; all other values map to Billet_150X150. Grade defaults to 3SP/PS when NULL, and TotalBilletsCount defaults to zero.
5. Spectrometer sample update — Quality_Spectro_IsLatestSample_Update_Usp is executed to update the latest spectrometer sample status.
Note:  This extract depends on variables declared or assigned elsewhere in the complete workflow procedure, including @StartTime and @HeatID.

### 4.4 Workflow Completed State — Stored Procedure Action

When the workflow reaches the Completed state, the action performs the post-casting processing for the CCM heat. It updates mould-tube life tracking, records the life-tracking transaction, executes the CCM SMS block historian calculation, updates the latest spectrometer sample flag, synchronizes quality and report-date information, calculates billet production weight using the operator-declared billet count and cross-section-specific set weight, updates CCM_Per_Heat, and executes the downstream GLS, daily-production, and billet-tracking procedures.

### 4.5 Workflow Completed SQL Action Details

1. Mould tube life update - Life_Tracking_Status records matching Mould Tube Life Strand % are updated. CurrentLife is incremented, HeatID is assigned to the current heat, timestamps are refreshed, and ConsumedLifePercentage is calculated against MaximumLife.
2. Life-tracking transaction - A record is inserted into Life_Tracking_Transaction_tbl preserving EntryDateTime, HeatID, Life, LifeType, CurrentLife, ConsumePercentage, and AlertPercentage.
3. CCM SMS block historian processing - Xstudio_Historian_CCM_SMS_Block_usp is executed for all attributes using the configured CCM equipment ID and workflow StartTime/EndTime.
4. Latest spectrometer sample update - Quality_Spectro_IsLatestSample_Update_Usp is executed.
5. Grade and section retrieval - Grade and CrossSection are retrieved from ccm_per_heat and CrossSection is converted to CrossSectionXCrossSection.
6. Heat chemistry quality update - Heat_Chemistry_Quality_Data is updated with the current heat's Grade and calculated section.
7. Report-date synchronization - Missing CCM HeatReportDate or ReportDate values are filled from EAF_PER_HEAT.
8. CCM production data retrieval - HeatID, TotalBilletsCount, TotalProduction, WorkOrder, and CrossSection are retrieved.
9. Set-weight retrieval - The latest non-deleted MaterialSpecificWeight for the current cross-section is retrieved from Billet_Cross_Section.
10. Billet-weight calculation - Total billet weight is calculated as
ISNULL(@ActualBilletsCountbyOperator, 0) * 12 * @Setweight.
11. CCM_Per_Heat update — Billet count, production weight, set weight, remaining posted quantities, actual count, SAP workflow status, and related billet-count/weight fields are updated.
12. GLS back-calculation — XMES_BackCalculation_GLS_Usp is executed for the current heat.
13. Daily production tracking — XBatch_SMS_Heat_Tracking_Daily_Production_Data is executed using @HeatID.
14. Billet tracking — XMES_I_Billets_Tracking_Usp is executed with @HeatID and parameter 1.
Note:  This SQL extract depends on workflow variables including @HeatID, @StartTime, @EndTime, and @ActualBilletsCountbyOperator. Confirm that these variables are declared and assigned before the Completed-state action executes.

---
## Tables (real technical detail -- tag mappings, state configs, condition logic)


### Table 1

| Project | SITC of X-Force Historian and Dashboard Development for Sohar Steel Oman |
|---|---|
| Prepared By | Mahesh Udar |
| Document Type | Billets Cast Count Data Insert Flow |
| Handover Date |  |
| Handover To |  |
| Document Version | 1.0 |

### Table 2

| Attribute | Tag Name |
|---|---|
| CCMTotalBilletsCount | CCM_TOTAL_BILLET_COUNT_PRM |
| CCMHeatNO | CCM_HEAT_NUMBER_PRM |
| ActualBilletCountByOperator | CCM_DECLARED_TOTAL_BILLET_COUNT_PER_HEAT_PRM |

### Table 3

| Event status name | Billets Produces Start |
|---|---|
| State sequence | 1 |
| Active | Yes |
| State-On delay | 0 seconds |
| State-Off delay | 0 seconds |
| Workflow enabled | Yes |
| Workflow type | Workflow |
| Workflow Attribute | WorkflowStatus |
| State-On workflow | Entered |
| State-Off workflow | Completed |

### Table 4

| {CCMTotalBilletsCount}>0 |
|---|

### Table 5

| Result | Condition evaluated | State action | Workflow |
|---|---|---|---|
| TRUE | CCMTotalBilletsCount > 0 | Turn the event state ON | Entered |
| FALSE | CCMTotalBilletsCount <= 0 | Turn the event state OFF | Completed |
| NULL | Not applicable — this state uses a direct boolean expression, not a nested IIF | — | — |

### Table 6

| Input | Value used | Operational meaning in this configuration |
|---|---|---|
| CCMTotalBilletsCount | > 0 | Billets are being counted for the current heat, confirming casting output exists and billet-count data should be captured. |

### Table 7

| SELECT @HeatID = (SELECT TOP 1 HeatID FROM [Xstudio_xbatch].[dbo].[CCM_PER_HEAT] WITH (NOLOCK)
WHERE Starttime < @StartTime
ORDER BY Createdon DESC);
 
UPDATE CCM
SET CCM.HeatReportDate = ISNULL(EAF.HeatReportDate, CAST(GETDATE() AS DATE)),
    CCM.ReportDate =  ISNULL(EAF.ReportDate, FORMAT(GETDATE(), 'yyyy-MM-dd')),
    CCM.ModifiedOn = GETDATE(), CCM.[Source] = 'T-SQL'
FROM [Xstudio_xbatch].[dbo].[CCM_PER_HEAT] AS CCM
JOIN [Xstudio_xbatch].[dbo].[EAF_PER_HEAT] AS EAF ON EAF.heatid = CCM.HeatID AND EAF.isdeleted = 0
WHERE EAF.heatid = @HeatID AND (CCM.HeatReportDate IS NULL OR CCM.ReportDate IS NULL);
 
DECLARE @ItemName VARCHAR(MAX),
        @MaterialGrade VARCHAR(MAX),
        @Grade VARCHAR(MAX),
        @Qty INT,
        @HeatNo INT,
        @TotalProduction DECIMAL(18,4),
        @WorkOrder VARCHAR(36),
        @CrossSection INT,
        @Setweight DECIMAL(18,4);
 
SELECT  @HeatNo = HeatID,
        @ItemName = (CASE WHEN CrossSection = 130
                     THEN 'Billet_130X130'
                     ELSE 'Billet_150X150' END),
        @MaterialGrade = ISNULL(Grade, '3SP/PS'),
        @Qty = ISNULL(TotalBilletsCount, 0)
FROM CCM_Per_Heat WITH (NOLOCK) WHERE HEATID = @HeatNo;
 
EXEC [Quality_Spectro_IsLatestSample_Update_Usp] |
|---|

### Table 8

| UPDATE Life_Tracking_Status
SET ModifiedOn = GETDATE(),
    CurrentLife = LTS.CurrentLife + 1,
    HeatID = @HeatID,
    ConsumedLifePercentage = CAST(CAST(LTS.CurrentLife AS DECIMAL(18,2)) / CAST(MaximumLife AS DECIMAL(18,2)) * 100 AS  DECIMAL(18,2)),
    LastUpdatedTime = GETDATE()
FROM Life_Tracking_Status LTS
JOIN (SELECT DISTINCT NAME, MaximumLife
       FROM [XStudio_Xbatch].[dbo].[Life_Tracking] AS LT WITH(NOLOCK)
       WHERE [Name] LIKE 'Mould Tube Life Strand %' AND IsDeleted = 0) AS LT ON LT.Name = LTs.LifeType
WHERE LTS.IsDeleted = 0 AND  LT.[Name] LIKE 'Mould Tube Life Strand %';
 
INSERT INTO Life_Tracking_Transaction_tbl (EntryDateTime, HeatID, Life, LifeType, CurrentLife, ConsumePercentage,AlertPercentage)
SELECT GETDATE(), HeatID, LTS.[Life], LTS.LifeType, LTS.CurrentLife, ConsumedLifePercentage, LTS.AlertPercentage
FROM Life_Tracking_Status LTS
JOIN  (SELECT DISTINCT NAME, MaximumLife
        FROM [XStudio_Xbatch].[dbo].[Life_Tracking] AS LT WITH(NOLOCK)
        WHERE [Name] LIKE 'Mould Tube Life Strand %' AND IsDeleted = 0) AS LT ON LT.Name = LTs.LifeType
WHERE LTS.IsDeleted = 0 AND  LT.[Name] LIKE 'Mould Tube Life Strand %';
 
EXEC [Xstudio_Historian_CCM_SMS_Block_usp]
        @Attribute='All',
        @EndTime = @EndTime,
        @Equipment = 'BF740CF1-17FF-4579-BECE-342EA6A59D3D',
        @StartTime = @StartTime;
 
EXEC [Quality_Spectro_IsLatestSample_Update_Usp];
 
DECLARE @grade VARCHAR(100), @Crosssection VARCHAR(100);
 
SELECT @grade = grade,
       @Crosssection = IIF(Crosssection IS NULL, NULL, CONCAT(CrossSection,'X', CrossSection))
FROM [ccm_per_heat] WITH(NOLOCK)
WHERE CAST(heatid AS INT) = CAST(@HeatID AS INT) AND isdeleted = 0;
 
UPDATE [Heat_Chemistry_Quality_Data]
SET Grade = @grade , section = @Crosssection,
    ModifiedOn = GETDATE()
WHERE HeatNo = CAST(CAST(@HeatID AS INT) AS VARCHAR(7)) AND isdeleted = 0;
 
UPDATE CCM
SET CCM.HeatReportDate = EAF.HeatReportDate,
    CCM.ReportDate = EAF.ReportDate,
    CCM.ModifiedOn = GETDATE()
FROM [Xstudio_xbatch].[dbo].[CCM_PER_HEAT] AS CCM
JOIN [Xstudio_xbatch].[dbo].[EAF_PER_HEAT] AS EAF ON EAF.heatid = CCM.HeatID AND EAF.isdeleted = 0
WHERE EAF.heatid = @HeatID AND (CCM.HeatReportDate IS NULL OR CCM.ReportDate IS NULL);
 
DECLARE @ItemName VARCHAR(MAX),
        @MaterialGrade VARCHAR(MAX),
        @Qty INT,
        @HeatNo INT,
        @TotalProduction DECIMAL(18,4),
        @WorkOrder VARCHAR(36),
        @Setweight DECIMAL(18,4),
        @CrossSection1 INT;
 
SELECT @HeatNo=HeatID,
        @Qty = ISNULL(TotalBilletsCount,0),
        @TotalProduction = TotalProduction,
        @WorkOrder = WorkOrder,
        @CrossSection1 = CrossSection
FROM CCM_Per_Heat WITH (NOLOCK)
WHERE HEATID = CAST(@HeatID AS INT);
 
SELECT TOP 1 @Setweight = MaterialSpecificWeight
FROM Billet_Cross_Section a WITH(NOLOCK)
WHERE a.CrossSection1 = @CrossSection1 AND isdeleted = 0
ORDER BY Createdon DESC;
 
DECLARE @Totalbilletweightton DECIMAL(18,4) = (SELECT (ISNULL(@ActualBilletsCountbyOperator,0) * 12 * @Setweight));
 
SET @ActualBilletsCountbyOperator = ISNULL(@ActualBilletsCountbyOperator,0);
 
UPDATE CCM_Per_Heat
SET ModifiedOn = GETDATE(),
    TotalBilletsCount = @ActualBilletsCountbyOperator,
    TotalProduction = @Totalbilletweightton,
    Noof140mmbillets = @ActualBilletsCountbyOperator,
    ActualBilletWeightTon = @Totalbilletweightton,
    RemainingPostedBilletCount = ISNULL(RemainingPostedBilletCount,@ActualBilletsCountbyOperator),
    RemainingPostedBilletWeightTon = ISNULL(RemainingPostedBilletWeightTon,@Totalbilletweightton),
    ActualBilletCount = @ActualBilletsCountbyOperator,
    SetWeightTon = @Setweight,
    SAPWorkflowStatus = ISNULL(SAPWorkflowStatus,'Entered'),
    NoofBillets1 = @ActualBilletsCountbyOperator,
    CalcBilletsWeight1 = @Totalbilletweightton
WHERE HeatID = @HeatNo;
 
EXEC [XMES_BackCalculation_GLS_Usp]
        @HeatNo = @HeatNo;
 
EXEC [XBatch_SMS_Heat_Tracking_Daily_Production_Data]
        @HeatID = @HeatID;
 
EXEC [XMES_I_Billets_Tracking_Usp]
        @HeatID,
        1; |
|---|