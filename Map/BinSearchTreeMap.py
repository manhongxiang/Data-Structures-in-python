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
                p._node._item._value = value
            elif key < p.key():
                self._add_left(p, self._Item(key, value))
            else:
                self._add_right(p, self._Item(key, value))

    def delete(self, p):
        element = p.element()
        if self.num_children(p) == 2:
            replace = self.before(p)
            self._replace(p, replace.element())
            self._replace(replace, element)
        else:
            self._delete(p)
        return element

    def __delitem__(self, key):
        if self.is_empty():
            raise KeyError(key)
        p = self._subtree_search(self.root(), key)
        if p.key() != key:
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
        pass

    #---------------------------nonpublic methods-----------------------------
    def _subtree_search(self, p, key):
        '''return the position that contains key or the last position accessed in an unsuccessful search'''
        if key == p.key():
            return p
        elif key < p.key() and self.left(p) is not None:
            return self._subtree_search(self.left(p), key)
        elif key > p.key() and self.right(p) is not None:
            return self._subtree_search(self.right(p), key)
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
    # del a[11]
    print("root height:", a.height(a.root()))
    print("len:", len(a))
    print("fist:", a.first().element(), "last:", a.last().element())
    for each in a:
        print(each)