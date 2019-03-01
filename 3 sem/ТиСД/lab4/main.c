#include "queue_array.h"
#include "queue_list.h"
#include "timetest.h"
#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <time.h>

int main(void)
{
    int64_t realtime1, realtime2, realtime;
    setbuf(stdout, NULL);
    int choice, flag = 2;
    int t1_in = 0, t2_in = 6, t1_w = 0, t2_w = 1;
    int temp1, temp2;
    int dequeued = 1000;
    while(1)
    {
        printf("------------------------------------------------------------\n");
        printf("|         Выберите вариант моделирования очереди            |\n");
        printf("------------------------------------------------------------\n");
        printf("|1 - массив, 2 - список                                     |\n");
        printf("|3 - изменить время поступления заявок в очередь            |\n");
        printf("|4 - изменить время обработки заявок                        |\n");
        printf("|5 - сравнить время реализаций                              |\n");
        printf("|6 - выход из программы                                     |\n");
        printf("------------------------------------------------------------\n");
        printf("Выбор: ");
        if(scanf("%d", &choice))
        {
            if(choice == 1)
            {
                arr_work(dequeued, t1_in, t2_in, t1_w, t2_w);
            }
            else if(choice == 2)
            {
                printf("Выводить данные о фрагментации? 1 - да, 2 - нет\n");
                scanf("%d", &flag);
                ll_work(dequeued, t1_in, t2_in, t1_w, t2_w, flag);
            }
            else if(choice == 3)
            {
                printf("Введите границы времен поступления заявок в очередь\n");
                printf("Ввод в одну строку через пробел\n");
                if(scanf("%d %d", &temp1, &temp2) != 2)
                {
                    printf("Неверный тип введенных данных\n");
                    scanf("%*c");
                    continue;
                }
                else
                {
                    t1_in = temp1;
                    t2_in = temp2;
                    printf("Время изменено\n");
                }
            }
            else if(choice == 4)
            {
                printf("Введите границы времен обработки заявок\n");
                printf("Ввод в одну строку через пробел\n");
                if(scanf("%d %d", &temp1, &temp2) != 2)
                {
                    printf("Неверный тип введенных данных\n");
                    scanf("%*c");
                }
                else
                {
                    t1_w = temp1;
                    t2_w = temp2;
                    printf("Время изменено\n");
                }
            }
            else if(choice == 5)
                timetest();
            else if(choice == 6)
            {
                printf("Выход из программы");
                return 0;
            }
            else
            {
                printf("Такой команды нет\n\n\n");
                scanf("%*c");
            }
        }
        else
        {
            printf("Такой команды нет\n\n\n");
            scanf("%*c");
        }
    }
    return 0;
}