from random import randint
from math import factorial

def prov_dv(mas, v1, v2):
    for i in range (len(mas)):
        if (mas[i][0] == v1 and mas[i][1] == v2) or (mas[i][1] == v1 and mas[i][0] == v2):
            return 0
    return 1

def generation_dvudolnii():

    dvudol = [0]* randint(2, 10) #массив для обозначения части вершин
    
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
    dugs = randint(1, n_1 * n_2)
    dvudol_dugs = [0] * dugs
    for i in range (dugs):
        dvudol_dugs[i] = [0] * 2

    for i in range(dugs):
        v1 = randint(0, len(dvudolnii) - 1)
            
        v2 = randint(0, len(dvudolnii) - 1)
        while dvudol[v2] == dvudol[v1] or prov_dv(dvudol_dugs, v1, v2) == 0:
            v2 = randint(0, len(dvudolnii) - 1)

        dvudol_dugs[i][0] = v1
        dvudol_dugs[i][1] = v2
        dvudolnii[v1] += 1
        dvudolnii[v2] += 1
    

    return dvudol, dvudolnii, dvudol_dugs, dugs

Dvudol_group, dvudol, dvudol_dugs, dvudol__n_dugs = generation_dvudolnii()
