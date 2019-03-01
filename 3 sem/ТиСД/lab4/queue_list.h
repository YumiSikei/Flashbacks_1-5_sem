#ifndef QUEUE_LIST_H
#define QUEUE_LIST_H

#include <stdlib.h>

#define STORAGE 10000

struct node
{
    double value;
    struct node *next;
};

struct lqueue
{
    struct node *pin, *pout;
    int size;
};

int is_full_list(struct lqueue *queue);
int is_empty_list(struct lqueue *queue);
struct node* create_node(double input);
struct lqueue *create_queue();
void ll_enqueue(struct lqueue *q, double input);
struct node *ll_dequeue(struct lqueue *q);
int ll_work(int dequeued, int t1_in, int t2_in, int t1_w, int t2_w, int flag);

#endif