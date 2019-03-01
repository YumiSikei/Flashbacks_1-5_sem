# Матасов Илья.
# Защита.Метод 3/8.
from math import trunc
def f(arg):
    return arg*arg
def ab(a,b):
    return abs(1/3*a**3-1/3*b**3)
def toe(a,b,n):
    s = 0
    s3 = 0
    h = abs(b-a)/n
    y = [0]*(n+1)
    for i in range(0,n+1):
        y[i]=f(a+i*h)
        if i % 3 == 0 and i>0:
            s3 += y[i]
        else:
             s += y[i]
        s3 *= 2
        s *= 3
    return 3*h/8*trunc(y[0]+y[n]+s+s3)    
aq,bq = map(float,input('Введите границы интегрирования:').split())
eps = float(input('Введите точность:'))
nq = 1
integ = ab(aq,bq)
q = toe(aq,bq,nq)
while abs(integ-q)> eps:
    nq*=3
    q=toe(aq,bq,nq)
print('При точности eps:',q,'Разбиений',nq)
    
