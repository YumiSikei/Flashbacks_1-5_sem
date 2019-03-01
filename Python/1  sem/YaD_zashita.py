M=int(input('Введите количество строк: '))
s=[0]*M
print('Введите текст по строкам: ')
for i in range(M):  #Ввод текста
    s[i]=input('')
print()
imax1=jmax1=0
imax2=M-1
jmax2=len(s[M-1])-1
signs={'.','?','!'}
coma={',',';'}
f=''
maxpr=leng=y=i=j=0
while i<len(s):
    j=0
    while j<len(s[i]):
        leng+=1
        t=s[i][j]
        if t in signs:
            if y==0:
                y+=1
                maxpr=minpr=leng
                imax2=i
                jmax2=j-1
            elif leng>maxpr:  #Находим самое длинное предложение
                maxpr=leng
                imax1=lki
                imax2=i
                jmax1=lkj
                jmax2=j-1
            lki=i
            lkj=j
            leng=0
        j+=1
    i+=1
if jmax1==len(s[imax1])-1:
    imax1+=1
    jmax1=0
for i in range(imax1,imax2+1):
    if i==imax1:
        j=jmax1
    else:
        j=0
    if i==imax2:
        lk=jmax2+1
    else:
        lk=len(s[i])
    while j<lk:
        f+=s[i][j]
        j+=1
    f+=' '
print(f)
i=j=0
f=f.split()
M=len(f)
for i in range(M-1):
    t=min(f)
    print(t,' ')
    f.remove(t)
