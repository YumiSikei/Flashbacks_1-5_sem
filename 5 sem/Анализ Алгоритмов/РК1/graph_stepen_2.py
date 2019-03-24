from random import randint
from math import factorial

def prov_st_2(mas, v1, v2):
    for i in range (len(mas)):
        if (mas[i][0] == v1 and mas[i][1] == v2) or (mas[i][1] == v1 and mas[i][0] == v2):
            return 0
    return 1

def generation_stepen_two():

    stepen_2 = [0]* randint(3, 10)
    dugs = randint(0, len(stepen_2) - 1) #количество дуг
    stepen_2_dugs = [0]
    stepen_2_dugs[0] = [0] * 2

    for i in range (dugs):
        v1 = randint(0, len(stepen_2) - 1)
        while stepen_2[v1] == 2:
            v1 = randint (0, len(stepen_2) - 1)
            
        v2 = randint(0, len(stepen_2) - 1)
        while v2 == v1 or stepen_2[v2] == 2 or prov_st_2(stepen_2_dugs, v1, v2) == 0:
            v2 = randint(0, len(stepen_2) - 1)

        if i > 0:
            stepen_2_dugs.append(0)
            stepen_2_dugs[i] = [0] * 2
        stepen_2_dugs[i][0] = v1
        stepen_2_dugs[i][1] = v2
        stepen_2[v1] += 1
        stepen_2[v2] += 1

    return stepen_2,stepen_2_dugs, dugs

Stepen_2, stepen_2_dugs, stepen_2__n_dugs = generation_stepen_two()
