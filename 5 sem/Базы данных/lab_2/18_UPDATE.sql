USE MangaDB
GO

UPDATE manga
SET Count_of_chapters = Count_of_chapters * 1.5
WHERE Count_of_sales = 10000