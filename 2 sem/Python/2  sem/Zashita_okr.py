#Янова Даниэлла ИУ7-23

from math import sqrt
from tkinter import *


N=0
N=int(input('Введите количество окружностей: '))
while N<=2:
     print('Окружностей должно быть не менее двух!')
     N=int(input('Введите количество окружностей: '))

x=[0]*N
y=[0]*N
rad=[0]*N
for i in range(N):
     xi,yi=map(float,input('Введите координаты центра окружности: ').split())
     x[i]=xi
     y[i]=yi
     rad[i]=float(input('Введите радиус этой окружности: '))
     print('---------')

maxk=0
xk=0
yk=0
radk=0
for i in range(N):
     #print(x[i],y[i],end=' ')
     k=0
     for j in range(N):
          if i!=j:
               l=sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
               #print('    ',x[j],y[j],'  ',l)
               if 0<l<=(rad[i]+rad[j]):
                    k=k+1
     #print(k)
     #print('--')
     if k>maxk:
          maxk=k
          xk=x[i]
          yk=y[i]
          radk=rad[i]
               


size = 700 # Размер холста

root = Tk()  # Настраиваем холст (Canvas) в окне
root.title("circuls")
root.geometry("700x700")
canv = Canvas(root, width=size, height=size, bg="aliceblue")
canv.pack(padx = 0, pady = 0)

# Создаем оси по центру
canv.create_line(size/2, size, size/2, 0, width=2, arrow=LAST) # OY
canv.create_line(0, size/2, size, size/2, width=2, arrow=LAST) # OX

# Подписи к осям
canv.create_text(size/2 + 15, 15, text="Y", font="Verdana 14", fill="red")
canv.create_text(size - 15, size/2 - 15, text="X",font="Verdana 14",fill="red")

# Рисуем точки
for i in range(N):
    canv.create_oval([x[i] - 5 + size/2, size/2 - (y[i]- 5)],
    [x[i]+ 5 + size/2, size/2 - (y[i] + 5)], fill = 'purple')
    
# Рисуем 
print()
print('Координаты нужной окружности: ')
print('Центр-',xk,' ',yk,'      Радиус=',radk)


for i in range(N):
     canv.create_oval([x[i]+rad[i]+ size/2,size/2 -y[i]+rad[i]],
                      [x[i]-rad[i]+ size/2,size/2 -y[i]-rad[i]],outline="blue")

canv.create_oval([xk+radk+ size/2,size/2 -yk+radk],
                 [xk-radk+ size/2,size/2 -yk-radk],outline="red")


canv.pack()
root.mainloop()

