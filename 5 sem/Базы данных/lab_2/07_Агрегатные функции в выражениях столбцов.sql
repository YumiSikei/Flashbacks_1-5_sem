
USE MangaDB
GO

SELECT SUM(TotalSales/TotalChapters) / COUNT(CountOfManga) AS 'AVG sales for 1 chapter'
FROM (
SELECT COUNT(id) AS CountOfManga, SUM(Count_of_sales) AS TotalSales, SUM(Count_of_chapters) AS TotalChapters
FROM manga
GROUP BY Chapter_release_format
 ) AS TableSales