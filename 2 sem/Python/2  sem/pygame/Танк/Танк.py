import pygame
from pygame import *
from math import *
import time

# Иницилиализируем pygame
pygame.init()	

# Создаем окно
DISPLAY = (1000, 700) 
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption('THE TANK')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               НАЧАЛЬНЫЕ КООРДИНАТЫ
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# облака
x_cloud1 =  -500
y_cloud1 =  0
x_cloud2 =  250
y_cloud2 = 70
x_cloud3 =  380
y_cloud3 = 30
x_cloud4 =  670
y_cloud4 = 80
x_cloud5 = 900
y_cloud5 = 40

# танк
x_surf_tank = -400
y_surf_tank = 450
xg = 50
xb = 70
teta = teta1 = 0
# полоски в колесах
x11 = x11_ = 50
y11 = y11_ = 100
x12 = x12_ = 50
y12 = y12_ = 140
x21 = x21_ = 30
y21 = y21_ = 120
x22 = x22_ = 70
y22 = y22_ = 120
# пуля
xp = 470

# самолёт
x_surf_plane = 1000
y_surf_plane = 0
# лопасти
xL = 5
yL1 = yL1_ = 40
yL2 = yL2_ = 90
Kx = Ky = 1

# Делает прозрачным Surface
def hide(surf):
    TRANSPARENT_COLOR = Color("#123456") # определяем прозрачный цвет
    surf.set_colorkey(TRANSPARENT_COLOR) # задаем для Surface прозрачный цвет 
    surf.fill(TRANSPARENT_COLOR)         # заливаем Surface прозрачным цветом



