#Янова Даниэлла ИУ7-13
#Отсортировать элементы одномернного массива по знаку
try:
    L=int(input('Введите количество элементов в массиве: '))
    D=[0]*(L+1)
    k=0
    k0=0
    print('Введите массив: ')
    for i in range (L):
        D[i]=float(input())
        if D[i]==0:
            k0+=1
        elif D[i]>0:
            k+=1
    j=0
    for i in range (0,k0):
        while D[j]!=0:
            j+=1
        D[L]=D[j]
        for j in range (j,L):
            D[j]=D[j+1]
        j=0
    
    for i in range (0,k):
        while D[j]<=0:
            j+=1
        D[L]=D[j]
        for j in range (j,L):
            D[j]=D[j+1]
        j=0

    for i in range (L):
        print(D[i],end=' ')
except ValueError:
    print('Введены неверные значения')
