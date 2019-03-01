#include "helpers.h"

// случайная вероятность
double get_random_probability(void)
{
    return ((double)rand()/(double)(RAND_MAX)) * 1.0;
}

//случайные времена обработок
double get_random_time(int t1, int t2)
{
    return ((double)rand()/(double)(RAND_MAX)) * (t2 - t1);
}

// определяем, отправить заявку повторно в очередь или нет
int process_again(double probability)
{
    if(probability < PROB)
        return 0;
    else
        return 1;
}