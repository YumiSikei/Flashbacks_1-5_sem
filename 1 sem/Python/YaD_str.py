#Янова Даниэлла ИУ7-13
#Все слова, которые начинаются с цифры, отсортировать по убыванию
#и найти сумму цифр слов строки

s=input('Введите строку: ')
summ=b=maxi=0
Max=-1
for i in range(len(s)):
    if '0'<=s[i]<='9':
        a=int(s[i])
        summ+=a
s=s.split()
m=[]
for k in range(len(s)-1):
    for i in range(len(s)):
        if '0'<=s[i][0]<='9':
            z=0
            while z<len(s[i]) and '0'<=s[i][z]<='9':
                a=int(s[i][z])
                b=b*10+a
                if Max<b:
                    Max=b
                    maxi=i
                z+=1
        b=0
    Max=-1
    if maxi>-1:
        m.append(s[maxi])
        del s[maxi]
    maxi=-1
f=' '.join(m)
s=' '.join(s)
f+=' '+s
print()
print('Полученная строка ',f)
print('Сумма цифр ',summ)
