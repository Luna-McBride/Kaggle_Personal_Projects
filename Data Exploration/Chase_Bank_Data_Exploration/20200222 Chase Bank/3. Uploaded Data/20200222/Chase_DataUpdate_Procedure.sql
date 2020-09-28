USE [Personal]
GO
/****** Object:  StoredProcedure [dbo].[__tmpl__BLD_WRK__ChaseDeposits]    Script Date: 2/22/2020 1:37:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

alter PROC [dbo].[BLD_WRK_ChaseDeposits]
-- =============================================
-- Author: Luna McBride		
-- Create date: 20200222
-- Description:	RAW -> WRK
-- Mod Date:
-- =============================================


AS
BEGIN
-- =============================================
-- Drop Table
-- =============================================
if object_id('WRK_ChaseDeposits') is not null
drop table [WRK_ChaseDeposits]

-- =============================================
-- Create Table
-- =============================================
create table [WRK_ChaseDeposits](
	[RowNumber]			int identity(1,1)
	,[Institution Name]	varchar(100)
	,[Main Office]		varchar(1)
	,[Branch Name]		varchar(1000)
	,[Branch Number]	varchar(10)
	,[Established Date]	DATE
	,[Acquired Date]	DATE
	,[Street Address]	varchar(1000)
	,[City]				varchar(100)
	,[County]			varchar(100)
	,[State]			varchar(2)
	,[Zipcode]			varchar(5)
	,[Latitude]			float
	,[Longitude]		float
	,[2010 Deposits]	int
	,[2011 Deposits]	int
	,[2012 Deposits]	int
	,[2013 Deposits]	int
	,[2014 Deposits]	int
	,[2015 Deposits]	int
	,[2016 Deposits]	int
)

-- =============================================
-- Truncate Table
-- =============================================
truncate table [WRK_ChaseDeposits]

-- =============================================
-- Insert Into
-- =============================================
insert into [WRK_ChaseDeposits](
	[Institution Name]	
	,[Main Office]		
	,[Branch Name]		
	,[Branch Number]	
	,[Established Date]	
	,[Acquired Date]	
	,[Street Address]	
	,[City]				
	,[County]			
	,[State]			
	,[Zipcode]			
	,[Latitude]			
	,[Longitude]		
	,[2010 Deposits]	
	,[2011 Deposits]	
	,[2012 Deposits]	
	,[2013 Deposits]	
	,[2014 Deposits]	
	,[2015 Deposits]	
	,[2016 Deposits]	
)
select [Institution Name]
      ,[Main Office]
      ,[Branch Name]
      ,[Branch Number]
      ,[Established Date]
      ,[Acquired Date]
      ,[Street Address]
      ,[City]
      ,[County]
      ,[State]
      ,[Zipcode]
      ,[Latitude]
      ,[Longitude]
      ,[2010 Deposits]
      ,[2011 Deposits]
      ,[2012 Deposits]
      ,[2013 Deposits]
      ,[2014 Deposits]
      ,[2015 Deposits]
      ,[2016 Deposits]
from [dbo].[RAW_ChaseDeposits_20200222]
--(5413 rows affected)

-- Get number of rows without an acquired date
select count(*) from RAW_ChaseDeposits_20200222
where [Acquired Date] = ''
-- 1615

-- Update work table to set null acquired date to established date, which is more honest than the default acquired date
update WRK_ChaseDeposits
set [Acquired Date] = [Established Date]
where [Acquired Date]='1900-01-01'
-- (1615 rows affected)
-- 1615=1615. Sanity check cleared

-- Look at rows for acquire date and established date, as another sanity check
select * from WRK_ChaseDeposits
where [Acquired Date] = [Established Date]

-- A quick check into dates established to check for issues.
select * from WRK_ChaseDeposits
where [Established Date]<'1900-01-01'
-- There are several that seem a bit weird, but due to age, it is more likely they just did not include the actual dates
-- when establishing the locations back in the 1800's. However, I cannot really check with JP Morgan/Chase to see.

-- Checks for locations made in the period being checked
select * from WRK_ChaseDeposits
where [Established Date]>'2010-01-01' or [Acquired Date]>'2010-01-01'
-- None looked to have values before they were established, so it looks to be fine

--Checks for valid latitude and longitude
select * from WRK_ChaseDeposits
where [Latitude]=0 or [Longitude]=0
-- There are 70 items with invalid latitude and/or longitude. 
-- These are not important to the metrics being looked at, but I am looking at various factors to explore the data

-- Check for 5 digit American zip code
select * from WRK_ChaseDeposits
where [Zipcode] not like '_____'
-- There are 269 zipcodes with 4 digits. After a bit of exploring, many of these are ones that start with 0 with the 0 dropped

-- Important check for valid state field structure
select * from WRK_ChaseDeposits
where [State] not like '__'
-- No results, thankfully. I wanted to look at state for metrics to analyze the company.

END

/*
	select * from [dbo].[RAW_ChaseDeposits_20200222]
	select * from [dbo].[WRK_ChaseDeposits]
*/
