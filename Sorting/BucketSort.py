import sys
sys.path.append("../Map")

def bucket_sort(S, N):
    '''only for list of numbers'''
    bucket = [0 for x in range(N)]
    while S:
        each = S.pop()
        bucket[each] += 1
    for i in range(N):
        for j in range(bucket[i]):
            S.append(i)

if __name__ == "__main__":
    from random import shuffle, randint
    MAX = 20
    alpha = "abcdefghijklmn"
    a = [randint(0, MAX - 1) for x in range(30)] * 2
    shuffle(a)
    print(a)
    bucket_sort(a, MAX)
    print(a)
