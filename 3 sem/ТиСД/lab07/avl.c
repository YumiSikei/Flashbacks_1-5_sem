// avl tree
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAX_CHAR 50

#define OK 0

#define ERR_NO_DELETE -1
#define ERR_MEMORY 2
#define ERR_FILE 3

#define MAX 250 /* размер хеш-таблицы */

#define HASH_DEL 11

#define FIRST 3
#define STEP 1
#define OVER 7


typedef struct avl_tree node;

struct avl_tree // структура для представления узлов дерева
{
	char  key[MAX_CHAR];
	unsigned char height;
	node* left;
	node* right;
	//node(int k) { key = k; left = right = 0; height = 1; }
};

//___________________________________________________________________________________AVL
node *init_key(char *k)
{
	node *head = malloc(sizeof(node));
	if (head)
	{
		//head->key = key;
		strcpy(head->key, k);
		head->height = 1;
		head->left = NULL;
		head->right = NULL;
	}
	
	return head;
}

unsigned char height(node* p)
{
	return p ? p->height : 0;
}

int bfactor(node* p)
{
	return height(p->right) - height(p->left);
}


void fixheight(node* p)
{
	unsigned char hl = height(p->left);
	unsigned char hr = height(p->right);
	p->height = ( hl > hr  ?  hl : hr) + 1;
}

node* rotateright(node* p) // правый поворот вокруг p
{
	node* q = p->left;
	p->left = q->right;
	q->right = p;
	fixheight(p);
	fixheight(q);
	return q;
}

node* rotateleft(node* q) // левый поворот вокруг q
{
	node* p = q->right;
	q->right = p->left;
	p->left = q;
	fixheight(q);
	fixheight(p);
	return p;
}

node* balance(node* p) // балансировка узла p
{
	fixheight(p);
	if( bfactor(p)==2 )
	{
		if( bfactor(p->right) < 0 )
			p->right = rotateright(p->right);
		return rotateleft(p);
	}
	if( bfactor(p)==-2 )
	{
		if( bfactor(p->left) > 0  )
			p->left = rotateleft(p->left);
		return rotateright(p);
	}
	return p; // балансировка не нужна
}

node* insert(node* p, char *k) // вставка ключа k в дерево с корнем p
{
	if( !p ) 
		return init_key(k);
	//if( k<p->key )
	if (strcmp(k, p->key) < 0)
		p->left = insert(p->left,k);
	else
		p->right = insert(p->right,k);
	return balance(p);
}

node* findmin(node* p) // поиск узла с минимальным ключом в дереве p 
{
	return p->left?findmin(p->left):p;
}

node* removemin(node* p) // удаление узла с минимальным ключом из дерева p
{
	if( p->left==0 )
		return p->right;
	p->left = removemin(p->left);
	return balance(p);
}
/*
node* remove(node* p, int k) // удаление ключа k из дерева p
{
	if( !p ) return 0;
	if( k < p->key )
		p->left = remove(p->left,k);
	else if( k > p->key )
		p->right = remove(p->right,k);	
	else //  k == p->key 
	{
		node* q = p->left;
		node* r = p->right;
		delete p;
		if( !r ) return q;
		node* min = findmin(r);
		min->right = removemin(r);
		min->left = q;
		return balance(min);
	}
	return balance(p);
}
*/

void to_s_avl(node *n, int spaces)
{
	char buf[100];
 if(n!=NULL)
 {
   memset(buf, ' ', spaces);
   buf[spaces]=0;
   strcat(buf, "%s %d\n");
   spaces+=5;
   to_s_avl(n->left, spaces);
   printf(buf, n->key, n->height);
   to_s_avl(n->right, spaces);
 }
}


void to_dot_avl(node *root, void *arg)
{	
	FILE *f = arg;

    if (root->left)
        fprintf(f, "%10s -- %10s [label=\"left\"];\n", root->key, root->left->key);

    if (root->right)
        fprintf(f, "%10s -- %10s [label=\"right\"];\n", root->key, root->right->key);
}


// обход дерева префиксно
void apply_pre_avl(node *root, void (*func)(node*, void*), void *arg)
{
    if (root == NULL)
        return;

    // pre-order
    func(root, arg);
    apply_pre_avl(root->left, func, arg);
    // in-order
    //func(root, arg);
    apply_pre_avl(root->right, func, arg);
    // post-order
    // func(root, arg);
}

