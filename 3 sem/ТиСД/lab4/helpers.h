#ifndef HELPERS_H
#define HELPERS_H

#include <stdlib.h>

#define PROB 0.8
#define REQUEST_SHOW 100

double get_random_probability(void);
double get_random_time(int t1, int t2);
int process_again(double probability);

#endif