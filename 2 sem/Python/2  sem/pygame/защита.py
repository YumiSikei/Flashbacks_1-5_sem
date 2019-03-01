#Доктор Артём
#Защита pygame

import pygame
import math

#Машина
def draw_car(screen, x, y):
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    #Тело машины
    poligon_car_points = [(x,y),(x + 15,y - 15),(x + 60, y - 15),
                            (x + 80, y - 35), (x + 105, y - 35),
                          (x + 120, y - 15),(x + 135, y - 15),
                          (x + 135,y+15), (x, y + 15)]
    pygame.draw.polygon(screen,yellow, poligon_car_points, 0)

    #Окно
    poligon_window_points = [(x + 60, y - 15),(x + 80, y - 35),
                             (x + 105, y - 35),(x + 105, y - 15),
                             (x + 60, y - 15)]
    pygame.draw.polygon(screen,blue, poligon_window_points, 0)

    #Шины
    pygame.draw.circle(screen, black, [x+20, y+5], 16, 0)
    pygame.draw.circle(screen, black, [x+120, y+5], 16, 0)

    #Лицо
    pygame.draw.circle(screen, white, [x+80, y-22], 8, 0)
    pygame.draw.circle(screen, black, [x+77, y-25], 3, 0)
    pygame.draw.circle(screen, black, [x+83, y-25], 3, 0)

    poligon_smile_points = [(x + 75, y - 20),(x + 80, y - 15),
                             (x + 85, y - 20),(x + 80, y - 17),
                            (x + 75, y - 20)]
    pygame.draw.polygon(screen,black, poligon_smile_points, 0)    

#Спица
def draw_luchi(screen,x1,y1,x2,y2,x3,y3,x4,y4):
    grey = (155,155,155)
    poligon_luchi_points = [(x1,y1),(x3,y3),(x4,y4),(x2,y2)]
    pygame.draw.polygon(screen,grey, poligon_luchi_points, 0)

#Поворот точки
def rotate(x_1,y_1):
    x_11 = x_1
    x_1 = x_center + (x_1 - x_center) * math.cos(0.09) + (
      (y_1 - y_center) * math.sin(0.09))
    y_1 = y_center + (y_1 - y_center) * math.cos(0.09) - (
      (x_11 - x_center) * math.sin(0.09))
    return x_1,y_1
    

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode([width, height])

x_car = 150
y_car = 300

x_center = x_car+20
y_center = y_car+5

#Координаты первой спицы
x_1 = x_center+14
y_1 = y_center+2
x_2 = x_center+14
y_2 = y_center-2
x_3 = x_center-14
y_3 = y_center+2
x_4 = x_center-14
y_4 = y_center-2

#Координаты второй спицы
x_5 = x_center+2
y_5 = y_center+14
x_6 = x_center+2
y_6 = y_center-14
x_7 = x_center-2
y_7 = y_center+14
x_8 = x_center-2
y_8 = y_center-14

clock = pygame.time.Clock()

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Рисуем небо и землю
    lightblue = (0, 200, 200)
    green = (0, 200, 0)
    pygame.draw.rect(screen, lightblue, [0, 0, width, height-305], 0)
    pygame.draw.rect(screen, green, [0, height - 305, width, 305], 0)
    
    #Изменение координат одной спицы        
    x_1,y_1 = rotate(x_1,y_1)
    x_2,y_2 = rotate(x_2,y_2)
    x_3,y_3 = rotate(x_3,y_3)
    x_4,y_4 = rotate(x_4,y_4)
    
    #Изменение координат второй спицы 
    x_5,y_5 = rotate(x_5,y_5)
    x_6,y_6 = rotate(x_6,y_6)
    x_7,y_7 = rotate(x_7,y_7)
    x_8,y_8 = rotate(x_8,y_8)
    
    #Машина
    draw_car(screen, x_car, y_car)
    
    #Первое колесо
    draw_luchi(screen, int(x_1), int(y_1), int(x_2), int(y_2),
               int(x_3), int(y_3), int(x_4), int(y_4))
    draw_luchi(screen, int(x_5), int(y_5), int(x_6), int(y_6),
               int(x_7), int(y_7), int(x_8), int(y_8))

    #Второе колесо
    draw_luchi(screen, int(x_1 + 100), int(y_1),int(x_2+100),
               int(y_2), int(x_3 + 100), int(y_3), int(x_4 + 100), int(y_4))
    draw_luchi(screen, int(x_5 + 100), int(y_5), int(x_6 + 100), int(y_6),
               int(x_7 + 100), int(y_7), int(x_8 + 100), int(y_8))
 
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
