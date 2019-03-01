#include "graph.h"
#include <math.h>

void free_matrix_rows(float **data, int n)
{
    for (int i = 0; i < n; i++)
       free(data[i]);

    free(data);
}

float **allocate_matrix_rows(int n)
{
    int m = n;
    float **data = (float **)calloc(n, sizeof(float*));
    if (!data)
    {
        panic("Memory allocation failure in allocate_matrix_rows #1.");
        return NULL;
    }

    for (int i = 0; i < n; i++)
    {
        data[i] = (float *)calloc(m, sizeof(float));
	if (!data[i])
        {
            free_matrix_rows(data, n);
            panic("Memory allocation failure in allocate_matrix_rows #2.");
            return NULL;
        }
    }

    return data;
}

matr *create_matr(unsigned int n)
{
	matr *res = (matr *)malloc(sizeof(matr));
	if (!res)
    {
        panic("Memory allocation failure in create_matr #1.");
		return NULL;
    }
	res->data = allocate_matrix_rows(n);
	if (!res->data)
	{
        panic("Memory allocation failure in create_matr #2.");
		free(res);
		return NULL;
	}
	res->n = n;
	return res;
}

matr *read_matr(FILE *f)
{
	rewind(f);
    unsigned int n;
    if (fscanf(f, "%u", &n) != 1)
    {
        panic("Read error while reading size of matr.");
        return NULL;
    }
    matr *res = create_matr(n);
    float tmp = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (fscanf(f, "%f", &tmp) != 1)
            {
                panic("Read error while reading matr.");
                return NULL;
            }
            res->data[i][j] = tmp;
        }
    }
    return res;
}

void print_matr(FILE *f, const matr *m)
{
    if (m != NULL)
    {
        for (int i = 0; i < m->n; i++)
        {
            for (int j = 0; j < m->n; j++)
            {
                fprintf(f, "%5.2f ", m->data[i][j]);
            }
            putc('\n', f);
        }
    }
    else
        fprintf(f, "It's empty!\n");
}

void free_matr(matr *matrix)
{
    if (matrix != NULL)
	{
        free_matrix_rows(matrix->data, matrix->n);
        free(matrix);
    }
}

matr *copy_matr(const matr *A)
{
    if (A != NULL)
	{
		matr *C = create_matr(A->n);
		memory_check(C, NULL, "Memory error!");
		memory_check(C->data, NULL, "Memory error!");

		C->n = A->n;
		C->n = A->n;
		for (int i = 0; i < A->n; ++i)
			for (int j = 0; j < A->n; ++j)
				C->data[i][j] = A->data[i][j];
		return C;
	}
	else
	{
		return NULL;
	}
}

matr *floyd_warshall(const matr *A)
{
    matr *res = copy_matr(A);
    memory_check(res, NULL, "Error!");
    for (int k = 0; k < A->n; k++)
    {
        for (int i = 0; i < A->n; i++)
        {
            for (int j = 0; j < A->n; j++)
            if (i != j)
            {
                res->data[i][j] = fmin(res->data[i][j], res->data[i][k]+res->data[k][j]);
            }
            else
                res->data[i][j] = 0.0;
        }
    }
    return res;
}

void show_matr_gv(const matr *a)
{
    if (a == NULL)
        return;
    FILE *f = fopen("output.gv", "w");
    memory_check(f, , "File open failure!");
    fprintf(f, "digraph My_graph {\n");
    for (int i = 0; i < a->n; i++)
        for (int j = 0; j < a->n; j++)
        {
            if (a->data[i][j] < INFINIT && a->data[i][j] != 0)
                fprintf(f, "%d -> %d [label=\"%.2f km\"];\n", i, j, a->data[i][j]);
        }
    fprintf(f, "}\n");
    fclose(f);
	puts("put this commands in cmd");
    puts("dot -Tpng output.gv -o graph.png");
    puts("open *.png");
}

void show_best_gv(const matr *a, const matr *not_best)
{
    if (a == NULL)
        return;
    FILE *f = fopen("output.gv", "w");
    memory_check(f, , "File open failure!");
    fprintf(f, "digraph My_graph {\n");
    for (int i = 0; i < a->n; i++)
        for (int j = 0; j < a->n; j++)
        {
            if (a->data[i][j] < INFINIT && a->data[i][j] != 0) // && a->data[i][j] = not_best->data[i][j])
                fprintf(f, "%d -> %d [label=\"%.2f km\"];\n", i, j, a->data[i][j]);
        }
    fprintf(f, "}\n");
    fclose(f);
	puts("put this commands in cmd");
    puts("dot -Tpng output.gv -o graph.png");
    puts("open *.png");
}

