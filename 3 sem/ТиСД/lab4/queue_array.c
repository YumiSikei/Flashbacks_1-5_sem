#include "queue_array.h"
#include "timetest.h"
#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <time.h>

double fabs(double x)
{
    double result;
    if(x < 0)
        x = -x;
    result = x;
    return result;
}

// добавление в очередь нового элемента
int arr_enqueue(array *arr, double elem)
{
    if(arr-> size == CAPACITY - 1)
        return -1;
    int p = arr->pin;
    arr->storage[p] = elem;
    arr->pin++;
    if(arr->pin == CAPACITY)
        arr->pin = 0;
    arr->size++;
    return 0;
}
// удаление элемента из очереди
void arr_dequeue(array *arr)
{
    int p = arr->pout;
    arr->storage[p] = 0.0;
    arr->pout++;
    if(arr->pout == CAPACITY)
        arr->pout = 0;
    arr->size--;
}

//проверка переполнения очереди
int is_full(array *arr)
{  
    return (arr->size >= CAPACITY);  
}

//проверка пустоты очереди
int is_empty(array *arr)
{  
    return (arr->size == 0); 
}

int arr_work(int dequeued, int t1_in, int t2_in, int t1_w, int t2_w) 
{
    array queue;
    queue.size = 0;
    queue.pin = 0;
    queue.pout = 0;
    double tr_in = 0;
    double tr_w = 0;
    double t_enq = 0, t_deq = 0, probability = 0, oawait = 0, tiq = 0;
    double midtiq = 0.0;
    double diff = 0.00001;
    double midsize = 0;
    int req_in = 0, req_out = 0;
    int trigger = 0;
    int res;
    tr_in = tr_w = 0;


    tr_in = get_random_time(t1_in, t2_in) + t1_in;
    tr_w = get_random_time(t1_w, t2_w) + t1_w;
    t_enq = 0;
    t_deq = tr_w - tr_in;
    while(req_out < dequeued)
    {
        if(fabs(tr_in - t_enq) <= diff)
        {   
            if(is_full(&queue) == 0)
            {
                res = arr_enqueue(&queue, tr_in);
                if(res == -1)
                {
                    printf("Переполнение очереди\n");
                    return 0;
                }
                tiq = 0;
                req_in++;
                tr_in = tr_in + get_random_time(t1_in, t2_in) + t1_in;
            }
            else
                t_enq -= diff;
        }
        if(fabs(tr_w - t_deq) <= diff)
        {
            if(is_empty(&queue) == 0)
            {
                arr_dequeue(&queue);
                midtiq = midtiq + tiq;
                trigger++;
                tr_w = tr_w + get_random_time(t1_w, t2_w) + t1_w;
                probability = get_random_probability();
                if(process_again(probability) == 0)
                {   
                    if(is_full(&queue) == 1)
                    {
                        printf("Переполнение очереди\n");
                        return 0;
                    }
                    else
                    {
                        res = arr_enqueue(&queue, tr_in);
                        if(res == -1)
                        {
                            printf("Переполнение очереди\n");
                            return 0;
                        }
                    }
                }
                else
                {
                    req_out++;
                    midsize = midsize + queue.size;
                    if(req_out % REQUEST_SHOW == 0)
                    {
                        printf("------------------------------------------------------------\n");
                        printf("Общая длина очереди: %d\n", queue.size);
                        printf("Средняя длина очереди: %d\n",queue.size/REQUEST_SHOW);
                        printf("------------------------------------------------------------\n");
                        midtiq = 0;
                    }
                }
            }
            else
            {
                oawait = oawait + diff;
                t_deq -= diff;
            }
        }
        tiq = tiq + diff;
        t_enq = t_enq + diff;
        t_deq = t_deq + diff;
    }
    printf("Общее время моделирования: %.3f\n", tr_in);
    printf("Количество вошедших заявок: %d\n", req_in);
    printf("Количество вышедших заявок: %d\n", req_out);
    printf("Среднее время пребывания заявки в очереди: %lf\n", midtiq/REQUEST_SHOW);
    printf("Время простоя аппарата: %.3f\n", oawait);
    printf("Аппарат сработал %d раз\n", trigger);
    printf("\nПроцент погрешности работы программы по входу: %.3f\n", 
           100 * fabs((req_in - tr_in * 2/(t2_in - t1_in)) * (t2_in - t1_in) / (2*tr_in)));
    printf("Процент погрешности работы программы по выходу: %.3f\n ", 100 * fabs((t_enq - t_deq - oawait)/ (t_deq + oawait)));
    printf("\n\n\n");
    return 0;
}
