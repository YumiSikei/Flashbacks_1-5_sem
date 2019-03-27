--Select с предикатом сравнения--
SELECT FeeType 
FROM Fee
WHERE FeeAmount > 500 AND Warning = 2
ORDER BY FeeAmount ASC

--оконная функция--
SELECT FeeType
RANK() OVER (ORDER BY val DESC) AS 'total'
FROM Fee
ORDER BY 'total'

--подзапросы--