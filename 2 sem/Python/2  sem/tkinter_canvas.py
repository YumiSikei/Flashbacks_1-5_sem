
# Пример графического модуля
from tkinter import *
root=Tk()

canv = Canvas(root,width=500,height=500,bg="lightblue")  # создание холста

canv.create_oval([120,200],[200,300],fill="peru")      # Эллипс
canv.create_oval([125,160],[195,210],fill="peru")
canv.create_arc([120,285],[150,315],start=0,extent=180, style=CHORD,fill="peru")
canv.create_arc([170,285],[200,315],start=0,extent=180, style=CHORD,fill="peru")

canv.create_line(135,200,185,200,width=1,fill="black") # moustage
canv.create_line(135,190,185,210,width=1,fill="black")
canv.create_line(135,210,185,190,width=1,fill="black")
canv.create_polygon([160,200],[152,192],[168,192],fill="firebrick") #nose

# paws
canv.create_polygon([180,220],[210,270],[220,273],[190,223],fill="peru", outline="black")


canv.create_text(20,30,text="Где Вячеслав",  # Текст
          font="Verdana 12",anchor="w",justify=CENTER)
canv.create_text(20,60,text="Туть",  # Текст
          font="Verdana 12",anchor="w",justify=CENTER)

canv.pack()
root.mainloop()
 
 