void export_to_dot_avl(FILE *stream, node *root)
{
    fprintf(stream, "\ngraph\n{\n");
    apply_pre_avl(root, to_dot_avl, stream);
    fprintf(stream, "}\n");
}

int have_simple_avl(node *head, char *simple)
{
	if (head)
	{
		int k = strcmp(head->key, simple);
		if (k == 0)
			return 1;
		if (k < 0)
			if (have_simple_avl(head->right, simple))
				return 1;
		if (k > 0)
			if (have_simple_avl(head->left, simple))
				return 1;
	}
	return 0;
}

node *find_avl_knot(node *head, char *simple, int *cmp)
{
	node *cor = NULL;
	if (head)
	{
		(*cmp)++;
		int k = strcmp(head->key, simple);
		if (k == 0)
			return head;
		if (k < 0)
			if ((cor = find_avl_knot(head->right, simple, cmp)) != 0)
				return cor;
		if (k > 0)
			if ((cor = find_avl_knot(head->left, simple, cmp)) != 0)
				return cor;
	}
	return 0;
}

node *scan_file_avl(FILE *stream, node *head)
{
	char buf[MAX_CHAR];
	int c;
	int cmp = 0;
	while ((c = fscanf(stream, "%s", buf)) == 1)
	{
		if (head)
		{
			node *nod = find_avl_knot(head, buf, &cmp);
			if (!nod)
			{
		//printf("buf 	- %s \n", buf);
				head = insert(head, buf);
			}
		}
		else
			head = insert(head, buf);
		//else
		//	return ERR_MEMORY;
	}
	
	return head;
}


void print_avl_knot(node*head)
{
	if (head)
	{
		printf("\nFINDING KNOT \n");
		printf("\tadress %p \n", head);
		printf(" \tdata %s\n", head->key);
		printf("\n left                right");
		printf("\n %16p   %16p", head->left, head->right);
		if (head->left)
			printf("\n %16s ", head->left->key);
		else
			printf("\n           ");
		if (head->right)
			printf("  %16s\n", head->right->key);
		else
			printf("\n\n");
	}
	else 
		printf("\nthere are no knot with this name\n");
}


//___________________________________________________________________________________________BINERY

struct tree_node
{
	const char *word;
	int count;
	struct tree_node *left;
	struct tree_node *right;	
	struct tree_node *parent;
};

// создать узел
struct tree_node* create_node(const char *word)
{
	struct tree_node *node = malloc(sizeof(struct tree_node));
	if (!node)
		return NULL;

	node->word = strdup(word);
	if (!node->word)
		return NULL;

	node->count = 1;
	node->left = NULL;
	node->right = NULL;
	node->parent = NULL;

	return node;
}

// печать обхода
void travel(struct tree_node *root, void *arg)
{	
	FILE *f = arg;
    fprintf(f, "%10s_%-2d\n", root->word, root->count);
}

// обход дерева префиксно
void apply_pre(struct tree_node *root, void (*func)(struct tree_node*, void*), void *arg)
{
    if (root == NULL)
        return;

    // pre-order
    func(root, arg);
    apply_pre(root->left, func, arg);
    // in-order
    //func(root, arg);
    apply_pre(root->right, func, arg);
    // post-order
    // func(root, arg);
}

// перевести данные на язык DOT
void to_dot(struct tree_node *root, void *arg)
{	
	FILE *f = arg;

    if (root->left)
        fprintf(f, "%10s_%-2d -> %10s_%-2d [label=\"left\"];\n", root->word, root->count, root->left->word, root->left->count);

    if (root->right)
        fprintf(f, "%10s_%-2d -> %10s_%-2d [label=\"right\"];\n", root->word, root->count, root->right->word, root->right->count);
}

// экспортировать данные на языке DOT в поток
void export_to_dot(FILE *stream, struct tree_node *root)
{
    fprintf(stream, "\ndigraph Dictionary \n{\n");
    apply_pre(root, to_dot, stream);
    fprintf(stream, "}\n");
}


// добавить узел в дерево двоичного поиска
struct tree_node* insert_in_tree(struct tree_node *root, struct tree_node *node)
{
	int cmp;

