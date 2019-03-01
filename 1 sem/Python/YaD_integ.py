#Янова Даниэлла ИУ7-13
#Найти интеграл функции методами правых прямоугольников и буля
a=float(input('Введите a из предела интегрирования [a,b]: '))
b=float(input('Введите b из предела интегрирования [a,b]: '))
n1=int(input('Введите число разбиений n1: '))
n2=int(input('Введите число разбиений n2: '))
eps=float(input('Введите точность вычислений: '))

def f(x):  #Функция f(x)
    return x*x
def integ1(n):  #Метод правых прямоугольников
    h=(b-a)/n
    I=0
    for i in range(1,n+1):
        xi=a+h*i
        y=f(xi)*h
        I+=y
    return(I)
def integ2(n):  #Метод буля
    h=(b-a)/n
    I=2/45*h*(7*f(a)+32*f(h+a)+12*f(2*h+a)+32*f(3*h+a)+7*f(b))
    return(I)
print()
I11=integ1(n1) 
I12=integ1(n2)
I21=I22=-1
if n1%4==0:
    I21=integ2(4)
if n2%4==0:
    I22=integ2(4)
print('Метод                  Количество разбиений        Интеграл')
print('Правых прямоугольников    ',n1,end='\t\t\t')
if I11<=-10e+2 or I11>=10e+2:
    print('{:13.6e}'.format(I11))
else:
    print('{:13.6f}'.format(I11))
print('                          ',n2,end='\t\t\t')
if I12<=-10e+2 or I12>=10e+2:
    print('{:13.6e}'.format(I12))
else:
    print('{:13.6f}'.format(I12))
print('Буля                      ',n1,end='\t\t\t')
if I21!=-1:
    if I21<=-10e+2 or I21>=10e+2:
        print('{:13.6e}'.format(I21))
    else:
        print('{:13.6f}'.format(I21))
else:
    print('  Не вычислен')
print('                          ',n2,end='\t\t\t')
if I22!=-1:
    if I22<=-10e+2 or I22>=10e+2:
        print('{:13.6e}'.format(I22))
    else:
        print('{:13.6f}'.format(I22))
else:
    print('  Не вычислен')
print()
k1=0
n=1
k2=integ1(n)
while abs(k2-k1)>eps:
    n*=2
    k1=k2
    k2=integ1(n)
print('Точность ',eps)
print('Количество разбиений ',n)
print('Интеграл, найденный методом правых прямоугольников равен',end=' ')
if k2<=-10e+2 or k2>=10e+2:
    print('{:10.6e}'.format(k2))
else:
    print('{:10.6f}'.format(k2))
