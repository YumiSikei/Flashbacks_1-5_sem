#Янова Даниэлла ИУ7-13
#Найти средние арифметические элементов массива в каждой строке и наибольшее
#из них
try:
    s=int(input('Введите количество строк в матрице: '))
    c=int(input('Введите количество столбцов в матрице: '))
    print('Введите матрицу')
    R=[0]*s
    for i in range(s):
        R[i]=[0]*c
    for i in range (s):
        n=i+1
        print('Введите',n,'-ю строку матрицы:',end=' ')
        R[i]=list(map(float,input().split()))
    print('Исходная матрица: ')
    for i in range(s):
        for j in range(c):
            if R[i][j]<=-10e+4 or R[i][j]>=10e+3:
                print('{:7.1e}'.format(R[i][j]),end=' ')
            else:
                print('{:7.1f}'.format(R[i][j]),end=' ')
        print()
    sr=0
    k=0
    for i in range(s):
        for j in range(c):
            sr+=R[i][j]
            k+=1
        R[i][0]=sr/k
        n=i+1
        print('Среднее арифметическое ',n,'-й строки =',end=' ')
        if R[i][0]<=-10e+4 or R[i][0]>=10e+3:
            print('{:7.1e}'.format(R[i][0]))
        else:
            print('{:7.1f}'.format(R[i][0]))
        sr=0
        k=0
    Max=R[0][0]
    for i in range(1,s):
        if R[i][0]>Max:
            Max=R[i][0]
    print()
    print('Наибольшее среднее арифметическое= ',end='')
    if Max<=-10e+4 or Max>=10e+3:
        print('{:7.1e}'.format(Max),end=' ')
    else:
        print('{:7.1f}'.format(Max),end=' ')
except ValueError:
    print('Введены неверные значения')
