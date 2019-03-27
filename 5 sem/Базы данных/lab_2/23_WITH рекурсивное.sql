
USE MangaDB
GO

SELECT *
FROM MangaArtist

INSERT INTO MangaArtist(id, Name_Surname, Nickname, Birth_Date, id_Assistant)
VALUES (1000, 'aaaa', 'a', '2012-12-12', NULL)

-- Определение ОТВ
WITH AssistantsOfMangaka ( id, Name_Surname)
AS
(
	-- Определение закрепленного элемента
	SELECT 1 AS Id, M.Name_Surname
	FROM MangaArtist AS M
	UNION ALL	
	-- Определение рекурсивного элемента
	SELECT m.id+1, M.Name_Surname
	FROM MangaArtist AS m
)

 --Инструкция, использующая ОТВ
SELECT Name_Surname
FROM AssistantsOfMangaka GROUP BY Name_Surname;

--WITH AssistantsOfMangaka ( id, Name_Surname, Nickname, Birth_Date, id_Assistant, Level)
--AS
--(
--	-- Определение закрепленного элемента
--	SELECT M.id, M.Name_Surname, M.Nickname, M.Birth_Date, M.id_Assistant, 0 AS Level
--	FROM MangaArtist AS M
--	--WHERE M.id_Assistant < 34
--	UNION ALL	
--	-- Определение рекурсивного элемента
--	SELECT M.id, M.Name_Surname, M.Nickname, M.Birth_Date, M.id_Assistant, Level + 1
--	FROM MangaArtist AS M INNER JOIN AssistantsOfMangaka AS am ON (M.id = am.id_Assistant)
--)

---- Инструкция, использующая ОТВ
--SELECT id, Name_Surname, Nickname, Birth_Date, id_Assistant, Level
--FROM AssistantsOfMangaka ORDER BY Level;

