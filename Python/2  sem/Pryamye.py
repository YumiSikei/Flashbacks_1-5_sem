#Вариант 14
#На плоскости задано множество прямых. Найти три прямые
#образующие треугольник минимальной площади

from math import *
from tkinter import *

#массивы точек линий

x1 = [] #абсцисса первой точки
x2 = [] #ордината первой точки
y1 = [] #абсцисса второй точки
y2 = [] #ордината второй точки


place = Tk() 
size = 500 #размер поля
h = size // 2 #середина поля
canv = Canvas(place, width = size, height = size, bg = "lightblue") #поле 


'''
-------------------------------Работа с канвой-----------------------------------------------------------------------------------------------------------
'''
def axis(): #оси 
    
    canv.create_line(h, size, h, 0, width = 2, arrow = LAST) #ось Х
    canv.create_line(0, h, size, h, width = 2, arrow = LAST) #ось У
    canv.pack()

def min_poly(poly): #треугольник минимальной площади
    canv.create_polygon(poly , fill="yellow")

def all_lines(x1, y1, x2, y2): #отрисовка каждой линии

    if (x1-x2) ==  0: #линия параллельна Оy
        canv.create_line(x1, 0, x2, size, width = 2, fill = "blue")
        canv.pack()
        
    else:
        k = (y1 - y2)/(x1 - x2) #тангенс наклона линии

        if k == 0: #линия параллельна Ох
            canv.create_line(0, y1, size, y2, width = 2, fill = "blue")
            canv.pack()
            
        elif k > 0: #угол наклона острый
            b = y1 - k*x1
            while x1 < size:
                x1 +=1
                y1 = k*(x1) + b
            while x2 > 0:
                x2 -=1
                y2 = k*(x2) + b
            canv.create_line(x1, y1, x2, y2, width = 2, fill = "blue")
            canv.pack()
            
        else: #угол наклона тупой
            b = y1 - k*x1
            while x1 > 0:
                x1 -=1
                y1 = k*(x1) + b
            while x2 < size:
                x2 +=1
                y2 = k*(x2) + b
            canv.create_line(x1, y1, x2, y2, width = 2, fill = "blue")
            canv.pack()
    

def canva(): #базовая отрисовка
    axis()
    min_poly(rem)
    for i in range(len(x1)):
        all_lines(x1[i], y1[i], x2[i], y2[i])

'''
-------------------------------Работа с данными-----------------------------------------------------------------------------------------------------------
'''


#точки пересечения
def search(x1, y1, x2, y2, x3, y3, x4, y4):

    #пересечение по Ох
    px = (x1*y2 - y1*x2)*(x3 - x4)
    px = px - (x1 - x2)*(x3*y4 - y3*x4)
    px = px / ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

    #пересечение по Оу
    py = (x1*y2 - y1*x2)*(y3 - y4)
    py = py - (y1 - y2)*(x3*y4 - y3*x4)
    py = py / ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

    return px, py


#площадь по пересечениям
def scalc(ax, ay, bx, by, cx, cy):
    
    a = sqrt((ax - bx) * (ax - bx) + (ay - by) * (ay - by)) #сторона а
    b = sqrt((bx - cx) * (bx - cx) + (by - cy) * (by - cy)) #сторона б
    c = sqrt((ax - cx) * (ax - cx) + (ay - cy) * (ay - cy)) #сторона с

    p = (a + b + c) /2 #полупериметр
    res = sqrt(p * (p - a) * (p - b) * (p - c)) #площаль

    return res



'''
-------------------------------Ввод данных-----------------------------------------------------------------------------------------------------------
'''


#ввод точек
def somelines():
    global x1, x2, y1, y2

    s = "*"
    
    while True :
        s = input("Введите координаты первой точки прямой: ")
        if s == "":
            if len(x1) <3:
                print("Необходимо ввести три и более прямых.")
                s = " "
            else:
                break
        s = s.split()
        while len(s) < 2:
            s = input("Введите координаты первой точки прямой: ")
            s = s.split()
            
        x1.append(int(s[0]) + h)
        y1.append(h - int(s[1]))

        s = input("Введите координаты второй точки прямой: ")
        s = s.split()

        while len(s) < 2:
            s = input("Введите координаты второй точки прямой: ")
            s = s.split()
        
        x2.append(int(s[0]) + h) #переход к системе координат канвы
        y2.append(h - int(s[1])) #переход к системе координат канвы


'''
-------------------------------Поиск прямых-----------------------------------------------------------------------------------------------------------
'''

def minsqr(x1, x2, y1, y2):
    global rem, minres
    minres = size*size

    for i in range(0, len(x1)-2, 1):
        for j in range(i+1, len(x1)-1, 1):
            for g in range(i+2, len(x1), 1):

                flag = True

                if x1[i] != x2[i]: #если линия не параллельна Оу
                    k1 = (y1[i]-y2[i])/(x1[i]-x2[i])
                else:
                    k1 = size

                if x1[j] != x2[j]: #если линия не параллельна Оу
                    k2 = (y1[j]-y2[j])/(x1[j]-x2[j])
                else:
                    k2 = size

                if x1[g] != x2[g]: #если линия не параллельна Оу
                    k3 = (y1[g]-y2[g])/(x1[g]-x2[g])
                else:
                    k3 = size

                
                if k1 != k2: #проверка на непараллельность
                    ax, ay = search(x1[i], y1[i],
                                    x2[i], y2[i],
                                    x1[j], y1[j],
                                    x2[j], y2[j])
                else:
                    flag = False
                    
                if k1 != k3: #проверка на непараллельность
                    bx, by = search(x1[i], y1[i],
                                    x2[i], y2[i],
                                    x1[g], y1[g],
                                    x2[g], y2[g])
                else:
                    flag = False
                    
                if k2 != k3: #проверка на непараллельность
                    cx, cy = search(x1[g], y1[g],
                                    x2[g], y2[g],
                                    x1[j], y1[j],
                                    x2[j], y2[j])
                else:
                    flag = False

                    
                if flag: #если образуется треугольник
                    #площадь треугольника
                    
                    res = scalc(ax, ay, bx, by, cx, cy)

                    #сравнение с минимальной площадью
                    if res < minres:
                        
                        minres = res
                        #координаты вершин треугольника
                        rem = [[ax, ay], [bx, by], [cx, cy]]
    print("Минимальная площадь равна %8.5f" % (minres))
    
    

'''
-------------------------------Тело программы-----------------------------------------------------------------------------------------------------------
'''

def main():
    
    somelines() #ввод линий

    rem = minsqr(x1, x2, y1, y2) #поиск линий по условию задачи
    canva() #отрисовка
    place.mainloop() #вывод на экран


if __name__ == '__main__':
    main()
    
    
    
    
    
            
