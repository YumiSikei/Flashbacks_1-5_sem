def insertion_sort(seq):

    for i in range (1, len(seq)):
        temp = seq[i]
        item = i - 1

        while ((item >= 0) and (seq[item] > temp)):
            seq[item + 1] = seq[item]
            seq[item] = temp
            item = item - 1
            
    return seq
