USE MangaDB
GO


--01__Предикат сравнения

SELECT manga.Name, manga.Description, manga.Count_of_chapters
FROM manga JOIN Publication ON manga.id = Publication.id_manga
WHERE manga.Count_of_chapters > 250 AND Publication.status = ' in process '
ORDER BY manga.Name


--02__Предикат BETWEEN

SELECT Name_Surname, Birth_Date
FROM MangaDB.dbo.MangaArtist
WHERE Birth_Date BETWEEN '2002-10-10' AND '2012-10-10'
ORDER BY Name_Surname


--03__Предикат LIKE

SELECT Name, Adress
FROM MangaDB.dbo.PublishingHouse
WHERE Adress LIKE ' Tokyo%'



--04__Предикат IN с вложенным подзапросом.
-- Получить список активных выпусков, выпущенных мангаками по имени Юи

SELECT manga.Name
FROM Publication JOIN manga ON Publication.id_manga = manga.id
WHERE id_Manga_Artist IN
(
 SELECT id
 FROM MangaArtist
 WHERE Name_Surname LIKE ' Yui%'
) AND status = ' in process '


--05__Предикат EXISTS с вложенным подзапросом.
-- Получить список манг, которые еще не закончены

SELECT Name_Surname 
FROM MangaArtist 
WHERE EXISTS
( 
SELECT id_Manga_Artist 
FROM Publication 
WHERe publication.End_year_of_publication is null 
)


--06__Предикат сравнения с квантором
-- Получить список манг, рейтинг которых больше рейтинга любой замороженной в выпуске манги

SELECT manga.Name, Publication.Rating
FROM Publication JOIN manga ON Publication.id_manga=manga.id
WHERE Rating > ALL
(
SELECT Rating
 FROM Publication
 WHERE status = ' frozen '
)


--07_Агрегатные функции в выражениях столбцов

SELECT SUM(TotalSales/TotalChapters) / COUNT(CountOfManga) AS 'AVG sales for 1 chapter'
FROM (
SELECT COUNT(id) AS CountOfManga, SUM(Count_of_sales) AS TotalSales, SUM(Count_of_chapters) AS TotalChapters
FROM manga
GROUP BY Chapter_release_format
 ) AS TableSales


 --08_Скалярные подзапросы в выражениях столбцов

 SELECT 
	(
	SELECT AVG(End_year_of_publication)
	FROM MangaArtist
	WHERE Publication.id_Manga_Artist = MangaArtist.id
	) AS AvgEndYear,
	(
	SELECT MIN(End_year_of_publication)
	FROM MangaArtist
	WHERE Publication.id_Manga_Artist = MangaArtist.id
	) AS MinEndYear
FROM Publication
group by id_Manga_Artist


--09_CASE_easy

SELECT MangaArtist.Name_Surname, manga.Name,
	CASE Count_of_sales
		WHEN 500 THEN 'exclusive edition'
		WHEN 2000 THEN 'small edition'
		WHEN 5000 THEN 'middle edition'
		ELSE 'large edition'
	END AS 'Edition'
FROM manga, Publication, MangaArtist
WHERE manga.id = Publication.id_manga AND MangaArtist.id = Publication.id_Manga_Artist


--10_CASE_search

SELECT manga.Name,
	CASE
		WHEN Publication.Rating < 4 THEN 'awful'
		WHEN Publication.Rating < 8 THEN 'Not Bad'
		ELSE 'Good'
	END AS Rating
FROM Publication JOIN manga ON manga.id = Publication.id_manga


--11_создание локал табл

SELECT Name,
	(Count_of_sales/Count_of_sales) AS Count_os_sales_for_1_chapter
INTO #SellingChapters
FROM manga
WHERE Chapter_release_format LIKE '%week%'
GROUP BY Name, Count_of_chapters, Count_of_sales


--12_Вложенные коррелированные подзапросы в качестве производных таблиц в предложении FROM

SELECT MP.Name, MangaArtist.Name_Surname , MP.Count_of_sales
FROM MangaArtist JOIN
(
	SELECT Publication.id_Manga_Artist, manga.Name, manga.Count_of_sales
	FROM manga JOIN Publication ON manga.id = Publication.id_manga
	WHERE Publication.status = ' finished '
) AS MP ON MP.id_Manga_Artist = MangaArtist.id


--13_ Вложенные подзапросы с уровнем вложенности 3

SELECT P.Name AS Manga, P.Count_of_chapters, P.Rating, P.Name_Surname AS Mangaka, P.Birth_Date , PublishingHouse.Name AS PublishingHouse
FROM PublishingHouse JOIN
	(
		SELECT id_Publishing_House, MangaArtist.Name_Surname, MangaArtist.Birth_Date, M.Name, M.Count_of_chapters, M.Rating
		FROM MangaArtist JOIN 
			(
				SELECT id_Manga_Artist, id_Publishing_House, manga.Name, manga.Count_of_chapters, PM.Rating
				FROM manga JOIN 
					(
						SELECT id_manga, id_Manga_Artist, id_Publishing_House, Rating
						FROM Publication
						WHERE Rating > 5
					) AS PM ON manga.id = PM.id_manga
				WHERE manga.Count_of_chapters < 200
			) AS M ON MangaArtist.id = M.id_Manga_Artist
		WHERE YEAR (MangaArtist.Birth_Date) > 2000
	) AS P ON P.id_Publishing_House = PublishingHouse.id


