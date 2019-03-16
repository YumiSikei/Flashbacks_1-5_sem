USE MangaDB
GO


WITH man (status, Count_of_chapters, Count_of_sales)
AS
(
	SELECT status, Count_of_chapters, Count_of_sales
	FROM manga JOIN Publication ON Publication.id_manga = manga.id
	WHERE End_year_of_publication IS NULL
)

SELECT *
FROM man
WHERE Count_of_chapters < 300 AND Count_of_sales <= 2000
