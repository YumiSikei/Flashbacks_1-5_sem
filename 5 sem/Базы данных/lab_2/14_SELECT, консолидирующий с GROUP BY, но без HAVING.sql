-- Для каждого заказанного продукта категории 1 получить его цену, среднюю цену,
-- минимальную цену и название продукта
USE MangaDB
GO

SELECT MangaArtist.Name_Surname AS 'Mangaka',
	SUM(manga.Count_of_sales) AS SumSales,
	AVG(manga.Count_of_sales) AS AvgSales,
	MIN(manga.Count_of_sales) AS MinSales
FROM Publication JOIN manga ON Publication.id_manga = manga.id
		RIGHT OUTER JOIN MangaArtist ON Publication.id_Manga_Artist = MangaArtist.id
WHERE manga.Chapter_release_format <> ' frozen '
GROUP BY MangaArtist.Name_Surname, manga.Count_of_sales