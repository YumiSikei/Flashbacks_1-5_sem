#Янова Даниэлла ИУ7-43
#Дано множество точек на плоскости.Найти треугольник, у которого угол между
#высотой и медианой, идущими из одной вершины, минимален.

from math import *
from tkinter import *
from math import sqrt, acos, degrees

N=0
x=[]
y=[]

def delete_all():
     global N; global x; global y
     x = []; y = []; N = 0
     root.text_status.delete('1.0', END)

def insert_point():
     global N; global x; global y
     x.append(float(root.point_x.get()))
     y.append(float(root.point_y.get()))
     N += 1
     root.text_status.delete('1.0', END)
     root.text_status.insert(INSERT, '1) ')
     root.text_status.insert(INSERT, x[0])
     root.text_status.insert(INSERT, ' ')
     root.text_status.insert(INSERT, y[0])
     root.text_status.insert(INSERT, '\n')
     for i in range (1, N):
          root.text_status.insert(INSERT, i+1)
          root.text_status.insert(INSERT, ') ')
          root.text_status.insert(INSERT, x[i])
          root.text_status.insert(INSERT, ' ')
          root.text_status.insert(INSERT, y[i])
          root.text_status.insert(INSERT, '\n')

def delete_point():
     global N; global x; global y
     k = int(root.entry_number.get())
     for i in range (k-1, N-1, 1):
          x[i] = x[i+1]
          y[i] = y[i+1]
     N -= 1
     root.text_status.delete('1.0', END)
     root.text_status.insert(INSERT, '1) ')
     root.text_status.insert(INSERT, x[0])
     root.text_status.insert(INSERT, ' ')
     root.text_status.insert(INSERT, y[0])
     root.text_status.insert(INSERT, '\n')
     for i in range (1, N):
          root.text_status.insert(INSERT, i+1)
          root.text_status.insert(INSERT, ') ')
          root.text_status.insert(INSERT, x[i])
          root.text_status.insert(INSERT, ' ')
          root.text_status.insert(INSERT, y[i])
          root.text_status.insert(INSERT, '\n')

def find_treug():
     global N; global x; global y
     u=0
     for i in range(N-2):
          for j in range(i+1,N-1):
               for k in range(j+1,N):
                    # Находим стороны
                    a=sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
                    b=sqrt((x[i]-x[k])**2+(y[i]-y[k])**2)
                    c=sqrt((x[k]-x[j])**2+(y[k]-y[j])**2) 
                    if ((a+b)>c and (a+c)>b and (b+c)>c):
                         # Находим площадь
                         p = (a + b + c) / 2
                         S = sqrt(p*(p - a)*(p - b)*(p - c))
                         # Находим высоты
                         ha = 2*S/a
                         hb = 2*S/b
                         hc = 2*S/c
                         # Находим медианы
                         ma = sqrt(2*b*b + 2*c*c - a*a)/2
                         mb = sqrt(2*a*a + 2*c*c - b*b)/2
                         mc = sqrt(2*b*b + 2*a*a - c*c)/2
                         # Находим минимальное отношение соотв. высот и медиан в этом треугольнике
                         if ha < ma:
                              hma = ma / ha
                         else:
                              hma = ha / ma
                    
                         if hb < mb:
                              hmb = mb / hb
                         else:
                              hmb = hb / mb

                         if hc < mc:
                              hmc = mc / hc
                         else:
                              hmc = hc / mc
                         mini = min(hma, hmb, hmc)

                         #Ищем самой минимальный нужный угол среди всех возможных
                         if u==0 or mini<min_hm:
                              u=1
                              min_hm=mini
                              #сохраняем нужные вершины
                              if (mini==hma):
                                   hh = ha; mm = ma
                                   xx=x[k]; xxb=x[i]; xxc=x[j]
                                   yy=y[k]; yyb=y[i]; yyc=y[j]
                              elif (mini==hmb):
                                   hh = hb; mm = mb
                                   xx=x[j]; xxb=x[i]; xxc=x[k]
                                   yy=y[j]; yyb=y[i]; yyc=y[k]
                              else:
                                   hh = hc; mm = mc
                                   xx=x[i]; xxb=x[j]; xxc=x[k]
                                   yy=y[i]; yyb=y[j]; yyc=y[k]
     return xx, yy, xxb, yyb, xxc, yyc, hh, mm

def paint_treug(xx, yy, xxb, yyb, xxc, yyc):
     canv.create_line(xx + size/2,size/2 - yy,xxb + size/2,size/2 - yyb,
                      width=3,fill="red")
     canv.create_line(xxc + size/2,size/2 - yyc,xxb + size/2,size/2 - yyb,
                      width=3,fill="red")
     canv.create_line(xxa + size/2,size/2 - yy,xxc + size/2,size/2 - yyc,
                      width=3,fill="red")
     # Рисуем медиану и высоту
     canv.create_line(xx + size/2,size/2 - yy,(xxb+xxc)/2 + size/2,
                      size/2 - (yyb+yyc)/2,width=3,fill="blue")

     if xxb==xxc:
          xxx=xxb
          yyy=yy
     elif yyb==yyc:
          yyy=yyb
          xxx=xx
     else:
          b_bc=0; b_h=0
          k_bc=(yyb-yyc)/(xxb-xxc)
          b_bc=-xxc*k_bc + yyc
          k_h=-1/k_bc
          b_h=yy-k_h*xx

          kk=k_bc-k_h
          bb=b_h-b_bc
          xxx=bb/kk
          yyy=k_h*xxx+b_h

     canv.create_line(xxx + size/2,size/2 - yyy,xx + size/2,
                      size/2 - yy,width=3,fill="purple")

     canv.pack()
     root.mainloop()

