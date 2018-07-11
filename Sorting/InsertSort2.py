def insert_sort(seq):
    for i in range(len(seq)):
        j = i - 1
        v = seq[i]
        while j >= 0 and v < seq[j]:    #a while loop is much better than if loop here
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = v

a = [1, 3, 5, 3, 2, 9, 8, 1, 12, 89, 61, 52]
insert_sort(a)
print(a)