	// найдено место добавления
	if (root == NULL)
		return node;

	cmp = strcmp(node->word, root->word);
	if (cmp == 0)
		root->count++;
	else if (cmp < 0)
	{
		root->left = insert_in_tree(root->left, node);
		root->left->parent = root;
		//printf("\n ro = %p", (void*)root);
		//printf("\n parent_left = %p", (void*)root->left->parent);
	}
	else
	{
		root->right = insert_in_tree(root->right, node);
		root->right->parent = root;
		//printf("\n ro = %p", (void*)root);
		//printf("\n parent_right = %p", (void*)root->right->parent);
	}
	
	return root;
}

// инициализация дерева, получение данных из файла
struct tree_node *init_tree(FILE *f, struct tree_node *root)
{
	char word[MAX_CHAR];
	//int pos_slash;
	struct tree_node *node;

	//while (fgets(word, MAX_BUF, f))
    while (fscanf(f, "%s", word) == 1)
	{
		// исключаем символ перехода
		//..pos_slash = strlen(word) - 1;
		//if (word[pos_slash] == '\n')
			//word[pos_slash] = '\0';

		// добавляем в дерево
		node = create_node(word);
		if (node)
			root = insert_in_tree(root, node);
		else 
			return NULL;
	}
	return root;
}

// очистка дерева
void free_tree(struct tree_node **root)
{
	if (*root == NULL)
		return;
	
	struct tree_node *copy_root = *root;
	free((void*)(*root)->word);
	free(*root);
	free_tree(&copy_root->left);
	free_tree(&copy_root->right);
	*root = NULL;
}

// поиск в дереве
struct tree_node* lookup_in_tree(struct tree_node *root, const char *word, int *count)
{
    int cmp;
    
    // искомый элемент отсутствует
    if (root == NULL)
    {
        (*count)++;
        return NULL;
    }

    cmp = strcmp(word, root->word);
    (*count)++;
    if (cmp == 0)
        return root;  // возвращаем указатель 
    else if (cmp < 0)
        return lookup_in_tree(root->left, word, count);
    else
        return lookup_in_tree(root->right, word, count);
}

// перевести строку в число
int str_to_int(const char *str, int *n)
{
    if (str == NULL)
        return _IOREAD;
    
    int len_s = strlen(str);
    int j = 0;
    int sign = 1;
    *n = 0;
    
    if (str[j] == '-')
    {
        j = 1;
        sign = -1;
    }
    if (str[j] == '+')
        j = 1;
    
    if (j == len_s)
        return _IOREAD;
    
    for (int i = j; i < len_s; i++)
        if (str[i] >= '0' && str[i] <= '9')
        {
            *n += str[i] - '0';
            if (i != len_s - 1)
                *n *= 10;
        }
        else
            return _IOREAD;    
   
    *n = *n * sign;
    return OK;
}

// считываем целое число в диапазоне
int read_int(const char *input, const char *err, int begin, int end)
{
    int num = 0;
    char buff[MAX_CHAR];
    int code = _IOREAD;
    while ((code == _IOREAD) || (num < begin) || (num > end))
    {
        printf("\n%s", input);
        gets(buff);
        code = str_to_int(buff, &num);
        if ((code == _IOREAD) || (num < begin) || (num > end))
            printf("%s\n\n", err);
    }
    return num;
}

void print_binary_knot(struct tree_node *head)
{
	if (head)
	{
		printf("\nFINDING KNOT \n");
		printf("\tadress %p \n", head);
		printf(" \tdata %s\n", head->word);
		printf("\n left                right");
		printf("\n %16p   %16p", head->left, head->right);
		if (head->left)
			printf("\n %16s ", head->left->word);
		else
			printf("\n           ");
		if (head->right)
			printf("  %16s\n", head->right->word);
		else
			printf("\n\n");
	}
	else 
		printf("\nthere are no knot with this name\n");
}

//______________________________________________________________________________________________hash open


struct htype
{
	char val[MAX_CHAR]; /* значение элемента данных */
	struct htype *next; /* указатель на следующий элемент цепочки */
};

//struct htype *index[MAX];

