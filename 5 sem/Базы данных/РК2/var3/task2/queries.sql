use RK2
GO

--предикат сравнения с квантором--
SELECT MarkBookNumber
FROM Marks
WHERE Marks.RepExamMark < ALL(
                SELECT Marks.RepExamMark
                FROM Marks
                WHERE DiplomaMark = 5)


--Или же(все из одной таблицы)--
SELECT MIN(MarkBookNumber) AS 'MarkBookNumber Min (ИУ)'
FROM Students 
WHERE Faculty = 'ИУ'
UNION
SELECT MIN(MarkBookNumber) AS 'MarkBookNumber Min (ФН)'
FROM Students
WHERE Faculty = 'ФН'
UNION
SELECT MIN(MarkBookNumber) AS 'MarkBookNumber Min (Л)'
FROM Students
WHERE Faculty = 'Л'

--Создание новой локальной таблицы--

SELECT MarkBookNumber,
       Cast ((RepExamMark + DiplomaMark) / 2 AS INT) AS INT
INTO #TestTable
FROM Marks 
GO

Select * From #TestTable
GO