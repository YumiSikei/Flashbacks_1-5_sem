-- Получить список активных выпусков, выпущенных мангаками по имени Юи

USE MangaDB
GO

SELECT manga.Name
FROM Publication JOIN manga ON Publication.id_manga = manga.id
WHERE id_Manga_Artist IN
(
 SELECT id
 FROM MangaArtist
 WHERE Name_Surname LIKE ' Yui%'
) AND status = ' in process '