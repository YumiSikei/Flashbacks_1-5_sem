#Янова Даниэлла ИУ7-23
#Написать программу, умеющую создавать файл, добавлять в него записи и искать
#нужные записи по одному из полей, сохраняя результат в новом файле.
choice=None
print('1- Создать файл')
print('2- Добавить запись')
print('3- Найти записи')
print('0- Выход')
print()
while choice!='0':
    choice=input('Выбор: ')
    print()
    if choice=='0':
        print('Выход')
    elif choice=='1':
        Name=open('new.txt','w')
        Name.close()
        print('Создан файл new.txt')
    elif choice=='2':
        fl=open('file.txt','a+')   #Открытие файла
        ws=input('Введите данные через пробел в одной строке: ')
        fl.write(ws)   #Добавление записи в файл
        fl.close()
    elif choice=='3':
        fl=open('file.txt','r')
        lines= fl.read().split()
        fl.close()

        fin=open('find.txt','a+')   #Открытие файла для ввода результата

        year=input('Аниме какого года начала выпуска вы хотите найти? ')
        i=1
        y=0
        print()
        while i<len(lines):
            if lines[i]==year:
                r=lines[i-1]+' '+lines[i]+' '+lines[i+1]
                y=1
                fin.write(r)
                fin.write('\n')
                print(r)
            i+=3
        if y==0:
            fin.write('Нет аниме, начало выхода которого будет в этом году')
            print('Нет аниме, начало выхода которого будет в этом году')
        fin.write('\n')
        fin.write('\n')
        fin.close()
    print()
