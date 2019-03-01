#include "queue_list.h"
#include "queue_array.h"
#include "helpers.h"
#include "timetest.h"
#include <math.h>
#include <stdio.h>
#include <time.h>

//проверка переполнения очереди
int is_full_list(struct lqueue *queue)
{  
    return (queue->size == STORAGE);  
}

//проверка пустоты очереди
int is_empty_list(struct lqueue *queue)
{  
    return (queue->size == 0); 
}

//создание узла списка
struct node* create_node(double input)
{
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    if(newnode)
    {
        newnode->value = input;
        newnode->next = NULL;
    }
    return newnode;
}

// конструктор очереди
struct lqueue* create_queue()
{
    struct lqueue *q = (struct lqueue*)malloc(sizeof(struct lqueue));
    q->pin = q->pout = NULL;
    q->size = 0;
    return q;
}

// добавление элемента в очередь
void ll_enqueue(struct lqueue *q, double input)
{
    struct node* tmp = create_node(input);
    if (tmp == NULL) 
    {
        return;
    }
    if(q->pout == NULL) 
    {
        q->pin = q->pout = tmp;
        return;
    }
    q->pout->next = tmp;
    q->pout = tmp;
}

struct node* ll_dequeue(struct lqueue *q)
{
    if (q->pin == NULL)
       return NULL;
    struct node* temp = q->pin;
    q->pin = q->pin->next;
    free(temp);
    if (q->pin == NULL)
       q->pout = NULL;
    return temp;
}

int ll_work(int dequeued, int t1_in, int t2_in, int t1_w, int t2_w, int flag) 
{
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
				printf("tiq = %lf\n", tiq);
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
                    if(req_out % REQUEST_SHOW == 0)
                    {
                        printf("------------------------------------------------------------\n");
                        printf("Общая длина очереди: %d\n", queue->size);
                        printf("Средняя длина очереди: %d\n",queue->size/REQUEST_SHOW);
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
    if(flag == 1)
    {
        printf("\n\nНезадействованные адреса элементов\n");
        for(int i = 0; i < n; i++)
        {
            printf("%p\n", array_free[i]);
        }
    }
    printf("\n\n\n");
}

