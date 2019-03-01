import pygame
from pygame import *


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
DISPLAY = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("bird")

x1 = 0; y1 = 30
x2 = 30; y2 = 30
x3 = 10; y3 =  20
x4 = 0; y4 = 0
xkoord = 9*SCREEN_WIDTH / 10
ykoord = SCREEN_HEIGHT / 8
n = 1
dx = 0
dy = 0

done = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1

    bg = Surface(DISPLAY)
    bg.fill(Color("light blue"))

    x_1 = xkoord + n*x1 + dx; y_1 = ykoord +n*y1 +dy
    x_2 = xkoord + x2*n + dx; y_2 = ykoord +y2*n +dy
    x_3 = xkoord + x3*n + dx; y_3 = ykoord +y3*n+dy
    x_4 = xkoord + x4*n + dx; y_4 = ykoord +y4*n+dy
    pygame.draw.polygon(bg, Color("black"),

    ((x_1,y_1),(x_2, y_2), (x_3, y_3), (x_4, y_4)), 0 )
    n +=.007
    dx -= 0.1
    dy +=0.1
    screen.blit(bg, (0,0))
    pygame.display.update()

pygame.quit()
