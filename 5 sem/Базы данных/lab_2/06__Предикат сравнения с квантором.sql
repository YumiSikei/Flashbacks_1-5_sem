-- Получить список манг, рейтинг которых больше рейтинга любой замороженной в выпуске манги
USE MangaDB
GO

SELECT manga.Name, Publication.Rating
FROM Publication JOIN manga ON Publication.id_manga=manga.id
WHERE Rating > ALL
(
SELECT Rating
 FROM Publication
 WHERE status = ' frozen '
)
