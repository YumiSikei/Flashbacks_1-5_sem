CREATE DATABASE RK_3
GO
USE RK_3
GO
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Workers')
CREATE TABLE Workers
(
	Id int IDENTITY(1,1) PRIMARY KEY,
	Name nchar(25),
	Birthday date,
	Spec nchar(60),
	Felial_id int
)
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Felials')
CREATE TABLE Felials
(
	Id int IDENTITY(1,1) PRIMARY KEY,
	Company nchar(60),
	Adres nchar(80),
	Telefone int
)
GO


INSERT INTO Felials VALUES ('Московский фелиал (ГО)','Герцена, 5',4567823)
INSERT INTO Felials VALUES ('Новосибирский доп. офис','Пролетарская, 8',54326234)
INSERT INTO Felials VALUES ('Саратовский доп офис','Шухова, 44',4525611)
INSERT INTO Felials VALUES ('Томский фелиал','Герцена, 7',9874674)



INSERT INTO Workers VALUES ('Иванов Иван Иванович','25/09/1990','ИТ',1)
INSERT INTO Workers VALUES ('Петров Петр Петрович','12/11/1987','Бухгалтерия',3)
