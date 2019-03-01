import pygame
from pygame import *
from math import *

# Иницилиализируем pygame
pygame.init()	

# Создаем окно
DISPLAY = (1000, 700) 
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption('Window for drawing')

# Начальные координаты для куба
x_1 = x1 = 0
y_1 = y1 = 50
x_2 = x2 = 50
y_2 = y2 = 50
x_3 = x3 = 50
y_3 = y3 = 100
x_4 = x4 = 0
y_4 = y4 = 100
xc = 50
yc = 100
teta = 0

# Начальные координаты для треугольника
xt_1 = xt1 = 0
yt_1 = yt1 = 500
xt_2 = xt2 = 25
yt_2 = yt2 = 500 - sqrt(50**2 - 25**2)
xt_3 = xt3 = 50
yt_3 = yt3 = 500
xtc = 50
ytc = 500
tetat = 0

# -------- Цикл главной программы -----------
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(Color('mint cream'))
    bg = Surface([700,700])
    bg.fill(Color('snow3'))

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #                                          КУБ
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    pygame.draw.polygon(bg, Color('cyan'), ((x_1, y_1), (x_2 ,y_2), (x_3, y_3), (x_4, y_4)), 0)
    pygame.draw.polygon(bg, Color('blue'), ((x_1, y_1), (x_2 ,y_2), (x_3, y_3), (x_4, y_4)), 2)
    pygame.draw.line(bg, Color('black'), (0, 100), (1000, 100), 4)
    
    x_1 = xc + (x1-xc)*cos(teta) + (y1-yc)*sin(teta)
    y_1 = yc + (y1-yc)*cos(teta) - (x1-xc)*sin(teta)
    x_2 = xc + (x2-xc)*cos(teta) + (y2-yc)*sin(teta)
    y_2 = yc + (y2-yc)*cos(teta) - (x2-xc)*sin(teta)
    x_3 = xc + (x3-xc)*cos(teta) + (y3-yc)*sin(teta)
    y_3 = yc + (y3-yc)*cos(teta) - (x3-xc)*sin(teta)
    x_4 = xc + (x4-xc)*cos(teta) + (y4-yc)*sin(teta)
    y_4 = yc + (y4-yc)*cos(teta) - (x4-xc)*sin(teta)

    # Движение куба
    teta -= pi/300
    if abs(teta) > pi/2:
        teta = 0
        xc += 50
        x1 += 50
        x2 += 50
        x3 += 50
        x4 += 50

    # Повтор 
    if xc > 700:
        x_1 = x1 = 0
        y_1 = y1 = 50
        x_2 = x2 = 50
        y_2 = y2 = 50
        x_3 = x3 = 50
        y_3 = y3 = 100
        x_4 = x4 = 0
        y_4 = y4 = 100
        xc = 50
        yc = 100
        teta = 0
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #                                     ТРЕУГОЛЬНИК
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    pygame.draw.polygon(bg, Color('cyan'), ((xt_1, yt_1), (xt_2 ,yt_2), (xt_3, yt_3)), 0)
    pygame.draw.polygon(bg, Color('blue'), ((xt_1, yt_1), (xt_2 ,yt_2), (xt_3, yt_3)), 2)
    pygame.draw.line(bg, Color('black'), (0, 500), (1000, 500), 4)
    
    xt_1 = xtc + (xt1-xtc)*cos(tetat) + (yt1-ytc)*sin(tetat)
    yt_1 = ytc + (yt1-ytc)*cos(tetat) - (xt1-xtc)*sin(tetat)
    xt_2 = xtc + (xt2-xtc)*cos(tetat) + (yt2-ytc)*sin(tetat)
    yt_2 = ytc + (yt2-ytc)*cos(tetat) - (xt2-xtc)*sin(tetat)
    xt_3 = xtc + (xt3-xtc)*cos(tetat) + (yt3-ytc)*sin(tetat)
    yt_3 = ytc + (yt3-ytc)*cos(tetat) - (xt3-xtc)*sin(tetat)


    # Движение треугольника
    tetat -= pi/200
    if abs(tetat) > pi - pi/3:
        tetat = 0
        xtc += 50
        xt1 += 50
        xt2 += 50
        xt3 += 50

    # Повтор 
    if xtc > 700:
        xt_1 = xt1 = 0
        yt_1 = yt1 = 500
        xt_2 = xt2 = 25
        yt_2 = yt2 = 500 - sqrt(50**2 - 25**2)
        xt_3 = xt3 = 50
        yt_3 = yt3 = 500
        xtc = 50
        ytc = 500
        tetat = 0

    screen.blit(bg, [0,0])
    
    # Обновление кадра
    pygame.display.update()

# Завершаем работу pygame
pygame.quit()
    
