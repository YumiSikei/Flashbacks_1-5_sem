s=input('введите: ')
s=s.split()
k=l=p=0
m=[]
pn=jn=-1
for i in range(len(s)):
    for j in range(len(s[i])):
        for p in range(len(s[i])):    #смотрим одинаковые ли буквы, без учета регистра
            if 'a'<=s[i][p]<='z':
                pn = ord(s[i][p]) - ord('a')
            elif 'A'<=s[i][p]<='Z':
                pn = ord(s[i][p]) - ord('A')
            if 'a'<=s[i][j]<='z':
                jn = ord(s[i][j]) - ord('a')
            elif 'A'<=s[i][j]<='Z':
                jn = ord(s[i][j]) - ord('A')
            if pn>-1 and jn>-1 and pn==jn:  #если это одинаковые буквы, считаем их количество
                k+=1
        if k<2:  #если это не буква и она не повторяется, то запоминаем это по l и заканчиваем смотреть дальше слово
            k=0
            l=0
            break
        l=1
        k=0
    if l==1:  #смотрим есть ли случаи с буквами без повторов
        m.append(s[i])
    l=0
    pn=jn=-1
print(m)
k=l=p=0


def compare_letter(a, b):  #сравниваем соответствующие буквы в словах
    if a == b:
        return 0
    
    if 'a'<=a<='z':
        an = ord(a) - ord('a')
    elif 'A'<=a<='Z':
        an = ord(a) - ord('A')
    if 'a'<=b<='z':
        bn = ord(b) - ord('a')
    elif 'A'<=b<='Z':
        bn = ord(b) - ord('A')
        
    if an > bn:
        return 1
    elif an == bn:
        # для случая, когда буквы одинаковы, но отличается регистр
        if a > b:
            return 1
        else:
            return -1
    else:
        return -1

# если вернёт True, то a < b
def compare(a, b):   #сравниваем слова, учитывая индекс букв у каждого
    # индекс, с которого начинать сравнение
    ai = bi = 0
    # пропускаем первые небуквы
    while not ('a' <= a[ai] <= 'z' or 'A' <= a[ai] <= 'Z'):
        ai += 1
    while not ('a' <= b[bi] <= 'z' or 'A' <= b[bi] <= 'Z'):
        bi += 1
    # сравниваем буквы
    c = compare_letter(a[ai], b[bi])
    # пока проверяемые одинаковы
    while c == 0:
        # сдвигаемся к проверке следующих
        ai += 1
        bi += 1
        # пропускаем небуквы
        # если у a буквы кончились быстрее, чем у b, то a меньше
        if ai == len(a):
            return True
        # если у b буквы кончились быстрее, чем у a, то a больше
        if bi == len(b):
            return False
        # снова сравниваем буквы
        c = compare_letter(a[ai], b[bi])
    if c == 1:
        return True
    else:
        return False

for i in range(len(m)):
    for j in range(i+1, len(m)):
        if compare(m[i], m[j]):
            # меняем местами
            m[i], m[j] = m[j], m[i]
print(m)
