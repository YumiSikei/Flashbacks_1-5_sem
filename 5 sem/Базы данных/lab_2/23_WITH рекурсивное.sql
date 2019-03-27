
USE MangaDB
GO

SELECT *
FROM MangaArtist

INSERT INTO MangaArtist(id, Name_Surname, Nickname, Birth_Date, id_Assistant)
VALUES (1000, 'aaaa', 'a', '2012-12-12', NULL)

-- ����������� ���
WITH AssistantsOfMangaka ( id, Name_Surname)
AS
(
	-- ����������� ������������� ��������
	SELECT 1 AS Id, M.Name_Surname
	FROM MangaArtist AS M
	UNION ALL	
	-- ����������� ������������ ��������
	SELECT m.id+1, M.Name_Surname
	FROM MangaArtist AS m
)

 --����������, ������������ ���
SELECT Name_Surname
FROM AssistantsOfMangaka GROUP BY Name_Surname;

--WITH AssistantsOfMangaka ( id, Name_Surname, Nickname, Birth_Date, id_Assistant, Level)
--AS
--(
--	-- ����������� ������������� ��������
--	SELECT M.id, M.Name_Surname, M.Nickname, M.Birth_Date, M.id_Assistant, 0 AS Level
--	FROM MangaArtist AS M
--	--WHERE M.id_Assistant < 34
--	UNION ALL	
--	-- ����������� ������������ ��������
--	SELECT M.id, M.Name_Surname, M.Nickname, M.Birth_Date, M.id_Assistant, Level + 1
--	FROM MangaArtist AS M INNER JOIN AssistantsOfMangaka AS am ON (M.id = am.id_Assistant)
--)

---- ����������, ������������ ���
--SELECT id, Name_Surname, Nickname, Birth_Date, id_Assistant, Level
--FROM AssistantsOfMangaka ORDER BY Level;

