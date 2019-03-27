USE MangaDB
GO

SELECT MP.Name, MangaArtist.Name_Surname , MP.Count_of_sales
FROM MangaArtist JOIN
(
	SELECT Publication.id_Manga_Artist, manga.Name, manga.Count_of_sales
	FROM manga JOIN Publication ON manga.id = Publication.id_manga
	WHERE Publication.status = ' finished '
) AS MP ON MP.id_Manga_Artist = MangaArtist.id