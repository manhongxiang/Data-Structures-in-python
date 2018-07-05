from BinSearchTreeMap import *

class SplayTree(BinSearchTreeMap):
    def _splay(self, x):    #splaying until x becomes the new root
        while x != self.root():
            y = self.parent(x)
            z = self.parent(y)
            if z is None:
                self._rotate(x)
            elif (x == self.left(y)) == (y == self.left(z)):    #zig-zig
                self._rotate(y)
                self._rotate(x)
            else:
                self._rotate(x)
                self._rotate(x)

    def _rebalance_insert(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)

if __name__ == "__main__":
    from random import randint, shuffle

    print("--------------sorted input------------------")
    # if elements are added in sored sequence, the tree will have height MAX, then it is very easy to cause "recursion depth exceeded" in _subtree_search
    MAX = 2 ** 8
    a = SplayTree()
    for i in range(MAX):
        a[i] = i
    print("len:", len(a))
    # print("height:", a.height(a.root()))
    for i in range(1000):   #randomly access to make the tree "balanced"
        a[randint(0, MAX - 1)]
    print("len:", len(a))
    print("height:", a.height(a.root()))

    print("--------------unsorted input------------------")
    MAX = 2 ** 14
    b = SplayTree()
    s = [i for i in range(MAX)]
    shuffle(s)
    for i in s:
        b[i] = i
    print("len:", len(b))
    print("height:", b.height(b.root()))
    print(b[5], b[MAX - 10])