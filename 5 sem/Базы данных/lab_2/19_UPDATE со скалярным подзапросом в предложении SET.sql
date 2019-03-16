USE MangaDB
GO

UPDATE manga
SET Count_of_chapters = 
(
	select max(Count_of_chapters)
	from manga
	where Count_of_chapters > 200
)
WHERE Count_of_sales = 10000