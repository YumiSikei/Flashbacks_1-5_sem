from tkinter import *
from tkinter import messagebox
from math import sqrt, acos, degrees

#Таблица ячеек для ввода координат
class Table:

    FW = 5

    #Таблица ввода
    def __init__(self, root):
        self.root = root
        self.rows1 = []
        self.vars1 = []
        self.frame = Frame(self.root)
        Label(self.frame, text='N').grid(row=0, column=0)
        Label(self.frame, text='X').grid(row=0, column=1)
        Label(self.frame, text='Y').grid(row=0, column=2)
        self.add1()

    #Добавление ячейки в 1 мн-во
    def add1(self):
        n = len(self.rows1) + 1
        num = Label(self.frame, text=str(n), padx=5, pady=5)
        num.grid(row=n, column=0)

        xv = StringVar()
        x = Entry(self.frame, width=self.FW, textvariable=xv)
        x.grid(row=n, column=1, padx=5)

        yv = StringVar()
        y = Entry(self.frame, width=self.FW, textvariable=yv)
        y.grid(row=n, column=2, padx=5)

        d = Button(self.frame, text='Удалить')
        d.grid(row=n, column=3, padx=5, ipady=-0.2)
        d.bind('<Button-1>', lambda event: self.remove1(n - 1))

        self.rows1.append([num, x, y, d])
        self.vars1.append([xv, yv])       

    #Удаление ячейки из 1 мн-ва        
    def remove1(self, n):
        if len(self.rows1) > 0:
            for i in range(n, len(self.rows1) - 1):
                self.vars1[i][0].set(self.vars1[i + 1][0].get())
                self.vars1[i][1].set(self.vars1[i + 1][1].get())
            self.vars1.pop()
            row = self.rows1.pop()
            for w in row:
                w.destroy()
                
    #Удаление всех ячеек  
    def remove_all(self):
        for row in self.rows1:
            for w in row:
                w.destroy()     
        self.rows1 = []
        self.vars1 = []

    def clear(self):
        self.remove_all()
        self.add1()

    #Получение координат из ячеек
    def get_points(self):
        x = []
        y = []
        try:
            for row in self.vars1:
                xx = float(row[0].get())
                yy = float(row[1].get())
                x.append(xx)
                y.append(yy)
        except Exception as e:
            messagebox.showerror('Ошибка', 'Координаты должны быть вещественными')
            x = None
            y = None
        return x,y

    #Решение задачи
    def do(self):
        x, y = table.get_points()
        N = len(x)
        sizeW = 1000
        sizeH = 800
        if x is not None and y is not None:
            canv.delete('all')

            www = 0
            for i in range (N-1):
                for j in range (i+1, N):
                    if x[i]==x[j] and y[i]==y[j]:
                        www = 1

            if len(x) < 3:
                messagebox.showerror('Error', 'Количество точек должно быть не меньше 3')
            elif www == 1:
                messagebox.showerror('Error', 'У вас есть одинаковые точки. Измените так, чтобы все были различны')
            else:
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
                                 hma = ma / ha
                                 hmb = mb / hb
                                 hmc = mc / hc
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


                canv.create_line(xx + sizeW/2,sizeH/2 - yy,xxb + sizeW/2,sizeH/2 - yyb, width=3,fill="red")
                canv.create_line(xxc + sizeW/2,sizeH/2 - yyc,xxb + sizeW/2,sizeH/2 - yyb, width=3,fill="red")
                canv.create_line(xx + sizeW/2,sizeH/2 - yy,xxc + sizeW/2,sizeH/2 - yyc, width=3,fill="red")
                # Рисуем медиану и высоту
                canv.create_line(xx + sizeW/2,sizeH/2 - yy,(xxb+xxc)/2 + sizeW/2, sizeH/2 - (yyb+yyc)/2,width=3,fill="blue")

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

                canv.create_line(xxx + sizeW/2,sizeH/2 - yyy,xx + sizeW/2,
                                 sizeH/2 - yy,width=3,fill="purple")
                
                
                ugl = degrees(acos(hh/mm))
                string = 'Координаты\n'+str(xx)+' '+str(yy)+' -вершина\n'+str(xxb)+' '+str(yyb)+'\n'+str(xxc)+' '+str(yyc)+'\n'
                string = string + 'Высота '+str(round(hh, 2))+'\nМедиана '+str(round(mm, 3))+'\nУгол '+str(round(ugl, 3))
                messagebox.showinfo('Информация',string)

                canv.pack()
                root.mainloop()

#Вывод задания на экран
def info():
    messagebox.showinfo('Задание', 'Дано множество точек на плоскости.Найти треугольник, у которого угол между '
                        'высотой и медианой, идущими из одной вершины, минимален. ')
    
W = 1000 #Ширина экрана вывода
H = 800 #Высота экрана вывода
BORDER = 50 #Рамка экрана вывода (что бы точки не были на краю экрана)
PR = 4 #Ширина точки
TEXT_STEP = -14 #Отступ текста от точки 
TEXT_FONT = 'Arial 9' #Размер текста у точек

root = Tk()
root.title('Yanova, Lab 1')

left_side = Frame(root)
left_side.pack(side=LEFT, fill=Y)

buttons = Frame(left_side)
buttons.pack(fill=X)

buttons_up = Frame(buttons)
buttons_up.pack(fill=X)

add = Button(buttons_up, text='Задание', command=info)
add.pack(side=BOTTOM, padx=5, pady=5, fill=X, expand=True)

add = Button(buttons_up, text='Добавить точку', background='#7070ff', command=lambda: table.add1())
add.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

rem_b = Button(buttons_up, text='Удалить все', command=lambda: table.clear())
rem_b.pack(side=LEFT, padx=5, pady=5)

draw_b = Button(buttons, text='Выполнить', command=lambda: table.do())
draw_b.pack(padx=5, pady=5, fill=X)

out = Label(buttons, justify=LEFT)
out.pack(side=BOTTOM, fill=X)

table = Table(left_side)
table.frame.pack()

canv = Canvas(root, width=W, height=H, bg='white')
canv.pack()

root.mainloop()
