from LinkedBased.LinkedQueue import LinkedQueue

def linked_quick_sort(S):
    if len(S) <= 1:
        return
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    pivot = S.first()
    while not S.is_empty():
        item = S.dequeue()
        if item < pivot:
            L.enqueue(item)
        elif item == pivot:
            E.enqueue(item)
        else:
            G.enqueue(item)
    linked_quick_sort(L)
    linked_quick_sort(G)
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

if __name__ == "__main__":
    from random import shuffle
    s = LinkedQueue()
    lst = [x for x in range(20)] * 2
    shuffle(lst)
    for i in lst:
        s.enqueue(i)
    for each in s:
        print(each, end=' ')
    print()
    linked_quick_sort(s)
    for each in s:
        print(each, end=' ')
    print()