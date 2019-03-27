USE MangaDB
GO

SELECT P.Name AS Manga, P.Count_of_chapters, P.Rating, P.Name_Surname AS Mangaka, P.Birth_Date , PublishingHouse.Name AS PublishingHouse
FROM PublishingHouse JOIN
	(
		SELECT id_Publishing_House, MangaArtist.Name_Surname, MangaArtist.Birth_Date, M.Name, M.Count_of_chapters, M.Rating
		FROM MangaArtist JOIN 
			(
				SELECT id_Manga_Artist, id_Publishing_House, manga.Name, manga.Count_of_chapters, PM.Rating
				FROM manga JOIN 
					(
						SELECT id_manga, id_Manga_Artist, id_Publishing_House, Rating
						FROM Publication
						WHERE Rating > 5
					) AS PM ON manga.id = PM.id_manga
				WHERE manga.Count_of_chapters < 200
			) AS M ON MangaArtist.id = M.id_Manga_Artist
		WHERE YEAR (MangaArtist.Birth_Date) > 2000
	) AS P ON P.id_Publishing_House = PublishingHouse.id