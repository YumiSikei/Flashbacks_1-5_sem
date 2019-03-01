# Евтеев Артём, группа ИУ7-13, строки

s=input('\nВведите строку: ')
s=s.split()
num = '0123456789'
a=[]
p=[]

# Заполняем массив "а" неповторяющимися числами
for i in range(len(s)):
    k=0
    for j in range(len(s[i])):
        if s[i][j] in num:
            k +=1
        if k==len(s[i]):
            if s[i] not in a:
                if s[i] not in p:
                    a.append(s[i])
            else:
                 a.remove(s[i])
                 p.append(s[i])

# Выводим массив а
print('\nНеповторяющиеся слова из строки, состоящие из чисел:')
for x in a:
    print(x,end=' ')

# Удаляем неповторяющиеся числа из строки
for x in a:
    s.remove(x)
    
# Выводим получившуюся строку
print('\n\nОставшаяся строка: ')
for x in s:
    print(x,end=' ')

# Сортируем по убыванию длин "пузырьком"
n=len(s)
for i in range(n):
    for j in range(n-2,i-1,-1):
        if len(s[j])<len(s[j+1]):
            s[j],s[j+1]=s[j+1],s[j]
            
