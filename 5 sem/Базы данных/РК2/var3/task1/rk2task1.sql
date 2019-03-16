USE master
GO
IF EXISTS (SELECT name FROM sys.databases WHERE name = N'RK2')
  DROP DATABASE RK2
GO
CREATE DATABASE RK2
GO

USE [RK2]
GO

CREATE TABLE dbo.Teachers
(
  TeacherID INT NOT NULL PRIMARY KEY,
  FullName NVARCHAR(85) NOT NULL,
  Degree NVARCHAR(85),
  Department NVARCHAR(5) NOT NULL
);
GO

CREATE TABLE dbo.Themes
(
  ThemeID INT NOT NULL PRIMARY KEY,
  Teacher INT NOT NULL,
  Theme NVARCHAR(85) NOT NULL,
  CONSTRAINT FK_Teachers FOREIGN KEY (Teacher) REFERENCES Teachers (TeacherID)
);
GO

CREATE TABLE dbo.Marks
(
  MarkID INT NOT NULL PRIMARY KEY,
  MarkBookNumber INT NOT NULL,
  RepExamMark INT NOT NULL,
  DiplomaMark INT NOT NULL,
);

CREATE TABLE dbo.Students
(
  StudentID INT NOT NULL PRIMARY KEY,
  MarkBookNumber INT NOT NULL, -- как задать правильно?
  FullName NVARCHAR(85) NOT NULL,
  Faculty NVARCHAR(85) NOT NULL,
  StGroup INT NOT NULL,
);
GO