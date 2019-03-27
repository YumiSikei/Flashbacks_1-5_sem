-- Для каждого автора вывести среднии, минимальные и максимальные продажи, распределив по формату выпуска глав

USE MangaDB
GO

SELECT Name_Surname AS Mangaka,
		Nickname,
		AVG(Count_of_sales) OVER(PARTITION BY Chapter_release_format, id_Manga_Artist) AS AvgSales,
		MIN(Count_of_sales) OVER(PARTITION BY Chapter_release_format, id_Manga_Artist) AS MinSales,
		MAX(Count_of_sales) OVER(PARTITION BY Chapter_release_format, id_Manga_Artist) AS MaxSales,
		Chapter_release_format
FROM Publication JOIN manga ON Publication.id_manga = manga.id
		RIGHT OUTER JOIN MangaArtist ON Publication.id_Manga_Artist = MangaArtist.id