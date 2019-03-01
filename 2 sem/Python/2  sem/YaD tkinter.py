#Янова Даниэлла ИУ7-23
#Дано множество точек на плоскости.Найти треугольник, для которого разность
#площадей треугольников, образованных делением дной из биссектрис, будет
#минимальна. Дать графическое изображение результатов.

from math import *
from tkinter import *


def Sm(a,c,l,h,g):  #Разность площадей треугольников, образованных биссектрисой
     p1=(a+l+h)/2
     #print(p1,a,l,h)
     s1=sqrt(p1*(p1-a)*(p1-l)*(p1-h))
     p2=(c+l+g)/2
     s2=sqrt(p2*(p2-c)*(p2-l)*(p2-g))
     minis=abs(s1-s2)
     return minis

def bis(xa,ya,xb,yb,xc,yc):    #Вычисление разности через биссектрису
     a=sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
     b=sqrt((x[i]-x[k])**2+(y[i]-y[k])**2)
     c=sqrt((x[k]-x[j])**2+(y[k]-y[j])**2)
     if a==b or a==c or b==c:
          return 0
     l=sqrt(a*c*(a+b+c)*(a+c-b))/(a+c)
     #print('l',a,b,c,l)
     D=b*b-4*a*c+4*l*l
     if D<0:
          return False
     else:
          #print(D)
          n=(b+sqrt(D))/2
          #print(n)
          m=b-n
          if abs(a/c-m/n)<0.1:
               minis=Sm(a,c,l,m,n)
          elif abs(a/c-n/m)<0.1:
               minis=Sm(a,c,l,n,m)
          #n=(b-sqrt(D))/2
          #print(n)
          #m=b-n
          #if n>0:
           #    print('yes')
            #   if abs(a/c-m/n)<0.1:
             #       minis=Sm(a,c,l,m,n)
              # elif abs(a/c-n/m)<0.1:
               #     minis=Sm(a,c,l,n,m)
          return minis


N=0
N=int(input('Введите количество точек: '))
while N<3:
     print('Точек должно быть более двух!')
     N=int(input('Введите количество точек: '))

x=[]
y=[]
for i in range(N):
     xi,yi=map(float,input('Введите координаты очередной точки: ').split())
     x.append(xi)
     y.append(yi)

u=0

print()

print('Координаты треугольника                Разница образованных треугольников')
for i in range(N-2):
     for j in range(i+1,N-1):
          for k in range(j+1,N):
               mina=bis(x[i],y[i],x[j],y[j],x[k],y[k])
               minb=bis(x[j],y[j],x[i],y[i],x[k],y[k])
               minc=bis(x[k],y[k],x[i],y[i],x[j],y[j])
               mini=min(mina,minb,minc)
               print(x[i],y[i],x[j],y[j],x[k],y[k],'              ',
                     '{:10.4f}'.format(mini))
                    
               if u==0:
                    u=1
                    minbis=mini
                    xma=x[i]; xmb=x[j]; xmc=x[k]
                    yma=y[i]; ymb=y[j]; ymc=y[k]
               elif mini<minbis:
                    minbis=mini
                    xma=x[i]; xmb=x[j]; xmc=x[k]
                    yma=y[i]; ymb=y[j]; ymc=y[k]


size = 700 # Размер холста

root = Tk()  # Настраиваем холст (Canvas) в окне
root.title("polygons")
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
    
# Рисуем треугольники
print()
print('Координаты нужного треугльника')
print(xma,yma,xmb,ymb,xmc,ymc)


for i in range(N-2):
     for j in range(i+1,N-1):
          for k in range(j+1,N):
               if not (x[i]==xma and x[j]==xmb and x[k]==xmc and
                       y[i]==yma and y[j]==ymb and y[k]==ymc):
                    canv.create_line(x[i]+size/2,size/2-y[i],x[j]+size/2,
                                     size/2-y[j],width=3,fill="green")
                    canv.create_line(x[k]+size/2,size/2-y[k],x[j]+size/2,
                                     size/2-y[j],width=3,fill="green")
                    canv.create_line(x[i]+size/2,size/2-y[i],x[k]+size/2,
                                     size/2-y[k],width=3,fill="green")

canv.create_line(xma + size/2,size/2 - yma,xmb + size/2,size/2 - ymb,
                 width=3,fill="red")
canv.create_line(xmc + size/2,size/2 - ymc,xmb + size/2,size/2 - ymb,
                 width=3,fill="red")
canv.create_line(xma + size/2,size/2 - yma,xmc + size/2,size/2 - ymc,
                 width=3,fill="red")


canv.pack()
root.mainloop()
