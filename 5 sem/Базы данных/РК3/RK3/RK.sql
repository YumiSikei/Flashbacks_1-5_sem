CREATE DATABASE TEST_RK
GO

USE TEST_RK
GO

CREATE SCHEMA RK
GO

CREATE TABLE RK.Bus (
ID int, 
BType nchar(20),
Mark nchar(20),
Num nchar(20), 
BusDriver nchar(20)
);
GO

CREATE TABLE RK.Way (
   ID int,
   Num int,
   Bus int
);
GO


INSERT INTO RK.Bus (ID, BType, Mark, Num, BusDriver) VALUES (1, 'city', 'A1', 'B304', 'Mr Driver1')
INSERT INTO RK.Bus (ID, BType, Mark, Num, BusDriver) VALUES (2, 'city', 'A3', 'B301', 'Mr Driver2')
INSERT INTO RK.Bus (ID, BType, Mark, Num, BusDriver) VALUES (3, 'subcity', 'A1', 'B304', 'Mr Driver3')
INSERT INTO RK.Bus (ID, BType, Mark, Num, BusDriver) VALUES (4, 'city', 'A2', 'A304', 'Mr Driver4')
INSERT INTO RK.Bus (ID, BType, Mark, Num, BusDriver) VALUES (5, 'city', 'A1', 'B4', 'Mr Driver5')

INSERT INTO  RK.Way (ID, Num, Bus) VALUES(1, 157, 1)
INSERT INTO RK.Way (ID, Num, Bus) VALUES(2, 151, 1)
INSERT INTO RK.Way (ID, Num, Bus) VALUES(1, 157, 2)
INSERT INTO RK.Way (ID, Num, Bus) VALUES(1, 157, 3)
INSERT INTO RK.Way (ID, Num, Bus) VALUES(3, 127, 1)


SELECT BusDriver FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus WHERE RK.Way.Num = 157

SELECT RK.Way.Num FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus WHERE (SELECT Count(*) FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus) >= 10

SELECT TOP(3) Mark  FROM RK.Bus JOIN RK.WAY ON RK.Bus.ID = RK.WAY.Bus WHERE RK.Way.Num = 157

