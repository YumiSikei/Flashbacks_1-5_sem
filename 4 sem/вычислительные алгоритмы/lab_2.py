#Янова Даниэлла ИУ7-43
#Многомерная интерполяция

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos

def z_f(x, y):
    return x**2 + y**2

def y_k(xi, xj, yi, yj):
    y = (yi - yj)/(xi - xj)
    return y

def interpolation(x, y, n, xx):
    y_n=[]
    for i in range (n - 1):
        f_ij = y_k(x[i], x[i+1],y[i],y[i+1])
        y_n.append(f_ij)
    nn = n - 1
    F = y[0] + (xx-x[0])*y_n[0]

    yy = (xx-x[0])
    while (nn>0):
        for i in range (nn-1):
            y_n[i] = y_k(x[i], x[i+1], y_n[i], y_n[i+1])
        yy *= (xx-x[n-nn])
        F += yy*y_n[0]
        nn -= 1
    return F

x=[]
y=[]
for i in range (10):
    x.append(i+1)
    y.append(i+1)
z=[0]*10
for i in range(10):
    z[i]=[0]*10
print("Table")
print(" X\Y   |", end='')
for i in range(10):
    print('{:5.1f}'.format(y[i]),end=' |')
print()
print('------------------------------------------------------------------------------')
for i in range (10): 
    print('{:5.1f}'.format(x[i]),end='  |')
    for j in range(10):
        z[i][j]=z_f(x[i],y[j])
        print('{:5.1f}'.format(z[i][j]),end=' |')
    print()
print()

xx=float(input('Введите х, в котором хотите узнать значение функции z: '))
yy=float(input('Введите y, в котором хотите узнать значение функции z: '))
n=int(input('Введите степень точности(натуральное число): '))

cx = xx // 1;    cy = yy // 1
sx = n // 2;   sy = n // 2
kx = cx-sx;      ky = cy-sy
x=[]; y=[]
n += 1
for i in range(n):
    x.append(kx)
    kx += 1
for i in range(n):
    y.append(ky)
    ky += 1

Z=[0]*(n)
zzx=[0]*(n)
for i in range (n):
    for j in range (n):
        zzx[j] = z_f(x[j],y[i])
    Z[i] = interpolation(x, zzx, n, xx)
Result = interpolation(y, Z, n, yy)
f = z_f(xx, yy)

print("Результат интерполяции: ",'{:.3e}'.format(Result))
print("Значение z: ", '{:.3f}'.format(f))

    
