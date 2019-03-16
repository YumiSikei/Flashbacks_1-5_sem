--

SELECT 
	(
	SELECT AVG(End_year_of_publication)
	FROM MangaArtist
	WHERE Publication.id_Manga_Artist = MangaArtist.id
	) AS AvgEndYear,
	(
	SELECT MIN(End_year_of_publication)
	FROM MangaArtist
	WHERE Publication.id_Manga_Artist = MangaArtist.id
	) AS MinEndYear
FROM Publication
group by id_Manga_Artist