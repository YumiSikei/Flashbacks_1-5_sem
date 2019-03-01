CC := gcc

# Опции компиляции
CFLAGS := -std=c99 -Wall -Werror -Wno-format -g3

# Общие объектные файлы
OBJS := func.o

main.exe : $(OBJS) main.o
	$(CC) $^ -o $@

%.o : %.c *.h
	$(CC) $(CFLAGS) -c $<

clean :
	$(RM) *.o *.exe