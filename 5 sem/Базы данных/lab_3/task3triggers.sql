USE CHGK;
GO

--C. Два `DML` триггера
--1) Триггер `AFTER` 
--2) Триггер `INSTEAD OF` 

-- Триггер `AFTER `--

drop trigger onInsertTrigger

create trigger onInsertTrigger
on manga
after insert
as
begin
	declare @mangaId int, @name nvarchar(25), @description nvarchar(200), @sales int,  @chapters int, @release nvarchar(20);
	declare insertedCursor cursor for
		select *
		from inserted
	open insertedCursor
	fetch next from insertedCursor into @mangaId, @name, @description, @sales, @chapters, @release
	while @@FETCH_STATUS = 0
	begin 
		print str(@mangaId) + ' ' + @name + ' ' + @description + ' ' + str(@sales) + ' ' + str(@chapters) + ' ' + @release 
		fetch next from insertedCursor into @mangaId, @name, @description, @sales, @chapters, @release
	end
	close insertedCursor
	deallocate insertedCursor
end

insert manga values (101, 'Моя геройская академия', 'Главный герой хочет стать героем. В этом ему помогает герой номер 1.', 10000, 230, '1 in week'), 
				   (102, 'Мой сосед Тоторо', 'Семья из отца и двух дочек переезжает в деревню. В доме живут чернушки, а сосед у них хранитель леса Тоторо.', 10000, 5, '1 every few months')

select*
from manga


-- Триггер `INSTEAD OF` --
CREATE TRIGGER DenyDelete
ON Publication
INSTEAD OF DELETE
AS
BEGIN
    RAISERROR('This is uneditable table.',10,1);
END;


DELETE Publication
WHERE id_manga = 12

select * from Publication