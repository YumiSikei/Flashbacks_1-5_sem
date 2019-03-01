#Янова Даниэлла ИУ7-43
#Дано множество точек на плоскости.Найти треугольник, у которого угол между
#высотой и медианой, идущими из одной вершины, минимален.

from math import *
from tkinter import *
from math import sin, cos
import copy

X=[]
Y=[]

root = Tk()

root.title("Guide robot")
root.geometry('1000x700')
root.resizable(width=False, height=False)

# холст
canv = Canvas(root, width = 700, height = 650, bg = 'white')
canv.place(x =5, y = 5)
x_size = 350
y_size = 250

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

# поворот
def turn(X, Y, xc, yc, a):
    a = a / 180 * pi
    n = len(X)
    for i in range(n):
        tx = X[i]
        X[i] = xc + (X[i] - xc) * cos(a) + (Y[i] - yc) * sin(a)
        Y[i] = yc - (tx - xc) * sin(a) + (Y[i] - yc) * cos(a)
    return X, Y

# рисовать по пикселям
def draw_by_pxl(X, Y):
    n = len(X)
    for i in range(n):
        canv.create_oval([X[i],Y[i]], [X[i] + 1, Y[i] + 1])

def draw(X, Y):
    canv.delete('all')
    
    #рисуем ушки
    canv.create_line(X[0],Y[0],X[1],Y[1], width=3,fill="black")
    canv.create_line(X[1],Y[1],X[2],Y[2], width=3,fill="black")
    canv.create_line(X[3],Y[3],X[4],Y[4], width=3,fill="black")
    canv.create_line(X[4],Y[4],X[5],Y[5], width=3,fill="black")

    #рисуем усики
    canv.create_line(X[6],Y[6],X[7],Y[7], width=3,fill="black")
    canv.create_line(X[8],Y[8],X[9],Y[9], width=3,fill="black")
    canv.create_line(X[10],Y[10],X[11],Y[11], width=3,fill="black")

    #рисуем круги/овалы
    XX=[]; YY=[]
    for i in range (12,len(X)):
        XX.append(X[i])
        YY.append(Y[i])
    draw_by_pxl(XX,YY)

    #canv.pack()
    root.mainloop()

def do_turn():
    global X; global Y; global X_past; global Y_past
    X_past = copy.copy(X); Y_past = copy.copy(Y)
    
    try:
        xc = x_size + float(povorot_x.get())
        yc = y_size - float(povorot_y.get())
        a = float(povorot_k.get())
        X,Y = turn(X,Y,xc,yc,a)
    except Exception as e:
        string = 'Числа должны быть вещественные'
        messagebox.showinfo('Ошибка',string)
        
    draw(X,Y)
    


# горячая клавиша - выход
root.bind('<Escape>',exit)



# кнопка изначальное положение
btn_start = Button(root, text = "Изначальное\nположение", width = 22, height = 1,
                   bg = 'dodgerblue', fg = 'aliceblue', font = 'arial 12', command = do_start)
btn_start.place(x = 750, y = 320)

# кнопка шаг назад
btn_past = Button(root, text = "Шаг назад", width = 22, height = 1, bg = 'dodgerblue',
                          fg = 'aliceblue', font = 'arial 12', command = do_step_back)
btn_past.place(x = 750, y = 360)


# метка переноса
lbl_perenos = Label(root, text = "Перенос", font = 'arial 10')
lbl_perenos.place(x = 800, y = 5)

# метка х переноса
lbl_perenos_x = Label(root, text = "По ОХ", font = 'arial 10')
lbl_perenos_x.place(x = 710, y = 25)

# поле Х переноса
perenos_x = Entry(root, width = 6)
perenos_x.place(x = 760, y = 25)

# метка У переноса
lbl_perenos_y = Label(root, text = "По ОУ", font = 'arial 10')
lbl_perenos_y.place(x = 820, y = 25)

# поле У переноса
perenos_y = Entry(root, width = 6)
perenos_y.place(x = 870, y = 25)

# кнопка переноса
btn_perenos = Button(root, text = "Перенести", width = 22, height = 1, bg = 'dodgerblue',
                          fg = 'aliceblue', font = 'arial 12', command = do_perenos)
btn_perenos.place(x = 750, y = 50)


# метка масштабирования
lbl_mashtab = Label(root, text = "Масштабирование", font = 'arial 10')
lbl_mashtab.place(x = 800, y = 90)

# метка х масштабирования
lbl_mashtab_x = Label(root, text = "Xс По ОХ", font = 'arial 10')
lbl_mashtab_x.place(x = 710, y = 115)

# поле Х масштабирования
mashtab_x = Entry(root, width = 6)
mashtab_x.place(x = 775, y = 115)

# метка У масштабирования
lbl_mashtab_y = Label(root, text = "Yс По ОУ", font = 'arial 10')
lbl_mashtab_y.place(x = 830, y = 115)

# поле У масштабирования
mashtab_y = Entry(root, width = 6)
mashtab_y.place(x = 895, y = 115)

# метка Kx масштабирования
lbl_mashtab_kx = Label(root, text = "K По ОХ", font = 'arial 10')
lbl_mashtab_kx.place(x = 710, y = 140)

# поле Kx масштабирования
mashtab_kx = Entry(root, width = 6)
mashtab_kx.place(x = 775, y = 140)

# метка kУ масштабирования
lbl_mashtab_ky = Label(root, text = "K По ОУ", font = 'arial 10')
lbl_mashtab_ky.place(x = 830, y = 140)

# поле kУ масштабирования
mashtab_ky = Entry(root, width = 6)
mashtab_ky.place(x = 895, y = 140)

# кнопка масштабирования
btn_mashtab = Button(root, text = "Масштабировать", width = 22, height = 1, bg = 'dodgerblue',
                          fg = 'aliceblue', font = 'arial 12', command = do_mashtab)
btn_mashtab.place(x = 750, y = 165)


# метка поворота
lbl_povorot = Label(root, text = "Поворот", font = 'arial 10')
lbl_povorot.place(x = 800, y = 205)

# метка х поворота
lbl_povorot_x = Label(root, text = "Xс По ОХ", font = 'arial 10')
lbl_povorot_x.place(x = 710, y = 230)

# поле Х поворота
povorot_x = Entry(root, width = 6)
povorot_x.place(x = 775, y = 230)

# метка У поворота
lbl_povorot_y = Label(root, text = "Yс По ОУ", font = 'arial 10')
lbl_povorot_y.place(x = 830, y = 230)

# поле У поворота
povorot_y = Entry(root, width = 6)
povorot_y.place(x = 895, y = 230)

# метка K поворота
lbl_povorot_k = Label(root, text = "Угол(град)", font = 'arial 10')
lbl_povorot_k.place(x = 750, y = 255)

# поле K поворота
povorot_k = Entry(root, width = 6)
povorot_k.place(x = 815, y = 255)

# кнопка поворота
btn_povorot = Button(root, text = "Повернуть", width = 22, height = 1, bg = 'dodgerblue',
                          fg = 'aliceblue', font = 'arial 12', command = do_turn)
btn_povorot.place(x = 750, y = 280)


# запускаем событийный цикл
root.mainloop()



