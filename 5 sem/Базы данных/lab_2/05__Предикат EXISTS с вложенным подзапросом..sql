-- Получить список продуктов, которые никто никогда не заказывал
USE MangaDB
GO

SELECT Name_Surname 
FROM MangaArtist 
WHERE EXISTS
( 
SELECT id_Manga_Artist 
FROM Publication 
WHERe publication.End_year_of_publication is null 
)