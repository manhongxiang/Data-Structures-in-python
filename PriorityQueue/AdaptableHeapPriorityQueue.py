from PriorityQueue.HeapPriorityQueue import *

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue._Item):
        __slots__ = "_index"
        def __init__(self, key, value, index):
            super().__init__(key, value)
            self._index = index

        def __str__(self):
            return "({0}, {1}, {2})".format(self._key, self._value, self._index)

    def __init__(self, seq=[]):
        self._data = []
        for index in range(len(seq)):
            key, value = seq[index]
            self._data.append(self.Locator(key, value, index))
        self._heapify()

    def _swap(self, j, k):
        super()._swap(j, k)
        self[j]._index = j
        self[k]._index = k

    def add(self, key, value):
        n = len(self)
        loc = self.Locator(key, value, n)
        self._data.append(loc)
        self._up_bubbling(n)
        return loc

    def min(self):
        item = self._min()
        return item._key, item._value, item._index

    def remove(self, loc):
        index = loc._index
        if index == len(self) - 1:
            self._data.pop()
        else:
            self._swap(index, len(self) - 1)
            self._data.pop()
            self._bubbling(index)
        return loc._key, loc._value

    def update(self, loc, new_key, new_val):
        index = loc._index
        item = self._data[index]
        item._key = new_key
        item._value = new_val
        self._bubbling(index)

    def _bubbling(self, j):
        parent = self._parent(j)
        if j > 0 and self[j] < self[parent]:
            self._up_bubbling(j)
        else:
            self._down_bubbling(j)

if __name__ == "__main__":
    s = [(6, 6), (2, 2), (5, 5), (7, 7), (1, 1), (3, 3), (4, 4)]
    a = AdaptableHeapPriorityQueue(s)
    loc1 = a.add(9, 9)
    loc2 = a.add(10, 10)
    loc3 = a.add(8, 8)
    loc4 = a.add(0, 0)
    print("len:", len(a))
    a.remove(loc1)
    print("len:", len(a))
    a.remove(loc2)
    for i in range(len(a)):
        print(a.remove_min())