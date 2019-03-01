s=input('Введите строку: ')
s=s.split()
k=l=p=t=0
m=[]

def compare(a,b):
    ia=ib=-1
    t=y=0
    while t<len(a) and ia<0: #Нахожу первые буквы в словах
        if 'a'<=a[t]<='z' or 'A'<=a[t]<='Z':
            ia=t
    t=0
    while t<len(b) and ib<0:
        if 'a'<=b[t]<='z' or 'A'<=b[t]<='Z':
            ib=t            
    while a[ia]==b[ib]: #Если они одинаковые, ищу первые различные буквы
        t=ia+1
        while t<len(a) and ia<0:
            if 'a'<=a[t]<='z' or 'A'<=a[t]<='Z':
                ia=t
        t=ib+1
        while t<len(b) and ib<0:
            if 'a'<=b[t]<='z' or 'A'<=b[t]<='Z':
                ib=t
    if a[ia]<b[ib]:
        y=1
    return y
    

k=l=p=t=0
m=[]
for i in range(len(s)):
    for j in range(len(s[i])):
        if 'a'<=s[i][j]<='z' or 'A'<=s[i][j]<='Z':
            t = 1
        for p in range(len(s[i])):
            if s[i][p]==s[i][j]:
                k+=1
        if k<2:
            k=0
            l=1
            break
        k=0
    if l==0 and t==1:
        m.append(s[i])
    l=t=k=0
print(m)
k=l=p=t=0
#сортировка слов по алфавиту в обратном порядке
for i in range(len(m)-1):
    for j in range(i+1, len(m)):
        if compare(m[i], m[j])==1:
            m[i], m[j] = m[j], m[i]
print(m)
