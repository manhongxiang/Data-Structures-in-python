from random import randint
def quick_sort(S):
    def quick_sort_recur(S, a, b):
        if a >= b:
            return
        pick = randint(0, b - a) + a
        S[pick], S[b] = S[b], S[pick]   #replace with the last element
        pivot = S[b]
        i, j = a, b
        while i < j:
            while i < j and S[i] < pivot:
                i += 1
            while i < j and S[j] > pivot:
                j -= 1
            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1  #to avoid infinite loop when S[i] == S[j]
                # j -= 1    #Remove this sentence to avoid the consequence that i > j, so that the following recursion has right borders
        quick_sort_recur(S, a, i - 1)
        quick_sort_recur(S, i, b)

    quick_sort_recur(S, 0, len(S) - 1)

if __name__ == "__main__":
    from random import shuffle
    s = [x for x in range(20)] * 2
    shuffle(s)
    # s = [3, 2, 0, 1, 4]
    # s = [0, 1]
    s = [1, 0]
    # s = [0]
    print(s)
    quick_sort(s)
    print(s)