import * from graph_stepen_2
print()
import * from graph_dvudolnii
print()

def extend(candidates, not_):
    

def task(A, a_dugs):
    compsub = [0]
    not_ = [0]
    k = 0
    n = 0
    for i in range(len(A)):
        if A[i] == 0:
            if k == 0:
                not_[0] = i
                k += 1
            else:
                not_.append(i)
        else:
            if n == 0:
                compsub[0] = i
            else:
                compsub.append(i)
            
    for i in range(len(A) - 1):
        
