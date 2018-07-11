import sys
sys.path.append("../LinkedQueue")
from LinkedBased.LinkedQueue import *

def radix_sort(S, *MAX):
    '''Priority: k1, k2, k3, ..., kn'''
    for i in range(len(MAX)-1, -1, -1):
        bucket = [LinkedQueue() for x in range(MAX[i])]
        while not S.is_empty():
            item = S.dequeue()
            k = item[i]
            bucket[k].enqueue(item)
        for queue in bucket:
            while not queue.is_empty():
                S.enqueue(queue.dequeue())

if __name__ == "__main__":
    from random import randint
    MAX1, MAX2, MAX3 = 10, 5, 3 #we will test with a 3D list
    s = [[randint(0, MAX1 - 1), randint(0, MAX2 - 1), randint(0, MAX3 - 1)] for x in range(50)]
    a = LinkedQueue()
    for each in s:
        a.enqueue(each)
    for each in a:
        print(each, end=' ')
    print()
    radix_sort(a, MAX1, MAX2, MAX3)
    for each in a:
        print(each, end=' ')
    print()