-- ѕолучить список мангак, у которых нет выпуска
USE MangaDB
GO

SELECT Name_Surname
FROM MangaArtist
WHERE EXISTS 
(
SELECT id_Manga_Artist
 FROM Publication RIGHT OUTER JOIN MangaArtist ON Publication.id_Manga_Artist = MangaArtist.id
 WHERE Publication.End_year_of_publication IS NULL
) 