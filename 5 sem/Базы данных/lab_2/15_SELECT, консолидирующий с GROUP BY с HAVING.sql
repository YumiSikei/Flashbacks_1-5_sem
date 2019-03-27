-- �������� ������ �������� ����, ������� ������� ������� ������ ������ ��������
-- �������� ����
use MangaDB
go

SELECT status, AVG(Rating) AS 'Average Rating'
FROM Publication
GROUP BY status
HAVING AVG(Rating) >
(
	SELECT AVG(Rating) AS MR
	FROM Publication
)