void init(struct htype* index[MAX]) 
{
	int i;
	for(i = 0; i < MAX; i++)
	{
		index[i] = NULL; /* хеш-таблица (массив начал цепочек) */
	}
}

int h_code(char *value)
{
	char *k =value;
	int res = 0;
	while( *k != 0)
	{
		res += *k;
		k++;
	}
	return res % HASH_DEL;
}

struct htype *create_hash(char *val)
{
	struct htype *head = malloc(sizeof(struct htype));
	//printf("%p ", head);
	if (head)
	{
		//printf(" %s ", val);
		strcpy(head->val, val);
		//printf("48 val %s", head->val);
		//printf("sd");
		head->next = NULL;
	}
	return head;
}

void adding_open_hash(struct htype**index, struct htype*new)
{
	int k = h_code(new->val);
	//printf("val - %s\n", new->val);
	if (index[k] != NULL)
	{
		struct htype* p = index[k];
		while (p->next)
		{
			p = p->next;
		}
		p->next = new;
	}
	else
		index[k] = new;
}


struct htype *search_open(struct htype **index, char *k, int *cmp) 
{
	int h = h_code(k);
	struct htype *p;
	
	// поиск ключа k 
	if(index[h] != NULL) 
	{
		//(*cmp)++;
		p = index[h];
		do 
		{
			(*cmp)++;
			if(strcmp(k, p->val) == 0) 
				return p;
			else p = p->next;
		} while (p != NULL);
	return NULL;
	}
	
	return NULL;
}



void print_open_hash(struct htype **index)
{
	for (int k = 0; k < MAX; k++)
	{
		if (index[k])
		{
			printf("%d ", k);
			for (struct htype *p = index[k]; p; p = p->next)
				printf("  %s", p->val);
			printf("\n");
		}
	}
	
}

int scan_to_open_hash(FILE *stream, struct htype **index)
{
	char buf[MAX_CHAR];
	struct htype* cur;
	int c;
	int cmp = 0;
	while ((c = fscanf(stream, "%s", buf)) == 1)
	{
		if (!search_open(index, buf, &cmp))
		{
			cur = create_hash(buf);
			if (cur)
				adding_open_hash(index, cur);
			else
				return ERR_MEMORY;
		}
	}	
	return OK;
}

//________________________________________________________________________________________hash close


struct close_hash
{
	char val[MAX_CHAR];
};


void init_close(struct close_hash* index[MAX]) 
{
	int i;
	for(i = 0; i < MAX; i++)
	{
		index[i] = NULL; /* хеш-таблица (массив начал цепочек) */
	}
}

struct close_hash *create_close_hash(char *val)
{
	struct close_hash *head = malloc(sizeof(struct close_hash));
	//printf("%p ", head);
	if (head)
	{
		strcpy(head->val, val);
	}
	return head;
}


int adding_close_hash(struct close_hash**index, struct close_hash *new)
{
	//printf("new - %p", new);
	int k = h_code(new->val);
	//printf("val - %s\n", new->val);
	//printf("k = %d", k);
	//printf("%p \n", index[k]);
	if (index[k] != NULL)
	{
		int d = FIRST;
		while (1)
		{
			//printf("k = %d\n", (k + d*d) % HASH_DEL);
			if (index[(k + d) % HASH_DEL] == NULL)
			{
				index[(k + d) % HASH_DEL] = new;
				break;
			}
			k += d;
			d += STEP;
			if (d > OVER)
			{
				//printf("sdsdsd");
				return -1;
				//assert(0);
			}
				
		}
	}
	else
		index[k] = new;
	
	return 0;
}

void printf_close_hash(struct close_hash **index)
{
	for(int k = 0; k < MAX; k++)
		if (index[k])
			printf("%d  %s\n", k, index[k]->val);
}

struct close_hash *search_close(struct close_hash **index, char *k, int *cmp) 
{
	int h = h_code(k);
	//struct close_hash *p;
	
	// поиск ключа k 
	if(index[h] != NULL) 
	{
		(*cmp)++;
		if (strcmp(index[h]->val, k) == 0)
			return index[h];
		
		for (int n = FIRST; n < OVER; n+=STEP)
		{
			(*cmp)++;
			if ( index[(h + n) % HASH_DEL] && (strcmp(index[(h + n) % HASH_DEL]->val, k) == 0))
			{
				return index[(h + n) % HASH_DEL];
				//h += n;
			}
			h += n;
		}
		return NULL;
		
	}
	
