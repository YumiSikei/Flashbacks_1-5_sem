--B. Четыре хранимых процедуры
--1) Хранимую процедуру без параметров или с параметрами 
--2) Рекурсивную хранимую процедуру или хранимую процедур с рекурсивным ОТВ 
--3) Хранимую процедуру с курсором 
--4) Хранимую процедуру доступа к метаданным 


USE MangaDB
GO

-- 1 ) Хранимую процедуру без параметров или с параметрами --

drop procedure dbo.SalesNum

create procedure SalesNum(@Name_Surname nvarchar(20))
as
begin
	declare @num int;
	select @num = count(id) from MangaArtist where Name_Surname like @Name_Surname
	print  @num
end
GO

exec SalesNum '%Yuki%'

select*
from MangaArtist
where Name_Surname like '%Yuki%'




--2 ) Рекурсивную хранимую процедуру или хранимую процедур с рекурсивным ОТВ 

drop procedure recursion
go 


create procedure recursion(@MangakaNum int)
as
begin
	declare @maxId int;
	select @maxId = max(MangaArtist.id)
	from MangaArtist
	if (@MangakaNum < @maxId)
	begin
		if (@MangakaNum >= 0)
		begin
			declare @mangakaId INT
			declare @name nvarchar(45)
			select @name = MangaArtist.Name_Surname , @mangakaId = MangaArtist.id
			from MangaArtist
			where MangaArtist.id = @MangakaNum order by MangaArtist.Birth_Date
			print @mangakaId
			print @name

			set @MangakaNum -= 1
			exec recursion @MangakaNum
		end
	end
	else
		print 'Too much plane';
end
go

exec recursion 5

select * from MangaArtist

--поправить


-- 3 ) Хранимая процедура с курсором--

drop procedure cursors
go

create procedure cursors(@begin VARCHAR(15), @end VARCHAR(15))
as
begin
	declare @mangakaid int, @name_surname varchar(70);
	declare tableCursor cursor for
		select id, Name_Surname
		from MangaArtist
		where Birth_Date between @begin and @end
	open tableCursor
	fetch next from tableCursor into @mangakaid, @name_surname
	while @@FETCH_STATUS = 0
	begin 
		print ' ' +str(@mangakaid) + ' ' + @name_surname
		fetch next from tableCursor into @mangakaid, @name_surname
	end
	close tableCursor
	deallocate tableCursor
end

exec cursors '01/01/1990', '01/01/1994'

select *
from MangaArtist
where Birth_Date BETWEEN '01/01/1990' AND '01/01/1994'


--определение курсора

-- 4 ) Хранимая процедура доступа к метаданным--

create procedure metaAccess(@schemaName nvarchar(100))
as
begin
select * from INFORMATION_SCHEMA.TABLES where table_schema=@schemaName
end

exec metaAccess 'dbo'