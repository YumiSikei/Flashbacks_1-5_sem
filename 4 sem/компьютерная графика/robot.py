from tkinter import *

root = Tk()

root.title("Guide robot")
root.geometry('1000x550')
root.resizable(width=False, height=False)

# горячая клавиша - выход
root.bind('<Escape>',exit)

# метки поставноки задачи
root.lbl_zadacha = Label(root, text = "Решаемая задача", font = 'arial 10')
root.lbl_zadacha.place(x = 30, y = 0)
root.lbl_zadacha1 = Label(root, text = "Найти треугольник, у которого угол между высотой и", font = 'arial 10')
root.lbl_zadacha1.place(x = 0, y = 20)
root.lbl_zadacha2 = Label(root, text = "медианой, идущими из одной вершины, минимален.", font = 'arial 10')
root.lbl_zadacha2.place(x = 0, y = 40)

# метка статус
root.lbl_status = Label(root, text = "Статус", font = 'arial 14')
root.lbl_status.place(x = 120, y = 60)

# поле статуса
root.text_status = Text(root, height = 8, width = 26, font = 'Arial 14', wrap = WORD)
root.text_status.place(x = 10, y = 90)

# метка Решение
root.lbl_result = Label(root, text = "Результат", font = 'arial 14')
root.lbl_result.place(x = 120, y = 270)

# поле решения
root.text_result = Text(root, height = 10, width = 26, font = 'Arial 14', wrap = WORD)
root.text_result.place(x = 10, y = 300)

# метка х
root.lbl_height = Label(root, text = "Ввод Х", font = 'arial 10')
root.lbl_height.place(x = 350, y = 60)

# поле Х 
root.entry_height = Entry(root, width = 6)
root.entry_height.place(x = 400, y = 63)

# метка У
root.lbl_length = Label(root, text = "Ввод У", font = 'arial 10')
root.lbl_length.place(x = 465, y = 60)

# поле У
root.entry_length = Entry(root, width = 6)
root.entry_length.place(x = 515, y = 63)

# кнопка добавить точку
root.btn_new_map = Button(root, text = "Добавить точку", width = 22, height = 1, bg = 'dodgerblue', fg = 'aliceblue', font = 'arial 12')
root.btn_new_map.place(x = 350, y = 20)

# кнопка удалить точку
root.btn_take_map = Button(root, text = "Удалить точку по номеру", width = 22, height = 1, bg = 'dodgerblue', fg = 'aliceblue', font = 'arial 12')
root.btn_take_map.place(x = 600, y = 20)

# метка номера
root.lbl_length = Label(root, text = "Ввод номера", font = 'arial 10')
root.lbl_length.place(x = 600, y = 60)

# поле номера
root.entry_length = Entry(root, width = 6)
root.entry_length.place(x = 690, y = 63)

# кнопка удалить все точки
root.btn_take_map = Button(root, text = "Удалить все точки", width = 22, height = 1, bg = 'dodgerblue', fg = 'aliceblue', font = 'arial 12')
root.btn_take_map.place(x = 600, y = 90)

# кнопка Выполнить
root.btn_track = Button(root, text = 'Выполнить', width = 13, height = 3, bg = 'dodgerblue', fg = 'aliceblue', font = 'arial 12')
root.btn_track.place(x = 850, y = 20)

# холст
canv = Canvas(root, width = 650, height = 380, bg = 'white')
canv.place(x = 330, y = 150)

# начальный статус кнопок
check_status_buttons()

# запускаем событийный цикл
root.mainloop()