	return NULL;
}


int scan_to_close_hash(FILE *stream, struct close_hash **index)
{
	char buf[MAX_CHAR];
	struct close_hash* cur;
	int c;
	int cmp = 0;
	while ((c = fscanf(stream, "%s", buf)) == 1)
	{
		if (search_close(index, buf, &cmp) == 0)
		{
			cur = create_close_hash(buf);
			if (cur)
			{
				if ( -1 == adding_close_hash(index, cur))
					return -1;
			}
			else
				return ERR_MEMORY;
		}
	}	
	return OK;
}

int count_close(struct close_hash**index)
{
	int n = 0;
	for (int k = 0; k < MAX; k++)
		if (index[k] != 0)
			n++;
	return n;
}


unsigned long long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__("rdtsc" : "=A" (d) );
    return d;
}


void iter_comparison(FILE *in)
{
	size_t t1 = 0, t2 = 0, time1 = 0, time2 = 0, time3 = 0, time4 = 0; 
	size_t t01 = 0, t02 = 0, t03 = 0, t04 = 0;
	//int cmp1 = 0, cmp2 = 0, cmp3 = 0 , cmp4 = 0;
	char choice[50];// = "the";
	
	struct tree_node *root = NULL;
	fseek(in, 0, SEEK_SET);
	root = init_tree(in, root);
	
	struct avl_tree *head = NULL;
	fseek(in, 0, SEEK_SET);
	head = scan_file_avl(in, head);
	
	struct htype *index1[MAX];
	init(index1);
	fseek(in, 0, SEEK_SET);
	scan_to_open_hash(in, index1);
	
	struct close_hash *index[MAX];
	init_close(index);
	fseek(in, 0, SEEK_SET);
	scan_to_close_hash(in, index);
	
	fseek(in, 0, SEEK_SET);
	int count = 0;
	int cmp;
	while(fscanf(in, "%s", choice) != EOF)
	{
		time1 = 0;
		time2 = 0;
		time3 = 0;
		time4 = 0;
		int n = 50;
		for (int k = 0; k< n; k++)
		{
			cmp = 0;
			t1 = tick();
			lookup_in_tree(root, choice, &cmp);
			t2 = tick();
			
			
			time1 += t2 - t1;
			
			cmp = 0;
			t1 = tick();
			find_avl_knot(head, choice, &cmp);
			t2 = tick();
			
			time2 += t2 - t1;
			
			cmp = 0;
			t1 = tick();
			search_open(index1, choice, &cmp);
			t2 = tick();
			
			time3 += t2 - t1;
			
			cmp = 0;
			t1 = tick();
			search_close(index, choice, &cmp);
			t2 = tick();
			time4 += t2 - t1;
		}
		t01 += time1 / n;
		t02 += time2 / n;
		t03 +=  time3 / n;
		t04 += ( time4 / n);
		count+=1;
	}
	printf("%5d  %10d %10d %10d %10d\n", root->count, (int)t01 / count, (int) t02 / count, (int) t03 / count, (int) t04 / count );
}

void comparison(void)
{
	printf("number      binery      AVL    openhash      closehash \n");
	{
		FILE *f = fopen("test1.txt", "r");
		iter_comparison(f);
		fclose(f);
	}
	{
		FILE *f = fopen("test2.txt", "r");
		iter_comparison(f);
		fclose(f);
	}
	{
		FILE *f = fopen("test3.txt", "r");
		iter_comparison(f);
		fclose(f);
	}
	{
		FILE *f = fopen("test4.txt", "r");
		iter_comparison(f);
		fclose(f);
	}
	{
		FILE *f = fopen("test5.txt", "r");
		iter_comparison(f);
		fclose(f);
	}
}


