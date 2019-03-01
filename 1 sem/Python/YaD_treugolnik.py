from math import sqrt
try:
    x1,y1=map(int,input('Введите координаты первой вершины: ').split())
    x2,y2=map(int,input('Введите координаты второй вершины: ').split())
    x3,y3=map(int,input('Введите координаты третьей вершины: ').split())

    a=sqrt((x1-x2)**2+(y1-y2)**2)  
    b=sqrt((x3-x2)**2+(y3-y2)**2)
    c=sqrt((x1-x3)**2+(y1-y3)**2)
    
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    if a<b and a<c:
        h=s*2/a 
    elif b<a and b<c:
        h=s*2/b
    else:
        h=s*2/c
    print('%.4f'%h)
        
except ValueError:
    print('Ведены неверные координаты')
