from MapBase import *

class SortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key, item._value

    def _find_index(self, k):
        def _find_index_inner(k, low, high):
            if high < low:
                # print("len:{0}, low:{1}, high:{2}".format(len(self), low, high))
                return low
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return _find_index_inner(k, low, mid - 1)
            else:
                return _find_index_inner(k, mid + 1, high)
        return _find_index_inner(k, 0, len(self) - 1)

    def __getitem__(self, k):
        index = self._find_index(k)
        if 0 <= index < len(self) and k == self._table[index]._key:
            item = self._table[index]
            return item._value
        else:
            raise KeyError(k)

    def __setitem__(self, k, v):
        index = self._find_index(k)
        if index < len(self) and k == self._table[index]._key:
            self._table[index]._value = v
        else:
            self._table.insert(index, self._Item(k, v))

    def __delitem__(self, k):
        index = self._find_index(k)
        if index < len(self) and self._table[index]._key == k:
            self._table.pop(index)
        else:
            raise KeyError(k)

    def find_min(self):
        if len(self) > 0:
            return self._table[0]._key, self._table[0]._value
        else:
            return None

    def find_max(self):
        if len(self) > 0:
            return self._table[-1]._key, self._table[-1]._value
        else:
            return None

    def find_le(self, k):
        index = self._find_index(k)
        if index < len(self) and self._table[index]._key == k:
            item = self._table[index]
        elif index > 0:
            item = self._table[index-1]
        else:
            return None
        return item._key, item._value

    def find_lt(self, k):
        index = self._find_index(k)
        if index > 0:
            item = self._table[index-1]
            return item._key, item._value
        else:
            return None

    def find_ge(self, k):
        index = self._find_index(k)
        if index >= len(self):
            return None
        else:
            item = self._table[index]
            return item._key, item._value

    def find_gt(self, k):
        index = self._find_index(k)
        if index < len(self) and self._table[index]._key == k:
            if index < len(self) - 1:
                item = self._table[index + 1]
            else:
                return None
        elif index < len(self):
            item = self._table[index]
        else:
            return None
        return item._key, item._value

if __name__ == "__main__":
    a = SortedTableMap()
    a[1] = 1
    a[2] = 2
    a[5] = 5
    a[4] = 4
    a[3] = 3
    a[1] = 1.1
    # a['a'] = 'a'
    # a['b'] = 'b'
    print(len(a))
    print(a.find_min(), a.find_max())
    print(a[1])
    # print(a[6])
    print(a.find_ge(6))

