#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <string.h>
#include <stdarg.h>

#define MAX_STACK_SIZE 50

typedef char tData;

typedef struct sNode{
	tData value;
	struct sNode *next;
} tNode;

typedef struct{
	tNode *p_begin;
	size_t m_size;
} tStack;

static int count_st = 0;
static tNode *empty_err[MAX_STACK_SIZE] = {NULL};

void print_arr(void)
{
	int flag = 0;
	printf("Empty addresses:\n");
	for (int i = 0; i < MAX_STACK_SIZE; i++){
		if (empty_err[i] != 0)
		{
			flag = 1;
			printf("%u\n", empty_err[i]);
		}
	}
	if (!flag)
		printf("[No adresess]\n");
}

void zero(void)
{
	for (int i = 0; i < MAX_STACK_SIZE; i++){
		empty_err[i] = NULL;
	}
}

void put_marker(int i)
{
	for (int j = 0; j < i; j++)
		printf(" ");
	printf("^\n");
}

int check_left_brace(char brace)
{
	return (brace == '(' || brace == '{' || brace == '[' || brace == '<');
}

int check_right_brace(char brace)
{
	return (brace == ')' || brace == '}' || brace == ']' || brace == '>');
}

char get_the_brace_left_pair(char brace)
{
	if (brace == ')')
		return '(';
	else if (brace == '}')
		return '{';
	else if (brace == ']')
		return '[';
	else if (brace == '>')
		return '<';
	else
		return brace;
}

void print_list(tNode *p_begin)
{
	tNode *p = p_begin;
	while (p != NULL)
	{
		//распечатать структуру данных
		printf("%c %u\n", p->value, p);
		//шагнуть вперед !!!
		p = p->next;
	}
}

void delete_list(tNode *p_begin)
{
	tNode *p = p_begin;
	while (p != NULL)
	{
		tNode *tmp;
		tmp = p;
		//шагнуть вперед !!!
		p = p->next;
		//удалить память ячейки
		free(tmp);
	}
}

void stack_push(tStack *s, tData value)
{
	tNode *p = (tNode *)malloc(sizeof(tNode));
	for (int j = 0; j < MAX_STACK_SIZE; j++)
	{
		if (empty_err[j] == p)
		{
			for (int k = j; k < MAX_STACK_SIZE-1; k++)
				empty_err[j] = empty_err[j+1];
			break;
		}
	}
	p->value = value;
	p->next = s->p_begin;
	s->p_begin = p;
	s->m_size++;
}

int stack_is_empty(const tStack *s)
{
	return s->m_size == 0;
}

tData stack_pop(tStack *s)
{
	if (stack_is_empty(s))
	{
		printf("Trying to pop from empty stack!\n");
		return '0';
	}
	tNode *tmp = s->p_begin;
	tData tmp_value = tmp->value;
	s->p_begin = s->p_begin->next;
	s->m_size--;
	for (int j = 1; j < MAX_STACK_SIZE; j++)
	{
		if (empty_err[j] == 0){
			empty_err[j] = tmp;
			break;
		}
	}
	free(tmp);
	return tmp_value;
}

tData stack_top(const tStack *s)
{
	if (stack_is_empty(s))
	{
		printf("Stack is empty!\n");
		return '0';
	}
	return s->p_begin->value;
}

size_t stack_size(const tStack *s)
{
	return s->m_size;
}

void stack_clear(tStack *s)
{
	delete_list(s->p_begin);
	s->p_begin = NULL;
	s->m_size = 0;
}

tStack stack_create()
{
	tStack new_stack = {NULL, 0};
	return new_stack;
}

void stack_print(const tStack *s)
{
	if (stack_is_empty(s))
		printf("[Empty stack]\n");
	print_list(s->p_begin);
}

int arr_stack_is_empty(const tData *s)
{
	if (s == NULL){
		return 1;
	}
	//printf("S: %s\n", s);
	if (check_left_brace(s[0]))
		return 0;
	else
		return 1;
}

size_t arr_stack_size(const tData *s)
{
	if (arr_stack_is_empty(s))
		return 0;
	int i = 0;
	while (s[i] != '\0')
	{
		if (!check_left_brace(s[i]))
			return i;
		i++;
	}
	return strlen(s);
}

tData arr_stack_pop(tData *s)
{
	count_st--;
	if (arr_stack_is_empty(s))
	{
		printf("Trying to pop from empty stack!\n");
		return '\n';
	}
	tData res = s[arr_stack_size(s)-1];
	//printf("5: %d\n", arr_stack_size(s));
	s[arr_stack_size(s)-1] = '0';
	return res;
}

tData arr_stack_top(const tData *s)
{
	return s[0];
}



void arr_stack_print(const tData *s)
{
	if (arr_stack_is_empty(s))
		printf("[Empty stack]\n");
	else
	{
		int i = 0;
		while (!(arr_stack_is_empty(s+i)))
		{
			putchar(*(s+i));
			i++;
		}
		putchar('\n');
	}
}

void arr_stack_clear(tData *s)
{
	free(s);
}

tData *arr_stack_create(int size)
{
	tData *s = malloc(sizeof(tData)*(size+1));
	s[size] = '\0';
	return s;
}

void zero_count(void)
{
	count_st = 0;
}

