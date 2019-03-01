import pygame
from pygame import *
from math import *

# Иницилиализируем pygame
pygame.init()	

# Создаем окно
DISPLAY = (1000, 700) 
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption('Window for drawing')
 
# -------- Цикл главной программы -----------
# Начальная позиция прямоугольника
x = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Установить фон окна
    screen.fill(Color('blue'))
    

    bg = Surface([500,500])
    bg.fill(Color('yellow'))
    
    pygame.draw.rect(bg, Color('white'), [0, 50, 50 , 50])
    
    screen.blit(bg, [x,0])
    

    # Двигаем прямоугольник
    x += 1

    if x > 1000:
        x = 0
    
    # Обновление кадра
    pygame.display.update()

# Завершаем работу pygame
pygame.quit()
    
    
