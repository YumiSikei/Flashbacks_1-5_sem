#Янова Даниэлла ИУ7-23
#Защита программы по методам сортировки. Быстрая сортировка.

def max_heapify(seq, i, n):
    l = 2 * i + 1
    r = 2 * i + 2

    if l <= n and seq[l] > seq[i]:
        largest = l
    else:
        largest = i
    if r <= n and seq[r] > seq[largest]:
        largest = r

    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        max_heapify(seq, largest, n)

def build_heap(seq):
    n = len(seq) - 1
    for i in range(n//2, -1, -1):
        max_heapify(seq, i, n)

def sort(seq):
    build_heap(seq)
    heap_size = len(seq) - 1
    for x in range(heap_size, 0, -1):
        seq[0], seq[x] = seq[x], seq[0]
        heap_size = heap_size - 1
        max_heapify(seq, 0, heap_size)

    return seq


print()
print('''Введите массив из 6 элементов для проверки работы быстрой сортировки
\каждый элемент вводить в отдельной строке\: ''')

mas=[0]*6
for i in range(6):
    u=i+1
    print(u,') ',end='')
    mas[i]=float(input())

def quick(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return sort(left) + [pivot] + sort(right)

print('Изначальный массив: ')
print(mas)
print()

quick_mas=quick(mas)
print('Массив, отсортированный методом шейкер: ')
print(quick_mas)

