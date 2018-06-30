from random import randint
from MapBase import *

INF = float('inf')

class SkipList(MapBase):
    class _Node:
        __slots__ = "_item", "_prev", "_next", "_above", "_below"
        def __init__(self, item, prev=None, next=None, above=None, below=None):
            self._item = item
            self._prev = prev
            self._next = next
            self._above = above
            self._below = below

        def __lt__(self, other):
            return self._item < other._item

        def __ge__(self, other):
            return self._item >= other._item

    # ----------------------------public methods------------------------------------
    def __init__(self):
        '''init a SkipList with only an 'empty' level(the height 0)'''
        self._height = 0
        self._size = 0
        self._top = self._Node(self._Item(-INF, None))
        inf_node = self._Node(self._Item(INF, None), prev=self._top)
        self._top._next = inf_node

    def __len__(self):
        return self._size

    def __getitem__(self, key):
        node = self._find_key(key)
        if key == node._item._key:
            return node._item._value
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        node = self._find_key(key)
        if key == node._item._key:
            node._item._value = value
            walk = node._above
            while walk is not None:
                walk._item._value = value
                walk = walk._above
        else:
            self._add_after(node, key, value, )

    def add(self, key, value):
        '''add a new (k,v) pair to the skiplist, creat a tower'''
        node = self._find_key(key)
        # print("find_key_node:", node._item._key, ", key to insert:", key)
        self._add_after(node, key, value)

    def __iter__(self):
        walk = self._bottom(self._top)
        while walk._next is not None:
            yield walk._item._key
            walk = walk._next

    #----------------------------nonpublic methods------------------------------------
    def _display(self):
        '''a method for debugging, showing the rough structure of the SkipList'''
        walk = self._top
        while walk is not None:
            move = walk
            while move is not None:
                print(move._item._key, end=' -> 'if move._item._key < INF else "")
                move = move._next
            walk = walk._below
            print()

    def _bottom(self, node):
        '''given a node, get the bottom node of this colomn'''
        walk = node
        while walk._below is not None:
            walk = walk._below
        return walk

    def _find_key(self, key):
        level = self._height
        walk = self._top
        while level >= 0:
            while key >= walk._next._item._key:
                walk = walk._next
            if level > 0:
                walk = walk._below  #if already in the bottom, not go below
            level -= 1
        return walk

    def _insert_after_above(self, node1, node2, key, value):
        next = None if node1 is None else node1._next
        new_node = self._Node(self._Item(key, value), prev=node1, next=next, above=None, below=node2)
        if node2 is not None:
            node2._above = new_node
        if node1 is not None and node1._next is not None:
            node1._next._prev = node1._next = new_node
        elif node1 is not None:
            node1._next = new_node
        return new_node

    def _add_after(self, node, key, value):
        h = self._height
        cur_h = 0
        new_node = self._insert_after_above(node, None, key, value)  # insert the bottom node
        self._size += 1
        while randint(0, 8):
            cur_h += 1
            # print("cur_h:", cur_h)
            if cur_h > h:   #create a new line at the top
                right_most = self._top
                while right_most._next is not None:
                    right_most = right_most._next
                self._top = self._insert_after_above(None, self._top, -INF, None)
                self._top._next = self._insert_after_above(self._top, right_most, INF, None)
                self._height += 1
            walk = new_node
            while walk._prev is not None and walk._above is None:
                walk = walk._prev
            # print("height:", self._height)
            walk = walk._above
            new_node = self._insert_after_above(walk, new_node, key, value)

if __name__ == "__main__":
    a = SkipList()
    a.add(1, 1)
    a.add(5, 5)
    a.add(3, 3)
    a.add(4, 4)
    a.add(2, 2)
    a._display()
    print("len:", len(a))
    print("height:", a._height)
    for key in a:
        print(key, a[key])
    print("a[1]:", a[1])
    print("a[3]:", a[3])
    a[4] = "abcde"
    for key in a:
        print(key, a[key])