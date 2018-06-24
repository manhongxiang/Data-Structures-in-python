from PositionalList import *
from PriorityQueue.PriorityQueueBase import *

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def min(self):
        return self._data.first().element()

    def remove_min(self):
        first = self._data.first()
        return self._data.delete(first)

    def add(self, key, value):
        item = self._Item(key, value)
        walk = self._data.first()
        while walk is not None and walk.element() <= item:
            walk = self._data.after(walk)
        if walk is None:
            return self._data.add_last(item)
        else:
            return self._data.add_before(walk, item)

if __name__ == "__main__":
    a = SortedPriorityQueue()
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