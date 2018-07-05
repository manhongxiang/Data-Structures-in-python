import sys
sys.path.append("../Tree")
from LinkedBinaryTree import *
from MapBase import *

class BinSearchTreeMap(LinkedBinaryTree, MapBase):
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self._node._element._key
        def value(self):
            return self._node._element._value

    #---------------------------public methods-------------------------------
    def __getitem__(self, key):
        if self.is_empty():
            raise KeyError(key)
        p = self._subtree_search(self.root(), key)
        self._rebalance_access(p)
        if p.key() != key:
            raise KeyError(key)
        else:
            return p.value()

    def __setitem__(self, key, value):
        if self.is_empty():
            self._add_root(self._Item(key, value))
        else:
            p = self._subtree_search(self.root(), key)
            if p.key() == key:
                p._node._element._value = value
                self._rebalance_access(p)
                return
            elif key < p.key():
                p = self._add_left(p, self._Item(key, value))
            else:
                p = self._add_right(p, self._Item(key, value))
            self._rebalance_insert(p)

    def delete(self, p):
        element = p.element()
        if self.num_children(p) == 2:
            replace = self.before(p)
            self._replace(p, replace.element())
            self._replace(replace, element)
            p = replace
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)
        return element

    def __delitem__(self, key):
        if self.is_empty():
            raise KeyError(key)
        p = self._subtree_search(self.root(), key)
        if p.key() != key:
            self._rebalance_access(p)
            raise KeyError(key)
        else:
            self.delete(p)

    def __iter__(self):
        for each in self.inorder():
            yield each.element()

    def first(self):
        return self._subtree_first_postion(self.root()) if not self.is_empty() else None

    def last(self):
        return self._subtree_last_position(self.root()) if not self.is_empty() else None

    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(p)
            while above is not None and self.left(above) == walk:
                walk = above
                above = self.parent(above)
            return above

    def after(self, p):
        self._validate(p)
        if self.right(p):
            return self._subtree_first_postion(self.right(p))
        else:
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(above)
            return above

    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            return self._subtree_search(self.root(), k)

    def find_min(self):
        if self.is_empty():
            return None
        p = self.first()
        return p.key(), p.value()

    def find_max(self):
        if self.is_empty():
            return None
        p = self.last()
        return p.key(), p.value()

    def find_ge(self, k):
        if self.is_empty():
            return None
        p = self._subtree_search(self.root(), k)
        if p.key() < k:
            p = self.after(p)
        return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        if self.is_empty():
            raise Exception("try to iter an empty map")
        start_p = self._subtree_search(self.root(), start)
        if start_p.key() < start:
            start_p = self.before(start_p)
        walk = start_p
        while walk.key() <= stop:
            yield walk.key(), walk.value()
            walk = self.after(walk)


    #---------------------------nonpublic methods-----------------------------
    def _subtree_search(self, p, key):
        '''return the position that contains key or the last position accessed in an unsuccessful search'''
        if key == p.key():
            return p
        elif key < p.key() and self.left(p) is not None:
            return self._subtree_search(self.left(p), key)
        elif key > p.key() and self.right(p) is not None:
            return self._subtree_search(self.right(p), key)
        # self._rebalance_access(p) #bing bu xu yao
        return p

    def _subtree_first_postion(self, p):
        if p is None:
            return None
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        if p is None:
            return None
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    #The methods below are for trees balancing
    def _relink(self, parent, child, bLeft):
        if bLeft:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        '''a single rotate operation, to make p over its parent'''
        x = p._node
        y = x._parent   #When calling this method, please make sure p is not the root
        z = y._parent
        bLeft = x is y._left
        if bLeft:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)
        if z is not None:
            self._relink(z, x, y is z._left)
        else:   #During each operation, the "border situation" should be considered
            self._root = x
            x._parent = None

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)  #When calling this method, please be sure that x is not the root, or y is None, then an error occurs here
        if z is None:
            self._rotate(x)
        else:
            if (x == self.left(y)) == (y == self.left(z)):
                self._rotate(y)
                return y
            else:
                self._rotate(x)
                self._rotate(x)
                return x

    def _rebalance_access(self, p):
        pass

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

if __name__ == "__main__":
    a = BinSearchTreeMap()
    a[7] = 7
    a[10] = 10
    a[9] = 9
    a[8] = 8
    a[1] = 1
    a[2] = 2
    a[6] = 6
    a[4] = 4
    a[3] = 3
    a[5] = 5
    del a[3]
    del a[4]
    del a[7]
    # del a[11]
    print("root height:", a.height(a.root()))
    print("len:", len(a))
    print("fist:", a.first().element(), "last:", a.last().element())
    for each in a:
        print(each)

    print("---------------------------------")
    for each in a.find_range(2, 4):
        print(each)