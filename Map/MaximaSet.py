from SortedTableMap import *

class MaximaSet(SortedTableMap):
    '''An application of SortedTableMap. Given several pairs of costs and performance, find the best performance within expected cost'''
    def add(self, c, p):
        other = self.find_le(c)
        if other is not None and other[1] >= p:
            return
        self[c] = p
        other = self.find_gt(c)
        while other is not None and other[1] <= p:
            del self[other[0]]
            other = self.find_gt(other[0])

    def best(self, c):
        item = self.find_le(c)
        if item is not None:
            return item

    def _dominate(self, master, slave):
        return master._key <= slave._key and master._value >= slave._value

if __name__ == "__main__":
    a = MaximaSet()
    a.add(100, 200)
    a.add(120, 200)
    a.add(200, 500)
    a.add(200, 300)
    a.add(500, 800)
    a.add(400, 800)
    a.add(100, 400)
    print(len(a))
    print(a.best(100))
    print(a.best(150))
    print(a.best(300))
    print(a.best(450))