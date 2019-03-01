from math import log
try:
    x=float(input('Введите значение Х: '))
    eps=float(input('Введите точность суммы: '))
    n=3
    t=x
    s=x
    f=1
    while abs(t)>eps:
        for i in range (1,n+1):
            f*=i
        t=-t*x**n/f
        s+=t
        n+=1
    print('{:4.3f}'.format(s))
except ValueError:
    print('Неверно введены значения')
