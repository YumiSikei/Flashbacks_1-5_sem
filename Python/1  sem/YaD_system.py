#Янова Даниэлла ИУ7-13
#Вычислить С(x) по заданной функции для вводимых A и X.
try:
    a,x=map(float,input('Введите значения А и Х: ').split())
    from math import exp, sin, log
    s=a*a/(5.1*x)
    t=sin(a*x)**(1/3)
    if s<=0:
        c=exp(t)
    else:
        c=log(s)-95.1
    print('c=','%.4f'%c)
except:
    print('Введены неверные значения')