int main ()
{
	setbuf(stdout, NULL);
	
	struct tree_node *root = NULL;
    struct tree_node *node = NULL;
    char word[MAX_CHAR];
	int res = OK;
	char choice[MAX_CHAR];
	unsigned long long t1, t2, time;  // измерение времени
	struct tree_node *find_t = NULL;  // указатель на слово для поиска в дереве
	int count = 0;
	FILE * data_out = NULL;           // файл для записи данных графа

	FILE *in = fopen("source.txt", "r+");
	if (in)
	{
		while (1)
		{
			printf("0 - exit\n");
			printf("1 - binary tree\n");
			printf("2 - AVL tree\n");
			printf("3 - hash open hash\n");
			printf("4 - hash close\n");
			printf("5 - comparison\n");
			printf("Choice : ");
			fgets(choice, MAX_CHAR, stdin);
			if (strlen(choice) == 2)
			{
				if (choice[0] == '0')
					break;
				else if (choice[0] == '1')   //дерево двоичного поиска
				{
					printf("binery tree\n\n");
					fseek(in, 0, SEEK_SET);
					root = init_tree(in, root); 
					while (1)
					{
						printf("\n\t0 - exit\n");
						printf("\t1 - add word\n");
						printf("\t2 - find knot\n");
						printf("\t3 - import to dot file\n");
						printf("Choice : ");
						fgets(choice, MAX_CHAR, stdin);
						if (strlen(choice) == 2)
						{
							if (choice[0] == '0')
							{
								break;
							}
							else if (choice[0] == '1')
							{
								fprintf(stdout, "\nInput the word to add: ");
								gets(word);
								node = create_node(word);
								if (node)
								{
									root = insert_in_tree(root, node);   // добавили в дерево
									fprintf(in, "%s\n", word);       // добавили в файл
									fprintf(stdout, "\n-----> The word is added.");
								}
								else
								{
									printf("Error of memory\n");
									choice[0] = '0';
								}
							}
							else if (choice[0] == '2')
							{
								fprintf(stdout, "\nInput the word to search in the tree: ");
								gets(word);
								count = 0;
								t1 = tick();
								find_t = lookup_in_tree(root, word, &count);
								t2 = tick();
								time = t2 - t1;
								fprintf(stdout, "\n-----> Time of searching = %d.", (int)(time));
								fprintf(stdout, "\n-----> Count of comparisons = %d.", count);
								// результат поиска
								print_binary_knot(find_t);
								
							}
							else if (choice[0] == '3')
							{
								printf("export to dot\n\n");
								//  dot -Tpng dotfile_binary.dot -o graph_binary.png
								data_out = fopen("dotfile_binary.dot", "w"); 
								if (data_out)
								{
									export_to_dot(data_out, root);
									fprintf(stdout, "\n-----> DOT-file is created. Please run GraphViz.");
									fclose(data_out);
								}
								else
								{
									printf("Error of open file\n");
									choice[0] = '0';
								}
							}
							else 
								printf("uncorrect point of menu\n\n");
						}
						else 
							printf("uncorerct point of menu\n\n");
					}
				}
				else if (choice[0] == '2')
				{
					printf("AVL\n\n");
					struct avl_tree *head = NULL;
					fseek(in, 0, SEEK_SET);
					head = scan_file_avl(in, head);
					while (1)
					{
						//to_s_avl(head, 0);
						printf("\n\t0 - exit\n");
						printf("\t1 - add word\n");
						printf("\t2 - find knot\n");
						printf("\t3 - import to dot file\n");
						printf("Choice : ");
						fgets(choice, MAX_CHAR, stdin);
						if (strlen(choice) == 2)
						{
							if (choice[0] == '0')
							{
								// надо удвление добавить
								break;
							}
							else if (choice[0] == '1')
							{
								printf("adding\n\n");
								printf("input one word: ");
								scanf("%s", choice); // пока что
								fflush(stdin);
								if (!have_simple_avl(head, choice))
								{
									head = insert(head, choice);
								}
								else
									printf("this word is exist in tree\n\n");
							}
							else if (choice[0] == '2')
							{
								printf("find knot \n\n");
								printf("\ninput name of knot\n");
								printf("input one word: ");
								scanf("%s", choice); // пока что
								fflush(stdin);
								
								int cmp = 0;
								t1 = tick();
								struct avl_tree *nod = find_avl_knot(head, choice, &cmp);
								t2 = tick();
								time = t2 - t1;
								fprintf(stdout, "\n-----> Time of searching = %d.", (int)(time));
								fprintf(stdout, "\n-----> Count of comparisons = %d.", cmp);
								print_avl_knot(nod);
							}
							else if (choice[0] == '3')
							{
								printf("export to dot\n\n");
								//  dot -Tpng dotfile_avl.dot -o graph_avl.png
								FILE *out = fopen("dotfile_avl.dot", "w");
								if (out)
								{
									export_to_dot_avl(out, head);
									fclose(out);
								}
							}
							else 
								printf("uncorrect point of menu\n\n");
						}
						else 
							printf("uncorerct point of menu\n\n");
					}
				}
				else if (choice[0] == '3')
				{
					printf("hash open hash\n\n");
					struct htype *index[MAX];
					init(index);
					fseek(in, 0, SEEK_SET);
					scan_to_open_hash(in, index);
				
					while (1)
					{
						print_open_hash(index);
						printf("\n\t0 - exit\n");
						printf("\t1 - add word\n");
						printf("\t2 - find knot\n");
						printf("Choice : ");
						fgets(choice, MAX_CHAR, stdin);
						if (strlen(choice) == 2)
						{
							if (choice[0] == '0')
							{
								break;
							}
							else if (choice[0] == '1')
							{
								printf("add\n\n");
								printf("input one word: ");
								scanf("%s", choice); // пока что
								fflush(stdin);
								int cmp = 0;
								if (!search_open(index, choice, &cmp))
								{
									adding_open_hash(index, create_hash(choice));
								}
								else
									printf("this word is exist in tree\n\n");
							}
							else if (choice[0] == '2')
							{
								printf("find\n\n");
								printf("input one word: ");
								scanf("%s", choice); // пока что
								fflush(stdin);
								int cmp = 0;
								t1 = tick();
								struct htype *find =(search_open(index, choice, &cmp));
								t2 = tick();
								time = t2 - t1;
								fprintf(stdout, "\n-----> Time of searching = %d.", (int)(time));
								fprintf(stdout, "\n-----> Count of comparisons = %d.", cmp);
								if (find)
									printf("\nFINDED:\n %p \n %s\n\n", find, find->val);
								else 
									printf("\nthere are no this word\n");
							}
							else 
								printf("uncorrect point of menu\n\n");
						}
						else 
							printf("uncorrect point of menu\n\n");
						
					}
				}
				else if (choice[0] == '4')
				{
					printf("hash close\n\n");
					struct close_hash *index[MAX];
					init_close(index);
					fseek(in, 0, SEEK_SET);
					scan_to_close_hash(in, index);
					while (1)
					{
						printf_close_hash(index);
						printf("\n\t0 - exit\n");
						printf("\t1 - add word\n");
						printf("\t2 - find knot\n");
						printf("Choice : ");
						fgets(choice, MAX_CHAR, stdin);
						if (strlen(choice) == 2)
						{
							if (choice[0] == '0')
							{
								break;
							}
							else if (choice[0] == '1')
							{
								printf("add");
								printf("input one word: ");
								scanf("%s", choice); // пока что
								fflush(stdin);
								int cmp = 0;
								if (search_close(index, choice, &cmp) == 0)
								{
									adding_close_hash(index, create_close_hash(choice));
								}
									
							}
							else if (choice[0] == '2')
							{
								printf("ind");
								printf("input one word: ");
								scanf("%s", choice); // пока что
								fflush(stdin);
								int cmp = 0;
								t1 = tick();
								struct close_hash* f = search_close(index, choice, &cmp);
								t2 = tick();
								time = t2 - t1;
								fprintf(stdout, "\n-----> Time of searching = %d.", (int)(time));
								fprintf(stdout, "\n-----> Count of comparisons = %d.", cmp);
								if (f)
									printf("\nSEARCHED:\n %p \n %s\n\n", f, f->val);
								else
									printf("\nthere is no this word \n\n");
							}
							else
								printf("uncorrect point of menu\n\n");
						}
						else 
							printf("uncorrect point of menu\n\n");
					}
				}
				else if (choice[0] == '5')
				{
					printf("comparison \n\n");
					comparison();
				}
				else
					printf("uncorect point of menu\n\n");
			}
			else
				printf("uncorrect point of menu\n\n");
			
		}
		fclose (in);
	}
	else
	{
		printf("uncprrect source file \n");
		res = ERR_FILE;
	}
	
	return res;
}


