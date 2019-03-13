def max_elem(array):
    m = array[0]
    for i in range(1, len(array)):
        if array[i] > m:
            m = array[i]
    return m

def patience_sort(seq):
    N = len(seq)
    M = [0] * N
    for i in range(N):
        M[i] = [0] * (N + 1)
    G = max_elem(seq) + 1

    i = j = k = 0
    
    M[i][j+1] = A[k]
    for k in range (1, N):
        if M[i][j+1] > A[k]:
            j += 1
            M[i][j+1] = A[k]
        else:
            M[i][0] = j + 1
            i += 1
            j = 0
            M[i][j+1] = A[k]
    M[i][0] = j + 1

    for k in range(0, N):
        min_el = G
        for j in range(0, j <= i):
            if M[j][0] != 0:
                if min_el > M[j][M[j][0]]:
                    min_el = M[j][M[j][0]]
                    s = j
        A[k] = min_el
        M[s][0] -= 1    

    return seq
