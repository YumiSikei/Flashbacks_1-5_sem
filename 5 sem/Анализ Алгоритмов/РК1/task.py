import copy
from random import randint
from math import factorial

from graph_stepen_2 import prov_st_2, generation_stepen_two 
from graph_dvudolnii import prov_dv, generation_dvudolnii 



def extend(candidates, not_, dugs):
    #print('candidates ', candidates)
    #print('not ', not_)
    
    #проверка, нет ли в not_ вершины, соедененной со всеми вершинами в candidates
    for i in range(len(not_)):
        n = 0
        for j in range (len(dugs)):
            if dugs[j][0] == not_[i] or dugs[j][1] == not_[i]:
                #если имеется дуга с вершиной из not_, проверяем соединяет ли она с вершиной из кандидатов
                for k in range (len(candidates)):
                    if dugs[j][0] == candidates[k] or dugs[j][1] == candidates[k]:
                        n += 1
        if n == len(candidates):
            return not_

    while len(candidates) > 0:
        candidat_not = len(candidates)
        #в кандидатах ищем вершину, не соединенную ни с одной из not_
        for i in range (len(candidates)):
            n = 0
            for j in range (len(dugs)):
                if dugs[j][0] == candidates[i] or dugs[j][1] == candidates[i]:
                    for k in range (len(not_)):
                        if dugs[j][0] == not_[k] or dugs[j][1] == not_[k]:
                            n += 1
            if n == 0:
                candidat_not = i
                break

        if candidat_not == len(candidates):
            return not_
        else:
            #переформировываем кандидатов и использованные вершины
            not_.append(candidates[candidat_not])
            candidates.remove(candidates[candidat_not])
            if len(candidates) == 0:
                return not_
            else:
                not_ = extend(candidates, not_, dugs)
                return not_



def task_step_2(A, dugs):
    print('\n\nGraph  Stepen 2','  ',A)
    print('Dugs: ')
    for i in range (len(dugs)):
        print(dugs[i])
    
    combsub = [0]   #независимое множество
    not_ = [0]  #вершины, добваленные в текущий варинт нез. множества
    empty = []  #вершины без дуг
    k = 0
    n = 0
    for i in range(len(A)):
        if A[i] == 0:
            empty.append(i)
            
    max_combsub = []  #максимальное независимое множество
            
    if len(dugs) == 0:   #проверка, есть ли дуги у графа
        max_combsub = empty
    else:
        for i in range(len(A) - 1):
            #берем первую вершину с дугой(ами), которая может быть в множестве
            if A[i] > 0:
                not_[0] = i
            candidates = []    #кандидаты в независимое множество

            #находим кандидатов-вершин в множество, которые не имеют дуг с первой вершиной
            for k in range(len(dugs)):
                if (dugs[k][0] != not_[0]) and (dugs[k][1] != not_[0]):
                    #смотрим, не добавили ли какую-либо вершину из дуги уже
                    if len(candidates) > 0:
                        can = 0
                        for j in range (len(candidates)):
                            if candidates[j] == dugs[k][0]:
                                can = 1 
                        if can == 0:
                            candidates.append(dugs[k][0])
                        else:
                            can = 0
                            for j in range (len(candidates)):
                                if candidates[j] == dugs[k][1]:
                                    can = 1
                            if can == 0:
                                candidates.append(dugs[k][1])
                                
                    else:
                        candidates.append(dugs[k][0])

            #вызываем рекурсивную функцию, которая будет пополнять текущий вариант независимого множества
            combsub = extend(candidates, not_, dugs)

            if i == 0 or len(max_combsub) < len(combsub):
                max_combsub = copy.copy(combsub)

    for i in range(len(empty)):
        max_combsub.append(empty[i])
    print('\nMax combination :', max_combsub)


task_dvudol(group, A, dugs):
    print('\n\nGraph  Dvudolnii','  ',A)
    print('Dugs: ')
    n_1 = 0
    n_2 = 0
    for i in range (group):
        if group[i] = 1:
            n_1 += 1
        else:
            n_2 += 1
    n_max = max(n_1, n_2)
    


Dvudol_group, dvudol, dvudol_dugs, dvudol__n_dugs = generation_dvudolnii()
Stepen_2, stepen_2_dugs, stepen_2__n_dugs = generation_stepen_two()


task(Dvudol_group, dvudol, dvudol_dugs)
task(Stepen_2, stepen_2_dugs)
