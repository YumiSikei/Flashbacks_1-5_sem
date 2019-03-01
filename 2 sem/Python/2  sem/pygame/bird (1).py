import pygame
from pygame import *


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
DISPLAY = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("bird")

x1 = 0; y1 = 0
x2 = 30; y2 = 0
x3 = 10; y3 =  10
x4 = 0; y4 = 30

x01 = 0 ; y01 = 0
x02 = 20; y02 = 10
x03 = 10; y03 = 10
x04 = 10; y04 = 20

xkoord = 9*SCREEN_WIDTH / 10
ykoord = SCREEN_HEIGHT / 8
n = 1
dx = 0
dy = 0

time  = 0
done = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1

    bg = Surface(DISPLAY)
    bg.fill(Color("light blue"))
    if time < 30:
        
        x_1 = xkoord + n*x1 + dx; y_1 = ykoord -n*y1 +dy
        x_2 = xkoord + x2*n + dx; y_2 = ykoord -y2*n +dy
        x_3 = xkoord + x3*n + dx; y_3 = ykoord -y3*n+dy
        x_4 = xkoord + x4*n + dx; y_4 = ykoord -y4*n+dy
    elif time <= 60:
        
        x_1 = xkoord + n*x01 + dx; y_1 = ykoord -n*y01 +dy
        x_2 = xkoord + x02*n + dx; y_2 = ykoord -y02*n +dy
        x_3 = xkoord + x03*n + dx; y_3 = ykoord -y03*n+dy
        x_4 = xkoord + x04*n + dx; y_4 = ykoord -y04*n+dy
    time +=1
    if time == 60:
        time = 0
    pygame.draw.polygon(bg, Color("white"),
         ((x_1,y_1),(x_2, y_2), (x_3, y_3), (x_4, y_4)), 0 )
    pygame.draw.polygon(bg, Color("black"),
         ((x_1,y_1),(x_2, y_2), (x_3, y_3), (x_4, y_4)), 2 )
    n +=.01
    dx -= 0.3
    dy +=0.3
    screen.blit(bg, (0,0))
    pygame.display.update()

pygame.quit()