--14_SELECT, консолидирующий с GROUP BY, но без HAVING
-- Для каждого мангаки, у которого есть замороженная манга, получить сумму продаж всех манг, их среднюю цену и минимальную


SELECT MangaArtist.Name_Surname AS 'Mangaka',
	SUM(manga.Count_of_sales) AS SumSales,
	AVG(manga.Count_of_sales) AS AvgSales,
	MIN(manga.Count_of_sales) AS MinSales
FROM Publication JOIN manga ON Publication.id_manga = manga.id
		RIGHT OUTER JOIN MangaArtist ON Publication.id_Manga_Artist = MangaArtist.id
WHERE trim(manga.Chapter_release_format) <> 'frozen'
GROUP BY MangaArtist.Name_Surname, manga.Count_of_sales


--15_SELECT, консолидирующий с GROUP BY с HAVING
-- Получить список статусов манг, средний рейтинг которых больше общего среднего рейтинга манг

SELECT status, AVG(Rating) AS 'Average Rating'
FROM Publication
GROUP BY status
HAVING AVG(Rating) >
(
	SELECT AVG(Rating) AS MR
	FROM Publication
)


--16_Однострочный INSERT

INSERT MangaDB.dbo.Publication (id_manga, id_Manga_Artist, id_Publishing_House, status, End_year_of_publication, Rating)
VALUES (101, 5, 94, 'frozen', NULL, 11.4)


--17_многострочный INSERT

INSERT MangaArtist(id, Name_Surname, Nickname, Birth_Date)
SELECT (MAX(id_Manga_Artist) + 1), ' Yuki Harune ', ' Nicko ', '1996-07-13'
FROM Publication


--18_UPDATE

UPDATE manga
SET Count_of_chapters = Count_of_chapters * 1.5
WHERE Count_of_sales = 10000


--19_UPDATE со скалярным подзапросом в предложении SET

UPDATE manga
SET Count_of_chapters = 
(
	select max(Count_of_chapters)
	from manga
	where Count_of_chapters > 200
)
WHERE Count_of_sales = 10000


--20_DELETE

DELETE Publication
WHERE End_year_of_publication = 1934


--21_DELETE  с вложенным коррелированным подзапросом в предложении WHERE

DELETE FROM Publication
WHERE Rating IN
(
	SELECT Rating
	FROM Publication LEFT OUTER JOIN PublishingHouse ON Publication.id_Publishing_House = PublishingHouse.id
	WHERE Creation_year < 1915
)


--22_WITH

WITH man (status, Count_of_chapters, Count_of_sales)
AS
(
	SELECT status, Count_of_chapters, Count_of_sales
	FROM manga JOIN Publication ON Publication.id_manga = manga.id
	WHERE End_year_of_publication IS NULL
)

SELECT *
FROM man
WHERE Count_of_chapters < 300 AND Count_of_sales <= 2000










--23_WITH рекурсивное
 
-- Определение ОТВ
WITH AssistantsOfMangaka ( id, Name_Surname, Lev)
AS
(
	-- Определение закрепленного элемента
	SELECT id, M.Name_Surname, 0 AS Lev
	FROM MangaArtist AS M
	where M.id_Assistant is NULL
	UNION ALL	
	-- Определение рекурсивного элемента
	SELECT A.id, A.Name_Surname, Lev + 1
	FROM MangaArtist AS A
	inner join  AssistantsOfMangaka as B on
	A.id_Assistant = B.id
)
 --Инструкция, использующая ОТВ
SELECT Name_Surname, Lev
FROM AssistantsOfMangaka 
OPTION (MAXRECURSION 1020)

















--24_оконные функции с AVG,MIN,MAX
-- Для каждого автора вывести среднии, минимальные и максимальные продажи, распределив по формату выпуска глав

SELECT Name_Surname AS Mangaka,
		Nickname,
		AVG(Count_of_sales) OVER(PARTITION BY Chapter_release_format, id_Manga_Artist) AS AvgSales,
		MIN(Count_of_sales) OVER(PARTITION BY Chapter_release_format, id_Manga_Artist) AS MinSales,
		MAX(Count_of_sales) OVER(PARTITION BY Chapter_release_format, id_Manga_Artist) AS MaxSales,
		Chapter_release_format
FROM Publication JOIN manga ON Publication.id_manga = manga.id
		RIGHT OUTER JOIN MangaArtist ON Publication.id_Manga_Artist = MangaArtist.id


--25_оконные функции с устранением дублей с ROW_NUMBER

WITH TT AS
	(
		SELECT id_Manga_Artist,
			ROW_NUMBER() OVER(PARTITION BY id_Manga_Artist ORDER BY id_Manga_Artist) AS rn
		FROM Publication JOIN manga ON Publication.id_manga = manga.id
				RIGHT OUTER JOIN MangaArtist ON Publication.id_Manga_Artist = MangaArtist.id
	)

select * 
from TT
where rn = 1