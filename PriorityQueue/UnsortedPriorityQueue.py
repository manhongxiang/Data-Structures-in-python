from PriorityQueue.PriorityQueueBase import PriorityQueueBase
from PositionalList import *

class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add(self, key, value):
        return self._data.add_last(self._Item(key, value))

    def _find_min(self):
        if self.is_empty():
            raise EmptyError("try to access an empty list")
        walk = self._data.first()
        min_elem = walk
        while walk is not None:
            if walk.element() < min_elem.element():
                min_elem = walk
            walk = self._data.after(walk)
        return min_elem

    def min(self):
        return self._find_min().element()

    def remove_min(self):
        min_elem = self._find_min()
        return self._data.delete(min_elem)

if __name__ == "__main__":
    a = UnsortedPriorityQueue()
    a.add(2, 2)
    a.add(1, 1)
    a.add(3, 3)
    a.add(6, 6)
    a.add(5, 5)
    a.add(4, 4)
    print(len(a))
    print(a.min())
    print("--------------------")
    for i in range(len(a)):
        print(a.remove_min())
    print(len(a))
    print(a.is_empty())
    # print(a.remove_min())