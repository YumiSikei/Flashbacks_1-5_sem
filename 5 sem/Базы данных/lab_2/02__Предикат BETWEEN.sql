SELECT Name_Surname, Birth_Date
FROM MangaDB.dbo.MangaArtist
WHERE Birth_Date BETWEEN '2002-10-10' AND '2012-10-10'
ORDER BY Name_Surname