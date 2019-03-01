#Янова Даниэлла ИУ7-13
#В тексте найти самые длинные слова в каждой строке, количество слов во всем
#тексте, наиболее часто встречающееся слово в самой длинном предложении,
#заменить слово другим в самом коротком предложении
#удалить из текста заданное слово
from math import trunc
M=int(input('Введите количество строк: '))
s=[0]*M
ss=[0]*M
maxlen=maxleni=summ=0
s1=' '
d=[0]*len(s)
print('Введите текст по строкам: ')
for i in range(M):  #Ввод текста
    s[i]=input('')
print()
imax1=jmax1=imin1=jmin1=0
imax2=imin2=M-1
jmax2=jmin2=len(s[M-1])-1
signs={'.','?','!'}
coma={',',';'}
ar={'*','-'}
wo={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
    'S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
ch={'0','1','2','3','4','5','6','7','8','9'}
d=[0]*M
for i in range(len(s)):  
    s[i].rstrip()  #Выравнивание по правому краю
    q=len(s[i])
    s[i].lstrip()
    ss[i]=s[i]+' '   #Создаем копию изначального текста
    if maxlen<len(s[i]):  #Находим самую длинную строку и запоминаем ее
        maxlen=len(s[i])
        d[i]=q-len(s)
    s[i]=s[i].split()  #Преобразуем текст в матрицу слов
    j=0
    Max=len(s[i][0])
    p=s[i][0][len(s[i][0])-1]
    if p in signs or p in coma:
        maxs=s[i][0][:-1]
    else:
        maxs=s[i][0]
    summ+=len(s[i])  #Находим количество слов в тексте
    while j<len(s[i]):
        p=s[i][j][len(s[i][j])-1]
        if p in signs or p in coma:
            mm=len(s[i][j])-1
            mms=s[i][j][:-1]
        else:
            mm=len(s[i][j])
            mms=s[i][j]
        if mm>Max:  #Находим самое длинное слово в данной строке
            Max=mm
            maxs=mms
        j+=1
    print('Самое длинное слово в',i,'строке: ',maxs)
print()
print('Количество слов в тексте: ',summ)
print()

maxpr=minpr=leng=y=i=j=0
while i<len(ss):
    j=0
    while j<len(ss[i]):
        leng+=1
        t=ss[i][j]
        if t in signs:
            if y==0:
                y+=1
                maxpr=minpr=leng
                imax2=imin2=i
                jmax2=jmin2=j-1
            elif leng>maxpr:  #Находим самое длинное предложение
                maxpr=leng
                imax1=lki
                imax2=i
                jmax1=lkj
                jmax2=j-1
            elif leng<minpr:  #Находим самое короткое предложение
                minpr=leng
                imin1=lki
                imin2=i
                jmin1=lkj
                jmin2=j-1
            lki=i
            lkj=j
            leng=0
        j+=1
    i+=1


k=maxk=0
sos=''
i=i1=imax1
while i<imax2+1:
    if i==imax1:
        j=jmax1
    else:
        j=0
    if i==imax2:
        lk=jmax2+1
    else:
        lk=len(ss[i])
    while j<lk:
        if j==0:
            sos+=' '
        sos+=ss[i][j]
        j+=1
    i+=1
slov=slov1=''
i=0
while i<len(sos):
    j=0
    if sos[i]!=' ' and sos[i] not in signs and sos[i] not in coma:
        slov+=sos[i]
    if (sos[i]==' ' or sos[i] in signs) and slov!='':
        while j<len(sos):
            if sos[j]!=' ' and sos[j] not in signs and sos[j] not in coma:
                slov1+=sos[j]
            if (sos[j]==' ' or sos[j] in signs) and slov!='':
                if slov==slov1:
                    k+=1
                slov1=''
            j+=1
        if k>maxk:
            maxk=k
            slovo=slov
        slov=''
        k=0
    i+=1
print('Самое частое слово в самом длинном предложении: ',slovo)
print()
print()

# Функция среза
def srez(x,i,j,inp=''):
    s=''
    t=0
    while t<i: 
        s+=x[t]
        t+=1
    s+=inp
    while j<len(x):
        s+=x[j]
        j+=1
    return s
       
# Функция замены арифм. выражения
def arifv(s,x):
    ch='0123456789'
    i=1
    ss=False
    while i<len(s)-1:
        if s[i]==x and s[i-1] in ch and s[i+1] in ch:
            k1=k2=''           
            # Число слева
            t=i-1
            while t<len(s) and s[t] in ch:
                k1+=s[t]
                t-=1            
            # Реверс
            k11=''
            for j in range(len(k1)-1,-1,-1):
                k11+=k1[j]            
            # Число справа
            q=i+1
            while q<len(s) and s[q] in ch:
                k2+=s[q]
                q+=1                
            # Сама замена
            c1=srez(s,t+1,q,str(k11))
            c2=srez(s,t+1,q,str(k2))
            c1=int(c1)-int(c2)*10**(len(c1)-len(c2))
            c2=int(c2)
            if x=='*':
                ss=str(c1*c2)
            elif x=='-':
                ss=str(c1-c2)        
        i+=1
    return ss

ud=input('Введите удаляемое слово: ')
zam=input('Введите какое слово нужно заменить: ')
zamen=input('Введите каким словом нужно его заменить: ')
f=[0]*M
for i in range(len(ss)):
    f[i]=''  #Выравниваем по левому краю длиннейшей строки
    j=0
    while j<len(ss[i]):
        while j<len(ss[i]) and not(ss[i][j] in wo or ss[i][j] in ch or
                                   ss[i][j] in ar):            j+=1
        t=''
        if j>=len(ss[i])-1:
            break
        while (ss[i][j] in wo or ss[i][j] in ch or ss[i][j] in
               ar) and j<len(ss[i])-1:
            t+=ss[i][j]
            j+=1
        j-=1
        if (j==len(ss[i])-1 and ss[i][j] not in signs and ss[i][j] not in coma
            and ss[i][j]!=' '):
            t+=ss[i][j]
        elif ss[i][j] in signs or ss[i][j] in coma:
            j-=1         
        if t!=ud:
            c=False
            if (( i==imin1 and jmin1<j) or imin1<i<imin2 or
                (i==imin2 and j<=jmin2)) and t==zam:
                f[i]+=zamen #Заменяем слово другим в кратчайшем предложении
            else:
                  #Выполняем арифметическое выражение
                c=arifv(t,'*')
                if c==False:
                    c=arifv(t,'-')
                    if c==False:
                        f[i]+=t
                    else:
                        f[i]+=c
                else:
                    f[i]+=c
        if j<len(ss[i]) and ss[i][j+1] in signs or ss[i][j+1] in coma:
            f[i]+=ss[i][j+1]
        if t!=ud:
            f[i]+=' '
        j+=1
maxlen=len(f[0])
dmax=0
for i in range(M):
    if maxlen<len(f[i]):
        maxlen=len(f[i])
        dmax=i
# Функция, определяющая длину макс. строки
def maxs(a):
    maxs=i=0
    for x in a:
        i+=1
        if len(x)>maxs:
            maxs=len(x)
            ots=d[i]
    return maxs,ots
# Выравниваю по ширине
for x in f:
    x=srez(x,len(x)-1,len(x))
    i=0
    mm,ots=maxs(f)
    while len(x)<mm:    
        if x[i]==' ' and x[i-1]!=' ':
            x=srez(x,i,i+1,'  ')
        i+=1
        if i==len(x):
            i=0
    print(' '*ots,x)        

        
