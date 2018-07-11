def insert_sort(seq):   #code not concise, see InserSort2.py
    list_seq = list(seq)
    n = len(seq)
    for index in range(n):
        cur = list_seq[index]
        for i in range(index - 1, -1, -1):
            if cur < list_seq[i]:
                list_seq[i + 1] = list_seq[i]
            else:
                list_seq[i + 1] = cur
                break
    return "".join(list_seq)

s = "13245998"
print(insert_sort(s))