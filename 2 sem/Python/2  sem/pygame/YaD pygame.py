import pygame
from pygame import *
from math import pi, cos, sin

SCREEN_WIDTH = 950
SCREEN_HEIGHT = 700
DISPLAY = (SCREEN_WIDTH,SCREEN_HEIGHT)		# задаем размеры окна
											 
pygame.init()	# иницилиализируем pygame
screen = pygame.display.set_mode(DISPLAY)	# создаем окно
pygame.display.set_caption('Romantic')		# даем название окну

#основной цикл программы, где происходит рисование
done = False

kach_WIDTH =  125                 # ширина качелей
kach_HEIGHT =  200                # высота качелей

fstar_WIDTH =  125                 # ширина падающей звезды
fstar_HEIGHT =  100                # высота падающей звезды

x1 = 620
y1 = 225

x2 = -50
y2 = 100

x_center=706
y_center=225

fi=1

#Поворот точки
def rotate(x_1,y_1,fi):
    x_11 = x_1
    y_11 = y_1
    if x1>650 or x1<600:
        fi*=-1
    x_1 = x_11+fi
    y_1 = y_11+fi
    return x_1,y_1,fi

def root(x_1,y_1):
    x_11 = x_1
    y_11 = y_1
    if x_11>=1050:
        x_11=-50
        y_11=100
    x_1 = x_11+2
    y_1 = y_11+1
    return x_1,y_1

while not done:
	
         
    # обработка завершения работы программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # выход из цикла

    bg = Surface(DISPLAY)	    # создаем Surface с разрамерами окна
    bg.fill(Color("dark slate blue"))     # заливаем голубым цветом командой fill
    screen.blit(bg, (0,0))      # отображаем Surface с заливкой на основной
                                # холст в точке (0,0)


