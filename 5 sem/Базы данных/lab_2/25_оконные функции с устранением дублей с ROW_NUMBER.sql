USE MangaDB
GO

WITH TT AS
	(
		SELECT id_Manga_Artist,
			ROW_NUMBER() OVER(PARTITION BY id_Manga_Artist ORDER BY id_Manga_Artist) AS rn
		FROM Publication JOIN manga ON Publication.id_manga = manga.id
				RIGHT OUTER JOIN MangaArtist ON Publication.id_Manga_Artist = MangaArtist.id
	)

select * 
from TT
where rn = 1