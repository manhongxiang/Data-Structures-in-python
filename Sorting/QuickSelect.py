from random import choice

def quick_select(S, k):
    '''find the kth smallest element of list S'''
    if len(S) < k:
        return
    pivot = choice(S)
    L, E, G = [], [], []
    for item in S:
        if item < pivot:
            L.append(item)
        elif item == pivot:
            E.append(item)
        else:
            G.append(item)
    if len(L) >= k:
        return quick_select(L, k)
    elif len(L) + len(E) >= k:
        return pivot
    else:
        return quick_select(G, k - len(L) - len(E))

if __name__ == "__main__":
    from random import shuffle
    s = [x for x in range(30)]
    shuffle(s)
    print(quick_select(s, 5))
    print(quick_select(s, 15))