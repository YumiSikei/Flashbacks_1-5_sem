#ifndef QUEUE_ARRAY_H
#define QUEUE_ARRAY_H

#define CAPACITY 10000

typedef struct Array
{
    double storage[CAPACITY];
    int pin;
    int pout;
    int size;
}array;

int arr_enqueue(array *arr, double elem);
void arr_dequeue(array *arr);
int is_full(array *arr);
int is_empty(array *arr);
int arr_work(int dequeued, int t1_in, int t2_in, int t1_w, int t2_w);
double fabs(double x);


#endif
