#Янова Даниэлла ИУ7-23
#Найти корни функции методом уточнения корней Стефансена и показать на графике
#экстремумы функции.

import numpy as np
import matplotlib.pyplot as plt
import time
from math import sin, cos, tan

def f(x):
    return tan(x)

def F(x):
    return 1/cos(x)**2

def dF(x):
    return sin(x)/2/cos(x)**3

def steff(x0,eps):
    x20=x0
    n=0
    while n<maxn:
        n+=1
        x1=x0-(f(x0)/(f(x0+f(x0))-f(x0))*f(x0))
        if abs(x1-x0) < eps:
            return x1,n,0
        x0=x1

    if n==maxn:
        return x1,n,1

def dfsteff(x20,eps):
    n=0
    while n<maxn:
        n+=1
        x2=x20-(F(x20)/(F(x20+F(x20))-F(x20))*F(x20))
        if abs(x2-x20) < eps:
            return x2
        x20=x2

    if n==maxn:
        return False

def ddfsteff(x20,eps):
    n=0
    while n<maxn:
        n+=1
        x2=x20-(dF(x20)/(dF(x20+dF(x20))-dF(x20))*dF(x20))
        if abs(x2-x20) < eps:
            return x2
        x20=x2

    if n==maxn:
        return False    

eps=float(input('Введите точность вычислений: '))
a,b=map(float,input('Введите а и b отрезка [a,b], на котором будет \
производиться уточнение корней: ').split())
h=float (input('Введите шаг: '))
maxn=int (input('Введите максимальное число итераций: '))

time.clock()

print('''
Код ошибки:
0 - нет ошибок
1 - превышено количество итераций
''')
print('''
                                                             Число       Код     
 № корня      X(n)      X(n+1)       X            f(X)       итераций    ошибки ''')

i=0
xk=a
xkn=a+h
mas=[]
df=[]
dfmas=[]

while xk<b:
    if xkn>b:
        xkn=b
    if f(xk)*f(xkn)<0:  #Проверка на наличие корня в отрезке
        i+=1

        X,n,code=steff(xk,eps)  #Поиск корня
        if xk<=X<=xkn:
            mas.append(X)
        

        if code == 0 and xk<=X<=xkn:
            print("{:4d}{:14.2f}  {:8.2f}   {:11.6f}   {:11.2e}{:9d}{:11d}"\
                .format(i, xk, xkn, X, f(X), n, code))
        elif code == 1 and xk<=X<=xkn:
            print("{:4d}{:14.2f}  {:8.2f}      ---             ---{:9d}{:11d}"\
                .format(i, xk, xkn, n, code))
    
    if F(xk)*F(xkn)<0:  #Проверка на наличие экстремума в отрезке
        n=0

        w=dfsteff(xk,eps)
        if w!=False and xk<=w<=xkn:
            df.append(w)

    if dF(xk)*dF(xkn)<0:  #Проверка на наличие перегиба в отрезке
        n=0

        r=ddfsteff(xk,eps)
        if r!=False and xk<=r<=xkn:
            dfmas.append(r)
            
    if f(xk)*f(xkn)==0:  #Проверка корень 
        i+=1
        if f(xk)==0 and not(xk in mas):
            mas.append(xk)
            print("{:4d}       {:7.2f}   {:7.2f}   {:11.6f}   {:11.2e}{:9d}{:11d}"\
                .format(i, xk, xkn, xk, 0, 0, 0))
        if f(xkn)==0 and not(xkn in mas):
            mas.append(xkn)
            print("{:4d}       {:7.2f}   {:7.2f}   {:11.6f}   {:11.2e}{:9d}{:11d}"\
                .format(i, xk, xkn, xkn, 0, 0, 0))
        if F(xk)==0 and not(xk in df):
            df.append(xk)
        if F(xkn)==0 and not(xkn in df):
            df.append(xkn)
        if dF(xk)==0 and not(xk in dfmas):
            dfmas.append(xk)
        if dF(xkn)==0 and not(xkn in dfmas):
            dfmas.append(xkn)

    xk=xkn
    xkn+=h
    
time = time.clock()
print("\nВремя выполнения программы = {:8.4f}".format(time))

x=np.linspace(a,b,100)
y=[]

for i in x:
    y.append(f(i))
plt.subplot(221)
plt.grid()
plt.plot(x,y,'blue')
plt.title(r'$tan(x)$')
   
plt.subplot(222)
plt.grid()
plt.plot(x,y,'blue')
plt.title(r'$Корни$')
for i in range(len(mas)):
    plt.scatter(mas[i],f(mas[i]),color='green')
   
plt.subplot(223) 
plt.grid()
plt.xlabel('x')
plt.plot(x,y,'blue')
plt.title(r'$Перегиб$')
for i in range(len(dfmas)):
    plt.scatter(dfmas[i],f(dfmas[i]),color='purple')
   
plt.subplot(224) 
plt.grid()
plt.plot(x,y,'blue')
plt.title(r'$Экстремумы$')
for i in range(len(df)):
    plt.scatter(df[i],f(df[i]),color='red')


plt.show()
