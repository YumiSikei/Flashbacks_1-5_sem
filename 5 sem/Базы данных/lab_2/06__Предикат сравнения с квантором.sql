-- �������� ������ ����, ������� ������� ������ �������� ����� ������������ � ������� �����
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
