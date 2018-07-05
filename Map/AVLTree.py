from BinSearchTreeMap import *

class AVLTree(BinSearchTreeMap):
    class _Node(BinSearchTreeMap._Node):
        def __init__(self, element=None, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

    def _is_balanced(self, p):
        return abs(self._left_height(p) - self._right_height(p)) <= 1

    def _left_height(self, p):
        return p._node._left._height if self.left(p) is not None else 0

    def _right_height(self, p):
        return p._node._right._height if self.right(p) is not None else 0

    def _tall_child(self, p, favorLeft):
        return self.left(p) if self._left_height(p) + (1 if favorLeft else 0) > self._right_height(p) else self.right(p)

    def _recompute_height(self, p):
        p._node._height = max(self._left_height(p), self._right_height(p)) + 1

    def _rebalance_insert(self, p):
        z = p
        while z is not None:
            self._recompute_height(z)
            if self._is_balanced(z):
                z = self.parent(z)
            else:
                break
        if z is not None:
            y = self._tall_child(z, True)
            x = self._tall_child(y, y == self.left(z))
            self._restructure(x)
            self._recompute_height(y)
            self._recompute_height(x)
            self._recompute_height(z)

    def _rebalance_delete(self, p):
        z = p
        while z is not None:
            self._recompute_height(z)
            if self._is_balanced(z):
                z = self.parent(z)
            else:
                y = self._tall_child(z, True)
                x = self._tall_child(y, y == self.left(z))
                self._restructure(x)
                self._recompute_height(y)
                self._recompute_height(x)
                self._recompute_height(z)
                z = self.parent(x)

if __name__ == "__main__":
    a = AVLTree()
    print(len(a))
    a[1] = 1
    for i in range(2 ** 15):
        # print("insert:", i)
        a[i] = i
    print("len:", len(a))
    a[5] = 'a'
    a[10000] = 'b'
    print("height:", a.height(a.root()))
    print(a[5], a[1])