tData *arr_stack_push(tData *s, tData value, ...)
{
	int max_size;
	va_list ap;
	va_start(ap, value);
	if (ap != NULL)
		max_size = va_arg(ap, int);
	else
		max_size = MAX_STACK_SIZE;
	count_st++;
	//printf("max_size: %d\n", max_size);
	if (s == NULL)
	{
		//printf("Pushing into empty stack...\nCreating stack...\n");
		s = arr_stack_create(max_size);
		s[0] = value;
		va_end(ap);
		return s;
	}
	if (count_st > max_size){
		printf("Stack overflow! Pushing abortred!\n");
		va_end(ap);
		return s;
	} else if (arr_stack_size(s) == strlen(s)){
		//printf("Stack is full...\nResizing stack, reallocing memory...\n");
		tData *new_s = arr_stack_create(arr_stack_size(s)*2);
		for (int i = arr_stack_size(s); i >= 0; i--){
			new_s[i] = s[i];
		}
		new_s[arr_stack_size(s)] = value;
		free(s);
		va_end(ap);
		return new_s;
	}
	else {
		s[arr_stack_size(s)] = value;
		va_end(ap);
		return s;
	}
}

void braces_succession_checker()
{
	int i = 0;
	int good_braces_succession = 1;
	tStack open_braces = stack_create();
	auto char brace = getchar();
	while (brace != '\n')
	{
		if (check_left_brace(brace))
		{
			stack_push(&open_braces, brace);
		}
		else if (check_right_brace(brace))
		{
			if (stack_is_empty(&open_braces))
			{
				put_marker(i);
				printf("There is a closing brace before opening one!\n");
				good_braces_succession = 0;
				break;
			}
			char pair_candidate = stack_pop(&open_braces);
			if (get_the_brace_left_pair(brace) != pair_candidate)
			{
				put_marker(i);
				printf("There is a closing brace before opening one!\n");
				good_braces_succession = 0;
				break;
			}
		} //else символ вообще не скобка

		brace = getchar();
		i++;
		//stack_print(&open_braces);
	}
	if (good_braces_succession && !stack_is_empty(&open_braces))
	{
		//остались незакрытые левые скобки
		put_marker(i);
		printf("There are left braces not closed left!\n");
		good_braces_succession = 0;
	}
	if (good_braces_succession)
	{
		put_marker(i);
		printf("It's OK!\n");
	}
	else
	{
		printf("Bad succession!\n");
	}
	while (brace != '\n')
		brace = getchar();
	if (i == 0)
		printf("The empty string.\n");
	
	stack_clear(&open_braces);
}



void arr_braces_succession_checker()
{
	int i = 0;
	int good_braces_succession = 1;
	tData *open_braces = NULL;
	auto char brace = getchar();
	int flag = 1;
	while (brace != '\n' || flag)
	{
		//arr_stack_print(open_braces);
		if (check_left_brace(brace))
		{
			open_braces = arr_stack_push(open_braces, brace, MAX_STACK_SIZE);
		}
		else if (check_right_brace(brace))
		{
			if (arr_stack_is_empty(open_braces))
			{
				put_marker(i);
				printf("There is a closing brace before opening one!\n");
				good_braces_succession = 0;
				break;
			}
			char pair_candidate = arr_stack_pop(open_braces);
			if (get_the_brace_left_pair(brace) != pair_candidate)
			{
				put_marker(i);
				printf("There is a closing brace before opening one!\n");
				good_braces_succession = 0;
				break;
			}
		} //else символ вообще не скобка

		brace = getchar();
		i++; flag = 0;
	}
	if (good_braces_succession && !arr_stack_is_empty(open_braces))
	{
		//остались незакрытые левые скобки
		put_marker(i);
		printf("There are left braces not closed left!\n");
		good_braces_succession = 0;
	}
	if (good_braces_succession)
	{
		put_marker(i);
		printf("It's OK!\n");
	}
	else
	{
		printf("Bad succession!\n");
	}
	while (brace != '\n')
		brace = getchar();
	arr_stack_clear(open_braces);
	if (i == 0)
		printf("The empty string.\n");
}

int main()
{
	clock_t t1, t2, t3, t4;
	int tmp = 0;
	printf("Stack by list\nInput string, please:\n");
	t1 = clock();
	braces_succession_checker();
	t2 = clock();
	printf("Executing time (msec): %f\n", (double)(t2-t1)/CLOCKS_PER_SEC*1000);
	
	printf("\nStack by array\nInput string, please:\n");
	t3 = clock();
	arr_braces_succession_checker();
	t4 = clock();
	printf("Executing time (msec): %f\n", (double)(t4-t3)/CLOCKS_PER_SEC*1000);
	
	printf("Working with stack:\n");
	int flag = 1;
	tStack st = stack_create();
	tData *arr_st = NULL;
	zero();
	static int msize;
	printf("Input size of stack by array:\n");
	scanf("%d", &msize);
	while (flag)
	{
		printf("1)Pop\n2)Push\n3)Print\n4)Print empty adresess\n5)Realloc stack by array size\n6)Exit\n");
		scanf("%d", &tmp);
		switch (tmp)
		{
			case 1:
				printf("Stack on list:\n");
				stack_pop(&st);
				printf("Stack on array:\n");
				arr_stack_pop(arr_st);
				break;
			case 2: 
				stack_push(&st, '(');
				arr_st = arr_stack_push(arr_st, '(', msize);
				break;
			case 3:
				printf("Stack on list:\n");
				stack_print(&st);
				printf("Stack on array:\n");
				arr_stack_print(arr_st);
				break;
			case 4:
				print_arr();
				break;
			case 5:
				printf("Array by stack will be zeroed.\n");
				printf("Input size of stack by array:\n");
				scanf("%d", &msize);
				zero_count();
				free(arr_st);
				arr_st = NULL;
				break;
			case 6:
				flag = 0;
				free(arr_st);
				stack_clear(&st);
				break;
		};
	}
	return EXIT_SUCCESS;
}