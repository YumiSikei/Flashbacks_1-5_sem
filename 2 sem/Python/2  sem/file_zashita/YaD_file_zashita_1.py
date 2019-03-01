#Янова Даниэлла ИУ7-23
#
fl=open('student.txt','r')
lines= fl.read().split()
fl.close()
fl=open('student.txt','w')
i=0
y=0
hv=0
while i<len(lines)-2:
    r=lines[i]+' '+lines[i+1]+' '+lines[i+2]+' '+lines[i+3]
    i+=1
    y=0
    while y<3 and lines[i]!='2':
        y+=1
        i+=1
    if y==3:
        fl.write(r)
        fl.write('\n')
    else:
        hv+=1
    i+=3-y
if hv==0:
    print('Нет хвостистов')
fl.close()
