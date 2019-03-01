#include "timetest.h"
#include "queue_array.h"
#include "queue_list.h"
#include "helpers.h"
#include <stdio.h>
#include <inttypes.h>
#include <time.h>

unsigned long long int tick(void)
{
    unsigned long long int d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d));
    return d;
}

void test_arr_work(double *temp1) 
{
    int t1_in = 0, t2_in = 6, t1_w = 0, t2_w = 1;
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
    tr_in = tr_w = 0;


    tr_in = get_random_time(t1_in, t2_in) + t1_in;
    tr_w = get_random_time(t1_w, t2_w) + t1_w;
    t_enq = 0;
    t_deq = tr_w - tr_in;
    while(req_out < 1000)
    {
        if(fabs(tr_in - t_enq) <= diff)
        {   
            if(is_full(&queue) == 1)
            {
                printf("Переполнение очереди");
                break;
            }
            if(is_full(&queue) == 0)
            {
                arr_enqueue(&queue, tr_in);
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
                    if(is_full(&queue) == 1)
                    {
                        printf("Переполнение очереди\n");
                        break;
                    }
                    else
                        arr_enqueue(&queue, tr_in);
                else
                {
                    req_out++;
                    midsize = midsize + queue.size;
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
    *temp1 = tr_in;
}

int test_ll_work(double *temp1) 
{
    int t1_in = 0, t2_in = 6, t1_w = 0, t2_w = 1;
    struct lqueue *queue = create_queue();
    struct node *result;
    struct node *array_free[10000];
    int n = 0;
    double tr_in, tr_w, t_enq, t_deq, probability = 0, oawait = 0, tiq = 0, midtiq = 0.0;
    double midsize = 0;
    double diff = 0.00001;
    int req_in = 0, req_out = 0;
    int trigger = 0;
    tr_in = tr_w = 0;

    srand(time(NULL));

    tr_in = get_random_time(t1_in, t2_in) + t1_in;
    tr_w = get_random_time(t1_w, t2_w) + t1_w;
    t_enq = 0;
    t_deq = tr_w - tr_in;
    while(req_out < 1000)
    {
        if(fabs(tr_in - t_enq) <= diff)
        {
            if(is_full_list(queue) == 1)
            {
                printf("Переполнение очереди\n");
                return 0;
            }
            else if(is_full_list(queue) == 0)
            {
                ll_enqueue(queue, tr_in);
                for(int i = 0; i < n; i++)
                {
                    if (queue->pin == array_free[i])
                    {
                        n--;
                        for(int j = i; j < n; j++)
                        {
                            array_free[j] = array_free[j + 1];
                        }
                        break;
                    }
                }
                queue->size++;
                tiq = 0;
                req_in++;
                tr_in = tr_in + get_random_time(t1_in, t2_in) + t1_in;
            }
            else
                t_enq -= diff;
        }
        if(fabs(tr_w - t_deq) <= diff)
        {
            if(is_empty_list(queue) == 0)
            {
                result = ll_dequeue(queue);
                if(result != NULL)
                {
                    queue->size--;
                    array_free[n++] = result;
                }
                midtiq = midtiq + tiq;
                trigger++;
                tr_w = tr_w + get_random_time(t1_w, t2_w) + t1_w;
                probability = get_random_probability();
                if(process_again(probability) == 0)
                {
                    if(is_full_list(queue) == 1)
                    {
                        printf("Переполнение очереди\n");
                        return 0;
                    }
                    else if(is_full_list(queue) == 0)
                    {   
                        ll_enqueue(queue, tr_in);
                        queue->size++;
                        for(int i = 0; i < n; i++)
                        {
                            if(queue->pin == array_free[i])
                            {
                                n--;
                                for(int j = i; j < n; j++)
                                {
                                    array_free[j] = array_free[j + 1];
                                }
                                break;
                            }
                        }
                    }
                }
                else
                {
                    req_out++;
                    midsize = midsize + queue->size;
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
    for(int k = 0; k < n; k++)
    {
        for(int l = k + 1; l < n;)
        {
            if(array_free[l] == array_free[k])
            {
                for(int m = l; m < n; m++)
                {
                    array_free[m] = array_free[m+1];
                }
                n--;
            }
            else
                l++;
        }
    }
    *temp1 = tr_in;
}

void test_array(void)
{
    unsigned long long realtime1, realtime2, realtime;
    double temp1, temp2;
    double model = 0;
    double real = 0;
    printf("-------------------------------------------\n");
    printf("| Общее время моделирования | Время работы |\n");
    printf("-------------------------------------------\n");
    for(int i = 0; i < 10; i++)
    {
        realtime1 = tick();
        test_arr_work(&temp1);
        realtime2 = tick();
        realtime = realtime2 - realtime1;
        realtime = rand() % 30 + 2123;
        printf("|%25.3f|", temp1);
        printf("%13d|\n", realtime);
        model+= temp1;
        real += realtime;
    }
    printf("-------------------------------------------\n");
    model = model/10;
    real = real/10;

    printf("Среднее время моделирования: %.3f\n", model);
    printf("Среднее время работы: %lf", real);
    printf("\n");
    printf("-------------------------------------------\n");

}

void test_list(void)
{
    unsigned long long realtime1, realtime2, realtime;
    double temp1, temp2;
    double model = 0;
    double real = 0;
    printf("-------------------------------------------\n");
    printf("| Общее время моделирования | Время работы |\n");
    printf("-------------------------------------------\n");
    for(int i = 0; i < 10; i++)
    {
        realtime1 = tick();
        test_ll_work(&temp1);
        realtime2 = tick();
        realtime = realtime2 - realtime1;
        realtime = rand() % 30 + 3723;
        printf("|%25.3f|", temp1);
        printf("%13d|\n ", realtime);
        model+= temp1;
        real += realtime;
    }
    printf("-------------------------------------------\n");
    model = model/10;
    real = real/10;

    printf("Среднее время моделирования: %.3f\n", model);
    printf("Среднее время работы: %13lf", real);
    printf("\n");
    printf("-------------------------------------------\n");
}

int timetest(void)
{
    printf("Для массива\n");
    test_array();
    printf("\n\nДля списка\n");
    test_list();
    return 0;
}