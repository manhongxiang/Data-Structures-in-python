def quick_sort(S):
    def quick_sort_recur(S, a, b):
        if a >= b:
            return
        pivot = S[b]
        i, j = a, b
        while i < j:
            while i < j and S[i] < pivot:
                i += 1
            while i < j and S[j] > pivot:
                j -= 1
            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1
        quick_sort_recur(S, a, i - 1)
        quick_sort_recur(S, i, b)

    quick_sort_recur(S, 0, len(S) - 1)

if __name__ == "__main__":
    from random import shuffle
    s = [x for x in range(20)] * 2
    shuffle(s)
    # s = [3, 2, 0, 1, 4]
    print(s)
    quick_sort(s)
    print(s)