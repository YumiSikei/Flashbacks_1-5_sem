USE MangaDB
GO

SELECT manga.Name,
	CASE
		WHEN Publication.Rating < 4 THEN 'awful'
		WHEN Publication.Rating < 8 THEN 'Not Bad'
		ELSE 'Good'
	END AS Rating
FROM Publication JOIN manga ON manga.id = Publication.id_manga