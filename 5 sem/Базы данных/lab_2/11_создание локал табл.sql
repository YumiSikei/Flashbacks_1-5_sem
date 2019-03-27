USE MangaDB
GO

SELECT Name,
	(Count_of_sales/Count_of_sales) AS Count_os_sales_for_1_chapter
INTO #SellingChapters
FROM manga
WHERE Chapter_release_format LIKE '%week%'
GROUP BY Name, Count_of_chapters, Count_of_sales