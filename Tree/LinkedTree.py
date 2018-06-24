from Tree import *

class LinkedTree(Tree):
    class _Node:
        __slots__ = "_element", "_parent", "_children"
        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

    class Position(Tree.Position):
        def element(self):
            return self._node._element

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def _validate(self, p):
        if p._container is not self:
            raise ValueError("position does not belong to this tree")
        if not isinstance(p.__class__, type(self.Position)):
            raise ValueError("invalid position type")
        if p._node is None:
            raise ValueError("position no longer valid")
        return p._node

    def root(self):
        return self._make_position(self._root)

    def is_root(self, p):
        node = self._validate(p)
        return node is self._root

    def is_leaf(self, p):
        node = self._validate(p)
        return len(node._children) == 0

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def children(self, p):
        node = self._validate(p)
        for each in node._children:
            yield self._make_position(each)

    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)

    def _add_root(self, e):
        if self._root:
            raise ValueError("root already exists")
        node = self._Node(e)
        self._root = node
        self._size += 1
        return self._make_position(node)

    def _add_child(self, p, e):
        parent = self._validate(p)
        child = self._Node(e, parent)
        parent._children.append(child)
        self._size += 1
        return self._make_position(child)

    def preorder(self):
        def preorder_recur(p):
            yield p
            for each in self.children(p):
                for other in preorder_recur(each):
                    yield other
        root = self.root()
        yield root
        for each in preorder_recur(root):
            yield each

    def positions(self):
        for each in self.preorder():
            yield each

    def __iter__(self):
        for each in self.positions():
            yield each._node._element

def preorder_indent(T, p, depth):
    print(' ' * 2 * depth + str(p.element()))
    for each in T.children(p):
        preorder_indent(T, each, depth + 1)

def preorder_label(T, p, depth, path):
    print(' ' * 2 * depth + ".".join([str(x) for x in path]), str(p.element()))
    count = 0
    for each in T.children(p):
        count += 1
        path.append(count)
        preorder_label(T, each, depth + 1, path)
        path.pop()

def parenthesize(T, p, path):
    if path and path[-1] != 0:
        print(', ', end='')
    else:
        print(' ', end='')
    print(p.element(), end='')
    if not T.is_leaf(p):
        print(" (", end='')
        count = 0
        for each in T.children(p):
            path.append(count)
            parenthesize(T, each, path)
            path.pop()
            count += 1
        print(')', end='')

if __name__ == "__main__":
    T = LinkedTree()
    root = T._add_root("Electronics R'Us")
    T._add_child(root, "R&D")
    p = T._add_child(root, "Sales")
    T._add_child(p, "Domestic")
    p = T._add_child(p, "International")
    T._add_child(p, "Canada")
    T._add_child(p, "S.America")
    p = T._add_child(p, "Overseas")
    T._add_child(p, "Africa")
    T._add_child(p, "Europe")
    T._add_child(p, "Asia")
    T._add_child(p, "Australia")
    T._add_child(root, "Purchasing")
    p = T._add_child(root, "Manufacturing")
    T._add_child(p, "TV")
    T._add_child(p, "CD")
    T._add_child(p, "Tuner")
    print(len(T))
    # for each in T:
    #     print(each)
    # preorder_label(T, T.root(), 0, [])
    parenthesize(T, root, [])



