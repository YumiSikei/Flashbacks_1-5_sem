main.out: main.o queue_array.o queue_list.o timetest.o helpers.o
	gcc -o main.out main.o queue_array.o queue_list.o timetest.o helpers.o

queue_array.o: queue_array.c queue_array.h helpers.h timetest.h
	gcc -std=c99 -c queue_array.c

queue_list.o: queue_list.c queue_list.h helpers.h timetest.h
	gcc -std=c99 -c queue_list.c

timetest.o: timetest.c timetest.h
	gcc -std=c99 -c timetest.c

helpers.o: helpers.c helpers.h
	gcc -std=c99 -c helpers.c

main.o: main.c queue_array.h queue_list.h timetest.h helpers.h
	gcc -std=c99 -c main.c 

clean:
	rm *.o *.out