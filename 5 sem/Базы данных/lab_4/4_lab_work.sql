-- первое задание
IF EXISTS (SELECT name FROM sysobjects WHERE name = 'max_rating')  
   DROP FUNCTION max_rating;  
go  

CREATE FUNCTION max_rating() RETURNS float   
AS EXTERNAL NAME Lab04.first.max_rating;   
GO  

SELECT dbo.max_rating();  
GO  

-- второе задание
IF EXISTS (SELECT name FROM sysobjects WHERE name = 'getPopularStatus')  
   DROP AGGREGATE getPopularStatus;  
go  

CREATE AGGREGATE getPopularStatus (@Rating float, @status nvarchar(50)) RETURNS nvarchar(50)  
AS EXTERNAL NAME Lab04.second.getPopularStatus;  
go  

select dbo.getPopularStatus(Rating, status) as 'Most popular' from Publication;
go

select status, count(status)  from Publication Group by status

-- третье задание
IF EXISTS (SELECT name FROM sysobjects WHERE name = 'getInfo')  
   DROP FUNCTION getInfo;  
go  

CREATE FUNCTION getInfo(@type int)   
RETURNS TABLE (  
   Name nvarchar(85),  
   Description nvarchar(1300),
   Count_of_sales int
)  
AS EXTERNAL NAME Lab04.third.getInfo
go  

SELECT * FROM getInfo(2);  
go  

-- четвертое задание
drop procedure if exists updatePublishingHouse;
go

create procedure updatePublishingHouse
	@year int,
	@id int
as external name Lab04.fourth.updatePublishingHouse;
go

exec updatePublishingHouse 2018, 10;
go

-- пятое задание
drop trigger if exists UpdatePubH

CREATE TRIGGER UpdatePubH 
ON PublishingHouse
FOR Insert  
AS  
EXTERNAL NAME Lab04.Triggers.fifth 

INSERT INTO PublishingHouse(id, Name, Creation_year, Adress) values
					 (101, 'С новым годом', 2019, 'Москва') 

-- шестое задание
CREATE TYPE Types  
EXTERNAL NAME Lab04.Types
CREATE TABLE dbo.Typity
( 
  id INT IDENTITY(1,1) NOT NULL, 
  tpt Types NULL,
);
GO

INSERT INTO dbo.Typity(tpt) VALUES('2, 6, 1'); 
INSERT INTO dbo.Typity(tpt) VALUES('1,0, 15'); 
INSERT INTO dbo.Typity(tpt) VALUES('2, 1,8');  
GO 

SELECT * FROM dbo.Typity;

SELECT id, tpt.ToString() AS Types 
FROM dbo.Typity;

DECLARE @v dbo.Types
SET @v = CAST('3, 1, 8' AS Types)
SELECT @v.Summ() AS 'summ'
GO
 
DROP TABLE dbo.Typity
GO

DROP TYPE Types
GO

