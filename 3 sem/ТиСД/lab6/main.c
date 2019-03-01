#include "func.h"

unsigned long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d) );
    return d;
}

int main(void)
{
    //SetConsoleOutputCP(1251); //установка кодовой страницы win-cp 1251 в поток вывода
    char str[15];
    char file_name[20];
    struct Tree_list Tree;

    FILE *f;
    int add_or_not = 1;

    Tree.Data.Count = 0;
   // strcpy(Tree.Data.Word, "str");
    Tree.Left = NULL;
    Tree.Right = NULL;

    int choise = 1;
    int first_input;
    int count;
	
    setbuf(stdout, NULL);
	fflush(stdin);

    long int t1, t2;
    while (choise)
    {
        printf("\n********************************************************************************\n");
        printf("\n   !!!   WARNING !!! The words in the file can only be in English \n");
        printf("\n   1 - Input data from file\n");
        printf("   2 - Output tree\n");
        printf("   3 - Search in tree\n");
        printf("   4 - Search in file\n");
		printf("   5 - Obhod\n");
		printf("   6 - Compare time\n");
        printf("   7 - Delete element\n");
        printf("\n   0 - Exit\n");
        printf("\n********************************************************************************");
        printf("\nChoise option: ");
        if (scanf("%d", &choise) == 1)
            switch (choise) {
            case 0:
                printf("\nEXITING...\n");
                break;
            case 1:

                printf("\n    Input file name: ");
                scanf("%s", file_name);

                f = fopen(file_name, "r");

                if(f)
                    input_file(&Tree, f);
                else
                    printf("\n  Error: filename error \n");

                break;
            case 2:
                if(Tree.Data.Count)
                {
                    printf("\n  Output Tree \n");
                    printf("A tree 'lies' on its side, the right branch goes up and the left - down\n\n\n");
                    output_tree(&Tree, "", "");
                }
                else
                {
                    printf("\n  Error:  Empry Tree \n");
                }
                break;
            case 3:
                if(Tree.Data.Count)
                {
                    printf("\n  Input word for searching: ");
                    scanf("%s", str);

                    t1 = tick();
                    if(search(&Tree, str) == NOT_FIND)
                    {
                        t2 = tick();
                        printf("\n  Ticks: %ld", t2 - t1);
                        printf("\n  Element not found\n  Would you like to add element?\n");
                        printf("    1 - yes\n    2 - no\n");
                        printf("Choise: ");
                        if(scanf("%d", &add_or_not) == 1)
                        {
                            if(add_or_not == 1)
							{
                                insert(&Tree, str);
								fclose(f);
								fopen(file_name, "a");
								fprintf(f, "\n%s", str);
								fclose(f);
								fopen(file_name, "r");
							}
                        }
                        else
                        {
                            gets(str);
                            printf("Error input, element not added");
                        }
                    }
                    else
                    {
                        t2 = tick();
                        printf("\n  Ticks: %ld", t2 - t1);
                        printf("\n  Element found, Answer mark <--- \n");
                        output_tree(&Tree, "", str);
                    }
                }
                else
                {
                    printf("\n  Error:  Empry Tree \n");
                }
                break;
            case 4:
                if(Tree.Data.Count)
                {
                    printf("\n  Input word for searching: ");
                    scanf("%s", str);
                    t1 = tick();
                    count = search_in_file(f, str, &first_input);
                    t2 = tick();

                    printf("\n  Ticks: %ld", t2 - t1);
                    if(count > 0)
                    {
                        printf("\n     Element found. First input in %d word, count %d", first_input, count);
                    }
                    else
                    {
                        printf("\n  Element not found\n  Would you like to add element?\n");
                        printf("    1 - yes\n    2 - no\n");
                        printf("Choise: ");
                        if(scanf("%d", &add_or_not) == 1)
                        {
                            if(add_or_not == 1)
							{
                                insert(&Tree, str);
								fclose(f);
								fopen(file_name, "a");
								fprintf(f, "\n%s", str);
								fclose(f);
								fopen(file_name, "r");
							}
                        }
                        else
                        {
                            gets(str);
                            printf("Error input, element not added");
                        }
                    }
                }
                else
                {
                    printf("\n  Error:  File not open \n");
                }
                break;
			case 5:
				printf("infix:\n\n");
				apply_in(&Tree, func);
				printf("\npostfix\n\n");
				apply_post(&Tree, func);
				printf("\nprefix\n\n");
				apply_pre(&Tree, func);
				
				break;
			case 6:
				if(Tree.Data.Count)
                {
					char str[30] = "search";
                    t1 = tick();
                    search(&Tree, str);
					t2 = tick();
					printf("\n Search in Tree (Ticks): %ld\n", t2 - t1);
					
					t1 = tick();
                    search_in_file(f, str, &first_input);
					t2 = tick();
					printf("\n Search in file (Ticks): %ld\n", t2 - t1);
                }
                else
                {
                    printf("\n  Error:  Empry Tree \n");
                }
			
				break;
            case 7:
                printf("\n  Input word for deleting: ");
                scanf("%s", str);
                delete_tree(&Tree, str);

                break;

            default:
                printf("\nUnknown option\n");
            }
        else
        {
            printf("\nUnknown option\n");
            scanf("%s", str);
            //break;
        }
    }
}

