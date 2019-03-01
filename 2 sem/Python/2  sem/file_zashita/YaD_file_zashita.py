#Янова Даниэлла ИУ7-23
#Защита файлов

fl=open('Computer.txt','r') #Открываю и сохраняю записи файла
lines= fl.read().split()
fl.close()
fin=open('find.txt','w') #Создаю пустой файл для результатов
fin.close()
fin=open('find.txt','a+') #Открываю созданный файл для вноса результатов
s=input('Компьютеры какой стоимости вы хотите найти? ') #Задаю критерий
i=2
while i<len(lines):
    r=lines[i-2]+' '+lines[i-1]+' '+lines[i]
    if lines[i]==s: #Ищу нужные записи по критерию
        fin.write(r)
        fin.write('\n')
    i+=3

fin.close()
