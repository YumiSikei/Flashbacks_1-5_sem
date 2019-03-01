#Янова Даниэлла ИУ7-43
#Полином Ньютона

import numpy as np
import matplotlib.pyplot as plt
#import time
from math import sin, cos

def f(x):
    return 0.5*x - 0.9

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
print("Table")
print("    X          Y")
for i in range (21):
    x.append(i-10)
    y_i = f(x[i])
    y.append(y_i)
    print('{:6.2f}'.format(x[i]),"   ",'{:4.4f}'.format(y[i]))
print('---------------')
print()

######
print('Обратная интерполяция- Поиск корня')
n_p=int(input('Введите степень точности(натуральное число): '))

s = n_p // 2
x_p=[]; y_p=[]
for i in range(20):
    if (y[i]>=0 and y[i+1]<0) or (y[i]<=0 and y[i+1]>0):
        c = x[i]
for i in range(n_p+1):
    x_p.append(c-s + i)
    y_p.append(f(x_p[i]))
for i in range (n_p+1):
    x_p[i],y_p[i]=y_p[i],x_p[i]
    
F = interpolation(x_p, y_p, n_p+1, 0)
print("Корень функции через обратную интерполяцию: ",'{:.4e}'.format(F))
print()

#######
print('Обычная Интерполяция')
xx=float(input('Введите х, в котором хотите узнать значение функции: '))
n_p=int(input('Введите степень точности(натуральное число): '))

c = xx // 1
s = n_p // 2
k = c-s
x=[]; y=[]
for i in range(n_p+1):
    x.append(k)
    k += 1
    y.append(f(x[i]))
n_p+=1

F = interpolation(x,y,n_p, xx)
fi = f(xx)

print("Результат интерполяции: ",'{:.4e}'.format(F))
print("Значение у: ", '{:.4f}'.format(fi))

########
xx=np.linspace(-10,10,100)
xxx=[]; yy=[]; yyy=[]
for i in xx:
    yy.append(f(i))
    yyy.append(0)
    xxx.append(0)

#plt.subplot(221)
plt.grid()
plt.plot(xx,yy,'blue')
plt.plot(xx,yyy,'red')
plt.plot(xxx,yy,'red')
plt.title(r'$0.5*x - 0.9$')

plt.show()
