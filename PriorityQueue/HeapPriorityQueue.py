from PriorityQueue.PriorityQueueBase import *

class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self, seq=[]):
        self._data = [self._Item(key, value) for key, value in seq]
        self._heapify()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, item):
        return self._data[item]

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._up_bubbling(len(self) - 1)

    def min(self):
        item = self._min()
        return item._key, item._value

    def _min(self):
        if self.is_empty():
            raise EmptyError("try to access an empty queue")
        return self[0]

    def remove_min(self):
        item = self._remove_min()
        return item._key, item._value

    def _remove_min(self):
        if self.is_empty():
            raise EmptyError("try to remove from an empty queue")
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._down_bubbling(0)
        return item

    def _up_bubbling(self, j):
        parent = self._parent(j)
        if j > 0 and self[j] < self[parent]:
            self._swap(parent, j)
            self._up_bubbling(parent)

    def _down_bubbling(self, j):
        min_child = None
        if self._has_left(j):
            min_child = self._left(j)
        if self._has_right(j):
            right = self._right(j)
            if self[right] < self[min_child]:
                min_child = right
        if min_child is not None and self[min_child] < self[j]:
            self._swap(min_child, j)
            self._down_bubbling(min_child)

    def _parent(self, j):
        return (j - 1) // 2

    def _has_left(self, j):
        return 2 * j + 1 < len(self)

    def _has_right(self, j):
        return 2 * j + 2 < len(self)

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _swap(self, j, k):
        self._data[j], self._data[k] = self._data[k], self._data[j]

    def _heapify(self):
        n = len(self)
        start = self._parent(n - 1)
        for node in range(start, -1, -1):
            self._down_bubbling(node)

if __name__ == "__main__":
    s = [(1, 1), (2, 2), (5, 5), (7, 7), (6, 6), (3, 3), (4, 4)]
    a = HeapPriorityQueue(s)
    a.add(4, 4)
    a.add(3, 3)
    a.add(1, 1)
    a.add(2, 2)
    print(len(a))
    for i in range(len(a)):
        print(a.remove_min())