from DoublyLinkedList import *

class PositionList(DLList):
    class Position:
        __slots__ = "_container", "_node"
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise ValueError("invalid position type")
        if p._container is not self:
            raise ValueError("position does not belong to this container")
        if p._node._element is None:
            raise ValueError("position is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def _insert_between(self, element, preNode, nextNode):
        node = super()._insert_between(element, preNode, nextNode)
        return self._make_position(node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        right = self._validate(p)
        return self._insert_between(e, right._prev, right)

    def add_after(self, p, e):
        left = self._validate(p)
        return self._insert_between(e, left, left._next)

    def replace(self, p, e):
        node = self._validate(p)
        old = p.element()
        node._element = e
        return old

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

if __name__ == "__main__":
    a = PositionList()
    a.add_first(1)
    a.add_last(2)
    a.add_first(0)
    p = a.add_last(4)
    a.add_before(p, 3)
    a.add_after(p, 5)
    print(len(a))
