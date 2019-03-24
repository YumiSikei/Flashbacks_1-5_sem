import copy

a = []
print(a)

b = [2,3]
a = copy.copy(b)
print(a)


c = [7,8,9]
a = copy.copy(c)
print(a,'\n')

for i in range (3):
    print(i)
    if i == 1:
        break
print()
a.remove(7)
print(a)

g = []
if len(g) > 0:
    print('ok')
