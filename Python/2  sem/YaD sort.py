#Янова Даниэлла ИУ7-23
#

import numpy as np
import random
import time


def VsSBar(array):

    back=array[0]
    
    for i in range(2, len(array)):
        if array[i - 1] > array[i]: 
            array[0] = array[i]
            j = i - 1

            while array[j] > array[0]:
                array[j + 1] = array[j]
                j = j - 1

            array[j + 1] = array[0]

    array[0]=back
    
    i=1
    while array[i]<back:
        array[i-1]=array[i]
        i+=1
        
    array[i-1]=back

    return array


def Shaker(seq):
    lower_bound = -1
    upper_bound = len(seq) - 1
    swapped = True
    while swapped:
        swapped = False
        lower_bound += 1
        for i in range(lower_bound, upper_bound):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        upper_bound -= 1
        for i in range(upper_bound, lower_bound, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                swapped = True
    return seq

el=100



print('''
 Количество   |                  Методы сортировки         
 элементов    |   Вставка с барьером   |      Шейкер''')

for i in range(3):
    
    array=np.random.randint(0,500,el)
        
    tw=time.clock()
    array=VsSBar(array)
    t1= time.clock()-tw

    
    array=Shaker(array)
    t2= time.clock()-t1
    
    print("{:7d}       |      {:8.4f}          |{:12.4f}".format(el,t1,t2))

    el*=10

print('''Введите массив из 10 элементов для личной проверки работы сортировки
\каждый элемент вводить в отдельной строке\
Внимание! 10-ый элемент должен быть обязательно равен нулю, чтобы
работал метод вставки с барьером!: ''')

mas=[0]*10
for i in range(10):
    u=i+1
    print(u,') ',end='')
    mas[i]=float(input())

print('Изначальный массив: ',mas)
print()

vssbar_mas=VsSBar(mas)
print('Массив, отсортированный методом вставки с барьером: ',vssbar_mas)
print()

shaker_mas=Shaker(mas)
print('Массив, отсортированный методом шейкер: ',shaker_mas)

