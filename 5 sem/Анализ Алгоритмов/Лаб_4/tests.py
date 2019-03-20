from patience_sort import patience_sort
from insertion_sort import insertion_sort
from smoothsort import smoothsort


from random import randint
from time import perf_counter_ns

def random_list_gen(a):
    return [randint(0, 1000) for x in range(a)]

def increasing_list_gen(a):
    return [i for i in range(a)]

def decreasing_list_gen(a):
    return [a-i for i in range(a)]

def sort_test(sort):
    for x in range(500, 5001, 500):
        print("N = {:d}".format(x))
        n = 100
        rlg = 0
        ilg = 0
        dlg = 0
        for i in range(n):
            rlist = random_list_gen(x)
            ilist = increasing_list_gen(x)
            dlist = decreasing_list_gen(x)
            
            time_b = perf_counter_ns()
            sort(rlist)
            rlg += perf_counter_ns() - time_b
            
            time_b = perf_counter_ns()
            sort(ilist)
            ilg += perf_counter_ns() - time_b
            
            time_b = perf_counter_ns()
            sort(dlist)
            dlg += perf_counter_ns() - time_b
        rlg /= (10**9*n)
        ilg /= (10**9*n)
        dlg /= (10**9*n)
        print("{0}".format(rlg))
        print("{0}".format(ilg))
        print("{0}".format(dlg))
        print("-----------")
    print()

#A = [4,7,9,2,6,4,1,8]
#print('Massiv: ',A,'\n')
#A_p = [0]*len(A)
#A_s = [0]*len(A)
#A_i = [0]*len(A)
#for i in range (len(A)):
#    A_p[i] = A[i]
#    A_s[i] = A[i]
#    A_i[i] = A[i]

      #working
print("Терпеливая сортировка:")
sort_test(patience_sort)
#A_p = patience_sort(A_p)
#print(A_p,'\n')

      #working
#print("Плавная сортировка:")
#sort_test(smoothsort)
#A_s = smoothsort(A_s)
#print(A_s,'\n')

      #working
#print("Сортировка со вставками:")
#sort_test(insertion_sort)
#A_i = insertion_sort(A_i)
#print(A_i)
