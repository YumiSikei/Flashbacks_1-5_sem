import pygame
from pygame import *
from math import *

# Иницилиализируем pygame
pygame.init()	

# Создаем окно
DISPLAY = (1000, 700) 
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption('Window for drawing')

# Цикл событий
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Surface - Фон
    bg = Surface([1000, 700])
    bg.fill(Color('blue'))
    # Расположить Surface - Фон
    screen.blit(bg, (0, 0)) 

    # Рисуем в Surface - box1
    box = Surface([200, 200])
    TRANSPARENT_COLOR = Color("#123456")    # определяем прозрачный цвет
    box.set_colorkey(TRANSPARENT_COLOR)    # задаем для Surface прозрачный цвет 
    box.fill(TRANSPARENT_COLOR)            # заливаем Surface прозрачным цветом
    # Рисуем прямоугольник в расположении Rect
    pygame.draw.rect(box, Color("red"), Rect(0, 25, 50, 50), 0)
    # Рисуем окружность радиусом 10 с центром в (0, 0)
    pygame.draw.circle(box, Color("yellow"), (100, 100), 50, 0)
    # Рисуем зеленый полигон - треугольник
    pygame.draw.polygon(screen, Color("darkgreen"), ((30,30), (50,100), (90, 150), (120, 50)), 0)
    # Расположить Surface - box1
    screen.blit(box, (500, 200))
    
    # Рисуем прямо в окне
    # Эллипс в окне (находится под всеми Surface???)
    pygame.draw.ellipse(screen, Color("green"), Rect(500, 200, 100, 300), 0)
    # Черный отрезок
    pygame.draw.line(screen, Color("black"), (0, 0), (700, 500), 5)
    # Дуга
    pygame.draw.rect(screen, Color("red"), Rect(100, 100, 400, 400), 4)
    pygame.draw.arc(screen, Color("brown"), Rect(100, 100, 400, 400), 3*pi/2, 2*pi, 3)
    # Кусочно-линейная кривая
    pygame.draw.lines(screen, Color("yellow"), True, ( (30,30), (50,100), (90, 150), (120, 50)),0)
    
    # Обновление кадра
    pygame.display.update()

# Завершаем работу pygame
pygame.quit()
    
    
    
