#Янова Даниэлла ИУ7-13
#Поменять первые и последние строки матрицы соответственно с номерами с начала
#и конца. В преобразованной матрице найти среднее арифметическое положительных
#элементов, лежащих выше главной диагонали.
try:
    s=int(input('Введите количество строк в матрице: '))
    c=int(input('Введите количество столбцов в матрице: '))
    print('Введите матрицу')
    R=[0]*s
    for i in range(s):
        R[i]=[0]*c
    for i in range (s):
        for j in range (c):
            R[i][j]=float(input())
    print('Исходная матрица: ')
    for i in range(s):
        for j in range(c):
            if R[i][j]<=-10e+4 or R[i][j]>=10e+3:
                print('{:7.2e}'.format(R[i][j]),end=' ')
            else:
                print('{:7.2f}'.format(R[i][j]),end=' ')
        print()
    if s%2==0:
        n=s/2
    else:
        n=(s-1)/2
    n=int(n)
    for i in range(n):
        j=s-i-1
        R[i],R[j]=R[j],R[i]
    sr=0
    k=0
    print('Сформированная матрица: ')
    for i in range(s):
        for j in range(c):
            if R[i][j]<=-10e+4 or R[i][j]>=10e+3:
                print('{:7.2e}'.format(R[i][j]),end=' ')
            else:
                print('{:7.2f}'.format(R[i][j]),end=' ')
        print()
    for i in range(s):
        for j in range(c):
            if i<j and R[i][j]>0:
                sr+=R[i][j]
                k+=1
    if k>0:
        sr=sr/k
        print()
        print('Среднее арифметическое элементов, лежащих выше главной',
              'диагонали=',end=' ')
        if sr<=-10e+4 or sr>=10e+3:
            print('{:7.2e}'.format(sr),end=' ')
        else:
            print('{:7.2f}'.format(sr),end=' ')
    else:
        print('Положительных элементов выше главной диагонали нет')
except ValueError:
    print('Введены неверные значения')
