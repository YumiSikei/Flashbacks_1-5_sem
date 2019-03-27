import copy
from random import randint
from math import factorial

from random import randint
from math import factorial

def prov(mas, v1, v2):
    for i in range (len(mas)):
        if (mas[i][0] == v1 and mas[i][1] == v2) or (mas[i][1] == v1 and mas[i][0] == v2):
            return 0
    return 1

def generation_dvudolnii():

    dvudol = [0]* randint(2, 10) #массив для обозначения части вершин

    #ищем первые элементы в каждую группу
    n1 = randint(0, len(dvudol) - 1)
    dvudol[n1] = 1
    n2 = randint(0, len(dvudol) - 1)
    while n2 == n1:
        n2 = randint(0, len(dvudol) - 1)
    dvudol[n2] = 2

    n_1 = 0
    for i in range (len(dvudol)):
        if dvudol[i] == 0:
            dvudol[i] = randint(1,2)
        if dvudol[i] == 1:
            n_1 += 1
    n_2 = len(dvudol) - n_1

    dvudolnii = [0] * len(dvudol)
    dugs = randint(0, n_1 * n_2)
    if dugs > 0:
        dvudol_dugs = [0] * dugs
        for i in range (dugs):
            dvudol_dugs[i] = [0] * 2
    else:
        dvudol_dugs = []

    for i in range(dugs):
        v1 = randint(0, len(dvudolnii) - 1)
        while (dvudol[v1] == 1 and dvudolnii[v1] == n_2) or (dvudol[v1] == 2 and dvudolnii[v1] == n_1):
            v1 = randint(0, len(dvudolnii) - 1)
            
        v2 = randint(0, len(dvudolnii) - 1)
        while dvudol[v2] == dvudol[v1] or prov(dvudol_dugs, v1, v2) == 0:
            v2 = randint(0, len(dvudolnii) - 1)

        dvudol_dugs[i][0] = v1
        dvudol_dugs[i][1] = v2
        dvudolnii[v1] += 1
        dvudolnii[v2] += 1
    

    return dvudol, dvudolnii, dvudol_dugs, dugs


def generation_stepen_two():

    stepen_2 = [0]* randint(3, 7)
    dugs = randint(0, len(stepen_2) - 1) #количество дуг
    if dugs > 0:
        stepen_2_dugs = [0]
        stepen_2_dugs[0] = [0] * 2
    else:
        stepen_2_dugs = []

    for i in range (dugs):
        v1 = randint(0, len(stepen_2) - 1)
        while stepen_2[v1] == 2:
            v1 = randint (0, len(stepen_2) - 1)
            
        v2 = randint(0, len(stepen_2) - 1)
        while v2 == v1 or stepen_2[v2] == 2 or prov(stepen_2_dugs, v1, v2) == 0:
            v2 = randint(0, len(stepen_2) - 1)

        if i > 0:
            stepen_2_dugs.append(0)
            stepen_2_dugs[i] = [0] * 2
        stepen_2_dugs[i][0] = v1
        stepen_2_dugs[i][1] = v2
        stepen_2[v1] += 1
        stepen_2[v2] += 1

    return stepen_2,stepen_2_dugs, dugs





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

def proverochka(dugs, not_, a): #проверка, есть у кандидата дуга с первой вершиной

    for i in range(len(dugs)):
        if dugs[i][0] == a or dugs[i][1] == a:
            if dugs[i][0] == not_[0] or dugs[i][1] == not_[0]:
                return 0
    return 1

def is_it_here(candidates, a):
    for i in range (len(candidates)):
        if candidates[i] == a:
            return 1
    return 0

def prov_candidates(not_, candidates, dugs):
    for i in range (len(dugs)):
        #print('  dug ', dugs[i])
        if dugs[i][0] != not_[0] and dugs[i][1] != not_[0]:
            if proverochka(dugs, not_, dugs[i][0]) == 1:
                h = is_it_here(candidates, dugs[i][0])
                if h == 0:
                    candidates.append(dugs[i][0])
            elif proverochka(dugs, not_, dugs[i][1]) == 1:
                h = is_it_here(candidates, dugs[i][1])
                if h == 0:
                    candidates.append(dugs[i][1])
        #print('      ', candidates)
    return candidates


def task(A, dugs, name_graph):
    print('\n\nGraph  ', name_graph,'  ',A)
    if len(dugs) > 0:
        print('Dugs: ')
        for i in range (len(dugs)):
            print(dugs[i])
    else:
        print('no dugs')
    
    combsub = [0]   #независимое множество

    empty = []  #вершины без дуг
    k = 0
    n = 0
    for i in range(len(A)):
        if A[i] == 0:
            empty.append(i)
    #print('\n\nEmpty   ', empty)
            
    max_combsub = []  #максимальное независимое множество
            
    if len(dugs) == 0:   #проверка, есть ли дуги у графа
        max_combsub = empty
    else:
        for i in range(len(A) - 1):
            #print('\n   ', i, ' try')

            not_ = [0]  #вершины, добавленные в текущий варинт нез. множества
            
            #берем первую вершину с дугой(ами), которая может быть в множестве
            if A[i] > 0:
                not_[0] = i
                #print('not ', not_)
            else:
                continue
            candidates = []    #кандидаты в независимое множество

            #находим кандидатов-вершин в множество, которые не имеют дуг с первой вершиной
            candidates = prov_candidates(not_, candidates, dugs)
            #print('candidates ', candidates)
                        
            #вызываем рекурсивную функцию, которая будет пополнять текущий вариант независимого множества
            combsub = extend(candidates, not_, dugs)
            print('combsub ', combsub)

            if i == 0 or len(max_combsub) < len(combsub):
                max_combsub = copy.copy(combsub)

        for i in range(len(empty)):
            max_combsub.append(empty[i])
            
    if len(max_combsub) == 0:
        print('\nCombination is none')
    else:
        print('\nMax combination :', max_combsub)


def task_dvudol(group, A, dugs):
    print('\n\nGraph  Dvudolnii','  ',A)
    print('Group: ', group)
    print('Dugs: ')
    for i in range (len(dugs)):
        print(dugs[i])
        
    n_1 = 0
    n_2 = 0
    for i in range (len(group)):
        if group[i] == 1:
            n_1 += 1
        else:
            n_2 += 1
    n_max = max(n_1, n_2)
    
    if n_max  == n_1:
        num = 1
    else:
        num = 2

    max_combsub = []
    for i in range(len(A)):
        if num == group[i]:
            max_combsub.append(i)
        else:
            if A[i] == 0:
                max_combsub.append(i)
            
    print('\nMax combination :', max_combsub)

Dvudol_group, dvudol, dvudol_dugs, dvudol__n_dugs = generation_dvudolnii()
Stepen_2, stepen_2_dugs, stepen_2__n_dugs = generation_stepen_two()


task(dvudol, dvudol_dugs, 'Dvudolnii')
task(Stepen_2, stepen_2_dugs, 'Stepen_2')
