import sys
sys.path.append("../LinkedBased")
from LinkedBased.LinkedQueue import LinkedQueue

def MergeSort(S):
    n = len(S)
    if n <= 1:
        return
    S1 = LinkedQueue()
    S2 = LinkedQueue()
    i = 0
    while i < n // 2:
        S1.enqueue(S.dequeue())
        i += 1
    while not S.is_empty():
        S2.enqueue(S.dequeue())
    MergeSort(S1)
    MergeSort(S2)
    Merge(S1, S2, S)

def Merge(S1, S2, S):
    while not S1.is_empty() or not S2.is_empty():
        if S1.is_empty():
            S.enqueue(S2.dequeue())
        elif S2.is_empty():
            S.enqueue(S1.dequeue())
        elif S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())

if __name__ == "__main__":
    from random import shuffle
    s = LinkedQueue()
    lst = [x for x in range(20)]
    shuffle(lst)
    for i in lst:
        s.enqueue(i)
    for each in s:
        print(each, end=' ')
    print()
    MergeSort(s)
    for each in s:
        print(each, end=' ')
    print()
