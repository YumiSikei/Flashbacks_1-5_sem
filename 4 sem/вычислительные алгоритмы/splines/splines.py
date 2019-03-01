from tkinter import *
import tkinter.messagebox as box
from tkinter.filedialog import *
#import fileinput
import random
import copy
import time
from math import *


EPS = 0.000000001

def func(x):
    return x*x*x - 0.7 # x*x*x*x*x + 3.56# x*x*x

def spline(lines):
    # сначала ище массив всех кси и тетта от 2 до n+1
    N = len(lines)
    ksi = [999]*(N -1)
    teta = [9]*(N -1)
    ksi[0] = 0 #(это под индеском 2)
    teta[0] = 0
    for k in range(1, N - 1):
        print(lines[k - 1][0], lines[k][0], lines[k + 1][0])
        Di = float(lines[k + 1][0]) - float(lines[k][0])# hi
        Bi = 2*((float(lines[k + 1][0]) - float(lines[k][0])) + float(lines[k][0]) - float(lines[k - 1][0]))# 2*(hi-1 + hi)
        Bi *= -1                                         # добавил
        Ai = float(lines[k][0]) - float(lines[k - 1][0]) # hi-1
        Fi = (float(lines[k + 1][1]) - float(lines[k][1]))/ Di # 3((yi - yi-1)/hi - (yi-1 - yi-2)/hi-1)
        Fi -= (float(lines[k][1]) - float(lines[k - 1][1]))/ Ai 
        Fi *= 3
        Fi *= -1
        ksi[k] = Di / (Bi - Ai*ksi[k-1])
        teta[k] = (Fi + Ai*teta[k-1]) / (Bi - Ai*ksi[k-1])


    print(ksi, "\n")
    print(teta, "\n")
    # получили кси и теты
    # теперь надо получить цешечки
    #koeffic = [[33]*(N - 1)]*4
    koeffic = [[33] * (N-1) for i in range(4)]
    Cnin1 = 0
    koeffic[2][N - 2] = ksi[N - 2]*Cnin1 + teta[N - 2] 
    koeffic[0][N - 2] = float(lines[N - 2][1])   #  fix было -2
    koeffic[1][N - 2] = (float(lines[N - 1][1]) - float(lines[N - 2][1])) / (float(lines[N - 1][0]) - float(lines[N - 2][0]))
    koeffic[1][N - 2] -= (float(lines[N - 1][0]) - float(lines[N - 2][0])) *( (Cnin1 +2*koeffic[2][N - 2])/3 ) # было +=
    koeffic[3][N - 2] = (Cnin1 - koeffic[2][N - 2]) / 3 # 
    koeffic[3][N - 2] /= float(lines[N - 1][0]) - float(lines[N - 2][0])
    for k in range(N - 3, -1, -1):
        #print(k, "aaaaaaaaa");
        koeffic[2][k] = ksi[k]*koeffic[2][k + 1] + teta[k]
        koeffic[0][k] = float(lines[k][1]) 
        koeffic[1][k] = (float(lines[k + 1][1]) - float(lines[k][1])) / (float(lines[k + 1][0]) - float(lines[k][0]))
        koeffic[1][k] -= (float(lines[k + 1][0]) - float(lines[k][0])) *( (koeffic[2][k + 1] +2*koeffic[2][k])/3 )
        koeffic[3][k] = (koeffic[2][k + 1] - koeffic[2][k]) / 3
        koeffic[3][k] /= float(lines[k + 1][0]) - float(lines[k][0])
    return koeffic


new= "x^3-0.7"# "x^2-5.txt" #"x^3-0.7.txt" #"x5+3.56.txt" #'x3.txt'
file=open(new,'r')
lines = []
li=[line for line in file]
for line in li:
    line=line.split() # двухмерный массив с точками
    # print(line)
    lines.append(line)
    #print("\n")
#print(lines)
file.close()
# готово
koeffic = spline(lines)
for i in range(4):
    print(koeffic[i], "  ")
    print("\n")

def interpolir_splines(x):
    ind = 0;
    for k in range(1, len(lines)):
        if (float(lines[k - 1][0]) < x <= float(lines[k][0])):
            ind = k - 1
            break
        if (k == len(lines) - 1):
            ind = k - 1
    # получен индекс левого края
    y = koeffic[0][ind]
    y += koeffic[1][ind]*(x -  float(lines[ind][0]))
    y += koeffic[2][ind]*((x - float(lines[ind][0]))**2)
    y += koeffic[3][ind]*((x - float(lines[ind][0]))**3)
    return y


def btn_do():
    x = entry_dot_x.get()
    if (x == ""):
        box.showinfo("Ошибка", "Введите x")
    #try:
    if (1):
        x = float(x)
        print(float(lines[0][0]) <= x <= float(lines[len(lines) - 1][0]));
        if (float(lines[0][0]) <= x <= float(lines[len(lines) - 1][0])):
            y_f = interpolir_splines(x)
            y_r = func(x)

            if (y_f == None):
                string = "    Ошибка\n\n" + "Нехватка точек для заданной степени полинома "
            else:
                string = "    Результат итерполяции " + str(y_f) + "\n\n" + "   Реальное значение " + str(y_r)
            text_result.delete(1.0, END)
            text_result.insert(1.0, string)
        else:
            box.showinfo("Ошибка", "эксраполяция недопустима ")
root = Tk()

root.title("heights and triangles")
root.geometry('400x400')

frame = Frame(root, width = 400, height = 400, bg = "grey20")
frame.place(x = 0, y = 0)

# поле кооординаты х
lbl_dot_x = Label(frame, text = "Ввод х",bg = 'grey20', fg = 'white', font = 'arial 10')
lbl_dot_x.place(x = 20, y = 30)


entry_dot_x = Entry(frame, width = 6)
entry_dot_x.place(x = 23, y = 50)

# делать
btn_DO = Button(frame, text = 'ИНТЕРПОЛИРОВАТЬ', width = 20, height = 3, bg = 'purple4', fg = 'aliceblue', font = 'arial 12', command = btn_do)
btn_DO.place(x = 180, y = 40)

# метка условие задачи
text1 = "Интерполировать функцию " + new
lbl_work1 = Label(frame, text = text1,bg = 'grey20', fg = 'aliceblue', font = 'arial 10')
lbl_work1.place(x = 70, y = 15)


# метка результат
lbl_result = Label(frame, text = "Результат",bg = 'grey20', fg = 'white', font = 'arial 14')
lbl_result.place(x = 70, y = 130)

# поле результат
text_result = Text(frame, height = 5 , width = 30, font = 'Arial 14', wrap = WORD)
text_result.place(x = 30, y = 160)

# запускаем событийный цикл
root.mainloop()

