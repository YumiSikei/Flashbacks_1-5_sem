M=int(input('Введите количество строк в матрице: '))
N=int(input('Введите количество столбцов в матрице: '))
R=[0]*M
for i in range (M):
    R[i]=[0]*N
print('Введите матрицу R построчно: ')
for i in range(M):
    R[i]=list(map(float,input().split()))
print('Исходная матрица: ')
for i in range(M):
    for j in range(N):
        print(R[i][j],end='\t')
    print()
Min=R[0][0]
h=0
for i in range (M):
    for j in range(M):
        if R[i][j]<Min:
            Min=R[i][j]
            h=j
for i in range(M):
    for j in range(h,N-1):
        R[i][j]=R[i][j+1]
print('Преобразованная матрица: ')
for i in range(M):
    for j in range(N-1):
        print(R[i][j],end='\t')
    print()
s=k=n=0
MT=[0]*(N-1)
for j in range(N-1):
    for i in range(M):
        s+=R[i][j]
        k+=1
    sr=s/k
    for i in range(M):
        if R[i][j]>sr:
            n+=1
    MT[j]=n
    n=s=k=0
print('Вектор МТ: ',MT)
