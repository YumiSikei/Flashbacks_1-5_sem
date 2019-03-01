#Янова Даниэлла ИУ7-43
#Дано множество точек на плоскости.Найти треугольник, у которого угол между
#высотой и медианой, идущими из одной вершины, минимален.

from math import *
from tkinter import *
from math import sin, cos

X=[]
Y=[]
X_start = []
Y_start = []
X_past = []
Y_past = []

# масштабирование 
def scale(X, Y, xm, ym, kx, ky): 
    n = len(X) 
    for i in range(n): 
        X[i] = kx * X[i] + (1 - kx) * xm 
        Y[i] = ky * Y[i] + (1 - ky) * ym 
    return X, Y

# поворот
def turn(X, Y, xc, yc, a):
    a = a / 180 * pi
    n = len(X)
    for i in range(n):
        tx = X[i]
        X[i] = xc + (X[i] - xc) * cos(a) + (Y[i] - yc) * sin(a)
        Y[i] = yc - (tx - xc) * sin(a) + (Y[i] - yc) * cos(a)
    return X, Y

# найти точки эллипса
def oval(x0, y0, a, b):
    t = 0
    X = []
    Y = []
    while (t <= 2 * pi):
        x = x0 + a * cos(t);
        y = y0 + b * sin(t); 
        t += 0.005
        X.append(x)
        Y.append(y)
    return X, Y

# рисовать по пикселям
def draw_by_pxl(X, Y):
    n = len(X)
    for i in range(n):
        canv.create_oval([X[i],Y[i]], [X[i] + 1, Y[i] + 1])

def draw(X, Y):
     canv.create_line(xx + size/2,size/2 - yy,xxb + size/2,size/2 - yyb,
                      width=3,fill="red")
     canv.create_line(xxc + size/2,size/2 - yyc,xxb + size/2,size/2 - yyb,
                      width=3,fill="red")
     canv.create_line(xxa + size/2,size/2 - yy,xxc + size/2,size/2 - yyc,
                      width=3,fill="red")

     canv.create_line(xx + size/2,size/2 - yy,(xxb+xxc)/2 + size/2,
                      size/2 - (yyb+yyc)/2,width=3,fill="blue")

     canv.create_line(xxx + size/2,size/2 - yyy,xx + size/2,
                      size/2 - yy,width=3,fill="purple")
     xo,yo = oval(X[],Y[],X[],Y[])
     draw_by_pxl(xo,yo)

     canv.pack()
     root.mainloop()

def do(k):
    global X; global Y; global X_start; global Y_start
    global X_past; global Y_past
    
    if k == 1: #start view
        X_past = X;  Y_past = Y
        X = X_start; Y_start = Y
    elif k == 2: #step_back
        X = X_past; Y_past = Y
    elif k == 3: #perenos
        hx = .get()
        hy = .get()
        X,Y = perenos(X,Y)
    elif k == 4: #masshtab
        kx = .get()
        ky = .get()
        xc = .get()
        yc = .get()
        X,Y = scale(X,Y,xc,yc,kx,ky)
    else: #turn
        xc = .get()
        yc = .get()
        a = .get()
        X,Y = turn(X,Y,xc,yc,a)
        
    draw(X,Y)
                               
root = Tk()

root.title("Guide robot")
root.geometry('1000x550')
root.resizable(width=False, height=False)

# горячая клавиша - выход
root.bind('<Escape>',exit)



# метка х переноса
lbl_perenos_x = Label(root, text = "По ОХ", font = 'arial 10')
lbl_perenos_x.place(x = 350, y = 60)

# поле Х переноса
perenos_x = Entry(root, width = 6)
perenos_x.place(x = 400, y = 63)

# метка У переноса
lbl_perenos_y = Label(root, text = "По ОУ", font = 'arial 10')
bl_perenos_y.place(x = 465, y = 60)

# поле У переноса
perenos_y = Entry(root, width = 6)
perenos_y.place(x = 515, y = 63)

# кнопка переноса
btn_perenos = Button(root, text = "Перенести", width = 22, height = 1, bg = 'dodgerblue',
                          fg = 'aliceblue', font = 'arial 12', command = do(3))
btn_perenos.place(x = 350, y = 20)



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
canv.place(x = 700, y = 500)

#Ушки
X_start.append(-50); X_start.append(-40); X_start.append(-15)
Y_start.append(0); Y_start.append(100); Y_start.append(47)

# запускаем событийный цикл
root.mainloop()


