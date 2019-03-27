use MangaDB
go

INSERT MangaArtist(id, Name_Surname, Nickname, Birth_Date)
SELECT (MAX(id_Manga_Artist) + 1), ' Yuki Harune ', ' Nicko ', '1996-07-13'
FROM Publication