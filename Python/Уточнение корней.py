from math import *
import numpy as np
import time
import matplotlib.pyplot as plt

Fi = 1.618033988

#основная функция
def f(x):
    return(x - cos(x))

#производная функции
def df(x):
    return(1 + sin(x))
    

#функция на получение данных
def main():
    global start #начало интервала
    global end #конец интервала
    global eps #точность
    global step #шаг разбиения
    global it #максимальное количество итераций

    start = float(input("Введите начало отрезка: "))
    end = float(input("Введите конец отрезка: "))
    eps = float(input("Введите точность, eps: "))
    step = float(input("Введите шаг разбиения: "))
    it = float(input("Введите максимальное количество итераций: "))
    
def iterations(x0, f, k, eps, i):
    while True:
        x1 = x0 - k*f(x0)
        if abs(x1-x0) < eps:
            return x1, 0, 2
        x0 = x1

main()

if df(start) < 0:
    k = -1
else:
    k = 1

print('''
Код ошибки:
0 - нет ошибок
1 - превышено количество итераций
''')

print('''
                                                             Число       Код     
 № корня      X(n)      X(n+1)       X            f(X)       итераций    ошибки ''')


i = 0
a_st = start
b_en = a_st + step
roots = []

while (a_st) < end:
    if b_en > end:
        b_en = end
    rit = 0
    #проверка на корень внутри
    if f(a_st)*f(b_en) < 0:
        i+=1
        x, code, rit = iterations(a_st, f, k, eps, it)
        roots.append(x)
        
        print("{:4d}       {:7.2f}   {:7.2f}   {:11.6f}   {:11.2e}{:9d}{:11d}"\
                    .format(i, a_st, b_en, x, f(x), rit, code))
    #проверка на корень на концах
    if f(a_st)*f(b_en) == 0:
        i+=1
        if f(a_st) == 0 and not(a_st in roots):
            print("{:4d}       {:7.2f}   {:7.2f}   {:11.6f}   {:11.2e}{:9d}{:11d}"\
                    .format(i, a_st, b_en, a_st, 0, 0, 0))
            roots.append(a_st)
        if f(b_en) == 0 and not(b_en in roots):
            print("{:4d}       {:7.2f}   {:7.2f}   {:11.6f}   {:11.2e}{:9d}{:11d}"\
                    .format(i, a_st, b_en, b_en, 0, 0, 0))
            
    a_st, b_en = b_en, b_en + step



