CC := gcc

CFLAGS := -Wall -O1

launch: main.exe

main.exe: main.o graph.c interface.c
	$(CC) -std=c11 -o $@ $^
	
%.o : %.c *.h
	$(CC) $(CFLAGS) -c $< -gdwarf-3
	
clean :
	rm *.o