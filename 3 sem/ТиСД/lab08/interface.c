#include "interface.h"

int menu_value(void) // Zotkin made
{
    int value = 0;
    int flag = 0;
    do
    {
        flag = 0;
        printf("Input: ");
        flag = scanf("%d", &value);
        // read all chars
        char ch;
        while( scanf("%c", &ch) && ch != '\n' )
            flag = 0;
    }
    while( flag == 0 );
    return value;
}

unsigned long long int tick(void)
{
	unsigned long long int time = 0;
	__asm__ __volatile__ ("rdtsc" : "=A" (time));
	return time;
}