def do():
     global N; global x; global y
     xx, yy, xxb, yyb, xxc, yyc, hh, mm = find_treug()
     ugl = degrees(acos(hh/mm))
     paint_treug(xx, yy, xxb, yyb, xxc, yyc)
     root.text_result.delete('1.0', END)
     root.text_result.insert(INSERT, 'Координаты треугольника\n')
     root.text_result.insert(INSERT, xx)
     root.text_result.insert(INSERT, ' ')
     root.text_result.insert(INSERT, yy)
     root.text_result.insert(INSERT, ' вершина\n')
     root.text_result.insert(INSERT, xxb)
     root.text_result.insert(INSERT, ' ')
     root.text_result.insert(INSERT, yyb)
     root.text_result.insert(INSERT, '\n')
     root.text_result.insert(INSERT, xxc)
     root.text_result.insert(INSERT, ' ')
     root.text_result.insert(INSERT, yyc)
     root.text_result.insert(INSERT, '\n Высота ')
     root.text_result.insert(INSERT, '{:.3f}'.format(hh))
     root.text_result.insert(INSERT, '\n Медиана ')
     root.text_result.insert(INSERT, '{:.3f}'.format(mm))
     root.text_result.insert(INSERT, '\n Угол ')
     root.text_result.insert(INSERT, '{:.3f}'.format(ugl))
                               
root = Tk()

root.title("Guide robot")
root.geometry('1000x550')
root.resizable(width=False, height=False)

# горячая клавиша - выход
root.bind('<Escape>',exit)

# метки поставноки задачи
root.lbl_zadacha = Label(root, text = "Решаемая задача", font = 'arial 10')
root.lbl_zadacha.place(x = 30, y = 0)
root.lbl_zadacha1 = Label(root, text = "Найти треугольник, у которого угол между высотой и", font = 'arial 10')
root.lbl_zadacha1.place(x = 0, y = 20)
root.lbl_zadacha2 = Label(root, text = "медианой, идущими из одной вершины, минимален.", font = 'arial 10')
root.lbl_zadacha2.place(x = 0, y = 40)

# метка статус
root.lbl_status = Label(root, text = "Статус", font = 'arial 14')
root.lbl_status.place(x = 120, y = 60)

# поле статуса
root.text_status = Text(root, height = 8, width = 26, font = 'Arial 14', wrap = WORD)
root.text_status.place(x = 10, y = 90)

# метка Результат
root.lbl_result = Label(root, text = "Результат", font = 'arial 14')
root.lbl_result.place(x = 120, y = 270)

# поле результата
root.text_result = Text(root, height = 10, width = 26, font = 'Arial 14', wrap = WORD)
root.text_result.place(x = 10, y = 300)

# метка х
root.lbl_point_x = Label(root, text = "Ввод Х", font = 'arial 10')
root.lbl_point_x.place(x = 350, y = 60)

# поле Х 
root.point_x = Entry(root, width = 6)
root.point_x.place(x = 400, y = 63)

# метка У
root.lbl_point_y = Label(root, text = "Ввод У", font = 'arial 10')
root.lbl_point_y.place(x = 465, y = 60)

# поле У
root.point_y = Entry(root, width = 6)
root.point_y.place(x = 515, y = 63)

# кнопка добавить точку
root.btn_new_point = Button(root, text = "Добавить точку", width = 22, height = 1, bg = 'dodgerblue',
                          fg = 'aliceblue', font = 'arial 12', command = insert_point)
root.btn_new_point.place(x = 350, y = 20)

# кнопка удалить точку
root.btn_delete_point = Button(root, text = "Удалить точку по номеру", width = 22, height = 1, bg = 'dodgerblue',
                               fg = 'aliceblue', font = 'arial 12', command = delete_point)
root.btn_delete_point.place(x = 600, y = 20)

# метка номера
root.lbl_number = Label(root, text = "Ввод номера", font = 'arial 10')
root.lbl_number.place(x = 600, y = 60)

# поле номера
root.entry_number = Entry(root, width = 6)
root.entry_number.place(x = 690, y = 63)

# кнопка удалить все точки
root.btn_delete_all = Button(root, text = "Удалить все точки", width = 22, height = 1, bg = 'dodgerblue',
                             fg = 'aliceblue', font = 'arial 12', command = delete_all)
root.btn_delete_all.place(x = 600, y = 90)

# кнопка Выполнить
root.btn_do = Button(root, text = 'Выполнить', width = 13, height = 3, bg = 'dodgerblue',
                        fg = 'aliceblue', font = 'arial 12', command = do)
root.btn_do.place(x = 850, y = 20)

# холст
canv = Canvas(root, width = 650, height = 380, bg = 'white')
canv.place(x = 330, y = 150)

# запускаем событийный цикл
root.mainloop()

# Рисуем треугольники
print()
print('Координаты нужного треугольника')
print(xx,yy,' , ',xxb,yyb,' , ',xxc,yyc)


