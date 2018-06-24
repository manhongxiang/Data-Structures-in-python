from BinaryTree import *

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"
        def __init__(self, element=None, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
    class Position(BinaryTree.Position):
        def element(self):
            return self._node._element

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def root(self):
        return self._make_position(self._root)

    def is_empty(self):
        return self._size == 0

    def is_root(self, p):
        node = self._validate(p)
        return node is self._root

    def is_leaf(self, p):
        node = self._validate(p)
        return node._left is None and node._right is None

    def _validate(self, p):
        if not isinstance(p.__class__, type(self.Position)):
            raise ValueError("invalid position type")
        if p._container is not self:
            raise ValueError("position does not belong this container")
        if p._node._parent is p._node:
            raise ValueError("position is no longer valid")
        return p._node
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def root(self):
        return self._make_position(self._root)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left:
            count += 1
        if node._right:
            count += 1
        return count

    def _add_root(self, e):
        if not self.is_empty():
            raise ValueError("root already exists")
        self._root = self._Node(e)
        self._size += 1
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left:
            raise ValueError("left child already exists")
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right:
            raise ValueError("right child already exists")
        node._right = self._Node(e)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _attach(self, p, t1, t2):
        if not(type(self) is type(t1) is type(t2)):
            # print(type(self), type(t1), type(t2))
            raise TypeError("three trees must be of the same type")
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position is not a leaf")
        if not t1.is_empty():
            node._left = t1._root
            t1._root._parent = node
        if not t2.is_empty():
            node._right = t2._root
            t2._root._parent = node
        self._size += len(t1) + len(t2)

    def preorder(self):
        def preorder_inner(p):
            yield p
            for each in self.children(p):
                for other in preorder_inner(each):
                    yield other
        if not self.is_empty():
            root = self.root()
            for each in preorder_inner(root):
                yield each

    def postorder(self):
        def postorder_recur(p):
            for each in self.children(p):
                for other in postorder_recur(each):
                    yield other
            yield p
        if not self.is_empty():
            root = self.root()
            for each in postorder_recur(root):
                yield each

    def inorder(self):
        def inorder_recur(p):
            left = self.left(p)
            if left:
                for each in inorder_recur(left):
                    yield each
            yield p
            right = self.right(p)
            if right:
                for each in inorder_recur(self.right(p)):
                    yield each
        if not self.is_empty():
            root = self.root()
            for each in inorder_recur(root):
                yield each

    def positions(self):
        for each in self.inorder():
            yield each

    def __iter__(self):
        for each in self.inorder():
            yield each.element()

if __name__ == "__main__":
    a = LinkedBinaryTree()
    a._add_root(1)
    p = a.root()
    a._add_left(p, 2)
    a._add_right(p, 3)
    p = a.left(p)
    p1 = a._add_left(p, 4)
    a._add_right(p, 5)
    p = a.right(a.root())
    a._add_left(p, 6)
    a._add_right(p, 7)
    p = a.right(p)
    a._add_left(p, 8)
    a._add_right(p, 9)

    b = LinkedBinaryTree()
    b._add_root(10)
    c = LinkedBinaryTree()
    c._add_root(11)
    a._attach(p1, b, c)
    for each in a:
        print(each)