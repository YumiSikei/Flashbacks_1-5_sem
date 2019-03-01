#Защита

from math import *
from tkinter import *

place = Tk()
size = 500
h = size // 2
canv = Canvas(place, width = size, height = size, bg = "lightblue")

def main():
    x_d = []
    y_d = []
    dots = int(input("Введите количество точек: "))
    for i in range(dots):
        s = input("Введите координаты точки: ")
        s = s.split()
        x_d.append(int(s[0]) + h)
        y_d.append(h - int(s[1]))

    x_c = []
    y_c = []
    r_c = []
    
    cir = int(input("Введите количество окружностей: "))
    for i in range(cir):
        s = input("Введите координаты точки и её радиус: ")
        s = s.split()
        x_c.append(int(s[0]) + h)
        y_c.append(h - int(s[1]))
        r_c.append(int(s[2]))



    min_dots = dots
    for i in range(len(x_c)):
        inside = 0
        outside = 0
        for j in range(len(x_d)):
            almost_r = sqrt(pow(x_c[i]-x_d[j],2) + pow(y_c[i]-y_d[j],2))
            if almost_r > r_c[i]:
                outside +=1
            else:
                inside +=1

        if (outside-inside) < min_dots:
            tmp = i
            min_dots = outside - inside

    canv.create_line(h, size, h, 0, width = 2, arrow = LAST) #ось Х
    canv.create_line(0, h, size, h, width = 2, arrow = LAST) #ось У
    canv.pack()
    
    for i in range(len(x_c)):
        if i != tmp:
            canv.create_oval([x_c[i]- r_c[i], y_c[i] - r_c[i]],[x_c[i] + r_c[i], y_c[i] + r_c[i]], fill="gray50")
            canv.pack()
        
    canv.create_oval([x_c[tmp]- r_c[tmp], y_c[tmp] - r_c[tmp]],[x_c[tmp] + r_c[tmp], y_c[tmp] + r_c[tmp]], fill="lightgreen")
    canv.pack()

    for i in range(len(x_d)):
        canv.create_oval([x_d[i]-2, y_d[i]-2], [x_d[i]+2, y_d[i]+2], fill = "blue")
        canv.pack()
    place.mainloop() 
        
        
            
if __name__ == '__main__':
    main()             
        
        
