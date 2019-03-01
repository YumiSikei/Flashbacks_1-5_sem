#Янова Даниэлла ИУ7-13
#Вычислить таблицу значений функции и построить график функции
try:
    a=float(input('Введите начальное значение А: '))
    al=float(input('Введите конечное значение А: '))
    an=float(input('Введите шаг: '))
    min=a**7-a**6+8*a**5-4*a**4+6*a**3+2*a**2-5*a+1
    max=min
    a0=a
    eps=0.5
    print('         A               C')
    while True:
        c=a**7-a**6+8*a**5-4*a**4+6*a**3+2*a**2-5*a+1
        if c>max:
            max=c
        if c<min:
            min=c
        if a>=10e+4:
            print('{:13.3e}'.format(a),end=' ')
        else:
            print('{:13.3f}'.format(a),end=' ')
        if c<=-10e+4 or c>=10e+3:
            print('\t{:13.3e}'.format(c),end='\n')
        else:
            print('\t{:13.3f}'.format(c),end='\n')
        a+=an
        if a>al:
            break
    print('---------------------------------------------------------')
    if min<=-10e+4 or min>=10e+3:
            print('{:4.3e}'.format(min),end=' ')
    else:
            print('{:4.3f}'.format(min),end=' ')
    print('                                    ',end=' ')
    if max<=-10e+4 or max>=10e+3:
            print('\t{:13.3e}'.format(max),end='\n')
    else:
            print('\t{:13.3f}'.format(max),end='\n')
    print('+',end='')
    for i in range (1,59):
        print('-',end='')
    print('+        A')
    a=a0
    j=-min/(max-min)*59+1
    while True:
        c=a**7-a**6+8*a**5-4*a**4+6*a**3+2*a**2-5*a+1
        m=(c-min)/(max-min)*59+1
        k=1
        while k<61:
            if abs(k-m)<=eps:
                print('*',end='')
            elif abs(k-j)<=eps:
                print('|',end='')
            else:
                print(' ',end='')
            k+=1
        print('   ','{:7.3f}'.format(a))
        a+=an
        if a>al:
            break
    r=max-min
    print('Разница максимального и минимального значения',
          'равна',end=' ')
    if r<=-10e+4 or r>=10e+3:
        print('{:6.3e}'.format(r))
    else:
        print('{:6.3f}'.format(r))
except ValueError:
    print('Введены неверные значения')