# Цикл событий
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # Задний фон
    background_image = pygame.image.load('phone.png').convert()
    screen.blit(background_image, [0,0])


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #                                ОБЛАКА
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # облако 1
    cloud1 = Surface([100, 50])
    hide(cloud1)           
    pygame.draw.ellipse(cloud1, Color("white"), Rect(10, 20, 40, 30), 0)
    pygame.draw.ellipse(cloud1, Color("white"), Rect(20, 10, 30, 30), 0)
    pygame.draw.ellipse(cloud1, Color("white"), Rect(40, 10, 35, 30), 0)
    pygame.draw.ellipse(cloud1, Color("white"), Rect(40, 30, 30, 20), 0)
    pygame.draw.ellipse(cloud1, Color("white"), Rect(40, 20, 40, 27), 0)
    screen.blit(cloud1, [x_cloud1, y_cloud1])
    
    x_cloud1 += 0.7
    if x_cloud1 >= 1000:
        x_cloud1 = -500
    
    # облако 2
    cloud2 = Surface([150, 70])
    hide(cloud2)
    pygame.draw.ellipse(cloud2, Color("white"), Rect(10, 20, 40, 30), 0)
    pygame.draw.ellipse(cloud2, Color("white"), Rect(20, 10, 30, 30), 0)
    pygame.draw.ellipse(cloud2, Color("white"), Rect(40, 10, 35, 30), 0)
    pygame.draw.ellipse(cloud2, Color("white"), Rect(30, 30, 40, 30), 0)
    pygame.draw.ellipse(cloud2, Color("white"), Rect(67, 40, 35, 20), 0)
    pygame.draw.ellipse(cloud2, Color("white"), Rect(85, 15, 40, 35), 0)
    pygame.draw.ellipse(cloud2, Color("white"), Rect(62, 10, 37, 40), 0)
    screen.blit(cloud2, [x_cloud2, y_cloud2])
    
    x_cloud2 += 0.5
    if x_cloud2 >= 1000:
        x_cloud2 = -150
    
    
    # облако 3
    cloud3 = Surface([150, 70])
    hide(cloud3)
    pygame.draw.ellipse(cloud3, Color("white"), Rect(10, 20, 30, 30), 0)
    pygame.draw.ellipse(cloud3, Color("white"), Rect(20, 10, 30, 30), 0)
    pygame.draw.ellipse(cloud3, Color("white"), Rect(40, 10, 35, 30), 0)
    pygame.draw.ellipse(cloud3, Color("white"), Rect(30, 30, 40, 30), 0)
    pygame.draw.ellipse(cloud3, Color("white"), Rect(57, 30, 35, 27), 0)
    pygame.draw.ellipse(cloud3, Color("white"), Rect(60, 15, 40, 35), 0)
    screen.blit(cloud3, [x_cloud3, y_cloud3])
    
    x_cloud3 += 0.6
    if x_cloud3 >= 1000:
        x_cloud3 = -150
    
    # облако 4
    cloud4 = Surface([100, 50])
    hide(cloud4)
    pygame.draw.ellipse(cloud4, Color("white"), Rect(10, 15, 30, 25), 0)
    pygame.draw.ellipse(cloud4, Color("white"), Rect(20, 7, 30, 20), 0)
    pygame.draw.ellipse(cloud4, Color("white"), Rect(24, 15, 30, 25), 0)
    pygame.draw.ellipse(cloud4, Color("white"), Rect(30, 10, 34, 24), 0)
    screen.blit(cloud4, [x_cloud4, y_cloud4])
    
    x_cloud4 += 1
    if x_cloud4 >= 1000:
        x_cloud4 = -100
    
    # облако 5
    cloud5 = Surface([100, 50])
    hide(cloud5)
    pygame.draw.ellipse(cloud5, Color("white"), Rect(10, 20, 40, 30), 0)
    pygame.draw.ellipse(cloud5, Color("white"), Rect(20, 10, 30, 30), 0)
    pygame.draw.ellipse(cloud5, Color("white"), Rect(40, 10, 35, 30), 0)
    pygame.draw.ellipse(cloud5, Color("white"), Rect(40, 30, 30, 20), 0)
    pygame.draw.ellipse(cloud5, Color("white"), Rect(40, 20, 40, 27), 0)
    screen.blit(cloud5, [x_cloud5, y_cloud5])
    
    x_cloud5 += 0.7
    if x_cloud5 >= 1000:
        x_cloud5 = -100
    

    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #                                ТАНК
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Surf_tank = Surface([400, 170])
    hide(Surf_tank)
    
    # тело гусениц
    pygame.draw.rect(Surf_tank, Color("darkolivegreen"), Rect(xg, 90, 200, 60), 0)
    pygame.draw.line(Surf_tank, Color("black"), (xg, 90), (xg + 200, 90), 3) 
    pygame.draw.line(Surf_tank, Color("black"), (xg, 150), (xg + 200, 150), 3)
    # окружности гусениц справа и слева 
    pygame.draw.circle(Surf_tank, Color("darkolivegreen"), (xg, 120), 30, 0)
    pygame.draw.arc(Surf_tank, Color("black"), Rect(xg - 30, 90, 80, 60), pi/2, 3*pi/2, 3)
    pygame.draw.circle(Surf_tank, Color("darkolivegreen"), (xg + 200, 120), 30, 0)
    pygame.draw.arc(Surf_tank, Color("black"), Rect(xg + 170, 90, 60 , 60), 3*pi/2, 5*pi/2, 3)

    # Функция колеса 
    def circle(xg, x11, y11, x12, y12, x21, y21, x22, y22):
        pygame.draw.circle(Surf_tank, Color("peachpuff4"), (xg, 120), 20, 0)
        pygame.draw.circle(Surf_tank, Color("black"), (xg, 120), 20, 2)
        pygame.draw.line(Surf_tank, Color("black"), (x11, y11), (x12, y12), 2)
        pygame.draw.line(Surf_tank, Color("black"), (x21, y21), (x22, y22), 2)
        pygame.draw.circle(Surf_tank, Color("peachpuff4"), (xg, 120), 7, 0)

    circle(xg, x11_, y11_, x12_, y12_, x21_, y21_, x22_, y22_)
    circle(xg + 200, x11_ + 200, y11_, x12_ + 200, y12_, x21_ + 200, y21_, x22_ + 200, y22_)
    circle(xg + 67, x11_ + 67, y11_, x12_ + 67, y12_, x21_ + 67, y21_, x22_ + 67, y22_)
    circle(xg + 134, x11_ + 134, y11_, x12_ + 134, y12_, x21_ + 134, y21_, x22_ + 134, y22_)

    # крутим колеса
    x11_ = xg + ((x11 - xg) * cos(teta) + (y11 - 120) * sin(teta))
    y11_ = 120 + ((y11 - 120) * cos(teta) + (x11 - xg) * sin(teta))
    x12_ = xg + ((x12 - xg) * cos(teta) + (y12 - 120) * sin(teta))
    y12_ = 120 + ((y12 - 120) * cos(teta) + (x12 - xg) * sin(teta))

    x21_ = xg + ((x21 - xg) * cos(teta1) + (y21 - 120) * sin(teta1))
    y21_ = 120 + ((y21 - 120) * cos(teta1) + (x21 - xg) * sin(teta1))
    x22_ = xg + ((x22 - xg) * cos(teta1) + (y22 - 120) * sin(teta1))
    y22_ = 120 + ((y22 - 120) * cos(teta1) + (x22 - xg) * sin(teta1))
    
    teta -= 0.1
    teta1 += 0.1
    
    # башня
    pygame.draw.rect(Surf_tank, Color("olivedrab"), Rect(xb, 50, 170, 40), 0)
    pygame.draw.rect(Surf_tank, Color("black"), Rect(xb, 50, 170, 40), 3)
    # звезда на башне
    pygame.draw.polygon(Surf_tank, Color("firebrick"),[(130, 55), (135, 65),
    (145, 65), (139, 70), (141, 80), (130, 73),
    (119, 80), (121, 70), (115, 65), (125, 65), ], 0)
    pygame.draw.polygon(Surf_tank, Color("black"),[(130, 55), (135, 65),
    (145, 65), (139, 70), (141, 80), (130, 73),
    (119, 80), (121, 70), (115, 65), (125, 65), ], 3)
    # люк
    pygame.draw.rect(Surf_tank, Color("darkolivegreen"), Rect(xb + 20, 40, 70, 10), 0)
    pygame.draw.rect(Surf_tank, Color("black"), Rect(xb + 20, 40, 70, 10), 3)
    # дуло
    pygame.draw.rect(Surf_tank, Color("black"), Rect(xb + 170, 60, 126, 13), 0)
    pygame.draw.rect(Surf_tank, Color("olivedrab"), Rect(xb + 170, 60, 126, 13), 2)
    
    # размещаем Surf_tank
    screen.blit(Surf_tank, [x_surf_tank, y_surf_tank])
    
    # летящая пуля в screen
    if x_surf_tank >= 60 and x_surf_tank <= 90:
        # искры
        pygame.draw.line(screen, Color("yellow"), (450, 510), (485, 500), 5)
        pygame.draw.line(screen, Color("red"), (450, 513), (490, 505), 5)
        pygame.draw.line(screen, Color("orange"), (450, 513), (495, 510), 5)
        pygame.draw.line(screen, Color("yellow"), (450, 513), (500, 515), 5)
        pygame.draw.line(screen, Color("orange"), (450, 514), (495, 520), 5)
        pygame.draw.line(screen, Color("red"), (450, 515), (490, 525), 5)
        pygame.draw.line(screen, Color("yellow"), (450, 517), (485, 530), 5)
        xp = 470
    if x_surf_tank >= 80:
        pygame.draw.polygon(screen, Color("dimgray"), [(xp, 510), (xp + 20, 510),
        (xp + 40, 516), (xp + 20, 523), (xp, 523) ], 0)
        pygame.draw.polygon(screen, Color("black"), [(xp, 510), (xp + 20, 510),
        (xp + 40, 516), (xp + 20, 523), (xp, 523) ], 3)
        xp += 8

    # Двигаем танк
    x_surf_tank += 4
    if x_surf_tank >= 1000:
        x_surf_tank = -400
    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #                           CАМОЛЁТ
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Surf_plane = Surface([180, 120])
    hide(Surf_plane)

    # корпус
    pygame.draw.polygon(Surf_plane, Color("darkseagreen"), [(15,50), (100,50),
    (130, 60), (145, 40), (170, 40), (150, 80), (15, 80)], 0)
    pygame.draw.polygon(Surf_plane, Color("black"), [(15,50), (100,50),
    (130, 60), (145, 40), (170, 40), (150, 80), (15, 80)], 2)
    
    # хвост
    pygame.draw.polygon(Surf_plane, Color("darkseagreen"), [(145, 58), (155, 58),
    (170, 70), (147, 70)], 0)
    pygame.draw.polygon(Surf_plane, Color("black"), [(145, 58), (155, 58),
    (170, 70), (147, 70)], 2)

    # кабина
    pygame.draw.polygon(Surf_plane, Color("lightcyan"), [(35,50), (40,40),
    (65, 40), (85, 50)], 0)
    pygame.draw.polygon(Surf_plane, Color("black"), [(35,50), (40,40),
    (65, 40), (85, 50)], 2)
    pygame.draw.line(Surf_plane, Color("black"), (50, 40), (50, 50), 2) 

    # крыло 1
    pygame.draw.polygon(Surf_plane, Color("darkseagreen"), [(65,40), (100,10),
    (120, 10), (100, 50), (85, 50)], 0)
    pygame.draw.polygon(Surf_plane, Color("black"), [(65,40), (100,10),
    (120, 10), (100, 50), (85, 50)], 2)

    # крыло 2
    pygame.draw.polygon(Surf_plane, Color("darkseagreen"), [(40,60), (85,60),
    (120, 110), (100, 115)], 0)
    pygame.draw.polygon(Surf_plane, Color("black"), [(40,60), (85,60),
    (120, 110), (100, 115)], 2)

    # лопасти
    pygame.draw.polygon(Surf_plane, Color("darkseagreen"), [(15,60), (15,70), (5,65)], 0)
    pygame.draw.polygon(Surf_plane, Color("black"), [(15,60), (15,70), (5,65)], 2)
    pygame.draw.line(Surf_plane, Color("black"), (xL, yL1_), (xL, yL2_), 4)

    # масштабируем лопасти
    yL1_ = 65 * (1 - Ky) + Ky * yL1
    yL2_ = 65 * (1 - Ky) + Ky * yL2
    Ky -= 0.1
    if Ky <= -1:
        Ky = 1
        
    # помещаем Surf_plane
    screen.blit(Surf_plane, [x_surf_plane, y_surf_plane])

    # двигаем самолёт
    x_surf_plane -= 6
    if  y_surf_plane != 40:
        y_surf_plane += 0.3
    if x_surf_plane <= -180 and x_surf_tank == -400:
        x_surf_plane = 1000
        y_surf_plane = 0

    
    # Обновление кадра
    pygame.display.update()

# Завершаем работу pygame
pygame.quit()
        
    
