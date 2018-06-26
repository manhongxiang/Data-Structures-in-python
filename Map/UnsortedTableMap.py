from MapBase import *

class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def _findkey(self, key):
        for i in range(len(self)):
            if key == self._table[i]._key:
                return i
        return None

    def __setitem__(self, key, value):
        i = self._findkey(key)
        if i is not None:
            self._table[i]._value = value
        else:
            self._table.append(self._Item(key, value))

    def __getitem__(self, item):
        i = self._findkey(item)
        if i is None:
            raise KeyError(item)
        else:
            return self._table[i]._value

    def __delitem__(self, key):
        i = self._findkey(key)
        if i is None:
            raise KeyError(key)
        else:
            del self._table[i]

    def __iter__(self):
        for item in self._table:
            yield item._key

if __name__ == "__main__":
    a = UnsortedTableMap()
    a[1] = 1
    a[2] = 2
    a['a'] = 'a'
    a[3] = 3
    a[4] = 4
    print(len(a))
    for i in a:
        print(i, a[i])

    del a[1]
    print(len(a))
    for i in a:
        print(i, a[i])