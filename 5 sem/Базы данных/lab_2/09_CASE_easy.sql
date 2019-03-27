SELECT MangaArtist.Name_Surname, manga.Name,
	CASE Count_of_sales
		WHEN 500 THEN 'exclusive edition'
		WHEN 2000 THEN 'small edition'
		WHEN 5000 THEN 'middle edition'
		ELSE 'large edition'
	END AS 'Edition'
FROM manga, Publication, MangaArtist
WHERE manga.id = Publication.id_manga AND MangaArtist.id = Publication.id_Manga_Artist