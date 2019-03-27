USE MangaDB
GO

SELECT manga.Name, manga.Description, manga.Count_of_chapters
FROM manga JOIN Publication ON manga.id = Publication.id_manga
WHERE manga.Count_of_chapters > 250 AND Publication.status = ' in process '
ORDER BY manga.Name