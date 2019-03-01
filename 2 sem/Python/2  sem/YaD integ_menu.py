#Янова Даниэлла ИУ7-23
#Создать меню с выбором способа вычисления интеграла методом правых
#прямоугольников

def f(x):
    return(x**2)

def ri(n):
    I=0
    t=(b-a)/n
    for i in range(1,n+1):
        xi=a+i*t
        I+=f(xi)
    return(I*t)

I=0
choice=None
print('1- Задать количество интервалов')
print('2- Задать степень точности')
print('0- Выход')
print()
while choice!='0':
    choice=input('Выбор: ')
    print()
    if choice=='0':
        print('Выход')
    elif choice=='1':
        a=float(input('Введите a из предела интегрирования [a,b]: '))
        b=float(input('Введите b из предела интегрирования [a,b]: '))
        n=int(input('Введите количество интервалов: '))
        I=ri(n)
        print('Интеграл: ')
        if I>=10e+2 or I<=-10e+2:
            print('{:13.6e}'.format(I))
        else:
            print('{:13.6f}'.format(I))
    elif choice=='2':
        a=float(input('Введите a из предела интегрирования [a,b]: '))
        b=float(input('Введите b из предела интегрирования [a,b]: '))
        eps=float(input('Введите точность вычислений: '))
        k1=0
        n=1
        k2=ri(n)
        while abs(k2-k1)>eps:
            n*=2
            k1=k2
            k2=ri(n)
        print('Точность ',eps)
        print('Количество разбиений ',n)
        print('Интеграл равен')
        if k2<=-10e+2 or k2>=10e+2:
            print('{:13.6e}'.format(k2))
        else:
            print('{:13.6f}'.format(k2))
    print()
