import pygame
from pygame import *
from math import pi, cos, sin, sqrt

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 400
DISPLAY = (SCREEN_WIDTH,SCREEN_HEIGHT)		# задаем размеры окна
											 
pygame.init()	# иницилиализируем pygame
screen = pygame.display.set_mode(DISPLAY)	# создаем окно
pygame.display.set_caption('Kvadrat')		# даем название окну

#основной цикл программы, где происходит рисование
done = False

x1 = 50
y1 = 300

x2 = 50
y2 = 200

x3 = 150
y3 = 200

x4 = 150
y4 = 300

x_center=150
y_center=300

fi=1
n=1
k=0

def rotate(x_1,y_1):
    x_11 = x_1
    x_1 = x_center + (x_1 - x_center) * cos(0.09) + (
      (y_1 - y_center) * sin(0.09))
    y_1 = y_center + (y_1 - y_center) * cos(0.09) - (
      (x_11 - x_center) * sin(0.09))
    return x_1,y_1

#Поворот точки
#def rotate(x_1,y_1,xx,x_center):
    #if xx==0:
     #   xx=100
    #    x_center+=100
    #x_11 = x_1
    #y_11=y_1
    #x_1=x_11+1
    #xx-=1
    #print(x1,x_center,xx)
    #yy=sqrt((x1-x_center)**2+(y1-y_center)**2-xx**2)
    #if (x_center-x_11)<=0:
    #    y_1=y_11-yy
    #else:
    #    y_1=y_11+yy
    #return x_1,y_1,xx,x_center

def treug(x1,y1,x2,y2,x3,y3,x4,y4,n):
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    col=[black,white,blue,yellow]
    if n==1 or n==5:
        n=1
        col=[black,white,blue,yellow]
    elif n==2:
        col=[yellow,black,white,blue]
    elif n==3:
        col=[blue,yellow,black,white]
    else:
        col=[white,blue,yellow,black]

    x1,y1 = rotate(x1,y1)
    x2,y2 = rotate(x2,y2)
    x3,y3 = rotate(x3,y3)
    x4,y4 = rotate(x4,y4)
    
    treug_points=[(x1,y1),(x1,y1-100),(x1+50,y1-50)]
    pygame.draw.polygon(screen, col[0],treug_points,0)
    treug_points=[(x2+100,y2),(x2+50,y2+50),(x2,y2)]
    pygame.draw.polygon(screen, col[1],treug_points,0)
    treug_points=[(x3,y3+100),(x3-50,y3+50),(x3,y3)]
    pygame.draw.polygon(screen, col[2],treug_points,0)
    treug_points=[(x4,y4),(x4-50,y4-50),(x4-100,y4)]
    pygame.draw.polygon(screen, col[3],treug_points,0)

    return n


#def root(x_1):
    #x_11 = x_1
    #if x_11>=(SCREEN_WIDTH+100):
        #x_11=-100
    #x_1 = x_11+1
    #return x_1


while not done:
	
         
    # обработка завершения работы программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # выход из цикла

    bg = Surface(DISPLAY)	    # создаем Surface с разрамерами окна
    bg.fill(Color("burlywood"))     # заливаем fon командой fill
    screen.blit(bg, (0,0))      # отображаем Surface с заливкой на основной
                                # холст в точке (0,0)


#--------Screen--------
    #if (x_center-x1)==100:
        #xx=100
    #x1,y1,xx,x_center= rotate(x1,y1,xx,x_center)

    #x1=int(x1)
    #y1=int(y1)

    if x1>1150:
        x1,x2,x3,x4==-50,-50,50,50


      # рисуем квадрат с разными треугольниками внутри
    #if k==500:
        #x1+=100
        #x2+=100
       # x3+=100
       # x4+=100
        #k=0
       # n+=1
    n=treug(x1,y1,x2,y2,x3,y3,x4,y4,n)
    k+=1


    #отображаем все изменения на экране
    pygame.display.update()


# завершаем работу pygame
pygame.quit()           
