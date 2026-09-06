# LMEL MES Stored Procedures Reference

_Generated automatically on 2026-09-02 10:42:31 IST_

**Database:** `XStudio_Helpdesk`  
**Server:** `10.2.6.204`  
**Script Run DateTime:** `2026-09-02 10:42:31 IST`  
**Script Run DateTime For File Name:** `2026-09-02_10-42-31`  
**Stored Procedure Count:** `12`  

This document provides:
- stored procedure list
- parameters
- exec template
- full stored procedure text

---

## Table of Contents

- [dbo.L3_Module_Import](#dbol3moduleimport)
- [dbo.L3_Module_Import_2](#dbol3moduleimport2)
- [dbo.Logsheet_Generation_Check](#dbologsheetgenerationcheck)
- [dbo.sp_assignhod](#dbospassignhod)
- [dbo.sp_assignsupportexecutive](#dbospassignsupportexecutive)
- [dbo.SP_Create_TicketNo](#dbospcreateticketno)
- [dbo.sp_handoverDetails](#dbosphandoverdetails)
- [dbo.Sp_Logsheet_Calculation_Adhoc](#dbosplogsheetcalculationadhoc)
- [dbo.Sp_Logsheet_Calculation_Adhoc_By_Date](#dbosplogsheetcalculationadhocbydate)
- [dbo.UAT_Test_Report_USP](#dbouattestreportusp)
- [dbo.UAT_Tracking_Transaction_DataInsert_USP](#dbouattrackingtransactiondatainsertusp)
- [dbo.UAT_U_Enddatetime_Ticket_Generate_USP](#dbouatuenddatetimeticketgenerateusp)


## Summary

**Database:** `XStudio_Helpdesk`  
**Server:** `10.2.6.204`  
**Generated On:** `2026-09-02 10:42:31 IST`  
**Stored Procedure Count:** `12`  

| Stored Procedure | Parameters | Created On | Modified On |
| --- | ---: | --- | --- |
| dbo.L3_Module_Import | 4 | 2023-06-28 11:33:07 | 2023-06-29 12:39:29 |
| dbo.L3_Module_Import_2 | 6 | 2023-08-31 12:28:54 | 2023-08-31 13:56:58 |
| dbo.Logsheet_Generation_Check | 0 | 2022-12-27 15:42:52 | 2023-01-28 12:19:16 |
| dbo.sp_assignhod | 1 | 2022-08-12 11:36:36 | 2022-09-22 16:21:07 |
| dbo.sp_assignsupportexecutive | 2 | 2022-08-12 11:30:28 | 2022-09-22 16:21:07 |
| dbo.SP_Create_TicketNo | 3 | 2022-08-12 12:07:52 | 2025-08-07 11:26:37 |
| dbo.sp_handoverDetails | 4 | 2023-02-24 16:54:09 | 2023-02-24 16:54:09 |
| dbo.Sp_Logsheet_Calculation_Adhoc | 3 | 2023-07-19 16:10:42 | 2023-07-19 16:54:17 |
| dbo.Sp_Logsheet_Calculation_Adhoc_By_Date | 1 | 2023-07-19 16:53:16 | 2023-07-19 16:53:16 |
| dbo.UAT_Test_Report_USP | 1 | 2025-08-06 18:06:18 | 2025-08-22 09:03:52 |
| dbo.UAT_Tracking_Transaction_DataInsert_USP | 0 | 2025-08-07 16:09:24 | 2025-08-22 09:53:08 |
| dbo.UAT_U_Enddatetime_Ticket_Generate_USP | 2 | 2025-08-05 18:34:56 | 2025-08-07 16:09:47 |

---



## Detailed Stored Procedure Information



## dbo.L3_Module_Import

**Schema:** dbo  
**Procedure Name:** L3_Module_Import  
**Created On:** 2023-06-28 11:33:07  
**Modified On:** 2023-06-29 12:39:29  
**Parameter Count:** 4  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @CS | nvarchar(500) | NO |  |
| @CR | nvarchar(500) | NO |  |
| @CT | nvarchar(500) | NO |  |
| @FP | nvarchar(500) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[L3_Module_Import]
    @CS = '',
    @CR = '',
    @CT = '',
    @FP = '';
```

### Full Definition

```sql
CREATE     PROCEDURE [dbo].[L3_Module_Import] (
    @CS NVARCHAR(500),
    @CR NVARCHAR(500),
    @CT NVARCHAR(500) = 'MDI',
    @FP NVARCHAR(500)
)
AS
BEGIN
    DECLARE @Command NVARCHAR(999),
            @CurrentRegister1 NVARCHAR(50),
            @StaticPath NVARCHAR(500),
            @FileName NVARCHAR(500),
            @FilePath NVARCHAR(500),
            @DBName NVARCHAR(100),
            @ConfigDBName NVARCHAR(100)

    -- Define the static path
    SET @StaticPath = 'D:\Publish\XStudio\wwwroot\HtmlPages\Helpdesk\Master\Documents\'

    -- Replace spaces in the CurrentRegister
    SET @CurrentRegister1 = REPLACE(@CR, ' ', '_')

    -- Extract the file name and path from the passed file path
    SET @FileName = SUBSTRING(@FP, CHARINDEX('"FileName":"', @FP) + LEN('"FileName":"'), CHARINDEX('","FilePath":"', @FP) - CHARINDEX('"FileName":"', @FP) - LEN('"FileName":"'))
    SET @FileName = REPLACE(@FileName, '.xlsx', '.xls') -- Replace the file extension if necessary

    -- Concatenate the static path with the extracted file name
    SET @FP = @StaticPath + @FileName

    -- Extract the system name from @CS parameter
    SET @DBName = 'Xstudio_' + REPLACE(@CS, '_', '_')

    -- Construct the configuration database name
    SET @ConfigDBName = 'Xstudio_Configuration_' + @CS

    SET @Command = 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -command "D:\Script\ImportData.ps1" -Type "' + @CT + '" -Register "' + @CurrentRegister1 + '" -System "' + @CS + '" -File "' + @FP + '"'
    EXEC xp_cmdshell @Command

    PRINT 'Type: ' + @CT
    PRINT 'Register: ' + @CurrentRegister1
    PRINT 'System: ' + @CS
    PRINT 'File: ' + @FP 
    PRINT 'Database Name: ' + @DBName
    PRINT 'Configuration Database Name: ' + @ConfigDBName

    -- Execute the dynamic SQL query

-- Execute the dynamic SQL query
DECLARE @DynamicSQL NVARCHAR(MAX),@tablename nvarchar(50),@name nvarchar(50)
SET @DynamicSQL = '
    DECLARE @RegisterName NVARCHAR(50)
    SET @RegisterName = REPLACE(' + QUOTENAME(@CurrentRegister1, '''') + ', ''_'', '' '')

    SELECT @name = b.name, @tablename = c.Name
    FROM ' + QUOTENAME(@DBName) + '..Sections_Master AS a
    JOIN ' + QUOTENAME(@DBName) + '..Logsheet_Master AS b ON b.id = a.LogsheetMasterID
    JOIN ' + QUOTENAME(@ConfigDBName) + '..XStudio_Entities_Mst_Tbl AS c ON c.id = a.EntityID
    WHERE a.IsDeleted = 0 AND b.IsDeleted = 0 AND c.IsDeleted = 0
    AND b.name = @RegisterName
    ORDER BY 1
	print @name
	print @tablename
	'

EXEC sp_executesql @DynamicSQL,N'@tablename nvarchar(50) output,@name nvarchar(50) ',@tablename = @tablename output ,@name = @name




END
```

---


## dbo.L3_Module_Import_2

**Schema:** dbo  
**Procedure Name:** L3_Module_Import_2  
**Created On:** 2023-08-31 12:28:54  
**Modified On:** 2023-08-31 13:56:58  
**Parameter Count:** 6  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @CS | nvarchar(500) | NO |  |
| @CR | nvarchar(500) | NO |  |
| @CT | nvarchar(500) | NO |  |
| @FP | nvarchar(500) | NO |  |
| @FM | datetime | NO |  |
| @TE | datetime | NO |  |

### EXEC Template

```sql
EXEC [dbo].[L3_Module_Import_2]
    @CS = '',
    @CR = '',
    @CT = '',
    @FP = '',
    @FM = '2026-05-04 00:00:00',
    @TE = '2026-05-04 00:00:00';
```

### Full Definition

```sql
Create   PROCEDURE [dbo].[L3_Module_Import_2] (
    @CS NVARCHAR(500) =null,
    @CR NVARCHAR(500)=null,
    @CT NVARCHAR(500) = 'MDI',
    @FP NVARCHAR(500) = null,
    @FM DATETIME,
    @TE DATETIME
)
AS
BEGIN
    DECLARE @Command NVARCHAR(999),
            @CurrentRegister1 NVARCHAR(50),
            @StaticPath NVARCHAR(500),
            @FileName NVARCHAR(500),
            @FilePath NVARCHAR(500),
            @DBName NVARCHAR(100),
            @ConfigDBName NVARCHAR(100)

    -- Define the static path
    SET @StaticPath = 'D:\Publish\XStudio\wwwroot\HtmlPages\Helpdesk\Master\Documents\'

    -- Replace spaces in the CurrentRegister
    SET @CurrentRegister1 = REPLACE(@CR, ' ', '_')

    -- Extract the file name and path from the passed file path
    SET @FileName = SUBSTRING(@FP, CHARINDEX('"FileName":"', @FP) + LEN('"FileName":"'), CHARINDEX('","FilePath":"', @FP) - CHARINDEX('"FileName":"', @FP) - LEN('"FileName":"'))
    --SET @FileName = REPLACE(@FileName, '.xlsx', '.xls') -- Replace the file extension if necessary

    -- Concatenate the static path with the extracted file name
    SET @FP = @StaticPath + @FileName

    -- Extract the system name from @CS parameter
    SET @DBName = 'Xstudio_' + REPLACE(@CS, '_', '_')

    -- Construct the configuration database name
    SET @ConfigDBName = 'Xstudio_Configuration_' + @CS

-------------------------------------------------------------------------------------------------------------------------------------------------------------
--DECLARE @FM DATETIME = N'2023-07-11T03:00:00' -- Replace with your datetime value
DECLARE @FromStart NVARCHAR(19) =
   CONVERT(NVARCHAR(10), @FM, 105) + ' ' +
   CONVERT(NVARCHAR(8), @FM, 108)

DECLARE @ToEnd NVARCHAR(19) =
   CONVERT(NVARCHAR(10), @TE, 105) + ' ' +
   CONVERT(NVARCHAR(8), @TE, 108)
   --select @formattedDateTime
 set @command  = 
   'powershell.exe -ExecutionPolicy Bypass -File "C:\Excel\ExcelReadingFilterScriptv1.ps1" -SPFromStart "' + @FromStart + '"  -SPToEnd "'+@ToEnd+'" -File '+@FP+' -Register '+@CurrentRegister1+' -System '+@CS+''

-- Execute PowerShell script passing the formatted datetime as a parameter
EXEC xp_cmdshell @command

    PRINT 'Type: ' + @CT
    PRINT 'Register: ' + @CurrentRegister1
    PRINT 'System: ' + @CS
    PRINT 'File: ' + @FP 
    PRINT 'FromStart : ' + @FromStart
    PRINT 'ToEnd : ' + @ToEnd
print (@command)

end
```

---


## dbo.Logsheet_Generation_Check

**Schema:** dbo  
**Procedure Name:** Logsheet_Generation_Check  
**Created On:** 2022-12-27 15:42:52  
**Modified On:** 2023-01-28 12:19:16  
**Parameter Count:** 0  

### Parameters

_No parameters_

### EXEC Template

```sql
EXEC [dbo].[Logsheet_Generation_Check];
```

### Full Definition

```sql
CREATE procedure [dbo].[Logsheet_Generation_Check]      
as begin      
      
drop table if exists #Logsheet_Status      
      
create table #Logsheet_Status      
(      
LogsheetCount int,     
LogsheetMasterCount int,    
LogsheetName varchar(2000),    
SystemName varchar(100)      
)      
       
SET NOCOUNT ON;      
      
declare @database varchar(100)      
declare @name varchar(100)      
      
DECLARE Datadatabase CURSOR for       
select DataDatabase,coalesce(displayname,name) as Name from XStudio_Configuration.dbo.XStudio_System_Mst_Tbl where IsDeleted=0 and IsSystem=0 and name not in ('SERPL','ERPL','SRPL','WRPL','NRPL','PLHO','Helpdesk')      
order by name--change database as require config or data data      
                                                                                                             
OPEN Datadatabase       
FETCH NEXT FROM Datadatabase into @database,@name      
while @@FETCH_STATUS = 0      
begin      
print @database    
       
 declare @query nvarchar(max) = '      
 insert into #Logsheet_Status      
 select isnull(count(1),0),    
 (select isnull(count(1),0) from '+@database+'.dbo.Logsheet_Master with (nolock) where IsDeleted=0 and controlroomID is not null),    
 (select string_Agg(Name,'','') from '+@database+'.dbo.Logsheet_Master with (nolock) where IsDeleted=0 and controlroomID is not null and id not in (select LogSheetMasterID from '+@database+'.dbo.Logsheets with (nolock)     
                                     where rotainsID1 in (select id from ['+@database+'].[dbo].[FN_Get_Current_Rota]()) and isdeleted=0)),     
 '''+@name+'''    
 from '+@database+'.dbo.Logsheets where rotainsID1 in (select id from ['+@database+'].[dbo].[FN_Get_Current_Rota]()) and isdeleted=0'   
   
 --print @query  
      
 exec (@query)      
      
 FETCH NEXT FROM Datadatabase INTO @database,@name        
      
end      
CLOSE Datadatabase       
DEALLOCATE Datadatabase      
      
select LogsheetCount,LogsheetMasterCount,SystemName,LogsheetName from #Logsheet_Status where LogsheetCount != LogsheetMasterCount    
      
drop table if exists #Logsheet_Status      
end
```

---


## dbo.sp_assignhod

**Schema:** dbo  
**Procedure Name:** sp_assignhod  
**Created On:** 2022-08-12 11:36:36  
**Modified On:** 2022-09-22 16:21:07  
**Parameter Count:** 1  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @RECORDID | varchar(36) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[sp_assignhod]
    @RECORDID = '';
```

### Full Definition

```sql
CREATE   procedure [dbo].[sp_assignhod]            
(            
 @RECORDID VARCHAR(36)      
)            
as            
begin            
            
   update Complaint_Mst_Tbl set AssignedUserID = (select UserID from Support_Executive_Mst_Tbl where Area in (select AreaID from Complaint_Mst_Tbl where id =@RECORDID and IsDeleted=0)and IsDeleted=0),
   ModifiedOn= getdate(),
   [Source]= 'T-SQL' where id = @RECORDID  and IsDeleted=0  
  
exec SP_Create_TicketNo @RECORDID  
           
end
```

---


## dbo.sp_assignsupportexecutive

**Schema:** dbo  
**Procedure Name:** sp_assignsupportexecutive  
**Created On:** 2022-08-12 11:30:28  
**Modified On:** 2022-09-22 16:21:07  
**Parameter Count:** 2  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @id | varchar(36) | NO |  |
| @userid | varchar(36) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[sp_assignsupportexecutive]
    @id = '',
    @userid = '';
```

### Full Definition

```sql
CREATE   procedure [dbo].[sp_assignsupportexecutive]          
(          
 @id varchar(36),  
 @userid varchar(36)  
)          
as          
begin          
          
   update Complaint_Mst_Tbl set AssignedUserID = @userid,ModifiedOn= getdate(),[Source]= 'T-SQL' where id = @id  and IsDeleted=0
         
end
```

---


## dbo.SP_Create_TicketNo

**Schema:** dbo  
**Procedure Name:** SP_Create_TicketNo  
**Created On:** 2022-08-12 12:07:52  
**Modified On:** 2025-08-07 11:26:37  
**Parameter Count:** 3  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @Id | varchar(36) | NO |  |
| @Entity | varchar(100) | NO |  |
| @ticketcolumn | varchar(100) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[SP_Create_TicketNo]
    @Id = '',
    @Entity = '',
    @ticketcolumn = '';
```

### Full Definition

```sql
CREATE Procedure [dbo].[SP_Create_TicketNo] --'9163DC48-C618-445B-98B3-5E3C93108975','Samplerecords','ticketno'  
(   
@Id varchar(36),  
@Entity varchar(100)= 'Complaint_Mst_Tbl',  
@ticketcolumn varchar(100)= 'TicketNo' 
)  
as  
BEGIN  
DECLARE @Str Nvarchar(MAX),@sr int  
SET @Str='select @sr=Isnull(count(*),0) FRom '+@Entity+'  where id=@Id and '+ @ticketcolumn + ' is null and isdeleted=0'  
EXECUTE SP_EXECUTESQL @str,N'@Id varchar(36),@sr int Output',@ID=@ID,@sr=@sr output  
IF(@SR<>0)  
BEGIN  
  set @Str= 'update TicketScheme_Mst_Tbl set Srno = isnull(srno,0)+1,[Source] = ''T-SQL'''  
  
  EXECUTE SP_EXECUTESQL @str  
  set @Str='update '+@Entity+' set '+@ticketcolumn+'= (select concat(Name,''_'',srno) FROM TicketScheme_Mst_Tbl where isdeleted=0),[Source]= ''T-SQL'' where id=@Id and '+ @ticketcolumn + ' is null'  

  EXECUTE SP_EXECUTESQL @str,N'@Entity varchar(100),@Id varchar(36)',@Entity=@Entity,@Id=@Id  
END  
END
```

---


## dbo.sp_handoverDetails

**Schema:** dbo  
**Procedure Name:** sp_handoverDetails  
**Created On:** 2023-02-24 16:54:09  
**Modified On:** 2023-02-24 16:54:09  
**Parameter Count:** 4  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @SYSTEMID | varchar(36) | NO |  |
| @USERID | varchar(36) | NO |  |
| @RECORDID | varchar(36) | NO |  |
| @STATUS | varchar(50) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[sp_handoverDetails]
    @SYSTEMID = '',
    @USERID = '',
    @RECORDID = '',
    @STATUS = '';
```

### Full Definition

```sql
Create   procedure Dbo.sp_handoverDetails  
(  
 @SYSTEMID VARCHAR(36) = NULL,    
 @USERID VARCHAR(36) = NULL,    
 @RECORDID VARCHAR(36) = NULL,    
 @STATUS VARCHAR(50) = NULL    
)  
as  
begin  
   
 begin transaction  
  
  begin try  
  
   if @STATUS = 'Shift Handedover'  
   begin  
      
    update hotointers set HandoverTime = getdate() ,ModifiedOn = GETDATE() ,ModifiedBy = @USERID where id = @USERID  
  
   end  
  
   else  
   begin  
    if exists (select * from hotointers where id = @RECORDID and IsHandover = 1)  
    begin  
     if exists (select 1 from HandoverDetails where ParentID = @RECORDID)  
     begin  
      update NHD set NHD.Details = OHD.Details ,  
            NHD.ModifiedOn = getdate() ,  
            NHD.[Source] = 'T-SQL' ,  
            NHD.ModifiedBy = @USERID  
      from HandoverDetails as NHD  
      join HandoverDetails as OHD  
      on NHD.[Description] = OHD.[Description]  
      and NHD.ParentID = @RECORDID  
      and OHD.ParentID in (select HandOverDetails from hotointers where id = @RECORDID)  
     end  
     else   
     begin  
      insert into HandoverDetails(ID,ParentID,Details,[Description],[Source],CreatedBy)  
      select newid(),@RECORDID,Details,[Description],'T-SQL',@USERID   
      from HandoverDetails where ParentID in (select HandOverDetails from hotointers where id = @RECORDID)  
      union all  
      select newid(),@RECORDID,null,ID,'T-SQL',@USERID   
      from HandoverDetailMaster   
      where IsDeleted=0 and ((len(@RECORDID)>0 and 0=0) or (len(@RECORDID)=0 and 1=0))  
     end  
  
    end  
  
   end  
  
   commit  
  
  end try  
  
 begin catch  
  
  rollback transaction  
  
 end catch  
  
end
```

---


## dbo.Sp_Logsheet_Calculation_Adhoc

**Schema:** dbo  
**Procedure Name:** Sp_Logsheet_Calculation_Adhoc  
**Created On:** 2023-07-19 16:10:42  
**Modified On:** 2023-07-19 16:54:17  
**Parameter Count:** 3  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @ID | varchar(36) | NO |  |
| @Entity | varchar(2000) | NO |  |
| @SystemID | varchar(36) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[Sp_Logsheet_Calculation_Adhoc]
    @ID = '',
    @Entity = '',
    @SystemID = '';
```

### Full Definition

```sql
Create   Procedure [dbo].[Sp_Logsheet_Calculation_Adhoc]
(
	@ID varchar(36),
	@Entity varchar(2000),
	@SystemID varchar(36) = null
)
as
begin

	--set nocount on;

	declare @query nvarchar(max)
	declare @datadatabase varchar(200)

	declare @flowrateaspernrc1 DECIMAL(18,4),
	        @flowrateaspernrc2 DECIMAL(18,4),
			@offsetnrc DECIMAL(18,4),
			@flowrateaspertank1 DECIMAL(18,4),
			@flowrateaspertank2 DECIMAL(18,4),
			@flowrateaspertank3 DECIMAL(18,4),
			@offsettank DECIMAL(18,4),
			@cumulativeflowrateaspertank DECIMAL(18,4),
			@flownrcminustank DECIMAL(18,4),
			@Cummulativedeliveryaspernrc DECIMAL(18,4),
			@CummulativedeliveryasperBatch DECIMAL(18,4),
			@CummulativedeliveryasperTank1 DECIMAL(18,4),
			@CummulativedeliveryasperTank2 DECIMAL(18,4),
			@CummulativedeliveryasperTank3 DECIMAL(18,4),
			@flowrateasper1 DECIMAL(18,4),
			@flowrateasper2 DECIMAL(18,4),
			@flowrateasper3 DECIMAL(18,4),
			@flowrateasper4 DECIMAL(18,4)

	if @SystemID is not null
	begin
		select @datadatabase = DataDatabase
		from XStudio_Configuration.dbo.XStudio_System_Mst_Tbl
		where IsDeleted = 0 and ID = @SystemID
	end
	else
	begin
		select @datadatabase = DataDatabase
		from XStudio_Configuration.dbo.XStudio_System_Mst_Tbl
		where IsDeleted = 0 and DataDatabase = db_name()
	end

	set @query = N'

	select @flowrateaspernrc1 = B ,
		   @flowrateaspernrc2 = D ,
		   @offsetnrc = E,
		   @flowrateaspertank1 = Q1 ,
		   @flowrateaspertank2 = Q2 ,
		   @flowrateaspertank3 = Q3 ,
		   @offsettank = QQ ,
		   @flowrateasper1 = E1 ,
		   @flowrateasper2 = E2,
		   @flowrateasper3 = E3,
		   @flowrateasper4 = E4,
		   @Cummulativedeliveryaspernrc = F,
		   @CummulativedeliveryasperBatch = G,
		   @CummulativedeliveryasperTank1 = H,
		   @CummulativedeliveryasperTank2 = I,
		   @CummulativedeliveryasperTank3 = J
		   from (
	select ID,
		   EntryDateTime,
		   isnull(NRCReading1,0) - isnull(LAG(NRCReading1,1,0) over (order by EntryDateTime),0) B,
		   isnull(NRCReading2,0) - isnull(LAG(NRCReading2,1,0) over (order by EntryDateTime),0) D,
		   isnull(OffsetNRCKL,0) E,
		   isnull(Quantity1KL,0) - isnull(LAG(Quantity1KL,1,0) over (order by EntryDateTime),0) Q1,
		   isnull(Quantity2KL,0) - isnull(LAG(Quantity2KL,1,0) over (order by EntryDateTime),0) Q2,
		   isnull(Quantity3KL,0) - isnull(LAG(Quantity3KL,1,0) over (order by EntryDateTime),0) Q3,
		   isnull(OffsetTankKL,0) QQ,
		   isnull(NRCReading3,0) - isnull(LAG(NRCReading3,1,0) over (order by EntryDateTime),0) E1,
		   isnull(InletNRCReading1,0) - isnull(LAG(InletNRCReading1,1,0) over (order by EntryDateTime),0) E2,
		   isnull(NRCReading4,0) - isnull(LAG(NRCReading4,1,0) over (order by EntryDateTime),0) E3,
		   isnull(InletNRCReading2,0) - isnull(LAG(InletNRCReading2,1,0) over (order by EntryDateTime),0) E4,
		   isnull(LAG(CumulativeDeliveryPumpingasperNRCKL,1,0) over (order by EntryDateTime),0) as F,
		   isnull(LAG(BatchwiseCumulativeDeliveryPumpingKL,1,0) over (order by EntryDateTime),0) as G,
		   isnull(LAG(Tank1wiseCumulativeDeliveryPumpingKL,1,0) over (order by EntryDateTime),0) as H,
		   isnull(LAG(Tank2wiseCumulativeDeliveryPumpingKL,1,0) over (order by EntryDateTime),0) as I,
		   isnull(LAG(Tank3wiseCumulativeDeliveryPumpingKL,1,0) over (order by EntryDateTime),0) as J
	from '+@datadatabase+'.dbo.'+@Entity+') as t
	where id = @ID'

	--print(@Query)

	EXEC sp_executesql @Query,N'@ID varchar(36),@flowrateaspernrc1 DECIMAL(18,4) OUTPUT,@flowrateaspernrc2 DECIMAL(18,4) OUTPUT,@offsetnrc DECIMAL(18,4) OUTPUT,@flowrateaspertank1 DECIMAL(18,4) OUTPUT,@flowrateaspertank2 DECIMAL(18,4) OUTPUT,@flowrateaspertank3 DECIMAL(18,4) OUTPUT,@offsettank DECIMAL(18,4) OUTPUT,@cumulativeflowrateaspertank DECIMAL(18,4) OUTPUT,@flownrcminustank DECIMAL(18,4) OUTPUT,@Cummulativedeliveryaspernrc DECIMAL(18,4) OUTPUT,@CummulativedeliveryasperBatch DECIMAL(18,4) OUTPUT,@CummulativedeliveryasperTank1 DECIMAL(18,4) OUTPUT,@CummulativedeliveryasperTank2 DECIMAL(18,4) OUTPUT,@CummulativedeliveryasperTank3 DECIMAL(18,4) OUTPUT,@flowrateasper1 DECIMAL(18,4) OUTPUT,@flowrateasper2 DECIMAL(18,4) OUTPUT,@flowrateasper3 DECIMAL(18,4) OUTPUT,@flowrateasper4 DECIMAL(18,4) OUTPUT',
	@ID=@ID,@flowrateaspernrc1 = @flowrateaspernrc1 OUTPUT ,@flowrateaspernrc2 = @flowrateaspernrc2 OUTPUT ,@offsetnrc = @offsetnrc OUTPUT ,@flowrateaspertank1 = @flowrateaspertank1 OUTPUT ,@flowrateaspertank2 = @flowrateaspertank2 OUTPUT ,@flowrateaspertank3 = @flowrateaspertank3 OUTPUT ,@offsettank = @offsettank OUTPUT ,@cumulativeflowrateaspertank = @cumulativeflowrateaspertank OUTPUT ,@flownrcminustank = @flownrcminustank OUTPUT ,@Cummulativedeliveryaspernrc = @Cummulativedeliveryaspernrc OUTPUT ,@CummulativedeliveryasperBatch = @CummulativedeliveryasperBatch OUTPUT ,@CummulativedeliveryasperTank1 = @CummulativedeliveryasperTank1 OUTPUT ,@CummulativedeliveryasperTank2 = @CummulativedeliveryasperTank2 OUTPUT ,@CummulativedeliveryasperTank3 = @CummulativedeliveryasperTank3 OUTPUT ,@flowrateasper1 = @flowrateasper1 OUTPUT ,@flowrateasper2 = @flowrateasper2 OUTPUT ,@flowrateasper3 = @flowrateasper3 OUTPUT ,@flowrateasper4 = @flowrateasper4 OUTPUT

	SET @query = '


	update '+@datadatabase+'.dbo.'+@Entity+' 
	set [FlowRateasperNRC1KLperhr] = iif(@flowrateaspernrc1<0,0,@flowrateaspernrc1),
		[FlowRateasperNRC2KLperhr] = iif(@flowrateaspernrc2<0,0,@flowrateaspernrc2),
		[CumulativeFlowasperNRCKL] = iif(@flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc<0,0,@flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc),
		[FlowRateasperTank1KLperhr] = iif(@flowrateaspertank1<0,0,@flowrateaspertank1),
		[FlowRateasperTank2KLperhr] = iif(@flowrateaspertank2<0,0,@flowrateaspertank2),
		[FlowRateasperTank3KLperhr] = iif(@flowrateaspertank3<0,0,@flowrateaspertank3),
		[CumulativeFlowasperTankKL] = iif(@flowrateaspertank1 + @flowrateaspertank2 + @flowrateaspertank3 + @offsettank<0,0,@flowrateaspertank1 + @flowrateaspertank2 + @flowrateaspertank3 + @offsettank),
		[FlowNRCTankdeltaKLperhr] = iif(@flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc - @flowrateaspertank1 - @flowrateaspertank2 - @flowrateaspertank3 - @offsettank<0,0,@flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc - @flowrateaspertank1 - @flowrateaspertank2 - @flowrateaspertank3 - @offsettank),
		[CumulativeDeliveryPumpingasperNRCKL] = iif(case when isnull(CumulativeDeliveryPumpingasperNRCKL,0) = 0 then 0 
												     else @Cummulativedeliveryaspernrc + @flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc end<0,0,case when isnull(CumulativeDeliveryPumpingasperNRCKL,0) = 0 then 0 
												     else @Cummulativedeliveryaspernrc + @flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc end),
		[BatchwiseCumulativeDeliveryPumpingKL] = iif(case when isnull(BatchwiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperBatch + @flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc end<0,0,case when isnull(BatchwiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperBatch + @flowrateaspernrc1 + @flowrateaspernrc2 + @offsetnrc end),
		[Tank1wiseCumulativeDeliveryPumpingKL] = iif(case when isnull(Tank1wiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperTank1 + @flowrateaspertank1 end<0,0,case when isnull(Tank1wiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperTank1 + @flowrateaspertank1 end),
		[Tank2wiseCumulativeDeliveryPumpingKL] = iif(case when isnull(Tank2wiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperTank2 + @flowrateaspertank2 end<0,0,case when isnull(Tank2wiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperTank2 + @flowrateaspertank2 end),
		[Tank3wiseCumulativeDeliveryPumpingKL] = iif(case when isnull(Tank3wiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperTank3 + @flowrateaspertank3 end<0,0,case when isnull(Tank3wiseCumulativeDeliveryPumpingKL,0) = 0 then 0 
													  else @CummulativedeliveryasperTank3 + @flowrateaspertank3 end),
		[FlowRate1KLperhr] = iif(@flowrateasper1<0,0,@flowrateasper1),
		[FlowRate2KLperhr] = iif(@flowrateasper2 - @flowrateaspernrc1 - @flowrateaspernrc2 - @offsetnrc<0,0,@flowrateasper2 - @flowrateaspernrc1 - @flowrateaspernrc2 - @offsetnrc),
		[FlowRate3KLperhr] = iif(@flowrateasper3<0,0,@flowrateasper3),
		[FlowRate4KLperhr] = iif(@flowrateasper4 - @flowrateasper2<0,0,@flowrateasper4 - @flowrateasper2),
		[Source] = ''T-SQL'',
		[ModifiedOn] = getdate() where ID = @ID'

	exec sp_executesql @Query,N'@ID varchar(36),@flowrateaspernrc1 DECIMAL(18,4),@flowrateaspernrc2 DECIMAL(18,4),@offsetnrc DECIMAL(18,4),@flowrateaspertank1 DECIMAL(18,4),@flowrateaspertank2 DECIMAL(18,4),@flowrateaspertank3 DECIMAL(18,4),@offsettank DECIMAL(18,4),@cumulativeflowrateaspertank DECIMAL(18,4),@flownrcminustank DECIMAL(18,4),@Cummulativedeliveryaspernrc DECIMAL(18,4),@CummulativedeliveryasperBatch DECIMAL(18,4),@CummulativedeliveryasperTank1 DECIMAL(18,4),@CummulativedeliveryasperTank2 DECIMAL(18,4),@CummulativedeliveryasperTank3 DECIMAL(18,4),@flowrateasper1 DECIMAL(18,4),@flowrateasper2 DECIMAL(18,4),@flowrateasper3 DECIMAL(18,4),@flowrateasper4 DECIMAL(18,4)',
	@ID=@ID,@flowrateaspernrc1 = @flowrateaspernrc1 ,@flowrateaspernrc2 = @flowrateaspernrc2 ,@offsetnrc = @offsetnrc ,@flowrateaspertank1 = @flowrateaspertank1 ,@flowrateaspertank2 = @flowrateaspertank2 ,@flowrateaspertank3 = @flowrateaspertank3 ,@offsettank = @offsettank ,@cumulativeflowrateaspertank = @cumulativeflowrateaspertank ,@flownrcminustank = @flownrcminustank ,@Cummulativedeliveryaspernrc = @Cummulativedeliveryaspernrc ,@CummulativedeliveryasperBatch = @CummulativedeliveryasperBatch ,@CummulativedeliveryasperTank1 = @CummulativedeliveryasperTank1 ,@CummulativedeliveryasperTank2 = @CummulativedeliveryasperTank2 ,@CummulativedeliveryasperTank3 = @CummulativedeliveryasperTank3 ,@flowrateasper1 = @flowrateasper1 ,@flowrateasper2 = @flowrateasper2 ,@flowrateasper3 = @flowrateasper3 ,@flowrateasper4 = @flowrateasper4 


end
```

---


## dbo.Sp_Logsheet_Calculation_Adhoc_By_Date

**Schema:** dbo  
**Procedure Name:** Sp_Logsheet_Calculation_Adhoc_By_Date  
**Created On:** 2023-07-19 16:53:16  
**Modified On:** 2023-07-19 16:53:16  
**Parameter Count:** 1  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @Date | date | NO |  |

### EXEC Template

```sql
EXEC [dbo].[Sp_Logsheet_Calculation_Adhoc_By_Date]
    @Date = '2026-05-04';
```

### Full Definition

```sql
Create   Procedure [dbo].[Sp_Logsheet_Calculation_Adhoc_By_Date]
(
	@Date date = null
)
as
begin
	
	set nocount on;

	set @Date = isnull(nullif(@date,''),cast(getdate() as date))

	begin try

		begin transaction

		declare @pipeline varchar(200)
		declare @EntityName varchar(200)
		declare @query nvarchar(max)

		DECLARE PipelineName Cursor LOCAL  FAST_FORWARD for   
		select pipeline,Entity from XStudio_List_Logsheet_Calculation_Mapping_Vw
		open PipelineName    
    
		FEtch next from PipelineName into @pipeline,@EntityName 
    
		While @@FETCH_STATUS=0    
		BEGIN  

			set @query = N'

			declare @ID varchar(36)
			declare @EntityName varchar(200)

			DECLARE LogsheetID Cursor LOCAL  FAST_FORWARD for    
			SELECT ID,EntityID
			from '+@EntityName+' with (Nolock)    
			where dbo.[FN_GET_ReportDate](EntryDateTime) = @date          

			open LogsheetID    
    
			FEtch next from LogsheetID into @ID,@EntityName
    
			While @@FETCH_STATUS=0    
			BEGIN  
			
				exec Sp_Logsheet_Calculation_Adhoc @ID,@EntityName

				FEtch next from LogsheetID into @ID,@EntityName		
    
			END    
			close LogsheetID     
			DEAllocate LogsheetID'  

			exec sp_executesql @query,N'@Date date',@Date=@Date

			FEtch next from PipelineName into @pipeline,@EntityName 
    
		END    
		close PipelineName     
		DEAllocate PipelineName  

		commit transaction;

	end try
	
	begin catch

		rollback transaction;

		DECLARE @ERROR_MSG VARCHAR(max) =  'SP : Sp_Logsheet_Calculation_Adhoc_By_Date | Line No : '+ Convert(varchar(1000),ERROR_LINE()) +'| Messge : '+ ERROR_MESSAGE() ;
		RAISERROR(@ERROR_MSG,16,1)		

	end catch

end
```

---


## dbo.UAT_Test_Report_USP

**Schema:** dbo  
**Procedure Name:** UAT_Test_Report_USP  
**Created On:** 2025-08-06 18:06:18  
**Modified On:** 2025-08-22 09:03:52  
**Parameter Count:** 1  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @EntityName | nvarchar(128) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[UAT_Test_Report_USP]
    @EntityName = '';
```

### Full Definition

```sql
CREATE PROCEDURE [dbo].[UAT_Test_Report_USP]
    @EntityName NVARCHAR(128)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        DECLARE @SQL NVARCHAR(MAX);
        DECLARE @HasQ4 BIT = 0;
        DECLARE @HasQ4Verdict BIT = 0;

        -- Check for optional columns
        SELECT 
            @HasQ4 = CASE WHEN EXISTS (
                SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = @EntityName AND COLUMN_NAME = 'Q4'
            ) THEN 1 ELSE 0 END,
            
            @HasQ4Verdict = CASE WHEN EXISTS (
                SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = @EntityName AND COLUMN_NAME = 'Q4Verdict'
            ) THEN 1 ELSE 0 END;

        -- Dynamic insert SQL
        SET @SQL = '
        INSERT INTO dbo.UAT_Test_Report_Data
        (
            AreaName,
            TestName,
            CreatedOn,
            ModifiedOn,
            TestingStartDatetime,
            TestingEndDatetime,
            TesterName,
            Q1Verdict,
            Q2Verdict,
            Q3Verdict,
            OverallVerdict,
            Q4Verdict,
            Remarks,
            EntityName
        )
        SELECT 
            TEST.AreaName,
            TEST.Name,
            UAT.CreatedOn,
            UAT.ModifiedOn,
            UAT.CreatedOn,
            Getdate(),
            CONCAT(USR.FirstName, '' '', USR.LastName),
            IIF(Q1Verdict = 1, ''Yes'', ''No''),
            IIF(Q2Verdict = 1, ''Yes'', ''No''),
            IIF(Q3Verdict = 1, ''Yes'', ''No''),
            IIF(OVERALLVerdict = 1, ''Pass'', ''Fail''),' + CHAR(10) +

            CASE 
                WHEN @HasQ4 = 1 AND @HasQ4Verdict = 1 
                THEN 'IIF(Q4Verdict = 1, ''Yes'', ''No'')'
                ELSE 'NULL'
            END + ' AS Q4Verdict,' + CHAR(10) +

            'CONCAT(
                ''Q1 Remarks : '', Q1,
                '' Q2 Remarks : '', Q2,
                '' Q3 Remarks : '', Q3,' +
                CASE 
                    WHEN @HasQ4 = 1 
                    THEN ' '' Q4 Remarks : '', Q4,'
                    ELSE ''
                END +
                ' '' Comment if any : '', Comments
            ) AS Remarks,' + CHAR(10) +

            '''' + @EntityName + ''' AS EntityName
        FROM ' + QUOTENAME(@EntityName) + ' AS UAT
        JOIN UAT_Test_Mst_Tbl AS TEST ON TEST.ID = UAT.TestName AND TEST.IsDeleted = 0
        JOIN XStudio_Configuration..XStudio_User_Mst_Tbl AS USR ON USR.ID = UAT.TesterName AND USR.IsDeleted = 0
        WHERE UAT.IsDeleted = 0;';

        EXEC sp_executesql @SQL;
    END TRY

    BEGIN CATCH
        DECLARE @ERROR_MSG VARCHAR(MAX) = 
            'SP : UAT_Test_Report_USP | Line No : ' + 
            CONVERT(VARCHAR(1000), ERROR_LINE()) + ' | Message : ' + ERROR_MESSAGE();
        DECLARE @ERROR_LINE VARCHAR(MAX) = CONVERT(VARCHAR(1000), ERROR_LINE());

        EXEC [XStudio_Configuration].[dbo].[XStudio_Add_ErrorLog_USP]
            @Type = 'SQL-Error',
            @Action = '[dbo].[UAT_Test_Report_USP]',
            @Message = @ERROR_MSG,
            @StackTrace = @ERROR_LINE,
            @UserID = '',
            @HostAddress = '',
            @Info = '',
            @Source = 'T-SQL';

        RAISERROR(@ERROR_MSG, 16, 1);
    END CATCH
END
```

---


## dbo.UAT_Tracking_Transaction_DataInsert_USP

**Schema:** dbo  
**Procedure Name:** UAT_Tracking_Transaction_DataInsert_USP  
**Created On:** 2025-08-07 16:09:24  
**Modified On:** 2025-08-22 09:53:08  
**Parameter Count:** 0  

### Parameters

_No parameters_

### EXEC Template

```sql
EXEC [dbo].[UAT_Tracking_Transaction_DataInsert_USP];
```

### Full Definition

```sql
-- =============================================
-- Author:		<Author,Mahesh Udar>
-- Create date: <Create Date,2025-08-07>
-- Description:	<Description,for insert into UAT_Tracking_Transaction table>
-- =============================================
CREATE PROCEDURE [dbo].[UAT_Tracking_Transaction_DataInsert_USP]
	-- Add the parameters for the stored procedure here
AS	
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

		Insert into XStudio_Helpdesk..UAT_Tracking_Transaction (EntryDateTime,LastTestConducted,TotalUATsTested,TotalUserConductedTest,TotalUATPassRate,TotalUATFailRate,UATDuration) 
		SELECT getdate() as EntryDateTime,format(MostRecentTestTime,'yyyy-MM-dd HH:mm:ss') as LastTestConducted,DistinctTestNames as TotalUATsTested,DistinctTesterNames as TotalUserConductedTest,CAST((PassRate/DistinctTestNames)*100 as Decimal(18,2)) as TotalUATPassRate,CAST((FailRate/DistinctTestNames)*100 as Decimal(18,2)) as TotalUATFailRate,null as UATDuration from (
		SELECT COUNT(DISTINCT TestName)     AS DistinctTestNames, COUNT(DISTINCT TesterName)   AS DistinctTesterNames, CAST(SUM(case when OverallVerdict='Pass' and rn=1 then 1 else 0 end)as Decimal(18,2)) as PassRate, CAST(SUM(case when OverallVerdict='Fail' and rn=1 then 1 else 0 end)as Decimal(18,2)) as FailRate, MAX(TestingStartDatetime) AS MostRecentTestTime
		FROM (SELECT DISTINCT TestName,TesterName,TestingStartDatetime, OverallVerdict, ROW_NUMBER() OVER (PARTITION BY TestName ORDER BY TestingStartDatetime DESC) AS rn FROM XStudio_Helpdesk..UAT_Test_Report_Data) as t) as UATDATA

END
```

---


## dbo.UAT_U_Enddatetime_Ticket_Generate_USP

**Schema:** dbo  
**Procedure Name:** UAT_U_Enddatetime_Ticket_Generate_USP  
**Created On:** 2025-08-05 18:34:56  
**Modified On:** 2025-08-07 16:09:47  
**Parameter Count:** 2  

### Parameters

| Parameter | Data Type | Output | Default Value |
| --- | --- | --- | --- |
| @ID | varchar(36) | NO |  |
| @Entity | varchar(100) | NO |  |

### EXEC Template

```sql
EXEC [dbo].[UAT_U_Enddatetime_Ticket_Generate_USP]
    @ID = '',
    @Entity = '';
```

### Full Definition

```sql
-- =============================================
-- Author:		Sagar Rana
-- Create date: 05-08-2025
-- Description:	Sp to update enddatetime on save
-- =============================================
CREATE PROCEDURE [dbo].[UAT_U_Enddatetime_Ticket_Generate_USP] 
    @ID VARCHAR(36),
    @Entity VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE 
        @sql NVARCHAR(MAX),
        @params NVARCHAR(MAX),
        @OverallVerdict BIT,
        @recordid UNIQUEIDENTIFIER = NEWID();

    -- Step 1: Update EndDateTime
    SET @sql = '
        UPDATE ' + QUOTENAME(@Entity) + '
        SET EndDateTime = GETDATE()
        WHERE ID = @ID';

    SET @params = N'@ID VARCHAR(36)';
    EXEC sp_executesql @sql, @params, @ID = @ID;

	   EXEC [dbo].[UAT_Test_Report_USP] @Entity;

	   EXEC [dbo].[UAT_Tracking_Transaction_DataInsert_USP];

    -- Step 2: Get OverallVerdict
    SET @sql = '
        SELECT @OV = OverallVerdict
        FROM ' + QUOTENAME(@Entity) + '
        WHERE ID = @ID';

    SET @params = N'@ID VARCHAR(36), @OV BIT OUTPUT';
    EXEC sp_executesql @sql, @params, @ID = @ID, @OV = @OverallVerdict OUTPUT;

    -- Step 3: If failure, insert complaint
    IF (@OverallVerdict = 0)
    BEGIN
        -- Insert directly without using temp table
        SET @sql = '
        INSERT INTO [XStudio_Helpdesk].[dbo].[Complaint_Mst_Tbl]
            ([ID], [ContactNo], [EmailID], [AreaID], [Attachment], [Status],
             [ComplaintTypeID], [messages], [BriefDetails], 
             [Priority], [subareadetails], [AskStatus], [Description], [FirstLastName],
             [CreatedBy], [HostAddress], [ModifiedBy], [ModifiedOn], [Source])
        SELECT 
            @recordid,
            ISNULL(b.ContactNo, ''1234567891''),
            ISNULL(b.EmailID, ''admin@ssm.com''),
            tm.AreaName,
            a.fileupload,
            ''Enter'',
            ''910C8925-5F72-41D5-AB8C-9FAF6C864DC3'',
            ''Enter'',
            CONCAT(''[UAT Failure] '', tm.AreaName, '': '', tm.Name),
            ''EEF8F1D9-180E-49E4-95C3-3F5CB0408028'',
            tm.Name,
            ''Enter'',
            CONCAT(
                    ''Q1 Remarks : '', Q1,
                    '' Q2 Remarks : '', Q2,
                    '' Q3 Remarks : '', Q3,
                '' Comment if any : '', Comments
                ) AS [Comments],
            CONCAT(b.FirstName, '' '', b.LastName),
            b.ID,
            ''10.2.6.163'',
            b.ID,
            GETDATE(),
            ''System''
        FROM ' + QUOTENAME(@Entity) + ' a
        JOIN [XStudio_Helpdesk].[dbo].[UAT_Test_Mst_Tbl] tm ON tm.ID = a.TestName
        LEFT JOIN XStudio_Configuration..XStudio_User_Mst_Tbl b ON a.TesterName = b.ID
        WHERE a.ID = @ID';

        SET @params = N'@ID VARCHAR(36), @recordid UNIQUEIDENTIFIER';
        EXEC sp_executesql @sql, @params, @ID = @ID, @recordid = @recordid;

        -- Step 4: Assign HOD
        EXEC [dbo].[sp_assignhod] @recordid;
    END
END
```

---
