#include "interface.h"
#include "graph.h"

/*Задана система двусторонних дорог.
 Для каждой пары городов найти длину кратчайшего пути между ними.*/

 /*Для поиска кратчайших путей между всеми вершинами используется алгоритм Флойда-Уоршалла. 
 По алгоритму Флойда-Уоршалла сначала ищется кратчайший путь от одной вершины ко всем вершинам,
  доступным из нее, затем проводятся те же действия, но пытаясь пройти от этой вершины ко всем 
  доступным из нее, проходя каждый раз через новую вершину (сначала через первую, затем – через вторую и т.д.). 
  Таким образом обрабатываются все вершины. [2].*/

int main(void)
{
    FILE *fin = fopen("input.txt", "r");
    memory_check(fin, EXIT_FAILURE, "File opening failure!");
    unsigned long long t1;
	setbuf(stdout, NULL);
	fflush(stdin);

    int menu = 0;
	int flag = 1;
	matr *graph = read_matr(fin);
	memory_check(graph, EXIT_FAILURE, "Error!");
    matr *best = NULL;
	do
	{
		puts("\nMENU:");
		puts(" 1 - Show graph");
		puts(" 2 - Get best routs");
		puts(" 3 - Exit");
		menu = menu_value();
		switch(menu)
		{
			case 1:
                show_matr_gv(graph);
                puts("Check graph.png");
                puts("Graph matrix");
                print_matr(stdout, graph);
                break;
            case 2:
                free_matr(best);
                t1 = tick();
                best = floyd_warshall(graph);
                printf("\nFinding time of the best roots(in ticks): %llu\n", tick()-t1);
                puts("Best roots matrix");
                print_matr(stdout, best);
				int minsum = 0;
				int mini = 0;
				for (int i = 0; i < best->n; i++)
					minsum += best->data[0][i];
				int sum;
				for (int i = 1; i < best->n; i++)
				{
					sum = 0;
					for (int j = 0; j < best->n; j++)
						sum += best->data[i][j];
					if (sum < minsum)
					{
						mini = i;
						minsum = sum;
					}
				}
				fprintf(stdout, "City with best sum is %d\n\n", mini);
                show_best_gv(best, graph);
                puts("Check graph.png");
                break;
            case 3:
                flag = 0;
                break;
            default:
                puts("Unknown operation.");
                break;
		}
	} while (flag);

	free_matr(graph);
	free_matr(best);
    fclose(fin);
	return EXIT_SUCCESS;
}
