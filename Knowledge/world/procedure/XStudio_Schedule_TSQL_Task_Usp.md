---
type: procedure
title: "XStudio_Schedule_TSQL_Task_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Schedule_TSQL_Task_Usp

Parameters: @name varchar, @ID nvarchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## What its own log shows

1,216 log rows, 2026-05-29 00:32 to 2026-09-02 07:10.

Steps:
- 1 Entered
- 2 Get Configuration database by system id of XBatch Start
- 3 Get Configuration database by system id of XBatch End
- 4 Set query to insert schedule task info for python script Campaign Master Excel Details Import Start
- 4 Set query to insert schedule task info for python script Electricity Meter Reading Start
- 4 Set query to insert schedule task info for python script WRM Campaign Master Excel Details Import Start
- 5 Set query to insert schedule task info for python script Campaign Master Excel Details Import End
- 5 Set query to insert schedule task info for python script Electricity Meter Reading End
- 5 Set query to insert schedule task info for python script WRM Campaign Master Excel Details Import End
- 6 Execute query (INSERT INTO [XStudio_Configuration_XBatch].[dbo].[XStudio_ScheduleTask_Trn_Tbl]
				     (Name,StepID,StepName,XMLParameter,STATUS)
				     VALUES
				     ('Campaign Master Excel Details Import' , 
				      'A377E979-985A-43E7-80B8-BEA9E69E470F', 
				      'PythonScript', 
				      '<XMLControls xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
				       <Controls>
				     	<XMLControl>
				     	  <ControlName>PythonScriptID</ControlName>
				     	  <ControlDisplayValue>A8CF3687-2DE6-494E-AA51-F91E252A3A0F</ControlDisplayValue>
				     	  <ControlValue>A8CF3687-2DE6-494E-AA51-F91E252A3A0F </ControlValue>
				     	</XMLControl>
				       </Controls>
				     </XMLControls>', 'waiting')) to insert schedule task info for python script Campaign Master Excel Details Import Start
- 6 Execute query (INSERT INTO [XStudio_Configuration_XBatch].[dbo].[XStudio_ScheduleTask_Trn_Tbl]
				     (Name,StepID,StepName,XMLParameter,STATUS)
				     VALUES
				     ('Electricity Meter Reading' , 
				      'A377E979-985A-43E7-80B8-BEA9E69E470F', 
				      'PythonScript', 
				      '<XMLControls xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
				       <Controls>
				     	<XMLControl>
				     	  <ControlName>PythonScriptID</ControlName>
				     	  <ControlDisplayValue>39FA8990-EB43-4E08-B953-AD3E873DCB1F</ControlDisplayValue>
				     	  <ControlValue>39FA8990-EB43-4E08-B953-AD3E873DCB1F </ControlValue>
				     	</XMLControl>
				       </Controls>
				     </XMLControls>', 'waiting')) to insert schedule task info for python script Electricity Meter Reading Start
- 6 Execute query (INSERT INTO [XStudio_Configuration_XBatch].[dbo].[XStudio_ScheduleTask_Trn_Tbl]
				     (Name,StepID,StepName,XMLParameter,STATUS)
				     VALUES
				     ('WRM Campaign Master Excel Details Import' , 
				      'A377E979-985A-43E7-80B8-BEA9E69E470F', 
				      'PythonScript', 
				      '<XMLControls xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
				       <Controls>
				     	<XMLControl>
				     	  <ControlName>PythonScriptID</ControlName>
				     	  <ControlDisplayValue>11E677FF-527C-4687-AE61-4A7ACCAD46AB</ControlDisplayValue>
				     	  <ControlValue>11E677FF-527C-4687-AE61-4A7ACCAD46AB </ControlValue>
				     	</XMLControl>
				       </Controls>
				     </XMLControls>', 'waiting')) to insert schedule task info for python script WRM Campaign Master Excel Details Import Start
- 7 Execute query (INSERT INTO [XStudio_Configuration_XBatch].[dbo].[XStudio_ScheduleTask_Trn_Tbl]
				     (Name,StepID,StepName,XMLParameter,STATUS)
				     VALUES
				     ('Campaign Master Excel Details Import' , 
				      'A377E979-985A-43E7-80B8-BEA9E69E470F', 
				      'PythonScript', 
				      '<XMLControls xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
				       <Controls>
				     	<XMLControl>
				     	  <ControlName>PythonScriptID</ControlName>
				     	  <ControlDisplayValue>A8CF3687-2DE6-494E-AA51-F91E252A3A0F</ControlDisplayValue>
				     	  <ControlValue>A8CF3687-2DE6-494E-AA51-F91E252A3A0F </ControlValue>
				     	</XMLControl>
				       </Controls>
				     </XMLControls>', 'waiting')) to insert schedule task info for python script Campaign Master Excel Details Import End
- 7 Execute query (INSERT INTO [XStudio_Configuration_XBatch].[dbo].[XStudio_ScheduleTask_Trn_Tbl]
				     (Name,StepID,StepName,XMLParameter,STATUS)
				     VALUES
				     ('Electricity Meter Reading' , 
				      'A377E979-985A-43E7-80B8-BEA9E69E470F', 
				      'PythonScript', 
				      '<XMLControls xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
				       <Controls>
				     	<XMLControl>
				     	  <ControlName>PythonScriptID</ControlName>
				     	  <ControlDisplayValue>39FA8990-EB43-4E08-B953-AD3E873DCB1F</ControlDisplayValue>
				     	  <ControlValue>39FA8990-EB43-4E08-B953-AD3E873DCB1F </ControlValue>
				     	</XMLControl>
				       </Controls>
				     </XMLControls>', 'waiting')) to insert schedule task info for python script Electricity Meter Reading End
- 7 Execute query (INSERT INTO [XStudio_Configuration_XBatch].[dbo].[XStudio_ScheduleTask_Trn_Tbl]
				     (Name,StepID,StepName,XMLParameter,STATUS)
				     VALUES
				     ('WRM Campaign Master Excel Details Import' , 
				      'A377E979-985A-43E7-80B8-BEA9E69E470F', 
				      'PythonScript', 
				      '<XMLControls xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
				       <Controls>
				     	<XMLControl>
				     	  <ControlName>PythonScriptID</ControlName>
				     	  <ControlDisplayValue>11E677FF-527C-4687-AE61-4A7ACCAD46AB</ControlDisplayValue>
				     	  <ControlValue>11E677FF-527C-4687-AE61-4A7ACCAD46AB </ControlValue>
				     	</XMLControl>
				       </Controls>
				     </XMLControls>', 'waiting')) to insert schedule task info for python script WRM Campaign Master Excel Details Import End
- 8 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XStudio_Schedule_TSQL_Task_Usp @name='WRM Campaign Master Excel Details Import', @ID='11E677FF-527C-4687-AE61-4A7ACCAD46AB'`