#--------Screen--------

    #----Fall-Star
    fstar = Surface( (DISPLAY) )    # создаем Surface для звезды
                                                # с ее размерами
    TRANSPARENT_COLOR = Color("#123456")   # определяем прозрачный цвет
    fstar.set_colorkey(TRANSPARENT_COLOR)    # задаем для surface прозрачный цвет 
    fstar.fill(TRANSPARENT_COLOR)            # заливаем surface прозрачным цветом

    x2,y2=root(x2,y2)
    x2=int(x2)
    y2=int(y2)

    poligon_tale1_points = [(x2+10,y2+40),(x2+20,y2+45),(x2+55,y2+37),
                            (x2+51,y2+32)]
    pygame.draw.polygon(fstar, Color("maroon"),poligon_tale1_points, 0)

    poligon_tale2_points = [(x2+55,y2+37),(x2+20,y2+45),(x2+15,y2+55),(x2+25,y2+57),
                            (x2+65,y2+42)]
    pygame.draw.polygon(fstar, Color("dark orange"),poligon_tale2_points, 0)

    poligon_tale3_points = [(x2+65,y2+42),(x2+25,y2+57),(x2+25,y2+67),
                            (x2+55,y2+49)]
    pygame.draw.polygon(fstar, Color("orchid"),poligon_tale3_points, 0)

    poligon_star_points = [(x2+70,y2+15),(x2+60,y2+30),(x2+45,y2+30),(x2+58,y2+40),
                           (x2+50,y2+55),(x2+70,y2+44),
                           (x2+90,y2+55),(x2+82,y2+40),(x2+95,y2+30),(x2+80,y2+30)]
    pygame.draw.polygon(fstar, Color("gold"),poligon_star_points, 0)

    screen.blit(fstar, (0,0) )
    

    
    # рисуем землю
    pygame.draw.ellipse(screen, Color("dark olive green"),
                    Rect(-300,400, 2000, 1000), 0)

    #Рисуем дерево
    pygame.draw.rect(screen, Color("saddle brown"), Rect(550, 220, 50, 270), 0)

    pygame.draw.ellipse(screen, Color("forest green"),
                        Rect(SCREEN_WIDTH//2,50, 200,100), 0)
    pygame.draw.ellipse(screen, Color("forest green"),
                        Rect(SCREEN_WIDTH//2,125, 200,100), 0)
    pygame.draw.ellipse(screen, Color("forest green"),
                        Rect(SCREEN_WIDTH//2,200, 200,100), 0)
    pygame.draw.ellipse(screen, Color("forest green"),
                        Rect(SCREEN_WIDTH//2+100,100, 200,100), 0)
    pygame.draw.ellipse(screen, Color("forest green"),
                        Rect(SCREEN_WIDTH//2+100,150, 200,100), 0)
    pygame.draw.ellipse(screen, Color("forest green"),
                        Rect(SCREEN_WIDTH//2-100,100, 200,100), 0)
    pygame.draw.ellipse(screen, Color("forest green"),
                        Rect(SCREEN_WIDTH//2-100,150, 200,100), 0)

    
    # рисуем звезды на небе
    poligon_star_points = [(50,15),(40,30),(25,30),(38,40),(30,55),(50,44),
                           (70,55),(62,40),(75,30),(60,30)]
    pygame.draw.polygon(screen, Color("gold"),poligon_star_points, 0)


    poligon_star_points = [(250,315), (240,330), (225, 330), (238, 340), (230, 355),
                        (250,344),(270,355),(262,340), (275,330), (260,330)]
    pygame.draw.polygon(screen, Color("gold"),poligon_star_points, 0)


    poligon_star_points = [(850,115), (840,130), (825, 130), (838, 140), (830, 155),
                        (850,144), (870, 155), (862,140),(875,130),(860,130)]
    pygame.draw.polygon(screen, Color("gold"),poligon_star_points, 0)

    #Moon
    pygame.draw.ellipse(screen, Color("light goldenrod"),
                        Rect(140,50, 60,60), 0)
    pygame.draw.ellipse(screen, Color("dark slate blue"),
                        Rect(165,64, 50,50), 0)

    #-----Kacheli
    kach = Surface( DISPLAY )    # создаем Surface для качелей
                                                # с ее размерами

    TRANSPARENT_COLOR = Color("#123456")   # определяем прозрачный цвет
    kach.set_colorkey(TRANSPARENT_COLOR)    # задаем для surface прозрачный цвет 
    kach.fill(TRANSPARENT_COLOR)            # заливаем surface прозрачным цветом

    x1,y1,fi=rotate(x1,y1,fi)
    x1=int(x1)
    y1=int(y1)

      #рисуем качели
    pygame.draw.line(kach, Color("sandy brown"),(623,225),(x1+3,y1+200), 5)
    pygame.draw.line(kach, Color("sandy brown"),(737,225),(x1+117,y1+200), 5)
    #pygame.draw.rect(kach, Color("sandy brown"), Rect(x1+3, y1+30, 5, 170), 5)
    #pygame.draw.rect(kach, Color("sandy brown"), Rect(x1+117, y1, 5, 200), 0)
    pygame.draw.rect(kach, Color("black"), Rect(x1, y1+180, 125, 10), 0)
    
      # рисуем Настю и Тёму
    pygame.draw.line(kach, Color("antique white"),(x1+25,y1+180),(x1+20,y1+195), 5)
    pygame.draw.line(kach, Color("antique white"),(x1+45,y1+180),(x1+40,y1+195), 5)
    pygame.draw.line(kach, Color("antique white"),(x1+30,y1+150),(x1+5,y1+160), 3)
    pygame.draw.line(kach, Color("antique white"),(x1+40,y1+150),(x1+65,y1+160), 3)
    treug_points=[(x1+15,y1+180),(x1+35,y1+140),(x1+55,y1+180)]
    pygame.draw.polygon(kach, Color("salmon"),treug_points,0)
    pygame.draw.circle(kach, Color("antique white"), (x1+35,y1+132), 12, 0)
    pygame.draw.arc(kach,Color("burlywood"),[x1+42,y1+120,12,12],  0, pi, 5)
    pygame.draw.arc(kach,Color("burlywood"),[x1+15,y1+120,12,12],  0, pi, 5)
    pygame.draw.arc(kach,Color("burlywood"),[x1+30,y1+120,12,12],  0, pi, 5)
    pygame.draw.arc(kach,Color("burlywood"),[x1+29,y1+120,12,12],  0, pi, 5)

    pygame.draw.line(kach, Color("antique white"),(x1+80,y1+180),(x1+75,y1+195), 5)
    pygame.draw.line(kach, Color("antique white"),(x1+100,y1+180),(x1+95,y1+195), 5)
    pygame.draw.line(kach, Color("antique white"),(x1+65,y1+160),(x1+90,y1+150), 3)
    pygame.draw.line(kach, Color("antique white"),(x1+125,y1+160),(x1+100,y1+150), 3)
    rect_points=[(x1+78,y1+180),(x1+90,y1+140),(x1+98,y1+140),(x1+102,y1+180)]
    pygame.draw.polygon(kach, Color("blue"),rect_points,0)
    pygame.draw.circle(kach, Color("antique white"), (x1+93,y1+132), 12, 0)
    pygame.draw.arc(kach,Color("black"),[x1+86,y1+120,12,12],  0, pi, 5)
    pygame.draw.arc(kach,Color("black"),[x1+88,y1+120,12,12],  0, pi, 5)
    pygame.draw.arc(kach,Color("black"),[x1+89,y1+120,12,12],  0, pi, 5)
    pygame.draw.arc(kach,Color("black"),[x1+85,y1+120,12,12],  0, pi, 5)
    

    screen.blit(kach, (0,0) )


    #отображаем все изменения на экране
    pygame.display.update()


# завершаем работу pygame
pygame.quit()           
