BULK INSERT MangaDB.dbo.manga
FROM 'C:\Users\Даниэлла\Documents\DataBase\Manga.csv'
WITH (DATAFILETYPE = 'char', FIRSTROW = 2, FIELDTERMINATOR = '@', ROWTERMINATOR = '0x0a', CODEPAGE = 1251);
GO 

BULK INSERT MangaDB.dbo.MangaArtist
FROM 'C:\Users\Даниэлла\Documents\DataBase\MangaArtist.csv'
WITH (DATAFILETYPE = 'char', FIRSTROW = 2, FIELDTERMINATOR = '@', ROWTERMINATOR = '0x0a');
GO 

BULK INSERT MangaDB.dbo.PublishingHouse
FROM 'C:\Users\Даниэлла\Documents\DataBase\PublishingHouse.csv'
WITH (DATAFILETYPE = 'char', FIRSTROW = 2, FIELDTERMINATOR = '@', ROWTERMINATOR = '0x0a');
GO 

BULK INSERT MangaDB.dbo.Publication
FROM 'C:\Users\Даниэлла\Documents\DataBase\Publication.csv'
WITH (DATAFILETYPE = 'char', FIRSTROW = 2, FIELDTERMINATOR = '@', ROWTERMINATOR = '0x0a');
GO 