USE MangaDB
GO

-- Пример для базы данных AdventureWorks
DELETE FROM Publication
WHERE Rating IN
(
	SELECT Rating
	FROM Publication LEFT OUTER JOIN PublishingHouse ON Publication.id_Publishing_House = PublishingHouse.id
	WHERE Creation_year < 1915
)