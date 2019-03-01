#ifndef __FUNC__H__
#define __FUNC__H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <locale.h>
#include <Windows.h>

#define MAX_WORD_SIZE 11
#define MAX_STRING_SIZE 301
#define OFFSET_COUNT 3

#define FIND 1
#define NOT_FIND -1


struct Node{
    char Word[MAX_WORD_SIZE];
    int Count;
};

struct Tree_list{
    struct Node Data;
    struct Tree_list *Left;
    struct Tree_list *Right;
};

void insert(struct Tree_list *Tree, char *str);
void input_file(struct Tree_list *Tree, FILE *f);
void output_tree(struct Tree_list *Tree, char *position, char *search);
int search(struct Tree_list *Tree, char *search);
int search_in_file(FILE *f, char *search, int *first_input);
int delete_element(struct Tree_list *Tree, char *del);
struct Tree_list *delete_tree(struct Tree_list *Tree, char *del);
void func(struct Tree_list *root);
void apply_post(struct Tree_list *root, void (*func)(struct Tree_list*));
void apply_in(struct Tree_list *root, void (*func)(struct Tree_list*));
void apply_pre(struct Tree_list *root, void (*func)(struct Tree_list*));

#endif //__FUNC__H__