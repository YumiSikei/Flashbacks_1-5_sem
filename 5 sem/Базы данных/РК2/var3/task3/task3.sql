USE RK2;
GO
--хранимая процедура с выходным параметром--
--понятия не имею, как это писать--GO  
IF OBJECT_ID('RK2.GetFunc', 'P') IS NOT NULL  
    DROP PROCEDURE RK2.GetFunc;  
GO  

CREATE PROCEDURE RK2.GetScalarFunc
@Amount INT OUTPUT
AS
SELECT * FROM sys.all_objects 
WHERE type = 'FN' AND CONTAINS(OBJECT_ID,'ufn')
SELECT @Amount = COUNT(OBJECT_ID) FROM sys.all_objects WHERE type = 'FN' AND CONTAINS(OBJECT_ID, 'ufn')
RETURN
GO

EXECUTE
OUTPUT @Amount