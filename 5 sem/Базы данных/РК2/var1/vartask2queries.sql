USE RK2;
GO

--использование простого CASE--
SELECT 
    CASE

FROM

--использование оконной функции--
--упорядочивание лекарств по дороговизне--
SELECT Name, Price 
    RANK() OVER (ORDER BY val DESC) AS 'cost'
FROM Medicine
ORDER BY 'cost';

--SELECT using HAVING--
--medicine, which price is less than average price--
SELECT Name
FROM Medicine
WHERE Price IS NOT NULL
GROUP BY Name
HAVING AVG(Price) < 
(
    SELECT AVG(Price)
    FROM Medicine
)